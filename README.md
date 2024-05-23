# Voice Chat System

This project is a Voice Chat System developed with Flask, enabling users to interact with an AI chatbot through voice input and receive responses in both text and audio formats.

## Features

- **Voice Input**: Users can record messages using their microphone.
- **Speech-to-Text**: Recorded audio messages are converted to text using Google's Speech Recognition service.
- **AI Chatbot**: Text messages are sent to an AI chatbot for processing.
- **Text-to-Speech**: The AI chatbot generates responses based on user input, which are then converted to speech using Google Text-to-Speech (gTTS) service.
- **Real-time Interaction**: Both text and audio responses are displayed to the user in real-time.

## Requirements

- Python 3.x
- Flask
- SpeechRecognition
- gTTS (Google Text-to-Speech)
- A modern web browser with support for JavaScript and WebRTC (for microphone access)
- Ollama LLaMa 3 server

## Installation and Setup

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/yourusername/voice-chat-system.git
    cd voice-chat-system
    ```

2. **Install Dependencies**: 
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Ollama LLaMa 3 on Linux**:
    You need to have a local Ollama server running to be able to continue. To do this:

    - Download the Ollama LLaMa 3 server from [https://ollama.com/](https://ollama.com/)
    - Run an LLM: [https://ollama.com/library](https://ollama.com/library)
        Example: `ollama run llama2`
        Example: `ollama run llama2:70b`
    - Then:
        ```bash
        curl https://ollama.ai/install.sh | sh
        ollama serve
        ```

4. **Run the Application**: 
    ```bash
    python app.py
    ```

5. **Access the Application**: 
    Open your web browser and navigate to `http://localhost:5000`.

## Usage

1. **Interface Overview**: Upon accessing the application, you'll see a chat interface.
2. **Record Message**: Click on the "Record Message" button to start recording your message using the microphone.
3. **Speak Clearly**: Speak clearly into the microphone.
4. **View Responses**: After recording, the system will display both the text and audio response from the AI chatbot.
5. **Continue Conversation**: You can continue the conversation by recording new messages.

## File Structure

- **app.py**: The main Flask application file containing the server-side logic.
- **source/**: Directory containing Python modules for speech-to-text, text-to-speech, and AI chatbot functionalities.
- **static/**: Directory for storing static files such as CSS, JavaScript, and audio files.
- **templates/**: Directory containing HTML templates for the web interface.

## Credits

- Flask microframework for web development.
- SpeechRecognition library for speech recognition functionality.
- gTTS (Google Text-to-Speech) library for text-to-speech conversion.
- OpenAI Llama conversational model for AI chatbot functionality.

## License

This project is licensed under the [MIT License](LICENSE).
