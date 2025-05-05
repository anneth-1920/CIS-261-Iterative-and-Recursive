print("Factorial Results Using Iterative Function")
for x in range(3):
    print(x)
for b in [10]:
    print (f"c!=", b)
for d in [5000]:
    print (f"v!=", d) 
for s in [1200000000000000000000000]:
    print (f"h!=", s)  

print("Factorial Results Using Recursive Function")
def print_the_next_number(start):
    if start == 0:
        return
    print(start - 1)
    return print_the_next_number(start - 1)
print_the_next_number(3) 
def print_the_next_number(start):
    if start == 0:
        return
    print(start - 1)
    return print_the_next_number(start - 1)
print_the_next_number(10)               