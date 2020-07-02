from datetime import datetime
from unittest.mock import patch

from django.test import TestCase
from message.models import db, Message


class TestSendMessages(TestCase):
    def setUp(self) -> None:
        db.create_all()

    def test_should_send_next_message(self):
        pass


class HealthCheckTest(TestCase):
    def test_should_check_topic_starter(self):
        pass
