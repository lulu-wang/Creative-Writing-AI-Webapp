# Creative Writing Generator Webapp
Creative writing sentence generator using user input prompts. AI images are generated from the prompt results.

Coded using the OpenAI API, HTML/CSS and Python (Flask) backend.
Powered by GPT-3.5. 

AI generated images from stable diffusion.

Preview Demo (v1):

With AI-generated images (stable diffusion): 

![gif](https://github.com/lulu-wang/Creative-Writing-AI-Webapp/assets/16969709/3e8b3127-fc80-470a-8f57-69e57d10f656)

Longer:
![gif2](https://github.com/lulu-wang/Creative-Writing-AI-Webapp/assets/16969709/56d20bef-d580-4916-87c1-f42eca069006)



## Setup (local)

1. Navigate into the project directory.

2. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

3. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```
   
   Make sure to have API keys for Open AI and Stable Diffusion.

4. Run the app:

   ```bash
   $ flask run
   ```

You can see the app at [http://localhost:5000](http://localhost:5000)
