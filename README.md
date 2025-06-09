
# Personalized AI Assistant 🤖✨

A fully voice-activated personalized AI assistant that uses speech recognition, text-to-speech, and a chatbot-like interface to interact with users via voice and visual animations—like your own desktop Siri!

---

## 🔧 Features

- 🎤 **Voice Command Input** via microphone (speech recognition)
- 🗣 **Speech Synthesis Output** using `pyttsx3` (offline TTS)
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
  `Python 3`, `pyttsx3`, `speech_recognition`, `gevent`, `eel`

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
```

---

## 📂 Project Structure

```
Personal-AI/
├── main.py
├── requirements.txt
├── assets/
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   ├── js/
│   └── animations/
└── engine/
    └── modules.py
```

---

## 🧠 Future Enhancements

- 📆 **Calendar and Schedule Management**  
- 🌍 **Weather, News, and Location-based Updates**  
- 🔐 **User Authentication / Personalization**

---

## 🤝 Contributing

Feel free to fork the repo, improve features, and submit a PR.

```bash
git checkout -b feature/YourFeature
git commit -m "Add new feature"
git push origin feature/YourFeature
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## 🙏 Acknowledgments

- OpenAI Whisper for optional transcription  
- Python + JS dev community for Eel integration  
- Inspiration from Apple's Siri and Google Assistant
