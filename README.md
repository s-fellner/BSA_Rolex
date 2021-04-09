# Big scale_Team Rolex ⌚

**Team members**

 - Déborah Hernandez 
 - Simon Fellner 
 - Maxime Dubi

This repository contains all the work done by the group Rolex for the project of Big Scale Analytics 2021.

## Project description 🗂️

The goal of the project is to build a model for predicting the difficulty level of a french sentence. The level concerns the reading understanding of the sentence for a native english speaker. The levels are ranked from A1 which correspond to beginner, to C1 which correspond to proficiency. 

We intend to assess the problem by building a text classifier which, based on the learning sentences we built, would suggest the language level of the sentence. 

## Methodology 🤓 

### Step 1

Do some literature reserach that could help us solve the problem : 

***Articles:***

- Flanagan, B., Hirokawa, S., Kaneko, E., & Izumi, E. (2017). Classification of Speaking Proficiency Level by Machine Learning and Feature Selection
- Preciado-Grijalva, A., & Brena, R. F. (2018). Speaker Fluency Level Classification Using Machine Learning Techniques
- Xiaoyu Bai (2018). Automatic Classification of English Learner Proficiency Using Elicited Versus Spontaneous Data

***Websites***

- https://monkeylearn.com/text-classification/
- https://medium.com/swlh/language-classification-using-machine-learning-in-python-fa0768daea67


**Step 2** 

Collect the dataset : 

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


The labelled data is uploaded here as CSV. 

***Sentences dataset***
 - A1 : 199 | 16%
 - A2 : 200 | 16%
 - B1 : 223 | 18%
 - B2 : 228 | 18%
 - C1 : 203 | 16%
 - C2 : 200 | 16%
 
 ***TOTAL : 1253***
 
 There are more than 1000 sentences, but for the model building, we'll keep 200 sentences per level.

**Step 3**



There could be different way to classify sentences : 
 - Based on the overall structure of the sentence (and also the time used for the verbs)
 - The overall lexical level of the sentence (proximity to english words, technical lexic, ...)
 - The use of expressions
 - The Context in which the sentence could be used (thesis, article, advertisement, meal, personnal letter, ...)

text classifier: auto ML 



# Log

**01.03**
 - Find CECRL scale (A1, A2, ...) evaluation system to assess the problem more precisely
 - Using contacts to find texts of each level (language school, ...)
 - Problem can be assessed globaly (global structure like article ? or like personnal letter ? ...)
 - Or can be assessed precisely, sentence per sentence and then averaged

**08.03**
 - Building data (sentences) based on texts found on internet : approx. 850 labelised sentences

**15.03**
 - Finishing data building (about 200 sentences per level)


 
  

