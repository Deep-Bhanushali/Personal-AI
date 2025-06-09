# Personalized AI Assistant 🤖✨

A fully voice-activated personalized AI assistant that uses speech recognition, facial recognition, and text-to-speech to interact with users via voice and visual animations — like your own desktop Siri!

---

## 🔧 Features

- 🎤 **Voice Command Input** via microphone (speech recognition)
- 🗣 **Speech Synthesis Output** using `pyttsx3` (offline TTS)
- 🧑‍💻 **Facial Recognition Login** for secure and personalized access
- 📺 **Siri-Style Wave Animation** for active listening feedback
- 💬 **Chat Interface**: Real-time chat canvas showing interactions with sender/receiver format, including plans to support **WhatsApp message automation**
- 📱 **WhatsApp Message Sending Support** via automation APIs  
- 🔍 **Smart Commands**: Open applications, search YouTube, control system tasks
- 🔄 **Hotword Detection** for instant assistant activation
- ⚡ **Real-Time Python-JS Integration** via Eel

---

## 🛠 Tech Stack

- **Frontend:**  
  `HTML`, `CSS`, `JavaScript`, `jQuery`, `Textillate.js`, `Animate.css`

- **Backend:**  
  `Python 3`, `pyttsx3`, `speech_recognition`, `OpenCV`, `gevent`, `eel`

- **Integration:**  
  `Eel` – for seamless bridging of Python logic with modern JS frontends

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/Deep-Bhanushali/Personal-AI.git
cd Personal-AI

# (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the app
python run.py
