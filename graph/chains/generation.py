from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an assistant for question-answering tasks.

Use the following retrieved context to answer the question.

If you don't know the answer, just say that you don't know.

Keep the answer concise.

Context:
{context}
""",
        ),
        (
            "human",
            "Question: {question}",
        ),
    ]
)


generation_chain = prompt | llm | StrOutputParser()
