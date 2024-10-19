import speech_recognition as sr
import io, time, requests, json
import torch

url = "http://localhost:1234/v1/chat/completions"
header = {
    "Content-Type": "application/json"
}

def set_device():
    """
    Sets the Device to "CUDA" if available else "CPU"
    Args:
        None
    Returns:
        device: torch.device
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    return device

def get_speech(r, file):
    """
    Accepts a Bytes File (Audio) and returns the Transcribed Text in Lower Case
    Args:
        r: sr.Recognizer
        file: Bytes
    Returns:
        MyText: str
    """
    audio_fle = io.BytesIO(file)
    try:
        with sr.AudioFile(audio_fle) as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            return MyText
    except sr.RequestError as e:
        print(f"Request Error: {e}")
    except sr.UnknownValueError as e:
        print(f"Unknown Value Error: {e}")

def stream_response(text):
    """
    Callback to Stream Response to st.write_stream
    Args:
        text: str
    Yields:
        word: str (with 0.05s delay)
    """
    for word in text.split():
        yield word+" "
        time.sleep(0.05)

def get_response(user_query):
    """
    Sends POST Request to the Chatbot API and returns the Response
    Args:
        user_query: str
    Returns:
        response: str
    """
    user_query = {
        "messages": [
            {"role": "user", "content": user_query}
        ]
    }
    response = requests.post(url, headers=header, data=json.dumps(user_query))
    response = response.json()
    response = response["choices"][0]["message"]["content"]
    return response