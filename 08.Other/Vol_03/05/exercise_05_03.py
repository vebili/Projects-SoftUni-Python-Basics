import pickle, shelve

first_name = ["David", "John", "Jane"]
last_name = ["Doe", "Smit", "Black"]

datafile = open("names.dat", "wb")

pickle.dump(first_name, datafile)
pickle.dump(last_name, datafile)

datafile.close()
