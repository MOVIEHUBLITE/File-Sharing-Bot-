import re
import os
from os import environ



id_pattern = re.compile(r'^.\d+$')

STAT_STICK = os.environ.get("STAT_STICK", "CAACAgIAAxkBAAIER2KU31lwWVS9nDiKrEWNn6UVtbT3AAJoAAPb234AAf0R7Tldu9yTHgQ")

PICS = os.environ.get("PICS", "https://telegra.ph/file/cb77c8e2ebf3473c9fbcf.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '1467649219').split()]

DELAY = int(os.environ.get("DELAY", "2"))
