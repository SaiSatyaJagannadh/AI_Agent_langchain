<div align="center">

# 🧠 AI Agents with LangChain — From Hello-Tool to Memory, SQL & Web

### A progressive set of agents: tools, structured output, memory, SQLite/Supabase, local Ollama models and a Flask chat UI.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-local_LLMs-000000?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

</div>

---

## 🪜 The learning path

| # | Script | Concept |
|---|---|---|
| 1 | `main.py` | First tool-calling agent — `get_weather` + `get_location` tools on Gemini 2.5 Flash |
| 2 | `main_real.py` | Same agent wired to **real APIs** (live weather + IP geolocation via ipapi) |
| 3 | `main_chatgpt.py` | Hardened tools — HTTP error handling and fallbacks |
| 4 | `agent.py` | Reverse geocoding with OpenStreetMap Nominatim + SQLite logging |
| 5 | `agent_structured.py` | **Structured output** — typed responses instead of free text |
| 6 | `recipe_generator.py` | Structured output applied: ingredients → recipe |
| 7 | `main_ai_memory.py` | **Conversation memory** across turns |
| 8 | `main_sqlite.py` | Agent that persists to and queries **SQLite** |
| 9 | `main_supabase.py` | Same, against hosted **Supabase/Postgres** |
| 10 | `main_ollama.py` | Run fully **local** with Ollama |
| 11 | `main_llmapi.py` + `client.py` | Agent exposed as a Flask **`/chat` REST API**, plus a Python client |
| 12 | `app.py`, `main_webflask.py` | **Flask chat UI** (`templates/chat.html`) with memory and SQLite history |

## 🚀 Run it

```bash
git clone https://github.com/SaiSatyaJagannadh/AI_Agent_langchain.git && cd AI_Agent_langchain
pip install -r requirements.txt
echo -e "GOOGLE_API_KEY=...\nOPENAI_API_KEY=..." > .env

python main.py             # start at step 1
python main_webflask.py    # chat UI in the browser
```

<details>
<summary>🦙 Using local models with Ollama</summary>

```bash
ollama --version
ollama list              # models you have pulled
lsof -i :11434           # confirm the Ollama server is listening
python main_ollama.py
```

</details>

---

<div align="center">

**Built by [Sai Satya Jagannadh Doddipatla (DJ)](https://saisatyajagannadh.github.io/PersonalPortfolio/)** · ⭐ Star the repo if it helped

</div>
