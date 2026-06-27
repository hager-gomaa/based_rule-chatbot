# 🤖 Rule-Based AI Chatbot

A simple rule-based chatbot built in Python that responds to predefined user inputs using `if-else` control flow logic. This project demonstrates core programming concepts that form the foundation of more advanced conversational AI systems.

## 📌 Overview

| | |
|---|---|
| **Goal** | Create a chatbot that responds to predefined user inputs |
| **Type** | Rule-based (no machine learning) |
| **Language** | Python 3 |
| **Dependencies** | None — built with the Python standard library |

## ✨ Features

- Handles greetings (e.g. `hi`, `hello`) and exit commands (`exit`, `quit`, `bye`)
- Responds to simple conversational prompts (name, mood, thanks, help)
- Supports both English and Arabic inputs
- Runs in a continuous loop until the user exits
- Clean separation between response logic (`get_response`) and the chat loop (`chatbot`), making it easy to test and extend

## 🛠️ Key Skills Demonstrated

- Control flow (`if / elif / else`)
- Decision-making logic
- String processing and normalization
- Basic conversational AI / NLP concepts

## 🚀 Getting Started

### Prerequisites
- Python 3.7+

### Run it
```bash
python project1_chatbot.py
```

### Example session
```
🤖 Welcome to SimpleBot! Type 'quit', 'exit', or 'bye' to end the chat.

You: hi
Bot: Hello! How can I help you today? 😊
You: what's your name
Bot: I'm SimpleBot, a rule-based chatbot built in Python.
You: bye
Bot: Goodbye! Have a great day 👋
```

## 📂 Project Structure
```
.
└── project1_chatbot.py
```

## 🔮 Possible Extensions
- Add more intents and a fallback intent classifier
- Swap rule-based matching for an NLP model (e.g. spaCy, sentence-transformers)
- Wrap it in a simple web UI with Streamlit or FastAPI

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
