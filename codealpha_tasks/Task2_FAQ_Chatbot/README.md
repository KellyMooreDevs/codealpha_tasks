# Askline — FAQ Chatbot

Built for CodeAlpha AI Internship — Task 2.

Topic chosen: **studying abroad** (visas, documents, applications, flights) — ties directly into KellyMoore Global Solutions' own services, so the FAQ set is genuinely useful, not just a demo.

## How it works
1. `faq_data.json` holds 10 question/answer pairs.
2. `chatbot.py` preprocesses text (lowercasing, punctuation stripping, tokenizing, stopword removal — via NLTK when available, with an offline fallback) and uses **TF-IDF + cosine similarity** (scikit-learn) to find the FAQ closest to what the user typed.
3. If nothing clears a confidence threshold, the bot says so instead of guessing.
4. `app.py` is a small Flask API (`/api/ask`) wrapping the matcher.
5. `static/index.html` is the optional chat UI — type a question, see the answer plus which FAQ it matched and the confidence score.

## Files
- `faq_data.json` — the FAQ dataset
- `chatbot.py` — preprocessing + matching engine, also runnable as a command-line chatbot
- `app.py` — Flask API + serves the chat UI
- `static/index.html` — the chat interface
- `requirements.txt` — dependencies

## Run it

### Command-line version (fastest way to test the matching)
```bash
pip install -r requirements.txt
python chatbot.py
```
Type a question, get an answer, type `quit` to exit.

### Full chat UI (the optional bonus)
```bash
pip install -r requirements.txt
python app.py
```
Then open **http://127.0.0.1:5000** in your browser.

> First run only: if NLTK's data isn't downloaded yet, the code tries to fetch it automatically. If there's no internet at runtime, it automatically falls back to a small built-in stopword list — the chatbot still works either way.

## Deploying so you have a live link to submit
Flask apps need a server that runs Python (Netlify alone won't run this — it's built for static sites, which is why Task 1 went there directly). Easiest free options:
1. **Render.com** (free tier): connect your GitHub repo, set the start command to `python app.py`, and it gives you a live URL.
2. **PythonAnywhere** (free tier): upload the files and point it at `app.py`.

If your CodeAlpha submission only needs code + a demo video/screenshot (check the submission form), you can skip hosting entirely and just submit the GitHub repo link with a short screen recording of it running locally.

## Push to GitHub
```bash
cd faq-chatbot
git init
git add .
git commit -m "Task 2: FAQ Chatbot"
git branch -M main
git remote add origin https://github.com/<your-username>/askline-faq-bot.git
git push -u origin main
```

## Customizing
To use this for a different topic, just replace the contents of `faq_data.json` with your own question/answer pairs — no other code changes needed.
