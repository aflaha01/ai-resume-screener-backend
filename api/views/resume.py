from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from db.models import Resume
import pdfplumber
from api.utils.llm_parser import parse_resume_with_llm


def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_resume(request):
    file = request.FILES.get("resume")

    if not file:
        return Response({"message": "Resume file required"}, status=400)

    resume = Resume.objects.create(
        user=request.user,
        file=file
    )

    try:
        text = extract_text_from_pdf(resume.file.path)
    except Exception:
        return Response(
            {"message": "Failed to read resume PDF"},
            status=500
        )

    # LLM-only parsing
    parsed_data = parse_resume_with_llm(text)

    # profile = Profile.objects.create(
    #     user=request.user,
    #     resume=resume,
    #     name=parsed_data["name"],
    #     email=parsed_data["email"],
    #     phone=parsed_data["phone"],
    #     summary=parsed_data["summary"],
    #     skills=parsed_data["skills"],
    #     education=parsed_data["education"],
    #     experience=parsed_data["experience"],
    #     projects=parsed_data["projects"],
    #     certifications=parsed_data["certifications"],
    # )

    return Response(
        {
            "message": "Resume processed successfully",
            "resume_id": resume.id,
            # "profile_id": profile.id,
            "profile": parsed_data,
        },
        status=201
    )
