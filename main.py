from fastapi import FastAPI, Query
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def hello():
    return {"data": "Hello"}

@app.get("/echo")
def echo(text: str = Query(..., description="Text to echo back")):
    return {"echo": text+" thank you using this api!!"}

@app.get("/youtube")
def youtube(video_id: str = Query(..., description="The id of YouTube video")):
    return {"transcript": "youtube!!"}
    # transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    # text = ""

    # for transcript in transcript_list:
    #     for tr in transcript.fetch():
    #         text += tr.text
    # return {"transcript": text}