from dotenv import load_dotenv
from graph.chains.retriever_grade import GradeDocuments, retriever_grade
from ingestion import retriever

load_dotenv()


def test_retrival_grade_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[1].page_content

    res: GradeDocuments = retriever_grade.invoke(
        {"question": question, "document": doc_txt}
    )
    print("the test passed successfully")
    assert res.binary_score == "yes"


def test_retrival_grade_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[1].page_content

    res: GradeDocuments = retriever_grade.invoke(
        {"question": "how to make pizaa", "document": doc_txt}
    )

    assert res.binary_score == "no"
