
# 🌍 AI Travel Planner

AI Travel Planner is a lightweight Streamlit app that generates personalized one-day travel itineraries using a Groq LLM (via LangChain). Enter a destination city and your interests, and the app produces a concise, bulleted day-trip plan tailored to your preferences.

Built with: Python • Streamlit • LangChain • Groq LLM

---

## Demo

Open the app locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the provided  URL shown by Streamlit (typically https://ai-travel-itinerary--planner.streamlit.app/).

---

## Features

- Interactive Streamlit UI for quick itinerary generation
- Supports comma-separated interests (e.g. "Food, Art, Photography")
- Uses Groq LLM via LangChain for natural, helpful travel suggestions
- Lightweight codebase intended for easy extension and experimentation

---

## Tech stack

- Python 3.10+ (recommended)
- Streamlit
- LangChain (langchain_core, langchain_groq)
- groq (via LangChain integration)
- dotenv for local environment variables

---

## Prerequisites

- Python 3.10+
- A Groq API key (GROQ_API_KEY). Obtain one from Groq and keep it private.

---

## Quickstart (Local)

1. Clone the repo
   ```bash
   git clone https://github.com/mdzaheerjk/AI-Travel-Planner.git
   cd AI-Travel-Planner
   ```

2. Create a virtual environment and install dependencies
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # Linux / macOS
   .venv\Scripts\activate        # Windows (PowerShell)
   pip install -r requirements.txt
   ```

3. Set your Groq API key (one of these approaches):
   - Create a `.env` file in the project root:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Or enter the key in the app sidebar when the app runs (it is used only for the session).

4. Run the app
   ```bash
   streamlit run app.py
   ```

---

## Running with Docker (suggested Dockerfile)

> Note: The repository currently has an empty Dockerfile. Use the snippet below to build a Docker image:

```dockerfile
# Example Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PORT=8501
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
```

Build and run:

```bash
docker build -t ai-travel-planner .
docker run -e GROQ_API_KEY="gsk_..." -p 8501:8501 ai-travel-planner
```

---

## Usage

1. Open the app in your browser.
2. Enter your Groq API key in the sidebar (or set it in `.env`).
3. Type a destination city (e.g., "Paris") and a comma-separated list of interests (e.g., "Food, Museums, Nightlife").
4. Click "Generate Itinerary" and get a neat, bulleted one-day plan.

Example interests to try:
- Food, History, Beaches, Shopping, Nature, Photography, Art, Nightlife

---

## Project structure

- app.py — Streamlit front-end and UI
- requirements.txt — Python dependencies
- setup.py — package metadata
- src/
  - config/config.py — loads GROQ_API_KEY from env
  - core/planner.py — TravelPlanner class, coordinates inputs and chain
  - chains/itinerary_chain.py — LangChain + Groq LLM integration
  - utils/logger.py — basic logging
  - utils/custom_exception.py — custom exception wrapper
- logs/ — runtime logs (created automatically)

---

## Known issues & recommended fixes

I reviewed the code and recommend these small fixes to improve correctness and clarity:

1. Spellings and naming:
   - The code consistently uses `itineary` — consider renaming to `itinerary` across functions and variables to avoid confusion.

2. Bug in TravelPlanner.create_itineary:
   - Current:
     ```py
     itineary = generate_itineary(self.city, self.interests)
     self.interests = self.itineary
     self.message.append(AIMessage(content=self.itineary))
     ```
   - Fix:
     ```py
     itineary = generate_itineary(self.city, self.interests)
     self.itineary = itineary
     self.message.append(AIMessage(content=itineary))
     ```
   - This prevents overwriting interests and ensures the AI message contains the generated itinerary.

3. Input validation & user feedback:
   - The app prompts for a Groq API key in the sidebar and sets os.environ when provided — good. Consider also validating the key format or catching LLM-specific auth errors and showing user-friendly messages.

4. Dockerfile:
   - The repository's Dockerfile is empty. Use the example Dockerfile above when you want containerized deployment.

5. Logging & exceptions:
   - custom_exception.get_detailed_error_message uses sys.exc_info() even when passing an explicit error_detail; that can be confusing if used outside exception contexts. Consider simplifying or providing a fallback.

---

## Roadmap / Future improvements

- Add unit tests and integration tests for the chain and TravelPlanner.
- Add CI (GitHub Actions) to run tests and linting.
- Add support for multi-day itineraries and travel time estimation.
- Add caching of generated itineraries to avoid repeated LLM calls for the same inputs.
- Add sample screenshots / demo GIF to the README.

---

## Contributing

Contributions are welcome! If you'd like to contribute:
- Open an issue describing the change or improvement
- Create a branch, implement your change, and open a PR
- Follow standard practice: unit tests, linting, small focused PRs

---

## License

Add your preferred license here (e.g., MIT). If you don't have one yet, consider adding an MIT license file (LICENSE).

---

## Contact

Maintainer: mdzaheerjk
Project: AI Travel Planner

---

Enjoy building — and happy travels! ✈️🌏
```

What I did and what I recommend next
- I inspected your repository (app.py, src/, requirements.txt, setup.py) and wrote a complete, professional README plus a concise repo description you can paste into GitHub.
- I also reviewed the code and flagged a functional bug (in src/core/planner.py) and some naming/spelling issues to fix — details are in the "Known issues & recommended fixes" section.
- Next, if you want, I can:
  - open a PR that adds this README and applies the small bugfix and variable-renaming changes,
  - create a working Dockerfile in the repo,
  - or produce unit tests for TravelPlanner and the chain.

Tell me which of those you'd like me to do next and I’ll proceed.
