import time
import random
crontable = []
outputs = []
convos = {}
responses = ["Why?", "Interesting. Why?", "Okay. But why?", "Keep going. Why?", "Right, I see. Why?"]
TIME_LIMIT_SECS = 300


def process_message(data):
    ch = str(data['channel'])
    now = time.time()

    if not convos.has_key(ch):
        convos[ch] = {"why_count": 0, "last_message": now}

    this_convo = convos[ch]

    if (now - convos[ch]["last_message"]) > TIME_LIMIT_SECS:
        this_convo["why_count"] = 0

    if this_convo["why_count"] >= 5:
        outputs.append([ch, "OK, enough of that! Thanks!"])
        this_convo["why_count"] = 0
    else:
        outputs.append([data['channel'], random.choice(responses)])
        this_convo["why_count"] += 1

    this_convo["last_message"] = now
