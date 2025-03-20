# Google Gemini Chatbot

🚀 **Google Gemini Chatbot** is a simple yet powerful chatbot application built using **Streamlit** and **Google's Generative AI (Gemini-1.5-Pro-Latest)**. This chatbot allows users to interact with Google's Gemini AI in real-time.

---

## 📌 Prerequisites
Before setting up the chatbot, ensure you have the following installed:

- **Python 3.8+**
- **pip (Python Package Manager)**
- **Google API Key** (for Generative AI)
- **Git** (optional, for version control)

---

## 🛠️ Installation & Setup
Follow these steps to set up and run the chatbot locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/saloni911/Google-Gemini-Chatbot.git
cd Google-Gemini-Chatbot
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv myenv
source myenv/bin/activate   # On macOS/Linux
myenv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key
Create a `.env` file in the root directory and add your Google API key:
```bash
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
```
Alternatively, you can manually create a `.env` file and add:
```plaintext
GOOGLE_API_KEY=your_google_api_key_here
```

### 5️⃣ Run the Chatbot
```bash
streamlit run main.py
```
This will start the chatbot on a local server. Open the displayed URL in your browser.

---

## 📌 Features
✅ **Real-time AI Chat** - Interact with Google's Gemini AI effortlessly.  
✅ **Streamed Responses** - AI responses appear dynamically, improving user experience.  
✅ **Session History** - Chat history is stored within the session.  
✅ **Simple UI with Streamlit** - Easy-to-use web-based interface.  

---

## 🎯 How to Use
1. Open the chatbot in your browser.
2. Type your question in the chat input field.
<img width="1439" alt="Screenshot 2025-03-21 at 12 40 39 AM" src="https://github.com/user-attachments/assets/88daea19-b232-4f55-bd9b-5a02a268161d" />
3. Get an AI-generated response in real-time.
4. Continue the conversation seamlessly.

---

## 🛠️ Technologies Used
- **Python** (Backend)
- **Streamlit** (UI Framework)
- **Google Generative AI (Gemini-1.5-Pro-Latest)** (AI Model)
- **dotenv** (For API Key Management)

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make changes and commit: `git commit -m "Added new feature"`
4. Push to your branch: `git push origin feature-branch`
5. Open a Pull Request.

---

## 📜 License
This project is licensed under the **MIT License**.

---

### 📩 Contact
For any issues or queries, feel free to reach out to [Saloni Nachankar](https://github.com/saloni911).

---

Happy Coding! 🚀

