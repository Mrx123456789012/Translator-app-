import streamlit as st
from googletrans import Translator

def translate_text(text, language):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=language)
    return translation.text

# Define the Streamlit app
def app():
    st.title("Text Translator")
    text = st.text_area("Enter text to translate:")
    language = st.selectbox("Select language to translate to:", ("English", "Spanish", "French", "German", "Bengali"))
    language_dict = {"English": "en", "Spanish": "es", "French": "fr", "German": "de", "Bengali": "bn"}
    language_code = language_dict[language]
    if st.button("Translate"):
        if text:
            translation = translate_text(text, language_code)
            st.write("Translation:")
            st.write(translation)
        else:
            st.warning("Please enter some text to translate")

# Run the app
if __name__ == "__main__":
    app()
