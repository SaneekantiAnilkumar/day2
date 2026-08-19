class Father:
    def show(self):
        super().show()
        print("Father method")

class Mother:
    def show(self):
        super().show()
        print("Mother method")

class Child(Father, Mother):
    def show(self):
        super().show()
        print("Child method")
         
c=Child("anil", "savarvathi",)
print(c.Father)
print(c.Mother)