from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from env.environment import SupportEnv
from env.models import Action

app = FastAPI()
env = SupportEnv()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Customer Support Simulator</title>
        <style>
            body { font-family: Arial; padding: 20px; background: #f5f5f5; }
            .card { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
            button {
                padding: 10px;
                margin: 5px;
                border-radius: 8px;
                border: none;
                background: #4CAF50;
                color: white;
                cursor: pointer;
            }
            button:hover { background: #45a049; }
        </style>
    </head>
    <body>

        <h2>📩 Customer Support Simulator</h2>

        <div class="card">
            <h3>Customer Message:</h3>
            <p id="message">Loading...</p>
        </div>

        <div class="card">
            <h3>Actions:</h3>
            <button onclick="sendAction('reply')">Reply</button>
            <button onclick="sendAction('issue_refund')">Refund</button>
            <button onclick="sendAction('escalate')">Escalate</button>
            <button onclick="sendAction('close_ticket')">Close</button>
        </div>

        <div class="card">
            <h3>Reward:</h3>
            <p id="reward">0</p>
        </div>

        <script>

            async function start() {
                let res = await fetch('/reset', {
                    method: "POST"
                });

                let data = await res.json();

                document.getElementById("message").innerText = data.customer_message;
                document.getElementById("reward").innerText = 0;
            }

            async function sendAction(actionType) {

                let message = "";

                if (actionType === "reply") {
                    message = "We are very sorry for the inconvenience.";
                }

                let res = await fetch('/step', {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        action_type: actionType,
                        message: message
                    })
                });

                let data = await res.json();

                if (data.error) {
                    alert(data.error);
                    return;
                }

                document.getElementById("reward").innerText = data.reward;

                if (data.done) {
                    alert("Task completed!");
                }
            }

            start();

        </script>

    </body>
    </html>
    """


@app.post("/reset")
def reset(task: str = "hard"):
    obs = env.reset(task)
    return obs


@app.post("/step")
def step(action: Action):
    if env.current_task is None:
        return {"error": "Call /reset first"}

    obs, reward, done, _ = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def state():
    return env.get_state()