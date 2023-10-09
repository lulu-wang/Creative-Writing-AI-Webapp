import os
import openai
import requests
import json
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
stableDiffusionKey = os.getenv("STABLEDIFFUSION_API_KEY")
stable_diffusion_url = "https://stablediffusionapi.com/api/v3/text2img"


@app.route("/", methods=("GET", "POST"))
def index():
    pictureUrl = ""
    if request.method == "POST":
        userText = request.form["userText"]
        # response = openai.Completion.create(
        #     model="gpt-3.5-turbo",
        #     prompt=generate_chat_prompt(userText),
        #     temperature=0.6,
        # )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are generating literary sentences based on the prompt word or words."},
                {"role": "user", "content": "England"},
                {"role": "assistant", "content": "As the sun set, England was lit up in a glowing light."},
                {"role": "user", "content": "Butterfly"},
                {"role": "assistant", "content": "A butterfly landed on my finger in the garden."},
                {"role": "user", "content": userText}
            ],
        )

        resultText = response['choices'][0]['message']['content']
        print (stableDiffusionKey)

        payload = json.dumps({
            "key": stableDiffusionKey,
            "prompt": resultText,
            "negative_prompt": "nudity",
            "width": "512",
            "height": "512",
            "samples": "1",
            "num_inference_steps": "20",
            "seed": None,
            "guidance_scale": 7.5,
            "safety_checker": "yes",
            "multi_lingual": "no",
            "panorama": "no",
            "self_attention": "no",
            "upscale": "no",
            "embeddings_model": stable_diffusion_url,
            "webhook": None,
            "track_id": None
        })

        headers = {
            'Content-Type': 'application/json'
        }

        responsePicture = requests.request("POST", stable_diffusion_url, headers=headers, data=payload)
        responseJson = responsePicture.json()

        if "output" in responseJson:
            pictureUrl = responseJson["output"]
        print(responseJson)

        return redirect(url_for("index", result=resultText, pictureUrl=pictureUrl))

    result = request.args.get("result")
    pictureUrl = request.args.get("pictureUrl")
    return render_template("index.html", result=result, pictureUrl=pictureUrl)

def generate_chat_prompt(topic):
    return """Write a proper sentence based on the prompt word.
    Prompt: England
    Sentence: As the sun set, England was lit up in a glowing light.
    Prompt: Butterfly
    Sentence: A butterfly landed on my finger in the garden.
    Prompt: {}
    Sentence:""".format(
        topic.capitalize()
    )