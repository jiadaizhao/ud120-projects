#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print "accuracy is ", clf.score(features, labels)

from sklearn import cross_validation

features_train, features_test, labels_train, lables_test = cross_validation.train_test_split(
    features, labels, test_size = 0.3, random_state = 42)
clf.fit(features_train, labels_train)
print "With cross validation, accuracy is ", clf.score(features_test, lables_test)

poi_num = 0
for l in lables_test:
    if l == 1:
        poi_num += 1
print "POI number is ", poi_num
print "People number is ", len(lables_test)

pred = clf.predict(features_test)
true_positive_num = 0
for p, l in zip(pred, lables_test):
    if l ==1 and p == l:
        true_positive_num += 1
print "True positive number is ", true_positive_num
