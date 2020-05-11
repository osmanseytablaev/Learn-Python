import pickle
f = open('mylist.pickle', 'rb')
other_array = pickle.load(f)
f.close()
print(other_array)