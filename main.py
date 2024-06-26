from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import os
import motor_GPIO

motor = motor_GPIO.motor_GPIO()

app = FastAPI()

VIDEO_FILE_PATH = "./assets/file_example_MP4_1920_18MG.mp4"

@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "How Cool": "Is This?! :-D"
    }

@app.get("/start")
def start():
    motor.setSpeed(4)
    return "success"

@app.get("/set_speed")
def set_speed(speed: int):
    try:
        motor.setSpeed(speed)
    except ValueError as e:
        print(e)
        return {
            "state": "failed",
            "message": str(e)
        }
    else:
        return {
            "state": "success",
            "speed": str(speed)
        }

@app.get("/stop")
def stop():
    motor.setSpeed(0)
    return "success"

@app.get("/video")
async def get_video():
    if not os.path.exists(VIDEO_FILE_PATH):
        raise HTTPException(status_code=404, detail="Video file not found")

    def iterfile():
        with open(VIDEO_FILE_PATH, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="video/mp4")
