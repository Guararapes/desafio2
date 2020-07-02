import logging
import sys

from django.apps import AppConfig

log = logging.getLogger('jobs')


class MessageConfig(AppConfig):
    name = 'message'
