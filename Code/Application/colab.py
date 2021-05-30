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

x = predict("J'aime les chats.")

top_score = x.payload[0]. classification.score
top_cat = x.payload[0].display_name

print('Niveau de langue :', top_cat, ' avec un indice de confiance de :', round(top_score * 100), '%.')
