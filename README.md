# 🕊️ PeacePal-AI: Your AI Mental Wellness Companion

An AI-powered mental health support chatbot built with **Streamlit** and the lightning-fast **Groq LLaMA-3** model. PeacePal-AI offers a safe and accessible space to receive general mental wellness suggestions through both text and voice.

---

## 1. Project Overview 📝

PeacePal-AI is an interactive and empathetic chatbot designed to provide initial mental wellness support. In a world where mental health is paramount, not everyone has immediate access to resources. This project aims to bridge that gap by offering a first point of contact—a digital companion that listens and provides thoughtful, safe suggestions. It's built to be a fast, responsive, and easy-to-use tool for anyone needing a moment of support.

**Disclaimer:** This chatbot is intended for general guidance and support. It is **not a substitute for a licensed professional therapist or medical advice**. If you are in crisis, please contact a local mental health hotline or emergency services.

---

## 2. The Problem 🤔

* **Accessibility:** Professional mental health support isn't always available 24/7 or may be financially out of reach for many.
* **Stigma:** Many individuals feel hesitant to discuss their mental health concerns with friends, family, or even professionals due to social stigma.
* **Immediacy:** Sometimes, people just need to talk or vent in the moment without the formality of scheduling an appointment.

---

## 3. The Solution ✨

PeacePal-AI provides a **confidential, non-judgmental, and instantly available** platform where users can:
* Engage in supportive conversations about their well-being.
* Receive general, AI-generated suggestions based on established wellness principles.
* Interact using either text or voice, making it accessible for different communication preferences.

This tool acts as a stepping stone, encouraging users to seek professional help when needed while offering immediate, low-pressure support.

---

## 4. Technical Approach 🛠️

The application's core is built on a few key components:
* **Frontend:** A clean and interactive user interface is created using **Streamlit**, which allows for rapid development of data-centric web apps in Python.
* **Backend Logic:** The chatbot's brain is powered by the **LLaMA-3** large language model, accessed via the **Groq API**. Groq is used for its incredibly low latency, ensuring real-time, natural-feeling conversations.
* **State Management:** Streamlit's `session_state` is used to maintain conversational history. This gives the chatbot "memory," allowing it to understand the context of the ongoing chat.
* **Voice Processing:** For voice input, the app uses the `SpeechRecognition` library to capture and transcribe audio from uploaded `.wav` files into text, which is then processed by the AI model.
* **Safety & Guidance:** A carefully crafted **system prompt** instructs the AI to act as a cautious and helpful advisor, ensuring responses are safe, empathetic, and always include a reminder to consult a professional for serious issues.

---

## 5. Key Features 🚀

* 🧠 **Intelligent Conversations:** Leverages the power of the LLaMA-3 model for nuanced and context-aware responses.
* ⚡ **Real-Time Interaction:** Ultra-fast response generation thanks to the Groq API.
* 🎤 **Dual Input Modes:** Communicate via **text input** or by uploading a **voice message** (`.wav` file).
* 🔄 **Conversational Memory:** Remembers the chat history for a seamless and coherent user experience.
* 🔒 **Safe & Cautious Tone:** The AI is pre-configured to provide supportive yet responsible advice.
* 🌐 **Simple Web UI:** Built with Streamlit for a clean, intuitive, and easy-to-navigate interface.

---

## 6. Project Workflow 🌊

1.  **User Interface:** The user opens the Streamlit application in their browser.
2.  **User Input:** The user chooses to either type a message or upload a `.wav` audio file.
3.  **Voice Transcription:** If an audio file is uploaded, `SpeechRecognition` processes it and converts the speech to text.
4.  **Append History:** The user's message (as text) is appended to the conversation history stored in `st.session_state`.
5.  **API Request:** The entire conversation history is sent as a payload to the Groq API endpoint.
6.  **AI Response:** The LLaMA-3 model generates a relevant and contextual response.
7.  **Display Output:** The AI's response is appended to the session state and instantly displayed in the chat UI.
8.  The loop continues, allowing for a continuous conversation.

---

## 7. Tech Stack 💻

| Component          | Technology                                                                                                  |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| **Language** | `Python`                                                                                                    |
| **Framework** | `Streamlit`                                                                                                 |
| **AI Model** | `LLaMA-3 (8B)`                                                                                              |
| **API Provider** | `Groq`                                                                                                      |
| **Voice-to-Text** | `SpeechRecognition` (Google Speech Recognition), `PyDub`                                                    |
| **API Client** | `requests`                                                                                                  |
| **Env Management** | `python-dotenv`                                                                                             |

---

## 8. Setup and Installation ⚙️

Follow these steps to set up the project locally.

**Prerequisites:**
* Python 3.8+
* An API key from [Groq](https://console.groq.com/keys)

**Steps:**

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ARES0093/PeacePal-AI.git](https://github.com/ARES0093/PeacePal-AI.git)
    cd PeacePal-AI
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: You may need to install `ffmpeg` on your system for `pydub` to work correctly. Visit the [ffmpeg official site](https://ffmpeg.org/download.html) for instructions.*

4.  **Set up your environment variables:**
    * Create a new file named `.env` in the root of your project directory.
    * Add your Groq API key to this file:
        ```
        GROQ_API_KEY="your_api_key_here"
        ```

---

## 9. How to Run ▶️

Once the setup is complete, run the following command in your terminal:

```bash
streamlit run app.py
```

##10. Future Improvements 💡
  This project has a strong foundation, but there are many ways it could be enhanced:

-Real-time Microphone Input: Implement live speech-to-text directly from the user's microphone instead of file uploads.

-Text-to-Speech (TTS): Add an option for the chatbot to speak its responses aloud.

-User Session History: Implement a simple database (like SQLite) to allow users to save and revisit their past conversations.

-Sentiment Analysis: Analyze the emotional tone of the user's input to provide more empathetic and tailored responses.

-Deployment: Containerize the application with Docker and deploy it to a cloud platform like Hugging Face Spaces or Streamlit Community Cloud for public access.
