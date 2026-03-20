#!/usr/bin/env python
import os
import sys
from my_first_crew_simple_chat.crew import ChatInputExtractionCrewCrew

def run():
    """Run the crew."""
    question = os.getenv("sample_value", "").strip()
    if not question:
        print("No 'sample_value' provided. Set it with: export sample_value='your question'")
        sys.exit(1)

    inputs = {
        'sample_value': question  # <-- correct key + actual value
    }
    ChatInputExtractionCrewCrew().crew().kickoff(inputs=inputs)

def train():
    """Train the crew for a given number of iterations."""
    question = os.getenv("sample_value", "").strip()
    if not question:
        print("No 'sample_value' provided. Set it with: export sample_value='your question'")
        sys.exit(1)

    inputs = {'sample_value': question}
    try:
        ChatInputExtractionCrewCrew().crew().train(
            n_iterations=int(sys.argv[2]),
            filename=sys.argv[3],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """Replay the crew execution from a specific task."""
    try:
        ChatInputExtractionCrewCrew().crew().replay(task_id=sys.argv[2])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """Test the crew execution and returns the results."""
    question = os.getenv("sample_value", "").strip()
    if not question:
        print("No 'sample_value' provided. Set it with: export sample_value='your question'")
        sys.exit(1)

    inputs = {'sample_value': question}
    try:
        ChatInputExtractionCrewCrew().crew().test(
            n_iterations=int(sys.argv[2]),
            openai_model_name=sys.argv[3],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <run|train|replay|test> [args]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
