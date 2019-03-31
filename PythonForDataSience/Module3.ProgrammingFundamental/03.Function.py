# function takes some input and provide output
# we can reuse the code by using the function


def sum(a, b):
    """
        First line of function, the doc for function
    """
    print(a+b)
	return (a+b)


def collectingName(*names):
    for name in names:
        print(name)


def returnVoid():
    print("this function return nothing")
    return

sum(1, 2)
collectingName("1", "2", "3", "4")
returnVoid()