import streamlit as st
from google import genai

from dotenv import load_dotenv
load_dotenv()
import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_itinerary(destination, days, nights):

    prompt = f"""
    Create a detailed and well-structured travel itinerary for:

    Destination: {destination}
    Duration: {days} days and {nights} nights

    Include:
    - Day-wise plan
    - Famous tourist places
    - Local food recommendations
    - Travel tips
    - Best time to visit spots
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
st.set_page_config(
    page_title="TravelGuideAI",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 TravelGuideAI")
st.markdown("### ✈️ Plan Smart. Travel Better. Powered by Gemini AI.")

# Sidebar
st.sidebar.header("🧳 Trip Preferences")

destination = st.sidebar.text_input("Destination")

days = st.sidebar.number_input("Number of Days", min_value=1, max_value=30)
nights = st.sidebar.number_input("Number of Nights", min_value=1, max_value=30)

interests = st.sidebar.multiselect(
    "Select Interests",
    ["Adventure", "Food", "Spiritual", "Nature", "Shopping", "Photography"]
)

generate = st.sidebar.button("🚀 Generate Itinerary")

if generate:
    if destination:
        with st.spinner("✨ Crafting your perfect travel plan..."):
            prompt_extra = f"\nTraveler interests: {', '.join(interests)}"
            itinerary = generate_itinerary(destination, days, nights + 0)

        st.success("🎉 Your Personalized Travel Plan is Ready!")

        st.markdown("## 🗺️ Your Travel Itinerary")
        st.write(itinerary)

        st.download_button(
            label="📥 Download Itinerary",
            data=itinerary,
            file_name="travel_itinerary.txt",
            mime="text/plain"
        )
    else:
        st.warning("⚠️ Please enter a destination.")