from lib2to3.pygram import pattern_grammar
from os import replace

from fontTools.misc.textTools import caselessSort

data = [
   {'price' : 10000, 'rooms':4,'district': 'Kathmandu'},
   {'price' : 20000, 'rooms':5,'district': 'Lalitpur'},
   {'price': 50000, 'rooms': 2, 'district':'Bhaktapur'},
   {'price': 42000, 'rooms' : 2, 'district': 'Bhaktapur'},
   {'price': 42000, 'rooms': 2, 'district':'Kavre'},
   {'price': 42000, 'rooms': 2, 'district':'Dhading'},
   {'price': 42000, 'rooms' : 2, 'district': 'Sindhupalchowk'}
]


from sklearn.feature_extraction import DictVectorizer
# vec = DictVectorizer (dtype = int, sparse = False)
vec = DictVectorizer (dtype = int,sparse=True)
newData = vec.fit_transform(data)
print(vec.get_feature_names_out())
print(newData)