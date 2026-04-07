from env.environment import SupportEnv
from env.models import Action

env = SupportEnv()

# Test EASY task
obs = env.reset("easy")
print("Initial:", obs)

done = False
total_reward = 0

while not done:
    action = Action(
        action_type="reply",
        message="You can reset your password using the reset link."
    )

    obs, reward, done, _ = env.step(action)
    
    print("Reward:", reward)
    total_reward += reward

    # close ticket
    action = Action(action_type="close_ticket")
    obs, reward, done, _ = env.step(action)

    print("Final Reward:", reward)
    total_reward += reward

print("Total Score:", total_reward)