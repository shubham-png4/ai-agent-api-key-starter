from agent import SimpleAIAgent


def main():
    agent = SimpleAIAgent()
    print("AI agent is ready. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        if not user_input:
            continue
        try:
            answer = agent.respond(user_input)
            print(f"Agent: {answer}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()