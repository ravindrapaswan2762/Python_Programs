
import pickle

# Pickling a python object
cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()

# reading a python object...
file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


# pickle.loads = ?




