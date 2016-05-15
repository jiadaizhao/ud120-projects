#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print("Number of people: %d " % len(enron_data))

print("Number of features: %d " % len(enron_data[enron_data.keys()[0]]))

num_poi = 0
for key in enron_data:
    if enron_data[key]["poi"] == 1:
        num_poi += 1
print("Number of poi: %d" % num_poi)

file = open('../final_project/poi_names.txt','r')
print("Number of poi: %d" % (len(file.readlines()) - 2)) 
file.close()

print("Total value of the stock belonging to James Prentice: %d" % enron_data["PRENTICE JAMES"]["total_stock_value"])

print("Email messages from Wesley Colwell to poi: %d" % enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])

print("Value of stock options exercised by Jeff Skilling: %d" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])


names = ["LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"]
max_total_paments = 0
max_total_paments_name = ""
for name in names:
    payments = enron_data[name]["total_payments"] 
    if payments > max_total_paments:
        max_total_paments = payments
        max_total_paments_name = name

print("Max total payments is %d by %s" % (max_total_paments, max_total_paments_name))

count_salary = 0
count_email = 0
for key in enron_data:
    if enron_data[key]["salary"] != "NaN":
        count_salary += 1
    if enron_data[key]["email_address"] != "NaN":
        count_email += 1
print("Number of quantified salay: %d" % count_salary)
print("Number of known email address: %d" % count_email)

count_NaN_tp = 0
for key in enron_data:
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp += 1
print("Number of NaN for total payments: %d " % count_NaN_tp)
print("Percentage is %f " % (float(count_NaN_tp) / len(enron_data)))

count_NaN_tp = 0
for key in enron_data:
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        count_NaN_tp += 1
print("Number of NaN for total payments: %d " % count_NaN_tp)
print("Percentage is %f " % (float(count_NaN_tp) / len(enron_data)))
