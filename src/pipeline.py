import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def build_verification_pipeline():
    llm = ChatGroq(
        temperature=0,
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_template("""
    You are a Document Evidence Verifier. Use the following snippets to verify the requirement.

    REQUIREMENT: {question}

    DOCUMENT EVIDENCE:
    {context}

    INSTRUCTIONS:
    1. If the evidence directly confirms the requirement, start with: "VERIFIED: Requirements Fulfilled".
    2. Provide a 2-3 sentence summary of exactly how the requirement is met.
    3. If the evidence is missing or insufficient, start with: "NOT VERIFIED: Requirements Not Found".
    4. Speak only about the facts in the snippets. Do not use outside knowledge.

    RESPONSE:
    """)

    return prompt | llm | StrOutputParser()