In our project, we'll use OpenAI's Whisper to transform speech into text. Next, we'll use IBM Watson's AI to summarize and find key points. We'll make an app with Hugging Face Gradio as the user interface.

OpenAI Whisper is an automatic speech recognition (ASR) model developed by OpenAI that converts spoken audio into text. It can also perform language identification and translation from several languages into English.

https://github.com/openai/whisper



pip3 install virtualenv 
virtualenv my_env # create a virtual environment my_env
source my_env/bin/activate # activate my_env


# installing required libraries in my_env
pip install --force-reinstall "setuptools<70" transformers==4.36.0 torch==2.1.1 gradio==5.23.2 langchain==0.0.343 ibm_watson_machine_learning==1.0.335 huggingface-hub==0.28.1


# We need to install ffmpeg to be able to work with audio files in python.

sudo apt update
sudo apt install ffmpeg -y


# you can use download_audio.py python code to download an audio file and save locally
