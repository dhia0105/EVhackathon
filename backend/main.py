from openai import AzureOpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware
import json
# FastAPI app setup
app = FastAPI()
origins = [
    "http://localhost:5173",  # Vue.js frontend running on localhost
    "http://localhost:3000",  # If using another port, change accordingly
]

# Add CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow only the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

#with open("context.txt", "r") as file:
#    context = file.read()
#context = ""
# Pydantic model for input data
class TextInput(BaseModel):
    question: str
    sector_initiative: str

class Post(BaseModel):
    title: str
    content: str
# Azure OpenAI setup (use environment variable for security)
openai_endpoint = "https://openai-track05-hackathon.openai.azure.com"     # Add the endpoint here
model_deployment =  "gpt-4o-mini-deployment" # Add the model deployment here
openai_key = "822c23a400ed42458de8bb9448041c3a"  # Set an environment variable with the credentials to not hardcode the key
openai_api_version = "2024-08-01-preview"   # From this version, structured responses are supported

system_message = """
You are a helpful assistant that only answers questions based on the provided context.
If the question is not answerable from the given context, respond with "No recommendations found.".
"""

def prepare_message_for_query(question, sector_initiative):
    context = "these are publications from companies in which they share best practices  \n"
    with open('posts.json', 'r') as file:
        posts = json.load(file)
    i = 1
    for post in posts["posts"]:
        context += "publication " + str(i) + ": \n" + "title: " + post["title"] + ". \n"
        context += "content: " + post["content"]
        i+=1
    print(context)
    messages=[
        {"role": "system", "content": system_message},  # Optionally, provide a system message
        {"role": "user", "content": context},  # Provide the context
        {"role": "user", "content": question}  # Provide the user's question
    ]
    return messages


def get_recommendations(question, client, sector_initiative):
    messages = prepare_message_for_query(question, sector_initiative)
    response = client.chat.completions.create(
        messages=messages,
        stream=False,
        model="gpt-4o-mini",
    )
    try:
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return None


def create_and_return_recommendations(question, sector_initiative):
    open_ai_client = AzureOpenAI(
        azure_endpoint=openai_endpoint,
        api_key=openai_key,
        azure_deployment= model_deployment,
        api_version=openai_api_version,
    )
    recommendation = get_recommendations(question, open_ai_client, sector_initiative)
    return recommendation

def create_post(title, content):
    try:
        # get posts
        with open('posts.json', 'r') as file:
            posts = json.load(file)
        # Append new post to the list
        posts["posts"].append({"title": title, "content": content})
        # Write posts back to the file
        with open('posts.json', 'w') as file:
            json.dump({"posts": posts["posts"]}, file, indent=4)  # 'indent' makes the file readable
    except Exception as e:
        print(e)
        return None
# FastAPI endpoint to query the database and get response from OpenAI
@app.post("/ask")
async def ask_openai(input_data: TextInput):
    try:
        recommendation = create_and_return_recommendations(input_data.question, input_data.sector_initiative)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with OpenAI: {str(e)}")
    return {"recommendations": recommendation}

# FastAPI endpoint to query the database and get response from OpenAI
@app.post("/post")
async def add_a_post(post: Post):
    try:
        create_post(post.title, post.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while creating the post: {str(e)}")
    return {"status": "success"}

# FastAPI endpoint to query the database and get response from OpenAI
@app.get("/posts")
async def get_posts():
    published_posts = []
    try:
        with open('posts.json', 'r') as file:
            published_posts = json.load(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting the posts: {str(e)}")
    return {"posts": published_posts["posts"]}