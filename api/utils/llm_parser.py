import os
import json
from google import genai
from django.conf import settings

# Initialize client
client = genai.Client(api_key=settings.GEMINI_API_KEY)


def build_resume_prompt(resume_text: str) -> str:
    return f"""
You are an expert resume parser.

Extract structured resume information from the text below.

Return ONLY valid JSON in this exact format:

{{
  "name": "",
  "email": "",
  "phone": "",
  "summary": [],
  "skills": [],
  "education": [],
  "experience": [],
  "projects": [],
  "certifications": []
}}

Rules:
- Use empty string "" if not found
- Use empty array [] if not found
- Split summary into short paragraphs
- Skills should be a list of individual skills
- Education, experience, projects, certifications should be bullet-like strings
- Do NOT include any explanation, ONLY JSON

Resume Text:
----------------
{resume_text}
----------------
"""


def parse_resume_with_llm(resume_text: str) -> dict:
    prompt = build_resume_prompt(resume_text)

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt,
        )

        raw_text = response.text.strip()

        print("==== LLM RAW OUTPUT ====")
        print(raw_text)
        print("==========")

        # Clean code fences if present
        if raw_text.startswith("```"):
            raw_text = raw_text.replace("```json", "").replace("```", "").strip()

        parsed_json = json.loads(raw_text)
        return parsed_json

    except Exception as e:
        print("LLM parsing failed:", str(e))

        # Safe fallback
        return {
            "name": "",
            "email": "",
            "phone": "",
            "summary": [],
            "skills": [],
            "education": [],
            "experience": [],
            "projects": [],
            "certifications": [],
        }

def build_enhance_summary_prompt(summary_paragraphs: list[str]) -> str:
    joined = "\n\n".join(summary_paragraphs)

    return f"""
You are an expert resume writer.

Enhance and improve the following professional summary.
Make it more impactful, concise, and professional.
Do NOT add fake experience.
Do NOT change meaning.
Do NOT invent skills.
Just improve language, clarity, and structure.

Return the result as separate short paragraphs.
Do NOT add explanations.

Original Summary:
----------------
{joined}
----------------
"""


def enhance_summary_with_llm(summary_paragraphs: list[str]) -> list[str]:
    prompt = build_enhance_summary_prompt(summary_paragraphs)

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt,
        )

        raw_text = response.text.strip()

        print("===== ENHANCED SUMMARY RAW ======")
        print(raw_text)
        print("==================")

        # Split into paragraphs safely
        enhanced_paragraphs = [
            p.strip()
            for p in raw_text.split("\n\n")
            if p.strip()
        ]

        return enhanced_paragraphs

    except Exception as e:
        print("LLM enhance summary failed:", str(e))
        return summary_paragraphs  # fallback to original

def build_generate_summary_prompt(context: dict) -> str:
    skills = "\n".join(context.get("skills", []))
    experience = "\n".join(context.get("experience", []))
    projects = "\n".join(context.get("projects", []))
    education = "\n".join(context.get("education", []))

    return f"""
You are an expert resume writer.

Generate a professional summary for a resume based on the details below.
Make it professional, concise, and impactful.
Do NOT invent fake experience.
Do NOT add company names if not provided.

Return 2-4 short paragraphs suitable for a resume summary.
Do NOT include explanations.

Skills:
{skills}

Experience:
{experience}

Projects:
{projects}

Education:
{education}
"""


def generate_summary_with_llm(context: dict) -> list[str]:
    prompt = build_generate_summary_prompt(context)

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt,
        )

        raw_text = response.text.strip()

        print("===== GENERATED SUMMARY RAW =====")
        print(raw_text)
        print("===============")

        paragraphs = [
            p.strip()
            for p in raw_text.split("\n\n")
            if p.strip()
        ]

        return paragraphs

    except Exception as e:
        print("LLM generate summary failed:", str(e))
        return []


