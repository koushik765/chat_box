# LangChain & Groq LLM Integration

A minimal, professional boilerplate demonstrating how to integrate **Groq's** lightning-fast inference engine with **LangChain** using Python. This repository provides a quickstart setup to invoke the `llama-3.3-70b-versatile` model.

## 🚀 Features
- **LangChain Integration:** Utilizes `langchain-groq` for seamless API interaction.
- **Environment Management:** Uses `python-dotenv` for secure API key handling.
- **Groq Llama 3:** Pre-configured to use the highly capable `llama-3.3-70b-versatile` model.

## 📁 Project Structure
- `groq_model.py`: The main execution script that initializes the LLM and runs a sample single-turn prompt.
- `reqiurement.txt`: Contains all necessary Python dependencies.

## 🛠️ Prerequisites
- Python 3.8+
- A [Groq API Key](https://console.groq.com/keys)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**
   Install the required packages using the provided requirements file:
   ```bash
   pip install -r reqiurement.txt
   ```

## ⚙️ Configuration

Create a `.env` file in the root directory of the project and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

## 🚀 Usage

Execute the main script to test the model's response to a sample prompt ("Can you give sample proof for how to create a portifoilo"):

```bash
python groq_model.py
```

## 📄 Dependencies
The following core libraries are used (as defined in `reqiurement.txt`):
- `langchain`
- `langchain_core`
- `langchain_community`
- `langchain-groq`
- `langchain-text-splitters`
