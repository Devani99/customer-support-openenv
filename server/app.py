from fastapi import FastAPI
from env.environment import SupportEnv
from env.models import Action
import uvicorn

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


def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()