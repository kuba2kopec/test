def add(x = 1, y = 2):
  return x+y

def mul(x = 1, y = 2):
  return x*y

def sub(x=1, y = 2):
  return x - y

#kom3
print("Witaj w kalkulatorze\n")
while True:
  m = str(input("Wybierz opcję:\n1 - dodawanie"))
  if m == "1":
    print(add())
  elif m == "2":
    print(sub())
  elif m == "3":
    print(mul())

#kom
