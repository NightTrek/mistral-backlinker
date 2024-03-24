
import os

def init():
    os.environ["OPENAI_API_KEY"] = "your API key HERE" # Mistral API key
    os.environ["SERPER_API_KEY"] = "Serper API key for agents" # serper.dev API key

    os.environ["OPENAI_API_BASE"] = "https://api.mistral.ai/v1/"
    os.environ["OPENAI_MODEL_NAME"] = 'mistral-large-latest'#   # Adjust based on available model

