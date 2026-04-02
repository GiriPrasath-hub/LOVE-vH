from fastapi import FastAPI
from fastapi.responses import JSONResponse
from openenv.environment import OpenEnvWrapper

app = FastAPI()
env = OpenEnvWrapper()

@app.get("/")
def health():
    return JSONResponse(content={"status": "running"})

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)

@app.get("/state")
def state():
    return env.state()