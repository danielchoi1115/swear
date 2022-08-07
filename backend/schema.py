from pydantic import BaseModel
from datetime import datetime
class Message(BaseModel):
    sendFrom: int
    sendTo: int
    time: datetime
    message : str