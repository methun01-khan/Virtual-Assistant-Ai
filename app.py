import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI


app = Flask(__name__)

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify(error="Please enter a message."), 400

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return jsonify(error="Groq API key is missing. Set the GROQ_API_KEY environment variable and restart the app."), 503

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1",
        )
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": message}],
        )
        return jsonify(content=completion.choices[0].message.content or "")
    except Exception:
        app.logger.exception("OpenAI request failed")
        return jsonify(error="The assistant could not get a response. Check the server log and your API key, then try again."), 502
    

if __name__=='__main__':
    app.run()

