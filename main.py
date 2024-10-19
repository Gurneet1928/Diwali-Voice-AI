import streamlit as st
from audio_recorder_streamlit import audio_recorder
import torch
import speech_recognition as sr
from aksharamukha import transliterate
from common.utils import set_device, get_speech, stream_response, get_response

st.set_page_config(layout='wide')
st.html(
    """
    <h1 style="text-align:center;">
        <img src="https://cdn-icons-png.flaticon.com/512/4119/4119712.png" width="50" height="50" />
            Diya Dost
        <img src="https://cdn-icons-png.flaticon.com/512/4119/4119712.png" width="50" height="50" />
    <h1>
    <h3 style="text-align:center;"> 
        Your Personal Diwali Bot to Talk to in Hindi 😀 
    <h3>
    """
)

l_col, main_col, r_col = st.columns([1,3,1])

r = sr.Recognizer() 
device = set_device()
model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                            model='silero_tts',
                            language='indic',
                            speaker='v4_indic')
model.to(device)


with main_col:
    audio_value = audio_recorder(text="Say Something Bombastic..... ", icon_name="microphone-lines", icon_size="2x", neutral_color="#FFFFFF")
    if audio_value is not None:
        user_text = get_speech(r, audio_value)
        with st.chat_message("user"):
            st.markdown(user_text)
        try:
            with st.spinner("Generating Response...."):
                response = get_response(user_text)
                roman_text = transliterate.process('Devanagari', 'ISO', response)
                model.save_wav(text=roman_text, speaker="hindi_male", sample_rate=48000)
            with st.chat_message("ai"):
                st.audio("test.wav", format="audio/wav", autoplay=True)
                st.write_stream(stream_response(response))
        except Exception as e:
            st.write(f"Error: {e}")
        