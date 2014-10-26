__author__ = 'cboys'

##########################################################
##
## connected_components_benchmark.py
##
## Code to cluster Kaggle Facebook egonet data by
## connected components using networkx graph
## package. This corresponds to a simple benchmark
## algorithm on the Kaggle competition.
##
## 25-10-2014
##
## run as:
## python connected_components_benchmark.py 'xxx.egonet'
##
##########################################################

import networkx as nx
import sys
import re

def read_egonet_to_graph(file):
    G=nx.Graph()
    for line in open(file):
        user, mutuals = line.split(':')
        mutuals = mutuals.split()
        for friend in mutuals:
            if friend == user: continue
            G.add_edge(int(user),int(friend))
    return G

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Expected egonet..."
        sys.exit(0)
    print "UserId,Predicted"
    for arg in sys.argv[1:]:
        clusters=nx.connected_components(read_egonet_to_graph(arg))
        try:
            ego=int(re.compile('\d+').findall(arg)[0])
        except Exception as e:
            print "Expected xxx.egonet..."
            sys.exit(0)
        clusters_sep=[]
        for cluster in clusters:
            clusters_sep.append(' '.join([str(y) for y in cluster]))
        print str(ego) + ',' + ';'.join(clusters_sep)