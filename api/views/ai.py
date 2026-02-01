from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.utils.llm_parser import enhance_summary_with_llm, generate_summary_with_llm


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def enhance_summary(request):
    summary = request.data.get("summary")

    if not summary or not isinstance(summary, list):
        return Response(
            {"message": "Summary list is required"},
            status=400
        )

    try:
        enhanced = enhance_summary_with_llm(summary)
    except Exception:
        return Response(
            {"message": "Failed to enhance summary"},
            status=500
        )

    return Response(
        {"enhanced_summary": enhanced},
        status=200
    )

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_summary(request):
    try:
        context = {
            "skills": request.data.get("skills") or [],
            "experience": request.data.get("experience") or [],
            "projects": request.data.get("projects") or [],
            "education": request.data.get("education") or [],
        }

        print("=== GENERATE SUMMARY CONTEXT ===")
        print(context)

        generated = generate_summary_with_llm(context)

        print("=== GENERATED SUMMARY RESULT ===")
        print(generated)

        return Response(
            {"generated_summary": generated},
            status=200
        )

    except Exception as e:
        print(" ERROR in generate_summary")
        traceback.print_exc()

        return Response(
            {
                "message": "Failed to generate summary",
                "error": str(e),
            },
            status=500
        )
