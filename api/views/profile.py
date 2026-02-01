# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from db.models import Profile


# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_profile(request, profile_id):
#     try:
#         profile = Profile.objects.get(
#             id=profile_id,
#             user=request.user
#         )
#     except Profile.DoesNotExist:
#         return Response(
#             {"message": "Profile not found"},
#             status=404
#         )

#     return Response(
#         {
#             "name": profile.name,
#             "email": profile.email,
#             "phone": profile.phone,
#             "summary": profile.summary,
#             "skills": profile.skills,
#             "education": profile.education,
#             "experience": profile.experience,
#             "projects": profile.projects,
#             "certifications": profile.certifications,
#         },
#         status=200
#     )
