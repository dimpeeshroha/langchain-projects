from dotenv import load_dotenv
import os
load_dotenv()
def main():
    
    print("Hello from langchain-course!")
    print("Your OpenAI API key is:", os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
