import openai
import time
from django.conf import settings

def generate_content_with_openai(prompt, remove_quotes=False, max_retries=3):
    # Get the OpenAI API Key from Django settings (configure it in your settings.py)
    openai.api_key = settings.OPENAI_API_KEY

    current_retry = 0
    while current_retry < max_retries:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            content = response.choices[0].message['content'].strip()
            return content.strip('"') if remove_quotes else content
        except openai.error.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            time.sleep(10)
            current_retry += 1
    return None