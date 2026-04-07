def get_task(task_id):
    tasks = {
        "easy": {
            "goal": "Help reset password",
            "initial_state": {
                "ticket_id": "T1",
                "customer_message": "How do I reset my password?",
                "conversation_history": [],
                "sentiment": 0.2,
                "urgency": 2
            }
        },
        "medium": {
            "goal": "Handle double charge refund",
            "initial_state": {
                "ticket_id": "T2",
                "customer_message": "I was charged twice!",
                "conversation_history": [],
                "sentiment": -0.3,
                "urgency": 4
            }
        },
        "hard": {
            "goal": "Handle angry customer + refund/escalation",
            "initial_state": {
                "ticket_id": "T3",
                "customer_message": "Worst service ever!! Refund NOW!",
                "conversation_history": [],
                "sentiment": -0.9,
                "urgency": 5
            }
        }
    }

    return tasks[task_id]