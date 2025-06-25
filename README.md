
# 🎙️ Voice To-Do List App

A desktop productivity application built with **Python** that lets you manage your to-do list using your **voice**. It supports **speech-to-text**, **checkboxes**, **editing**, **deleting**, and **cloud sync** with a Flask + MongoDB backend. Includes offline **text-to-speech** to read tasks aloud.

---
## screenshots

![image](https://github.com/user-attachments/assets/88bc812f-2f29-43a0-812e-1bfdd6751f6d)
![image](https://github.com/user-attachments/assets/5e4b1a2e-327a-4074-b0a8-fb6a0aed77a4)

---

## 🚀 Features

- 🎤 Add tasks using **voice input**
- 🔁 Tasks sync to the **cloud (MongoDB Atlas via Flask API)**
- ✅ Mark tasks as **completed** with checkboxes
- ✏️ **Edit** and 🗑️ **Delete** tasks easily
- 🔊 Click to **speak all tasks** out loud
- 💾 Tasks persist across sessions

---

## 🖥️ Tech Stack

### 🧠 Frontend (Tkinter)
- Python + Tkinter (GUI)
- SpeechRecognition (`Google Speech API`)
- `pyttsx3` (Text-to-Speech)
- REST calls via `requests`

### ☁️ Backend (Flask API)
- Flask + flask-cors
- MongoDB Atlas (cloud NoSQL database)
- pymongo
- dotenv

---

## 📁 Folder Structure

```

voice\_todo\_project/
├── frontend/
│   └── voice\_todo.py
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ManneUdayKiran/Voice-TodoList-App.git
cd Voice-TodoList-App
````

---

### 2. Backend (Flask API)

```bash
cd backend
pip install -r requirements.txt
# Set up your Mongo URI in a .env file
echo MONGO_URI=your_mongo_connection_string > .env
python app.py
```

🛠️ API runs at `http://localhost:5000`

---

### 3. Frontend (Voice Todo App)

```bash
cd ../frontend
pip install requests SpeechRecognition pyttsx3 pyaudio
python voice_todo.py
```

🗣️ Click "Start Speaking" and say your task aloud
🔊 Use "Speak Tasks" to hear your to-do list read out

---

## 📸 Screenshots

> *(Add screenshots of the UI and app in action here)*

---

## 🌐 Deployment

* You can deploy the Flask backend to platforms like:

  * [Render](https://render.com)
  * [Railway](https://railway.app)
  * [Heroku](https://heroku.com)

Update `API_URL` in `voice_todo.py` to the deployed backend URL.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

[MIT License](LICENSE)


