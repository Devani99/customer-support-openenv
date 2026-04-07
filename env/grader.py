def grade_step(task, state, action, step_count):
    reward = 0.0
    done = False
    info = {}

    msg = (action.message or "").lower()

    # -------------------------
    # GENERAL REWARD SHAPING
    # -------------------------
    if action.message:
        reward += 0.1

    if not action.message and action.action_type == "reply":
        reward -= 0.1

    # -------------------------
    # EASY TASK
    # -------------------------
    if "password" in task["goal"].lower():
        if "reset" in msg:
            reward += 0.4

        if action.action_type == "close_ticket":
            reward += 0.5
            done = True

    # -------------------------
    # MEDIUM TASK
    # -------------------------
    elif "refund" in task["goal"].lower() and "angry" not in task["goal"].lower():
        if action.action_type == "issue_refund":
            reward += 0.5

        if action.action_type == "close_ticket":
            reward += 0.4
            done = True

    # -------------------------
    # HARD TASK
    # -------------------------
    elif "angry" in task["goal"].lower():

        # STEP 1 → empathy
        if step_count == 1:
            if "sorry" in msg or "apolog" in msg:
                reward += 0.3
            else:
                reward -= 0.1  # softer penalty

            if action.action_type in ["issue_refund", "escalate"]:
                reward += 0.1  # mild penalty

        # STEP 2 → resolution
        elif step_count == 2:
            if action.action_type in ["issue_refund", "escalate"]:
                reward += 0.4
            else:
                reward -= 0.1

        # closing
        if action.action_type == "close_ticket":
            reward += 0.2
            done = True

    # -------------------------
    # EFFICIENCY PENALTY
    # -------------------------
    if step_count > 3:
        reward -= 0.05

    # -------------------------
    # CLAMP REWARD (VERY IMPORTANT)
    # -------------------------
    reward = max(0.0, min(1.0, reward))

    return reward, done, info