from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
app = Flask(__name__)

model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = prompt

            response = model.generate_content(question)

            if response.text:
                return response.text
            else:
                return "Sorry, but I think Gemini didn't want to answer that!"
        except Exception as e:
            return "Sorry, but Gemini didn't want to answer that!"

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
