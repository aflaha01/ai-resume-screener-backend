from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from db.models import Resume
import pdfplumber
from api.utils.llm_parser import parse_resume_with_llm


def extract_text_from_pdf(path):

    """
    Author: Aflaha on Jan 30, 2026
    Purpose: Extracts plain text content from an uploaded PDF resume file.
    Input parameters: path (file path to PDF)
    Return: Returns extracted text as a single string
    """

    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_resume(request):

    """
    Author: Aflaha on Jan 30, 2026
    Purpose: Uploads a resume PDF, extracts text, parses resume data using LLM, and returns structured profile data.
    Input parameters: resume (PDF file)
    Return: Returns resume_id, parsed profile data, message, and status code
    """

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

    
    print(parsed_data)
    return Response(
        {
            "message": "Resume processed successfully",
            "resume_id": resume.id,
            # "profile_id": profile.id,
            "profile": parsed_data,
        },
        status=201
    )
