# Finance AI Agent

An intelligent finance assistant that fetches real-time stock data, searches the web for financial news, and provides insights using AI-powered models. This project leverages multiple agents to deliver accurate and up-to-date information.

## 🚀 Features

- **Stock Market Insights**: Retrieves stock data using `yfinance`.
- **Web Search Capabilities**: Searches for the latest financial news using `DuckDuckGo`.
- **AI-Powered Analysis**: Utilizes Groq’s AI models for generating financial insights.
- **Multi-Agent System**: Implements different specialized agents to handle finance and search tasks separately.
- **Customizable Responses**: Generates structured output, including tables for better readability.

## 🛠️ Tech Stack

- **Programming Language**: Python 🐍
- **AI Model**: Groq (`llama-3.3-70b-versatile`)
- **Web Search Tool**: DuckDuckGo API
- **Stock Market Data**: `yfinance`
- **Environment Management**: `dotenv` for API key handling
- **Dependency Management**: Virtual environment (`.venv`)
- **Version Control**: Git & GitHub

---

## Screenshots
### Command Line Interface
- Image1
  ![Image1](https://github.com/MeeturiAjay/Finance-AI-Agent/blob/main/Screenshots/Screenshot%202025-03-30%20100528.png)

- Image2
  ![Image2](https://github.com/MeeturiAjay/Finance-AI-Agent/blob/main/Screenshots/Screenshot%202025-03-30%20100558.png)

- Image3
  ![Image3](https://github.com/MeeturiAjay/Finance-AI-Agent/blob/main/Screenshots/Screenshot%202025-03-30%20100612.png)

### PhiData Web Interface
- View1
  ![View1](https://github.com/MeeturiAjay/Finance-AI-Agent/blob/main/Screenshots/Screenshot%202025-03-30%20095148.png)

- View2
  ![View2](https://github.com/MeeturiAjay/Finance-AI-Agent/blob/main/Screenshots/Screenshot%202025-03-30%20100334.png)

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/MeeturiAjay/Finance-AI-Agent.git
   cd Finance-AI-Agent
   ```
2. **Create and activate a virtual environment**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add the following API keys:
     ```ini
     GROQ_API_KEY=your_groq_api_key
     OPENAI_API_KEY=your_openai_api_key (if needed)
     PHIDATA_API_KEY=your_phidata_api_key (if needed)
     ```

## 🚀 Usage

Run the agent using:
```sh
python Agent.py
```
Example query:
```python
multi_agent.print_response("What is the difference between the NVIDIA & Tesla's share prices? Which one should I buy?")
```

## 🤝 Contributing

1. Fork the repository 🍴
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request 🚀

---

## 📩 Contact

Feel free to reach out via:
- **LinkedIn** - [Meeturi Ajay Kumar](https://www.linkedin.com/in/meeturi-ajay-kumar-a02743248/)
- **Email** - meeturiajaykumar.23@gmail.com

---

🔗 **GitHub Repository**: [Finance AI Agent](https://github.com/MeeturiAjay/Finance-AI-Agent)

