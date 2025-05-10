
def initialize_state(questions):
    return {q['prompt']: {'attempts': 0, 'correct': 0} for q in questions}

def should_ask_question(state, question):
    stats = state[question['prompt']]
    # Stop asking if the user has answered correctly twice
    return stats['correct'] < 2

def update_state(state, question, is_correct):
    stats = state[question['prompt']]
    stats['attempts'] += 1
    if is_correct:
        stats['correct'] += 1
