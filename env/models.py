from pydantic import BaseModel
from typing import List, Optional, Literal

class Observation(BaseModel):
    ticket_id: str
    customer_message: str
    conversation_history: List[str]
    sentiment: float
    urgency: int
    resolved: bool = False


class Action(BaseModel):
    action_type: Literal[
        "reply",
        "ask_clarification",
        "issue_refund",
        "escalate",
        "close_ticket"
    ]
    message: Optional[str] = None


class Reward(BaseModel):
    value: float
    reason: str