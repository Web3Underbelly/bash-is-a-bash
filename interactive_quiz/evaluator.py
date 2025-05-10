# Module to evaluate user responses

def evaluate_response(user_response, correct_answer):
    """Evaluate the user's response against the correct answer."""
    # TODO: Implement evaluation logic
    pass
import shell_executor

def evaluate_answer(question, user_answer):
    expected_output = shell_executor.execute_command(question['answer'])
    user_output = shell_executor.execute_command(user_answer)
    
    if user_output == expected_output:
        return True, "✅ Correct!"
    else:
        feedback = f"❌ Incorrect.\nExpected Output:\n{expected_output}\nYour Output:\n{user_output}"
        return False, feedback
