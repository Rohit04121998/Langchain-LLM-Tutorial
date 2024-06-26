import langchain_helper as lch
import streamlit as st

st.title("🐶 Pet Name Generator")

animal_type = st.sidebar.selectbox(
    "What is your pet?", ("Dog", "Cat", "Fish", "Bird", "Hamster")
)

animal_labels = {
    "Dog": "What color is your dog?",
    "Cat": "What color is your cat?",
    "Hamster": "What color is your hamster?",
    "Rat": "What color is your rat?",
    "Snake": "What color is your snake?",
    "Lizard": "What color is your lizard?",
    "Cow": "What color is your cow?",
}

pet_color = st.sidebar.text_area(label=animal_labels[animal_type], max_chars=15)

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key", key="langchain_search_api_key_openai", type="password"
    )
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/Rohit04121998/langchain-llm-tutorial/tree/main/Pet%20Name%20Generator)"

if pet_color:
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text(response["pet_name"])
