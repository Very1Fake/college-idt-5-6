import re

from bottle import post, request

# Short regex of IETF RFC 5322
email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


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
        elif email_regex.match(email) is None:
            err = "Invalid email address"

    if err is None:
        return f'Thanks for your question! The answer will be sent to your email "{email}".' \
            + redirect_ext
    else:
        return f'Your question hasn\'t been accepted. Due to an error: {err}'
