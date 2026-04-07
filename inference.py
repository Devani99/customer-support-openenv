import os
from env.environment import SupportEnv
from env.models import Action

env = SupportEnv()


def agent(observation):
    msg = observation.customer_message.lower()

    if "password" in msg:
        return Action(action_type="reply", message="Reset using link")

    elif "charged" in msg or "refund" in msg:
        return Action(action_type="issue_refund", message="Refund issued")

    elif "worst" in msg or "refund now" in msg:
        return Action(action_type="reply", message="We are sorry for inconvenience")

    return Action(action_type="close_ticket", message="Resolved")


def run_task(task):
    print(f"[START] task={task}")

    obs = env.reset(task)
    done = False
    total_reward = 0
    step_id = 0

    while not done and step_id < 10:
        action = agent(obs)

        obs, reward, done, _ = env.step(action)

        print(f"[STEP] step={step_id} action={action.action_type} reward={reward}")

        total_reward += reward
        step_id += 1

        if not done:
            obs, reward, done, _ = env.step(
                Action(action_type="close_ticket")
            )
            total_reward += reward

    print(f"[END] task={task} total_reward={round(total_reward,2)}\n")


if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        run_task(t)