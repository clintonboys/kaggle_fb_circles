__author__ = 'cboys'
import re
import json
import sys

##########################################################
##
## features_parser.py
##
## Code to parse and store the user features
## from the Kaggle Facebook egonets data.
## Take features.txt as input and output a list of
## key-value dictionaries, one for each user, with more
## sensible key names.
##
## 25-10-2014
##
## run as:
## python features_parser.py 'str.txt'
##
##########################################################

if __name__ == '__main__':
    if len(sys.argv)<2:
        print "Expected features file.."
        sys.exit(0)

    with open(sys.argv[1]) as f:
        content=f.readlines()

    contents=[]

    for i in range(0,len(content)):
        contents.append(content[i].split(' '))

    #for item in contents:
    #    for entry in item:
    #        entry = re.sub('([\D])([;])([\D])','\g<1>_\g<3>',entry)

    for i in range(0,len(contents)):
        for j in range(0,len(contents[i])):
            contents[i][j]=re.sub('([\D])([;])([\D])','\g<1>_\g<3>',contents[i][j])

    ## Question: why the hell didn't that work
    ## iterating through the list by item normally???

    features_dict_list=[]

    for i in range(0,len(contents)):
        features_dict_list.append({})
        for j in range(1,len(contents[i])):
            features_dict_list[i][contents[i][j].split(';')[0]]=int(contents[i][j].split(';')[1])

    with open('clean_features.txt','a') as final_file:
        for item in features_dict_list:
            json.dump(item,final_file)
            final_file.write('\n')

    # final_file=open('clean_features.txt','w')
    # for item in features_dict_list:
    #     final_file.write('%s\n' %item)
    # final_file.close()

    ## This really should be json so Python can
    ## read the dictionaries later...