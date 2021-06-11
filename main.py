def add(x = 1, y = 2):
  return x+y

print("Witaj w kalkulatorze\n")
while True:
  m = str(input("Wybierz opcję:\n1 - dodawanie"))
  if m == "1":
    print(add())