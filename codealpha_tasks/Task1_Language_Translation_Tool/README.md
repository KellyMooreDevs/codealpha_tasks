# Wordbridge — Language Translation Tool

Built for CodeAlpha AI Internship — Task 1.

## What it does
- Lets a user type text, pick a source and target language, and translate it.
- Uses the free [MyMemory](https://mymemory.translated.net) translation API — no signup, no API key, and it supports CORS so it works directly from a browser (public LibreTranslate mirrors were tried first but proved unreliable and several now require paid keys or block browser requests).
- Free tier is limited to ~500 characters per request and roughly 5,000 characters/day per IP — fine for a demo tool, so the input box is capped at 500 characters.
- Includes the optional extras: a copy-to-clipboard button and text-to-speech (via the browser's built-in Web Speech API) for both the original and translated text.
- Swap button flips source/target languages and the two texts in one click.

## Files
- `index.html` — the entire app (HTML + CSS + JS in one file, nothing to build or install).

## Run it locally
Just open `index.html` in a browser. No server, no dependencies.

## Deploy to Netlify (free, ~2 minutes)
1. Go to [app.netlify.com](https://app.netlify.com) and log in (you already have an account from TL-TRENDS).
2. Click **Add new site → Deploy manually**.
3. Drag the `translate-tool` folder (or just `index.html`) into the upload box.
4. Netlify gives you a live URL immediately (e.g. `your-site-name.netlify.app`) — that's your submission link.
5. Optional: rename the site under **Site settings → Change site name** to something like `wordbridge-translate`.

## Submitting to CodeAlpha
1. Grab your live Netlify URL.
2. Fill out the submission form shared in your CodeAlpha WhatsApp group.
3. Paste the Netlify link where it asks for the project link (and the GitHub repo link if they ask for one — see below).

## Optional: push to GitHub first (if the form asks for a repo link)
```bash
cd translate-tool
git init
git add .
git commit -m "Task 1: Language Translation Tool"
git branch -M main
git remote add origin https://github.com/<your-username>/wordbridge-translate.git
git push -u origin main
```
Then deploy that repo on Netlify via **Add new site → Import from Git** instead of manual upload — same result, but auto-redeploys if you push updates later.

## Notes
- If a translation fails, it's most likely the daily free quota (about 5,000 characters/IP) being reached — the app shows this clearly rather than a generic error. It resets daily.
- To raise the quota to 50,000 characters/day, add `&de=your@email.com` to the request URL in `index.html` (MyMemory just wants a contact email, no verification needed).
- If you later want a paid, higher-volume provider instead, swap the `tryTranslate` function for Google Cloud Translate or DeepL's API.
