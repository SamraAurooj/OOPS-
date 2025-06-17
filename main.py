class student:
     def __init__(self, name, marks):
       self.name = name
       self.marks= marks
  
     def display(self):
          print(f"Name:{self.name},Marks:{self.marks}")

if __name__== "__main__":
 student1 = student("samra", 95)
 student1.display() 

     

