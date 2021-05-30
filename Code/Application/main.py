# Import flask
from flask import Flask, request, render_template

app = Flask(__name__)

# Load our precit functions (API of NL, Tables and our Monitor Classifier)
from predict import full_pred, Monitor_Classification


@app.route('/', methods =['GET', 'POST'])
def evaluate():
        phrase = ''
        top_cat = ''
        top_score = ''
        if request.method == "POST":
            phrase =  request.form.get('phrase')
            if phrase != '':
                full_prediction = full_pred(phrase, monitor=True)
                monitor_pred = Monitor_Classification(full_prediction)
                phrase = '"' + phrase + '"'
                top_score = ' with a probability of ' + str(round(monitor_pred['top_score'] * 100, 2)) + '%.'
                top_cat = 'Level ' + str(monitor_pred['top_cat'])
        return render_template("index.html", phrase = phrase, top_cat = top_cat, top_score = top_score)          

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
