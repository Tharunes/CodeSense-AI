# Your Django Code (Text Version)

import os
import json
import time
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path
from django.core.wsgi import get_wsgi_application
from django.views.decorators.csrf import csrf_exempt

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='your-secret-key-here',
        ROOT_URLCONF=__name__,
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                    ],
                },
            },
        ],
        STATIC_URL='/static/',
        STATICFILES_DIRS=[os.path.join(os.path.dirname(__file__), 'static')],
        OLLAMA_URL="http://localhost:11434",
        CHAT_MODEL="mistral:latest",
    )

def log_message(message):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def get_ollama_response(prompt):
    try:
        response = requests.post(
            f"{settings.OLLAMA_URL}/api/generate",
            json={"model": settings.CHAT_MODEL, "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json().get('response', 'Sorry, I could not generate a response.')
    except requests.exceptions.RequestException as e:
        log_message(f"ERROR: Could not connect to Ollama for generation: {e}")
        return "Error: Could not connect to the Ollama server. Is it running?"

def detect_language(code):
    code_lower = code.lower()

    if any(keyword in code_lower for keyword in ['def ', 'import ', 'from ', 'print(', 'elif ', 'pass', 'self.']):
        return "Python"

    if any(keyword in code_lower for keyword in ['function ', 'const ', 'let ', 'var ', 'console.log', '=>', 'document.']):
        return "JavaScript"

    if any(keyword in code_lower for keyword in ['#include', 'printf(', 'scanf(', 'int main', 'void main', 'stdio.h']):
        return "C"

    return "Unknown"

def index(request):
    return render(request, 'AI_Reviewer.html')

@csrf_exempt
def analyze_code(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    data = json.loads(request.body)
    code = data.get("code", "")
    analysis_type = data.get("analysis_type", "simple")

    if not code:
        return JsonResponse({"error": "Code cannot be empty."}, status=400)

    language = data.get("language", detect_language(code))

    if analysis_type == "simple":
        prompt = f"Explain the following {language} code in simple terms:\n\n{code}"

    elif analysis_type == "stepwise":
        prompt = f"Provide a step by step explanation of the following {language} code:\n\n{code}"

    elif analysis_type == "complexity":
        prompt = f"Analyze the time and space complexity of the following {language} code:\n\n{code}"

    elif analysis_type == "beginner":
        prompt = f"Rewrite the following {language} code to be easier for beginners:\n\n{code}"

    elif analysis_type == "errors":
        prompt = f"Identify errors and issues in the following {language} code:\n\n{code}"

    else:
        return JsonResponse({"error": "Invalid analysis type."}, status=400)

    log_message(f"INFO: Generating {analysis_type} analysis for {language} code...")
    explanation = get_ollama_response(prompt)

    return JsonResponse({
        "explanation": explanation,
        "language": language,
        "analysis_type": analysis_type
    })

urlpatterns = [
    path('', index, name='index'),
    path('analyze/', analyze_code, name='analyze'),
]

application = get_wsgi_application()

if __name__ == '__main__':
    import django
    django.setup()
    from django.core.management import execute_from_command_line
    execute_from_command_line(['AI_reviewer.py', 'runserver'])
