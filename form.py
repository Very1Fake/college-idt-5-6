from pathlib import Path
import re
import json
import atexit
from time import time

from bottle import post, request

# Log path
LOG_PATH = "./questions.log.json"
# Questions log storage
questions = {}

# Load log if exists
if Path(LOG_PATH).is_file():
    with open(LOG_PATH, "r") as log:
        questions = json.load(log)

# Exit handler. Used to save log to `questions.log.json`
def exit_log_handler():
    with open(LOG_PATH, "w+") as log:
        json.dump(questions, log, indent=4)

atexit.register(exit_log_handler)

# Short regex of IETF RFC 5321 4.5.3.1
email_regex = re.compile(r"^((?!\.)[a-z0-9.]{1,64}(?<!\.))@((?!-)[a-z0-9-]{1,63}(?<!-)\.)+[a-z]{2,6}$")


redirect_ext = '''<br/><br/><br/>
You will be redirected to home page in 3 seconds.<br/>
<a href="/">Click here</a> if weren't redirected.
<script>
    window.setTimeout(function() {{
        window.location.href = "/";
    }}, 3000);
</script>
'''

def validate(question, email):
    err = None
    if question is None or question == '':
        err = "Empty question field"
    elif len(question) < 16:
        err = "Question too short (min 16 symbols)"
    else:
        if email is None or email == '':
            err = "Empty email field"
        elif email_regex.match(email) is None or len(email) > 254:
            err = "Invalid email address"
    
    return err

@post('/home', method='post')
def form():
    question = request.forms.get('QUESTION')
    email = request.forms.get('EMAIL')
    err = validate(question, email)

    # Appending to log (with timestamp)
    if email not in questions:
        questions[email] = []

    questions[email].append({
        "question": question,
        "timestamp": int(time()),
    })

    return (
        f'Thanks for your question! The answer will be sent to your email "{email}".'
        if err is None else
        f'Your question hasn\'t been accepted. Due to an error: {err}'
    ) + redirect_ext
