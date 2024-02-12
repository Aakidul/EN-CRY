import os

def main():
         print ("ENTER 1 TO ENCRYPT")
         print ("ENTER 2 TO DECRYPT")

         user = int(input("ENTER NO: "))
         a = int(1)
         if (user==a):
              user1 = input("ENTER TXT: ")
              if len(user1)<5:
                    b = user1[::-1]
                    print(b)
          
