from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    return '''
<html>
    <head>
        <title>Home Page- testpy</title>
    </head>
    <body>
        <h1>Hello,''' + user['username'] + '''!</h1>
    </body>
</html>'''