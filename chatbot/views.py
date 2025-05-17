from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import os
import json
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

def chatbot(request):
    return render(request, "chatbot.html")


# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        try:
            # Parse user message from request
            data = json.loads(request.body)
            user_message = data.get("message", "")

            # Send request to OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            reply = response.choices[0].message.content
            return JsonResponse({"reply": reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

