def toplama(a,b):
  print(a+b)
def carpma(a,b):
  print(a*b)
def cikarma(a,b):
  print(a-b)
def bolme(a,b):
  print(a/b)
a=int(input("Bakiye"))
b=int(input("Ücret"))
rezervasyonucreti=input("rezervasyon ucreti")
if rezervasyonucreti>="70":
  print("Buyurun")
elif rezervasyonucreti<="70":
  print("Yetersiz Bakiye")
  
  