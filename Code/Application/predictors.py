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

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="clefadmin.json"

##### API of Google automl natural language
# Supported mime_types: 'text/plain', 'text/html'
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#textsnippet
def predict(content):

  from google.cloud import automl

  # You must first create a dataset, using the `eu` endpoint, before you can
  # call other operations such as: list, get, import, delete, etc.
  client_options = {'api_endpoint': 'eu-automl.googleapis.com:443'}
  project_id = '685330484131'
  # (model AI Crowd) model_id = 'TCN3300918624537018368'
  model_id = 'TCN4629621252099670016'

  prediction_client = automl.PredictionServiceClient(client_options=client_options)

  # Get the full path of the model.
  model_full_id = automl.AutoMlClient.model_path(project_id, "eu", model_id)
  text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
  payload = automl.ExamplePayload(text_snippet=text_snippet)

  response = prediction_client.predict(name=model_full_id, payload=payload)
  return response
##### END


##### API for google automl table
# Copyright 2019 Google LLC
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

"""This application demonstrates how to perform basic operations on prediction
with the Google AutoML Tables API.
For more information, the documentation at
https://cloud.google.com/automl-tables/docs.
"""

import argparse


def predictables(
    project_id,
    compute_region,
    model_display_name,
    inputs,
    feature_importance=None,
    print=None,
):
    """Make a prediction."""
    # [START automl_tables_predict]

    from google.cloud import automl_v1beta1 as automl

    client = automl.TablesClient(project=project_id, region=compute_region)

    if feature_importance:
        response = client.predict(
            model_display_name=model_display_name,
            inputs=inputs,
            feature_importance=True,
        )
    else:
        response = client.predict(
            model_display_name=model_display_name, inputs=inputs
        )

    if print:
      print("Prediction results:")
      for result in response.payload:
          print(
              "Predicted class name: {}".format(result.tables.value)
          )
          print("Predicted class score: {}".format(result.tables.score))

          if feature_importance:
              # get features of top importance
              feat_list = [
                  (column.feature_importance, column.column_display_name)
                  for column in result.tables.tables_model_column_info
              ]
              feat_list.sort(reverse=True)
              if len(feat_list) < 10:
                  feat_to_show = len(feat_list)
              else:
                  feat_to_show = 10

              print("Features of top importance:")
              for feat in feat_list[:feat_to_show]:
                  print(feat)
        
    return response

    # [END automl_tables_predict]
#####END


##### custom Tokenizer setting
# Loading every module needed :
import pandas as pd
import re 
import string


import spacy
import fr_core_news_sm
sp = spacy.load('fr_core_news_sm')

# Loading our custom cognate list
cognates_df = pd.read_csv("https://raw.githubusercontent.com/s-fellner/BSA_Rolex/main/Data/Cognates_2.1.csv", sep=',')
cognates = cognates_df['cognates'].to_list()

# Create a list of stopwords
stop_words = spacy.lang.fr.stop_words.STOP_WORDS

# Create a list of punctuation marks
punctuations = string.punctuation

def spacy_tokenizer(sentence):

  # Create token object, which is used to create documents with linguistic annotations.
  mytokens = sp(sentence)

  # Lemmatize each token and convert each token into lowercase
  mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]

  # Remove stop words and punctuation
  mytokens = [word for word in mytokens if word not in stop_words and word not in punctuations]

  mytokens = [word for word in mytokens if len(word)>1]

  # Return preprocessed list of tokens
  return mytokens
##### END


##### Function to shape a sentence accordingly to data format constraints of google automl

def mef(sentence, col):

#Init
  df = pd.DataFrame()
  sen = []

#Adding sentence in a list
  sen.append(sentence)

#Entering the list in the DF
  df[col] = sen

#Create a column "tokenizer" on which the custom tokenizer is applied
  df['tokenized'] = df[col].apply(spacy_tokenizer)

#Init of 3 lists for the additionnal features
  wordnb = []
  cognate = []
  punctuation = []

#Loop to generate our additionnal features to the DF
  x=0
  while x < df.shape[0]:
    cogs = []
    wordnb.append(len(re.findall(r'\w+', df[col][x])))
    punctuation.append(len(re.findall(r'[.?\-",]+', df[col][x])))
    for token in df['tokenized'][x]:
      if token in cognates:
        cogs.append(token)
    cognate.append(cogs)
    x+=1

  df['wordnb'] = wordnb
  df['cognate'] = cognate
  df['cognatenb'] = df.cognate.map(len)
  df['cognateratio'] = df['cognatenb'] / df['wordnb']
  df['punctuation'] = punctuation
  df['token_nb'] = df.tokenized.map(len)
  df['tokenratio'] = df['token_nb'] / df['wordnb']

  return df
##### END


##### Complete prediction function which do 2 predictions (one on natural language and one on table)
# monitor = True if predictions are used in the Monitor model (specific format)
# print = True to give more details in the prediction process

def full_pred(sentence, monitor=None, print=None):

# formating the sentence
  sentence_df = mef(sentence, 'sentence')

# Natural language prediction
  nl_response = predict(sentence)

# best class predicted retrieved
  nl_top_score = nl_response.payload[0].classification.score
  nl_top_cat = nl_response.payload[0].display_name

# Response init
  response={}

# special format if monitor = True : Full scores are needed
  if monitor:
    for entry in nl_response.payload:
      response['nl_' + entry.display_name]=entry.classification.score

# table prediction
  tl_response = predictables(685330484131, 'us-central1', "Train_3000_Feat", {
      "cognatenb": sentence_df['cognatenb'][0].astype(float),
      "cognateratio": sentence_df['cognateratio'][0].astype(float),
      "punctuation": sentence_df['punctuation'][0].astype(float),
      "sentence": sentence_df['sentence'][0],
      "token_nb": sentence_df['token_nb'][0].astype(float),
      "tokenratio": sentence_df['tokenratio'][0].astype(float),
      "wordnb": sentence_df['wordnb'][0].astype(float),
      "cognate": str(sentence_df['cognate'][0]),
      "tokenized": str(sentence_df['tokenized'][0])})

# saving variable init
  tl_top_score = 0.0
  tl_top_cat = ''

# Finding best class and score
  for entry in tl_response.payload:
    if entry.tables.score > tl_top_score:
      tl_top_score = entry.tables.score
      tl_top_cat = entry.tables.value
  
  response['nl_score']=nl_top_score
  response['nl_cat']=nl_top_cat
  response['tl_score']=tl_top_score
  response['tl_cat']=tl_top_cat

# special format if monitor = True : Full scores are needed
  if monitor:
    for entry in tl_response.payload:
      response['tl_' + entry.tables.value]=entry.tables.score

# if print : printing the local scores
  if print:
    print('Natural language response :', round(nl_top_score*100, 1) , '% level' , nl_top_cat)
    print('AutoML Tables response :', round(tl_top_score*100,1) , '% level' , tl_top_cat)

  return response
##### END


##### Monitor model API (google automl table)
def Monitor_Classification(entry):
    response = predictables(685330484131, 'us-central1', "Train_Monitor_full", 
                            {'nl_A1': entry['nl_A1'],
                            'nl_A2': entry['nl_A2'],
                            'nl_B1': entry['nl_B1'],
                            'nl_B2': entry['nl_B2'],
                            'nl_C1': entry['nl_C1'],
                            'nl_C2': entry['nl_C2'],
                            'nl_cat': entry['nl_cat'],
                            'nl_score': entry['nl_score'],
                            'tl_A1': entry['tl_A1'],
                            'tl_A2': entry['tl_A2'],
                            'tl_B1': entry['tl_B1'],
                            'tl_B2': entry['tl_B2'],
                            'tl_C1': entry['tl_C1'],
                            'tl_C2': entry['tl_C2'],
                            'tl_cat': entry['tl_cat'],
                            'tl_score': entry['tl_score']})
    
    to_return = {}

    top_score = 0
    top_cat = ''

    for result in response.payload:
      if result.tables.score > top_score:
        top_score = result.tables.score
        top_cat = result.tables.value

    to_return['top_score'] = top_score
    to_return['top_cat'] = top_cat

    return to_return
##### END
