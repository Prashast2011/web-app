from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/",response_class=HTMLResponse)

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


@app.get("/chat/room",response_class=HTMLResponse)
async def chatroom():
    return open("chatlog.txt").read()



    



