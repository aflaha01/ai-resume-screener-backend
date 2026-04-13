from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from db.models.job import Job
from db.models.profile import UserProfile
from api.serializers.job_serializer import JobSerializer
from django.db.models import Q
from django.utils.timezone import now
import re

class MatchedJobsView(APIView):
    permission_classes = [IsAuthenticated]

    
    def get(self, request):
        user = request.user

        try:
            profile_obj = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return Response([])

        skills = profile_obj.profile_json.get("skills", [])

        if not skills:
            return Response([])

        skills = list(set(skill.lower().strip() for skill in skills))[:10]

        query = Q()
        for skill in skills:
            query |= Q(title__icontains=skill) | Q(description__icontains=skill)

        jobs = Job.objects.filter(
            status="active"
        ).filter(
            Q(last_date__gte=now().date()) | Q(last_date__isnull=True)
        ).filter(query).distinct()

        job_scores = []

        for job in jobs:
            job_text = (job.title + " " + job.description).lower()

            # tokenize words
            job_words = set(re.findall(r"\b\w+\b", job_text))

            # count skill matches
            # match_count = sum(
            #      skill in job_text if " " in skill else skill in job_words
            #      for skill in skills
            #     )
            total_skills = len(skills)

            match_count = sum(
                 skill in job_text if " " in skill else skill in job_words
                 for skill in skills
                )

            match_percentage = int((match_count / total_skills) * 100)

            if match_count >= 2:
                job_scores.append((match_percentage, job))
        job_scores.sort(reverse=True, key=lambda x: x[0])

        # return top 20 jobs
        matched_jobs = []

        for score, job in job_scores[:20]:
            job.match_percentage = score   # attach dynamic field
            matched_jobs.append(job)

        serializer = JobSerializer(matched_jobs, many=True)
        return Response(serializer.data)