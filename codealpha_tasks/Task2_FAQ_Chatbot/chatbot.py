"""
FAQ Chatbot — CodeAlpha AI Internship, Task 2

Matches a user's question against a set of FAQs using text preprocessing
(tokenization + stopword removal) and TF-IDF + cosine similarity.

Run directly for a command-line chat:
    python chatbot.py
"""

import json
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------------------------
# Preprocessing
# ---------------------------------------------------------------------------
# We try to use NLTK for proper tokenization + stopword removal (the library
# named in the task brief). If NLTK's data files aren't downloaded yet (no
# internet at runtime), we fall back to a small built-in stopword list and a
# simple regex tokenizer, so the chatbot still works offline.

_NLTK_READY = False
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    try:
        stopwords.words("english")
        word_tokenize("test sentence")
        _NLTK_READY = True
    except LookupError:
        try:
            nltk.download("punkt", quiet=True)
            nltk.download("punkt_tab", quiet=True)
            nltk.download("stopwords", quiet=True)
            stopwords.words("english")
            word_tokenize("test sentence")
            _NLTK_READY = True
        except Exception:
            _NLTK_READY = False
except ImportError:
    _NLTK_READY = False

_FALLBACK_STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "have", "has", "had", "i", "you", "he", "she",
    "it", "we", "they", "my", "your", "his", "her", "its", "our", "their",
    "to", "of", "in", "on", "at", "for", "with", "about", "as", "by",
    "and", "or", "but", "if", "so", "this", "that", "these", "those",
    "can", "could", "will", "would", "should", "what", "how", "when",
    "where", "why", "which", "who"
}


def preprocess(text: str) -> str:
    """Lowercase, strip punctuation, tokenize, and remove stopwords."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    if _NLTK_READY:
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words("english"))
    else:
        tokens = re.findall(r"\b\w+\b", text)
        stop_words = _FALLBACK_STOPWORDS

    cleaned = [t for t in tokens if t not in stop_words and t.strip()]
    return " ".join(cleaned) if cleaned else text


# ---------------------------------------------------------------------------
# Matching engine
# ---------------------------------------------------------------------------
class FAQBot:
    def __init__(self, faq_path: str = "faq_data.json", threshold: float = 0.2):
        with open(faq_path, "r", encoding="utf-8") as f:
            self.faqs = json.load(f)

        self.threshold = threshold
        self.questions = [item["question"] for item in self.faqs]
        self.processed_questions = [preprocess(q) for q in self.questions]

        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.processed_questions)

    def get_answer(self, user_question: str):
        """Return (answer, matched_question, score) for the closest FAQ,
        or (None, None, score) if nothing clears the confidence threshold."""
        cleaned = preprocess(user_question)
        user_vec = self.vectorizer.transform([cleaned])

        similarities = cosine_similarity(user_vec, self.question_vectors)[0]
        best_idx = similarities.argmax()
        best_score = float(similarities[best_idx])

        if best_score < self.threshold:
            return None, None, best_score

        matched_faq = self.faqs[best_idx]
        return matched_faq["answer"], matched_faq["question"], best_score


# ---------------------------------------------------------------------------
# Command-line chat loop
# ---------------------------------------------------------------------------
def main():
    bot = FAQBot("faq_data.json")
    print("FAQ Chatbot — ask a question about studying abroad (type 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"quit", "exit"}:
            print("Bot: Goodbye!")
            break

        answer, matched_question, score = bot.get_answer(user_input)
        if answer:
            print(f"Bot: {answer}")
        else:
            print("Bot: I'm not confident I have an answer for that yet — "
                  "try rephrasing, or ask about visas, passports, applications, "
                  "flights, or English tests.")


if __name__ == "__main__":
    main()
