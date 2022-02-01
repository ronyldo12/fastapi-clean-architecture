from datetime import datetime
import uuid

class Entity():
    id: str
    created_at: str
    updated_at: str
    deleted_at: str

    def __init__(self) -> None:
        now = datetime.now()
        self.created_at = now.strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        self.deleted_at = ''

    def new_id(self):
        self.id = str(uuid.uuid4())