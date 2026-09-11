"""
Flask API + chat UI for the FAQ Chatbot (optional bonus for Task 2).

Run:
    python app.py
Then open http://127.0.0.1:5000 in a browser.
"""

from flask import Flask, jsonify, request, send_from_directory

from chatbot import FAQBot

app = Flask(__name__, static_folder="static", static_url_path="")
bot = FAQBot("faq_data.json")


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()

    if not question:
        return jsonify({"error": "Please send a question."}), 400

    answer, matched_question, score = bot.get_answer(question)

    if answer is None:
        return jsonify({
            "answer": None,
            "matched_question": None,
            "confidence": round(score, 3)
        })

    return jsonify({
        "answer": answer,
        "matched_question": matched_question,
        "confidence": round(score, 3)
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
