# Interactive Bash Quiz

This project is an interactive quiz application designed to help users learn and practice Bash commands. It uses LLMs to generate questions, evaluates user responses, and adapts to user performance.

## Project Structure

- `main.py`: Entry point for the application
- `question_generator.py`: Module to generate questions using LLM
- `evaluator.py`: Module to evaluate user responses
- `shell_executor.py`: Module to execute and test Bash commands
- `state_manager.py`: Module to track user performance and adapt questions
- `requirements.txt`: List of dependencies
- `README.md`: Documentation

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python main.py
   ```

## License

MIT
