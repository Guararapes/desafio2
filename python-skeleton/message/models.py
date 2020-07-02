import json
from datetime import datetime

from django_sorcery.db import databases

db = databases.get("default")


class Message(db.Model):
    pk = db.Column(db.Integer(), primary_key=True)
    event = db.Column(db.String(length=256))
    message_raw = db.Column(db.String())
    error_message = db.Column(db.String())
    dispatched_at = db.Column(db.DateTime(), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=True)
    version = db.Column(db.TIMESTAMP(), nullable=False)
    locked = db.Column(db.Boolean(), nullable=False)

    undelivered = db.queryproperty(dispatched_at=None)

    __mapper_args__ = {
        "version_id_col": version,
        'version_id_generator': lambda version: datetime.now()
    }

    def __int__(self):
        self.locked = False

    @property
    def message(self):
        return json.loads(self.message_raw)

    @message.setter
    def message(self, message):
        self.message_raw = json.dumps(message)

    def lock(self):
        self.locked = True
        db.commit()
