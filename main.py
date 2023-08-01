import flask
from time import sleep
from bypass import *

app = flask.Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if flask.request.method == 'POST':
        user_Input = flask.request.form["input"]
        try:
            requests.get(user_Input)
            return_data = main(user_Input)
            extracted_FU = extract_data_between_strings(return_data, '<form method="post" action="https://namemeaningbengali.com/" rel="nofollow"><input type="hidden" name="FU5" value="', '"')
            return flask.render_template('bypassed.html', extracted_FU=extracted_FU)
        except Exception as e:
            error_message = type(e).__name__
            sleep(2)
            return flask.render_template('error.html', error_message=error_message)
    else:
        return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)