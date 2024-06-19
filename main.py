from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import os

app = FastAPI()

VIDEO_FILE_PATH = "./assets/file_example_MP4_1920_18MG.mp4"

@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "How Cool": "Is This?! :-D"
    }

@app.get("/video")
async def get_video():
    if not os.path.exists(VIDEO_FILE_PATH):
        raise HTTPException(status_code=404, detail="Video file not found")

    def iterfile():
        with open(VIDEO_FILE_PATH, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="video/mp4")