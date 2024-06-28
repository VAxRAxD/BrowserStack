from flask import Flask, make_response

app = Flask(__name__)
@app.route('/')
def hello_world():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BrowserStack</title>
    </head>
    <body>
        <h1>Hello, <b style="color:orange">BrowserStack</b></h1>
        <h3>I am <span style="font-style: italic">Automation Support Engineer<span></h3>
        <h5 style="color:red;">I solve real problems</h5>
        <button class="link-button" onclick="location.href='https://github.com/VAxRAxD'">Go to Github</button>
    </body>
    </html>
    """
    return make_response(html_content)

if __name__ == '__main__':
    app.run(debug=True)