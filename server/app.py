from fastapi import FastAPI
from env.environment import SupportEnv
from env.models import Action

app = FastAPI()
env = SupportEnv()


@app.post("/reset")
def reset(task: str = "easy"):
    return env.reset(task)


@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return env.get_state()