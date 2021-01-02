from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import Basemodel


class msg(Basemodel):
    user: str
    message: str


app = FastAPI()


#makes "app" = "FastAPI"


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <html>
            <head>
                <title>hello</title>
            <head>
            <body>
                <h1>hello</h1>
            </body>
        <html>
        """


#changes the page language to html


@app.get("/chat/room", response_class=HTMLResponse)
async def chatroom():
    return open("chatlog.txt").read()


#creates webpage in site
