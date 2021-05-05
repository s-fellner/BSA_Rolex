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
### Step 1 📚

Do some literature reserach that could help us solve the problem : 

***Articles:***

- Flanagan, B., Hirokawa, S., Kaneko, E., & Izumi, E. (2017). Classification of Speaking Proficiency Level by Machine Learning and Feature Selection
- Preciado-Grijalva, A., & Brena, R. F. (2018). Speaker Fluency Level Classification Using Machine Learning Techniques
- Xiaoyu Bai (2018). Automatic Classification of English Learner Proficiency Using Elicited Versus Spontaneous Data

***Websites***

- https://monkeylearn.com/text-classification/
- https://medium.com/swlh/language-classification-using-machine-learning-in-python-fa0768daea67


### Step 2 📊

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
### Step 3 🖥️

Classify the sentences: 

We used google cloud services to classify the data. It is done with AutoMl from natural language, app engine and the automMl api. 
It is possible to adjust the sensibility of the model by balancing the precision and recal rate. 

***Results of the model***

- The overall precision of the model is 57,84%
- The overall recall of the model is 46,09%
- The F1 score of the model is 51,30%
- The per-class scores are : 

<img src="https://user-images.githubusercontent.com/74456180/116883278-b7105380-ac25-11eb-87b7-943c2e1bc6b3.png" width="200" height="200">

- The confusion Matrix of the model is : 

<img src="https://user-images.githubusercontent.com/74456180/117110810-fb673500-ad86-11eb-8df8-68fa9df088a1.png" width="500" height="300">

## Milestone 3

To increase the accuracy of the model, we reused the cognates seen in the assignment to built a table of the 500000 more used cognates. 
We will then calculate the cognates'percentaga in each sentence to evaluate the level. 
