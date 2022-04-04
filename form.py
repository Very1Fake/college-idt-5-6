import re
import pdb

from bottle import post, request

# Questions storage
questions = {}

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

@post('/home', method='post')
def form():
    err = None
    question = request.forms.get('QUESTION')
    email = request.forms.get('EMAIL')

    if question is None or question == '':
        err = "Empty question field"
    elif len(question) < 16:
        err = "Question too short (min 16 symbols)"
    else:
        if email is None or email == '':
            err = "Empty email field"
        elif email_regex.match(email) is None or len(email) > 254:
            err = "Invalid email address"

    questions[email] = question
    pdb.set_trace()
    return (
        f'Thanks for your question! The answer will be sent to your email "{email}".'
        if err is None else
        f'Your question hasn\'t been accepted. Due to an error: {err}'
    ) + redirect_ext
