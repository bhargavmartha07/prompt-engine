from prompt_engine.engine import PromptEngine
from prompt_engine.exceptions import MissingInputVariableError


def main():
    print("Initializing PromptEngine...\n")
    engine = PromptEngine("templates")

    print("Available templates:")
    for name in engine.list_templates():
        print("-", name)
    print()

    # 1. Zero-shot example
    print("Zero-shot example:")
    output = engine.render(
        "zero_shot_basic",
        {"text": "Artificial Intelligence is changing the world."}
    )
    print(output)
    print("-" * 50)

    # 2. Few-shot example
    print("Few-shot example:")
    output = engine.render(
        "few_shot_math",
        {"question": "6 + 7"}
    )
    print(output)
    print("-" * 50)

    # 3. Chain-of-Thought example
    print("Chain-of-Thought example:")
    output = engine.render(
        "cot_reasoning",
        {"problem": "If you have 3 apples and buy 2 more, how many do you have?"}
    )
    print(output)
    print("-" * 50)

    # 4. Role-based example
    print("Role-based example:")
    output = engine.render(
        "role_teacher",
        {"question": "What is recursion?"}
    )
    print(output)
    print("-" * 50)

    # 5. Structured output example
    print("Structured output example:")
    output = engine.render(
        "structured_summary",
        {"text": "Python is a popular programming language used in AI and web development."}
    )
    print(output)
    print("-" * 50)

    # 6. Validation error example
    print("Validation error example:")
    try:
        engine.render("zero_shot_basic", {})
    except MissingInputVariableError as e:
        print("Caught error:", e)
    print("-" * 50)

    # 7. Prompt chaining example (FIXED)
    print("Prompt chaining example:")
    final_output = engine.chain([
        {
            "template": "zero_shot_basic",
            "inputs": {
                "text": "Machine learning enables systems to learn from data."
            },
            "output_key": "summary"
        },
        {
            "template": "zero_shot_explain",
            "inputs": {
                "topic": "summary"
            },
            "output_key": "explanation"
        }
    ])

    print(final_output)
    print("\nPrompt chaining completed successfully.")


if __name__ == "__main__":
    main()
