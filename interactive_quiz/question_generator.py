# Module to generate questions using LLM

def generate_question():
    """Generate a new quiz question using LLM."""
    # TODO: Implement question generation logic
    pass
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_questions(commands):
    questions = []
    for cmd in commands:
        prompt = f"Create a quiz question to test understanding of the Bash command: {cmd.strip()}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        question_text = response['choices'][0]['message']['content']
        questions.append({
            'command': cmd.strip(),
            'prompt': question_text,
            'answer': cmd.strip()  # Assuming the correct answer is the command itself
        })
    return questions
