from env.models import Observation, Action
from env.tasks import get_task
from env.grader import grade_step

class SupportEnv:
    def __init__(self):
        self.current_task = None
        self.state = None
        self.steps = 0

    def reset(self, task_id="easy"):
        self.current_task = get_task(task_id)
        self.state = Observation(**self.current_task["initial_state"])
        self.steps = 0
        return self.state

    def step(self, action):
        if self.current_task is None:
            raise ValueError("Environment not initialized. Call reset() first.")

        self.steps += 1

        reward, done, info = grade_step(
            self.current_task,
            self.state,
            action,
            self.steps
        )

        if action.message:
            self.state.conversation_history.append(
                f"Agent: {action.message}"
            )

        if action.action_type == "close_ticket":
            self.state.resolved = True
            done = True

        return self.state, reward, done, info

    def get_state(self):
        return self.state