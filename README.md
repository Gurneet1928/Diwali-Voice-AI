<h1 style="text-align: center;"><img src="https://cdn-icons-png.flaticon.com/512/4119/4119712.png" alt="alt_text" width="50"/> Diya Dost AI <img src="https://cdn-icons-png.flaticon.com/512/4119/4119712.png" alt="alt_text" width="50"/> </h1>

<h3 style='text-align:center'>Talk to a Diwali Based AI Bot in Hindi | Made with 💖 </h3>
<hr>

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/torch?style=flat-square) 
![GitHub License](https://img.shields.io/github/license/Gurneet1928/Diwali-Voice-AI?style=flat-square) 
![GitHub last commit](https://img.shields.io/github/last-commit/Gurneet1928/Diwali-Voice-AI?style=flat-square) 
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Gurneet1928/Diwali-Voice-AI?style=flat-square) 
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/Gurneet1928/Diwali-Voice-AI/total)


This repository contains a Streamlit web application that leverages speech-to-text, text-to-speech, and Connection to LLM API using Request. The project is built for an interactive and engaging speech experience, allowing users to record their voice, generate AI responses, and listen to the output in a fun, festive way.
Made especially for the festival of Diwali. 

## Features

- **Speech Recording**: The app allows users to record their voice directly through the interface using `audio_recorder`.
- **Connect to API Endpoint**: Using `request`, users can connect to any LLM Endpoint to inference. For saving cost, we tested it out using LMStudio and LLama 3.2 3B
- **Text-to-Speech**: The AI response is converted into speech with the `silero  Hindi Language` TTS model, and the resulting audio is played back to the user.

## Images
![Page 1](/ignore/page_1.png)
![Page 2](/ignore/page_2.png)
  
## Demo

The app's interface includes:
- An **audio recording button** that prompts the user to "Say Something Bombastic..."
- The **recorded message** is transcribed and displayed in the chat interface.
- AI generates a response based on the user's input, which is then transliterated and converted into audio.

## Sample Prompt to Use:
For generating the required output, I created this prompt. Feel free to modify it and use accordingly:
- [ You are दिवाली एआई, specially created for the festive occasion of Diwali. Your mission is to assist users with any queries regarding Diwali celebrations. Your responses must always be positive, full of energy, and include a playful pun or festive humor. All responses should be in Devanagari language, including the name दिवाली एआई. Never use any other Language to respond back. Keep your replies clear, concise, short and funny. ]


## Project Structure

- **Streamlit Interface**: The UI is built with `Streamlit`, providing a clean and responsive design for user interaction.
- **Speech Recognition**: Audio input is processed using the `speech_recognition` package.
- **Text-to-Speech**: AI-generated responses are turned into audio using the `silero` TTS model for Hindi voices.
- **Aksharamukha Transliteration**: Converts AI responses from Devanagari to Romanized ISO format.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Gurneet1928/Diwali-Voice-AI.git
    cd speech-diwali-ai
    ```

2. **Set up a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt --use-deprecated=legacy-resolver
    ```

4. **Download necessary models**: The `silero` TTS model and other language models are loaded directly from `torch.hub` within the code.

## Usage

1. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

2. **Configure the LLM Endpoint API (Optional)**:
    - Go to `common - utils.py`
    - Change the variables `url` and `headers` as required and save the file.
    - If you are using LMStudio, the default Endpoint will be `http://localhost:1234/v1/chat/completions`, so you can Ignore this.

3. **Interact with the app**: 
    - Click on the microphone button to record your voice.
    - Wait for the app to transcribe the audio, generate an AI response, and listen to the response in audio format.

## Requirements

- Python 3.7+
- Libraries:
  - `streamlit`
  - `audio_recorder_streamlit`
  - `torch`
  - `speech_recognition`
  - `aksharamukha`
  - `silero-models`

## Customization

- **Transliteration**: Currently, the app transliterates text from Devanagari to Romanized ISO format. This can be adjusted by modifying the transliteration language pairs in the `transliterate.process()` function.
- **Voice Settings**: The TTS model defaults to `hindi_male`, but this can be changed by selecting a different speaker from the `silero` models.

## Known Issues

- Minor Lag when the response is fetched from backend and converted to Audio format. Can depend on Device to Devcie

## Contributing

Feel free to open an issue or a pull request if you would like to contribute or encounter any issues!

## License

MIT License

Distributed under the License of MIT, which provides permission to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software. Check LICENSE file for more info.

OR Free to use But please make sure attribute the developer....

Free Software, Hell Yeah!

Reached the End ? I appreciate you reading this README in its entirety (maybe). Please remember to give this software a star if you found it useful in any way. ƪ(˘⌣˘)ʃ ƪ(˘⌣˘)ʃ

and also 
<h1> Happy Diwali to GitHub Fam</h1>

<img src="ignore\happy-diwali-diwali-greeting.gif" alt="alt_text" width="300"/> 