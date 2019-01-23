from slackbot.bot import listen_to
import random

serif = []
serif_file = "plugins/serif_merlin.txt"
with open(serif_file, 'r') as f:
    serif = [l.strip() for l in f.readlines()]

prefix = ['おはよう！', 'おはようマスター。']

@listen_to('しゅっしゃ')
def listen_func(message):
    message.send(random.choice(prefix) + random.choice(serif))
