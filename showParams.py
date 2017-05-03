import cPickle as pickle

f = open("params.pkl")
info = pickle.load(f)
print info
