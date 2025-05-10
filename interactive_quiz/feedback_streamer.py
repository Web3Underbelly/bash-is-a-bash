# feedback_streamer.py
import os
import time
import openai
openai.api_key = 'os.getenv("OPENAI_API_KEY")'

def stream_hint(prompt):
    return openai.ChatCompletion.create(
      model="gpt-4",
      messages=[{"role":"user","content":prompt}],
      stream=True
    )
