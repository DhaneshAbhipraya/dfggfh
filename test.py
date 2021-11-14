from time import sleep as sl


while True:
  name = input("str? ")
  l:list = []
  for i in name:
    l.append(ord(i))
  print(l)
