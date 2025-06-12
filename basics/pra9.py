#function

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child1)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def gsp(u_id):
  for i in range(int(u_id)):
    print(i)
  
u_id=input("enter id:")
gsp(u_id)

#Recursion 
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
print("LAMBDA")
#lambda
x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
