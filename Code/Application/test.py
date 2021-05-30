from predictors import full_pred, Monitor_Classification

test = full_pred('Ceci est un test', monitor=True)
test_moni = Monitor_Classification(test)

top_score = ' with a probability of ' + str(round(test_moni['top_score'] * 100, 2)) + '%.'
top_cat = 'level :'+ str(test_moni['top_cat'])

print(top_cat, top_score)
