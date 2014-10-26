__author__ = 'cboys'
import sys

##########################################################
##
## circles_parser.py
##
## Code to parse and the .circles files containing
## training data for the Kaggle Facebook competition.
## Takes as input a .circle file of circled user IDs
## and outputs a list of lists of IDs headed by the
## circle number.
##
## 26-10-2014
##
## run as:
## python circles_parser.py 'xxx.circles'
##
##########################################################

def parse_circles(circle_content):
    contents=[]
    for i in range(0,len(circle_content)):
        contents.append(circle_content[i].split(' '))
    for i in range(0,len(contents)):
        for j in range(1,len(contents[i])):
            contents[i][j] = int(contents[i][j])
    return contents

if __name__ == '__main__':
    if len(sys.argv)<2:
        print "Expected features file.."
        sys.exit(0)

    with open(sys.argv[1]) as f:
        content=f.readlines()

    print parse_circles(content)


