print("hello")

a = 32
print(a)
b = 'stdg'
print(b)

d, f, g = (9, "pop", 44)
print("{} {} {}".format("value", f, g))
# List
a = [4, 5, "hui"]
a.insert(2, 78)
print(a[1:2])
print(a[0])
a.append("don't worry")
print(a)
del a[2]
print(a)
# Tuple
a = (1, 3)
print(a[0])

# dict

pr = {2: "abc", "prt": "hui"}
print(pr[2])

#function, if, for,while

def pr():
    rtr = "abc"
    if rtr == "abc":
        print("true")
    else:
        print("false")
    print("end")

    for i in range(1,10,2):
        if(i==7):
            print("Got 7 in for loop")
        print(i)
    ijj=74
    while ijj>4:
        print("while loop")
        break



pr()
