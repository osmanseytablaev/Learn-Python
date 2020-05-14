import pickle
mylist = ['some text', 123, [4, 5, True]]
f = open('mylist.pickle', 'wb')
pickle.dump(mylist, f)
f.close()
print(mylist)