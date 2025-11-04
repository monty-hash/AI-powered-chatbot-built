from PIL import Image
import streamlit as st
import os
from dotenv import load_dotenv

# Optional OpenAI import
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ModuleNotFoundError:
    OPENAI_AVAILABLE = False

# Load API key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client if available
if OPENAI_AVAILABLE and API_KEY:
    client = OpenAI(api_key=API_KEY)
else:
    client = None

# Streamlit UI

# Load your image
img = Image.open("your_image.png")

# Display image instead of emoji in title
st.set_page_config(page_title="Manish Pokhrel Ask", page_icon=img)
st.image(img, width=100)  # Display your picture at the top
st.title("Manish Pokhrel Ask")
st.write("Ask me anything and I will provide answers in simple language!")


# Chat input
user_question = st.text_input("Type your question:")

if st.button("Ask AI"):
    if user_question.strip() != "":
        with st.spinner("AI is thinking..."):

            # If OpenAI is available and API key is set
            if client:
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": user_question}]
                    )
                    answer = response.choices[0].message.content

                except Exception as e:
                    # Handle quota or other errors gracefully
                    answer = f"Error contacting OpenAI: {str(e)}"

            else:
                # Fallback response if API not available
                answer = f"[Sample Answer] You asked: '{user_question}'. AI response goes here."

        st.success("Answer:")
        st.write(answer)

    else:
        st.warning("Please type a question!")
