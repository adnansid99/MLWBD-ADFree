import flask
from time import sleep
from src.bypass import *
from src.search import *

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'POST':
        search_query = flask.request.form["userInput"]
        search_result = json.loads(search(search_query))
        return flask.render_template('home.html', itemsJson=search_result)
    else:
        search_result = json.loads(search(''))
        return flask.render_template('home.html', itemsJson=search_result)
    

@app.route("/bypass/<mainurl>", methods=["GET", "POST"])
async def index(mainurl):
    if flask.request.method == "POST":
        mainUrl = flask.request.form["myInput"]
        user_Input = "https://mlwbd.media/movie/"+mainUrl
        try:
            return_data = await main(user_Input)
            extracted_FU = await extract_data_between_strings(return_data, '<form method="post" action="https://namemeaningbengali.com/" rel="nofollow"><input type="hidden" name="FU5" value="', '"')
            return flask.render_template('bypassed.html', extracted_FU=extracted_FU)
        except Exception as e:
            error_message = type(e).__name__
            sleep(2)
            return flask.render_template('error.html', error_message=error_message)
    else:
        return flask.render_template('loading.html', mainurl=mainurl)


if __name__ == '__main__':
    app.run(port=443)
