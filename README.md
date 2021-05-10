![585e9f11cb11b227491c3502](https://user-images.githubusercontent.com/74456354/114553079-8d3ac100-9c65-11eb-910d-816316ef4790.png)


# Big scale_Team Rolex ⌚

**WEB APPLICATION IN DEVELOPMENT** 👉 https://rich-wavelet-306313.oa.r.appspot.com/

**Team members**

 - Déborah Hernandez 
 - Simon Fellner 
 - Maxime Dubi

This repository contains all the work done by the group Rolex for the project of Big Scale Analytics 2021.

## Project description 🗂️

The goal of the project is to build a model for predicting the difficulty level of a french sentence. The level concerns the reading understanding of the sentence for a native english speaker. The levels are ranked from A1 which correspond to beginner, to C1 which correspond to proficiency. 

We intend to assess the problem by building a text classifier which, based on the learning sentences we built, would suggest the language level of the sentence. 

## Methodology 🤓 

## Milestone 1
### Step 1 📚 Literature

Do some literature reserach that could help us solve the problem : 

***Articles:***

- Flanagan, B., Hirokawa, S., Kaneko, E., & Izumi, E. (2017). Classification of Speaking Proficiency Level by Machine Learning and Feature Selection
- Preciado-Grijalva, A., & Brena, R. F. (2018). Speaker Fluency Level Classification Using Machine Learning Techniques
- Xiaoyu Bai (2018). Automatic Classification of English Learner Proficiency Using Elicited Versus Spontaneous Data

***Websites***

- https://monkeylearn.com/text-classification/
- https://medium.com/swlh/language-classification-using-machine-learning-in-python-fa0768daea67


### Step 2 📊 Dataset

Collect the dataset : 

The labelled data is uploaded in our repository as CSV. 

***Sentences dataset***
 - A1 : 199 | 16%
 - A2 : 228 | 18%
 - B1 : 223 | 17%
 - B2 : 228 | 18%
 - C1 : 203 | 16%
 - C2 : 200 | 16%
 
 ***TOTAL : 1281***
 
There are more than 1000 sentences, but for the model building, we'll keep 200 sentences per level.


We collected the french sentences from websites with exercices for non-french speakers and from articles about specific topics : 

***Exercices de langue***

- https://lingua.com/fr/francais/lecture/
- https://www.leplaisirdapprendre.com/portfolio/selection-activites-comprehension-ecrite-a1-a2-b1-b2/
- https://www.podcastfrancaisfacile.com/tag/intermediaire+texte
- https://www.francepodcasts.com/
- https://www.france-education-international.fr/sites/default/files/atoms/files/dalf-c2_sujet-demo1_candidat_coll_pe.pdf

***Citations de livres ou films***

- https://scripts.fandom.com/fr/wiki/OSS_117_:_Le_Caire,_nid_d%27espions
- https://www.gqmagazine.fr/pop-culture/cinema/diaporama/100-rpliques-cultes/725?image=5b992a115e8dfe001124c9a5
- https://dicocitations.lemonde.fr/citation.php?mot=these
- http://mapage.noos.fr/r.ferreol/langage/archiduchesse.html

***Thèses***

- http://www.theses.fr/fr/?q=

***Dictionnaire***

- https://www.hobbesworld.com/dico/mots.php

***Articles spécifiques***

- https://www.linternaute.com/
- https://www.wikipedia.fr/
- Solange Ghernaouti (2016) Cybersécurité - 5e éd.: Sécurité informatique et réseaux
 

To label the data with the difficulty levels, we found some criterias in the internet : 

 - https://www.worddy.co/fr/magazine/connaitre-son-niveau-de-langue-selon-cecrl
 - https://www.france-langue.fr/niveaux-de-francais/
 - http://www.provincedeliege.be/sites/default/files/media/7476/Europass_-_European_language_levels_-_Self_Assessment_Grid.pdf

## Milestone 2
### Step 3 🔎 First model

Classify the sentences: 

For our first model, we used google cloud services to classify the data. We only uploaded our dataset on AutoMl from natural language. 
It is possible to adjust the sensibility of the model by balancing the precision and recal rate. 

A DEVELOPPER???

***Results of the model***

- The overall precision of the model is 57,84%
- The overall recall of the model is 46,09%
- The F1 score of the model is 51,30%
- The per-class scores are : 

<img src="https://user-images.githubusercontent.com/74456180/116883278-b7105380-ac25-11eb-87b7-943c2e1bc6b3.png" width="200" height="200">

- The confusion Matrix of the model is : 

<img src="https://user-images.githubusercontent.com/74456180/117110810-fb673500-ad86-11eb-8df8-68fa9df088a1.png" width="500" height="350">

By looking at misclassified samples, we can say that 

BLABLA!!!

### Step 4 🖥️ API and UI

To create the API, we worked with app engine and the automMl API. We coded a python code to make a functionnal API. We made some HTML code to create the UI and make it look fancy. 

Our callable API and UI can be found in this link : https://rich-wavelet-306313.oa.r.appspot.com/

## Milestone 3
### Step 5 📈 Improve the model

***Model 2***

To increase the accuracy of the model, we made some feature engineering still with Natural Language. To do so, we used : 

- The total number of words of the phrase 
- The list of cognates present in the phrase
- The number of cognates in the phrase
- The ratio of cognates in the phrase (number of cognates over total number of words)
- The number of punctuation

To find the cognates in the phrases, we reused the exercise of the course's assignment where we had to find the cognates with the highest term frequency in english (not considering those where the difference between the term frequency in French and in English exceed 1,000,000). We cleaned the cognates dictionnary to delete the numbers. We buidt a table with 500,000 cognates. 

***Results of the model***

- The overall precision of the model is 43,48%
- The overall recall of the model is 31,25%
- The F1 score of the model is 36,36%

We note that this model did not improve our results. Indeed, we don't have a lot of information about how AutoML works and how it creates the models. Thanks to this model, we understood that it does not interpret the different features, it only takes into account the meaning of the phrase.

***Model 3***

We used the Tables module of google cloud platform. It allow us to sturucture our data per features. It supports different types of formats for each feature and detects the correlation with the target. Then it built the optimal model on several features as we can see in the picture below. 

<img src="https://user-images.githubusercontent.com/74456180/117634742-84afaa80-b17f-11eb-9165-6ffffc815862.png" width="1700" height="200">

IMPROVEMENT

To improve the model 3, we decided to do some preprocess on our data. Here are the steps: 

- We tockenized the sentences with spicy 
- we extracted the cognates from the tokens 
- We vectorized the sentences with Tfidf

***Model 4***

The final model will be a combination of the model 1 and 3. 
