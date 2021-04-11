import sys

from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1
from google.cloud.automl_v1.proto import service_pb2

def inline_text_payload(content):
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def get_prediction(content, model_name):
  options = ClientOptions(api_endpoint='eu-automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  payload = inline_text_payload(content)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned

if __name__ == '__main__':
  file_path = sys.argv[1]
  model_name = sys.argv[2]

  print get_prediction(content, model_name)
