def greet(name):
    print("Hello", name)


def goodbye(name):
    print("GoodBye", name)


def message(name, func):
    func(name)


def hello():
    print("Hello") # this doesnt work


message("Jack", greet)
message("Mark", goodbye)
#message("Bill", hello)  