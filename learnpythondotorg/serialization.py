# There are two basic formats for JSON data. Either in a string or the object datastructure. 
# The object datastructure, in Python, consists of lists and dictionaries nested inside each other. 
# The object datastructure allows one to use python methods (for lists and dictionaries) 
#   to add, list, search and remove elements from the datastructure. 
# The String format is mainly used to pass the data into another program or load into a datastructure.

import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
print(type(json_string))

# Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))