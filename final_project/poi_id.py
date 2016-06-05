#!/usr/bin/python

import matplotlib.pyplot as plt
import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'total_stock_value', 'deferred_income', 'from_poi_email_fraction', 
                        'to_poi_email_fraction', 'shared_receipt_with_poi', 'salary', 'bonus', 'total_payments',
                        ] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


### Task 2: Remove outliers
data_dict.pop('TOTAL', 0)

### Task 3: Create new feature(s)
for key, value in data_dict.items():
    if (value["from_poi_to_this_person"] == "NaN") or (value["to_messages"] == "NaN"):
        data_dict[key]["from_poi_email_fraction"] = 0
    else:
        data_dict[key]["from_poi_email_fraction"] = float(value["from_poi_to_this_person"]) / value["to_messages"]
        
    if (value["from_this_person_to_poi"] == "NaN") or (value["from_messages"] == "NaN"):
        data_dict[key]["to_poi_email_fraction"] = 0
    else:
        data_dict[key]["to_poi_email_fraction"] = float(value["from_this_person_to_poi"]) / value["from_messages"]
### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=5)

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
'''
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)
'''

### use KFold for split and validate algorithm

from sklearn.cross_validation import KFold
kf=KFold(len(labels),3)
for train_indices, test_indices in kf:
    #make training and testing sets
    features_train= [features[ii] for ii in train_indices]
    features_test= [features[ii] for ii in test_indices]
    labels_train=[labels[ii] for ii in train_indices]
    labels_test=[labels[ii] for ii in test_indices]



clf = clf.fit(features_train, labels_train)
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
pred = clf.predict(features_test)  
print "precision is ", precision_score(labels_test, pred)
print "recall is ", recall_score(labels_test, pred)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)