from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
project_id = 685330484131
model_id = 'TCN4837384969284222976'

prediction_client = automl.PredictionServiceClient()

# Get the full path of the model.
model_full_id = automl.AutoMlClient.model_path(project_id, "eu", model_id)

# Supported mime_types: 'text/plain', 'text/html'
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#textsnippet

def lvl_predict(content):
    text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
    payload = automl.ExamplePayload(text_snippet=text_snippet)
    response = prediction_client.predict(name=model_full_id, payload=payload)

    for annotation_payload in response.payload:
        answer = "Predicted class name: {}".format(annotation_payload.display_name)) + "Predicted class score: {}".format(annotation_payload.classification.score)
    return answer