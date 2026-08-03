import os
import streamlit as st
from dotenv import load_dotenv

from src.core.planner import TravelPlanner

load_dotenv()

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.title("⚙️ Settings")

    api_key = st.text_input(
        "Groq API Key",
        value=os.getenv("GROQ_API_KEY", ""),
        type="password",
        placeholder="gsk_************************"
    )

    if api_key:
        os.environ["GROQ_API_KEY"] = api_key
        st.success("API Key Loaded")

    st.divider()

    st.subheader("💡 Example Interests")
    st.markdown("""
- 🍕 Food
- 🏛️ History
- 🏖️ Beaches
- 🛍️ Shopping
- 🌿 Nature
- 📸 Photography
- 🎨 Art
- 🌃 Nightlife
""")

    st.info("Your API key is only used during this session.")

# -------------------------
# Main Page
# -------------------------
st.title("🌍 AI Travel Itinerary Planner")
st.caption("Create a personalized one-day travel itinerary powered by AI.")

st.divider()

left, right = st.columns(2)

with left:
    city = st.text_input(
        "📍 Destination City",
        placeholder="e.g. Paris, Tokyo, Bengaluru"
    )

with right:
    interests = st.text_input(
        "🎯 Interests",
        placeholder="Food, Shopping, Museums, Nature"
    )

generate = st.button(
    "🚀 Generate Itinerary",
    use_container_width=True
)

st.divider()

# -------------------------
# Generate Itinerary
# -------------------------
if generate:

    if not api_key:
        st.error("Please enter your Groq API Key from the sidebar.")
        st.stop()

    if not city:
        st.warning("Please enter a destination city.")
        st.stop()

    if not interests:
        st.warning("Please enter your interests.")
        st.stop()

    with st.spinner("Generating your personalized itinerary..."):

        try:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)

            itinerary = planner.create_itineary()

            st.success("Your itinerary is ready!")

            with st.container():
                st.subheader("📄 Your Travel Plan")
                st.markdown(itinerary)

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Built with ❤️ using Streamlit and Groq")