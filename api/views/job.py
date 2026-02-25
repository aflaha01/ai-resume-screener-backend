from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from db.models.job import Job
from api.serializers.job_serializer import JobSerializer


class JobListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.filter(created_by=request.user).order_by("-created_at")
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data["created_by"] = request.user.id

        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)