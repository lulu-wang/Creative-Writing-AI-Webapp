import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        userText = request.form["userText"]
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=generate_chat_prompt(userText),
            temperature=0.6,
        )
        print(response)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )


def generate_chat_prompt(topic):
    return """Write a sentence based on the prompt word.
    Prompt: England
    Sentence: As the sun set, England was lit up in a glowing light.
    Prompt: Butterfly
    Sentence: A butterfly landed on my finger in the garden.
    Prompt: {}
    Sentence:""".format(
        topic.capitalize()
    )