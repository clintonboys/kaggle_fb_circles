__author__ = 'cboys'
import json
import sys
import circles_parser as cp

##########################################################
##
## common_features.py
##
## Code which takes as input user IDs and outputs a list
## of features they have in common. Requires a cleaned
## feature list.
##
## 25-10-2014
##
## run as:
## python common_features.py a 'xxx.txt' ID1 ID2 ...
## where xxx.txt is a cleaned feature file (a file with
## a dictionary corresponding to a user ID on each line)
## and a is 0 or 1 depending on whether to consider
## gender as a feature or not.
##
## or as:
## python common
##
##########################################################

def find_common_features(list_of_ids,features_dict,ignore_gender=True):

    these_features_list=[]

    for i in range(0,len(features_dict)):
        if (features_dict[i][u'id'] in list_of_ids):
            these_features_list.append(features_dict[i])

    if ignore_gender:
        for i in range(0,len(these_features_list)):
            try:
                del these_features_list[i][u'gender']
            except KeyError:
                pass

    intersection_dict=these_features_list[0]
    for i in range(0,len(these_features_list)-1):
        intersection_dict={x:intersection_dict[x] for x in intersection_dict if x in these_features_list[i+1]}

    common_features={}

    for key in intersection_dict:
        keys=[]
        for d in these_features_list:
            keys.append(d[key])
        if all(x==keys[0] for x in keys):
            common_features[key]=keys[0]

    return common_features

gender=True

if __name__ == '__main__':

    our_features_dict=[]

    with open(sys.argv[1]) as input_file:
        for line in input_file:
            our_features_dict.append(json.loads(line))

    if int(sys.argv[2])==0:
        gender=False

    if len(sys.argv[3].split('.'))==1:    # we've been given a small list of
        id_str_list=sys.argv[1:]      # user IDs as integers
        id_list=[]
        for entry in id_str_list:
            id_list.append(int(entry))
        print find_common_features(id_list,our_features_dict,gender)

    if len(sys.argv[3].split('.'))==2:    # we've been given a .circle file
        with open(sys.argv[3]) as f:
            content=f.readlines()

        circles_list=cp.parse_circles(content)

        for i in range(0,len(circles_list)):
            print 'Circle of size ', len(circles_list[i]),', features in common: ', find_common_features(circles_list[i][1:],our_features_dict,gender)