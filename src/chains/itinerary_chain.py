from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

itinerary_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful travel assistant. Create a day trip itinerary for {city} based on the user's interests: {interests}. Provide a brief, bulleted itinerary."
    ),
    (
        "human",
        "Create an itinerary for my day trip."
    )
])

def generate_itineary(city: str, interests: list[str]) -> str:

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.3,
    )

    response = llm.invoke(
        itinerary_prompt.format_messages(
            city=city,
            interests=", ".join(interests)
        )
    )

    return response.content