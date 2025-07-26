from openai import OpenAI
from config import OPENAI_API_KEY
from tools import calculator_tool, get_current_time, web_search


# Initialize client
client = OpenAI(api_key= OPENAI_API_KEY)

def run_basic_chat():
    print("🤖 Bot: Hello! I'm your assistant. Ask me anything (type 'exit' to quit).")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("\n You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=messages
            )

            reply = response.choices[0].message.content
            print(f"Bot: {reply}")
            messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_basic_chat()


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator_tool",
            "description": "Safely evaluate a math expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression like 'sqrt(25) + 2'"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current time in a specific timezone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string",
                        "description": "Timezone like 'UTC' or 'Asia/Tokyo'"
                    }
                },
                "required": ["timezone"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Perform a simple web search using DuckDuckGo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search keywords"
                    },
                    "num_results": {
                        "type": "integer",
                        "description": "Number of search results (1-5)",
                        "default": 3
                    }
                },
                "required": ["query"]
            }
        }
    }
]


function_map = {
    "calculator_tool": calculator_tool,
    "get_current_time": get_current_time,
    "web_search": web_search,
}
