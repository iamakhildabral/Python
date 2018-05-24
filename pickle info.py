#pickle some records and use them later in the program:
import pickle,shelve

list1 = {"Akhil","Dabral","Age is 24"}
list2 = {"Height:","5'7''"}
dict1 = {"Name":"Akhil Dabral","Age":24,"Sex":"M"}
file_object = open("Pickle.dat","wb")
pickle.dump(list1,file_object)
pickle.dump(list2,file_object)
pickle.dump(dict1,file_object)
file_object.close()


file_object = open("Pickle.dat","rb")
listy2 = pickle.load(file_object)
listy1 = pickle.load(file_object)
dictionary1 = pickle.load(file_object)

print(listy2)
print(dictionary1)
print(listy1)
