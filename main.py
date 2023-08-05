import flask
from time import sleep
from bypass import *
from search import *

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'POST':
        search_query = flask.request.form["userInput"]
        search_result = json.loads(search(search_query))
        return flask.render_template('home.html', itemsJson=search_result)
    else:
        return flask.render_template('home.html')

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if flask.request.method == 'POST':
#         search_query = flask.request.form["userInput"]
#         search_result = json.loads(search(search_query))
#         return flask.render_template('home.html', itemsJson=search_result)
#     else:
#         return flask.render_template('home.html')


@app.route("/name/<mainurl>")
def index(mainurl):
        user_Input = "https://mlwbd.love/movie/"+mainurl
        # print(user_Input)
        try:
            # scraper.get(user_Input)
            return_data = main(user_Input)
            extracted_FU = extract_data_between_strings(return_data, '<form method="post" action="https://namemeaningbengali.com/" rel="nofollow"><input type="hidden" name="FU5" value="', '"')
            return flask.render_template('bypassed.html', extracted_FU=extracted_FU)
        except Exception as e:
            error_message = type(e).__name__
            sleep(2)
            return flask.render_template('error.html', error_message=error_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9797, debug=True)