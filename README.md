# BSA_Rolex 

This repository contains all the work done by the group Rolex for the project of Big Scale Analytics 2021.

We intend to assess the problem by building a text recognition classifier which, based on the learning sentences we buildt, would suggest the language level of the sentence. There could be different way to classify sentences : 
 - Based on the overall structure of the sentence (and also the time used for the verbs)
 - The overall lexical level of the sentence (proximity to english words, technical lexic, ...)
 - The use of expressions
 - The Context in which the sentence could be used (thesis, article, advertisement, meal, personnal letter, ...)

**Sentences dataset**
 - A1 : 199
 - A2 : 200
 - B1 : 223
 - B2 : 228
 - C1 : 203
 - C2 : 200
 **TOTAL : 1253**

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

# Sources

 **Litterature about language classification**
  - https://arxiv.org/pdf/1808.10556.pdf
  - https://monkeylearn.com/text-classification/
  - https://medium.com/swlh/language-classification-using-machine-learning-in-python-fa0768daea67
  - https://www.researchgate.net/publication/313841337_Classification_of_Speaking_Proficiency_Level_by_Machine_Learning_and_Feature_Selection
  - Automatic Classification of English Learner Proficiency Using Elicited Versus Spontaneous Data by Xiaoyu Bai

 **Language level :**
  - https://www.worddy.co/fr/magazine/connaitre-son-niveau-de-langue-selon-cecrl
  - https://www.france-langue.fr/niveaux-de-francais/
  - http://www.provincedeliege.be/sites/default/files/media/7476/Europass_-_European_language_levels_-_Self_Assessment_Grid.pdf

  **Sentences :**
  - https://lingua.com/fr/francais/lecture/
  - https://scripts.fandom.com/fr/wiki/OSS_117_:_Le_Caire,_nid_d%27espions
  - https://www.gqmagazine.fr/pop-culture/cinema/diaporama/100-rpliques-cultes/725?image=5b992a115e8dfe001124c9a5
  - https://www.wikipedia.fr/
  - https://www.leplaisirdapprendre.com/portfolio/selection-activites-comprehension-ecrite-a1-a2-b1-b2/
  - https://www.podcastfrancaisfacile.com/tag/intermediaire+texte
  - http://www.theses.fr/fr/?q=
  - https://dicocitations.lemonde.fr/citation.php?mot=these
  - https://www.francepodcasts.com/
  - http://mapage.noos.fr/r.ferreol/langage/archiduchesse.html
  - https://www.hobbesworld.com/dico/mots.php
  - https://www.linternaute.com/
  - Cybersécurité - 5e éd.: Sécurité informatique et réseaux Solange Ghernaouti
  - https://dicocitations.lemonde.fr/citation.php?mot=these
  - https://www.france-education-international.fr/sites/default/files/atoms/files/dalf-c2_sujet-demo1_candidat_coll_pe.pdf
