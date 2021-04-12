# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
# [START gae_python3_render_template]

from google.cloud import automl

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="clefadmin.json"

# You must first create a dataset, using the `eu` endpoint, before you can
# call other operations such as: list, get, import, delete, etc.
client_options = {'api_endpoint': 'eu-automl.googleapis.com:443'}

# TODO(developer): Uncomment and set the following variables
project_id = '685330484131'
model_id = 'TCN4837384969284222976'

prediction_client = automl.PredictionServiceClient(client_options=client_options)

# Get the full path of the model.
model_full_id = automl.AutoMlClient.model_path(project_id, "eu", model_id)

# Supported mime_types: 'text/plain', 'text/html'
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#textsnippet
def predict(content):
  text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
  payload = automl.ExamplePayload(text_snippet=text_snippet)

  response = prediction_client.predict(name=model_full_id, payload=payload)
  return response

from flask import Flask, request, render_template
    
app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def evaluate():
        phrase = ''
        if request.method == "POST":
            phrase =  request.form.get('phrase')
            if phrase != '':
                lvl = predict(phrase)
                top_score = lvl.payload[0]. classification.score
                top_cat = lvl.payload[0].display_name
                phrase = top_cat
        return render_template("index.html", phrase = phrase)        

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
