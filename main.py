# PROJECT FILE

import pickle
import os


def Add():
  f=open("Product.dat", "ab")
  while True:
    prod_code=input("Enter Product Code: ")
    prod_name=input("Enter Product Name: ")
    stock=int(input("Enter Product stock: "))
    price=int(input("Enter the price: "))
    rec={"Product Code": prod_code, "Product Name": prod_name, "Stock": stock,
         "Price": price}
    pickle.dump(rec,f)
    chr=input("Do you want to enter more products(Y/N)")
    if chr in "Nn":
      break
  f.close()

def Display():
  f=open("Product.dat", "rb")
  while True:
    try:
      print(pickle.load(f))
    except:
      break
  f.close()

def Search():
  f=open("Product.dat", "rb+")
  while True:
    pname=input("Enter the product name you want to search for")
    while True:
      try:
        rpos=f.tell()
        data=pickle.load(f)
        if data["Product Name"]==pname:
          print(data)
      except:
        break
    chr1=input("Do you want to search for more products(Y/N)")
    if chr1 in "Nn":
      break
    f.close()


def Update():
  f=open("Product.dat", "rb+")
  while True:
    pcode=input("Enter the product code you want to update")
    while True:
      try:
        rpos=f.tell()
        data=pickle.load(f)
        if data["Product Code"]==pcode:
          prod_code=data["Product Code"]
          prod_name=data["Product Name"]
          stock=data["Stock"]
          chr1=input("Do you want to change amount of stock(Y/N) (in kgs)")
          if chr1 in "Yy":
            stock=int(input("Enter New Stock: "))
          else:
            stock=data["Stock"]

          chr2=input("Do you want to change price(Y/N)")
          if chr2 in "Yy":
            price=int(input("Enter New price: "))
          else:
            price=data["Price"]
          rec={"Product Code": prod_code, "Product Name": prod_name,
               "Stock": stock, "Price": price}
          f.seek(rpos)
          pickle.dump(rec,f)
      except:
        break
    chr3=input("Do you want to update more products(Y/N)")
    if chr3 in "Nn":
      break
  f.close()

def Delete():
  f1=open("Product.dat", "rb")
  f2=open("Product2.dat", "ab")
  while True:
    pcode=input("Enter the product code you want delete")
    while True:
      try:
        data=pickle.load(f1)
        if data["Product Code"]==pcode:
          pass
        else:
          pickle.dump(data,f2)
      except:
        break
    os.remove("Product.dat")
    os.rename("Product2.dat", "Product.dat")
    chr3=input("Do you want to delete more products(Y/N)")
    if chr3 in "Nn":
      break
  f2.close()


def Sell():
  Amount=0
  f=open("Product.dat", "rb+")
  while True:
    pcode=input("Enter the product code which consumer wants to buy")
    while True:
      try:
        rpos=f.tell()
        data=pickle.load(f)
        if data["Product Code"]==pcode:
          prod_code=data["Product Code"]
          prod_name=data["Product Name"]
          stock=data["Stock"]
          price=data["Price"]
          num=int(input("How many kgs do you want to buy?"))
          Amount+=num*price
          stock=stock-num
          rec={"Product Code": prod_code, "Product Name": prod_name,
               "Stock": stock, "Price": price}
          f.seek(rpos)
          pickle.dump(rec,f)
      except:
        break
    chr1=input("Do you want to buy more products(Y/N)")
    if chr1 in "Nn":
      break
  f.close()
  print("The consumer has to pay Rs", Amount)



while True:
  print("Please press a number as per following:")
  print("Press 1 to Add")
  print("Press 2 to Display")
  print("Press 3 to Search")
  print("Press 4 to Update")
  print("Press 5 to Delete")
  print("Press 6 to Sell")
  print("Press any other key to exit")
  ch=int(input(""))
  if ch==1:
    Add()
  elif ch==2:
    Display()
  elif ch==3:
    Search()
  elif ch==4:
    Update()
  elif ch==5:
    Delete()
  elif ch==6:
    Sell()
  else:
    break
