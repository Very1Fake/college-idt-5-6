from bottle import post, request

@post('/home', method='post')
def form():
    email = request.forms.get('EMAIL')
    return f'''
        Thanks for your feedback! The answer will be sent to your email "{email}".<br/><br/><br/>
        You will be redirected to home page in 3 seconds.<br/>
        <a href="/">Click here</a> if weren't redirected.
        <script>
            window.setTimeout(function() {{
                window.location.href = "/";
            }}, 3000);
        </script>
    '''
