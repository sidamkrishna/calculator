def calculator():
 while True:
     print(" calculator ")
     print("1 - addition ")
     print("2 - substration")
     print("3 - dividion")
     print("4 - multiplication")
     print("5 - Exit")
     
     try:
       choice= int(input("choose any option"))
       if(choice==5):
           print("exiting the calculator")
           break
       if(choice not in [1,2,3,4]):
           print("invalid choice")
           continue
       x=float(input("Enter x: "))
       y=float(input("Enter y: "))
       if(choice == 1):
          result = x+y
          print(result)
       elif(choice == 2):
          result = x-y
          print(result)
       elif(choice == 3):
          if(y==0):
             print("zero error")
          else:
           result = x/y
           print(result)
       elif(choice == 4):
           result = x*y
           print(result)
     except ValueError:
          print("invalid choice")
           
def main():
    calculator()
if __name__ == "__main__":
   main()
    



    

