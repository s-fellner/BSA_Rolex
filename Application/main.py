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

from flask import Flask, request, render_template
import predict

import sys
from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1
from google.cloud.automl_v1.proto import service_pb2

model_name = 'projects/685330484131/locations/eu/models/TCN4837384969284222976'

def inline_text_payload(content):
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def get_prediction(content):
  options = ClientOptions(api_endpoint='eu-automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  payload = inline_text_payload(content)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def evaluate():
        phrase = ''
        if request.method == "POST":
                phrase =  request.form.get('phrase')
                return get_prediction(phrase)
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
