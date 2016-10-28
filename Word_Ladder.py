import json
import csv
from collections import defaultdict

def words_at_one_distance(word_a, word_b):
    count = 0
    for a, b in zip(word_a, word_b):
        if a != b:
            count += 1
            if count > 1:
                # quit early
                return False

    # in case we're equal
    return count == 1

def Hamming_Distance(word_a, word_b):

    distance = 0;

    if(len(word_a) == len(word_b)):

        for i in range(len(word_a)):

            if word_a[i] != word_b[i]:
                distance += 1;

    else:
        distance = -1;

    return distance

#import json
#objects = json.load(open('dictionary.json'))
#s = ''
#for obj in objects:
    # This depends on the json file... but something like:
#    s += ', '.join(obj)
#    s += '\n'
#    print "Doing"
#f = open('dict.csv','w')
#f.write(s)

#print "Done\n"

with open("dictionary.json") as data_file:
    data=json.load(data_file)

source_word = raw_input("Enter source word: ")
dest_word = raw_input("Enter destination word: ")

list_of_all_chains = []
counter = 0

if source_word in data and dest_word in data:
    temp = len(source_word)

    for word in data:
        if temp == len(word):
            list_of_all_chains.append(str(word))

#print list_of_all_chains

all_chains = {}

def create_all_chains(word):

    for key, value in data.items():
        key=str(key)
        if len(word)==len(key):

            if Hamming_Distance(word,key) == 1:
                print Hamming_Distance(word,key)

                if word in all_chains:
                    all_chains[word].append(key)
                else:
                    all_chains[word] = [key]

temp_dict = {}

for word in list_of_all_chains:
    for word2 in list_of_all_chains:
        if Hamming_Distance(word, word2) == 1:
            ## print word, word2
            if word in temp_dict:
                temp_dict[word].append(word2)
            else:
                temp_dict[word] = [word2]

#print temp_dict["SELY"]

#Searching through bfs
visited_nodes = []
paths = [source_word]

queue_of_paths = [paths]

while queue_of_paths:
    current_path = queue_of_paths.pop(0)
    current_node = current_path[-1]


    if current_node == dest_word:
        print current_path
        break;
    elif current_node not in visited_nodes:
        visited_nodes.append(current_node)

        for node in temp_dict[current_node]:
            new_path = []
            new_path = list(current_path)
            new_path.append(node)
            queue_of_paths.append(new_path)

