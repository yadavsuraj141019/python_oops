class Finance:
    def __init__(self):
        self.__revenue=100000    #__revenue means its private data (__) two underscore means private (_) one underscore means protected
        self.number_of_sales=110

f1=Finance()
print(f1.__dict__)


class HR:
    def __init__(self):
        self.number_of_emp=20
        f1.__revenue=1
h1=HR()
print(f1.__dict__)


# upar vale example mai aesa pehle revenue ke value thi 100000 par hr class ne usko change kar diya like 1 par aap kis aur ke class ka 
# property access nahi karna dena chhahte isliye encapsulation ka use hota hai

# hr class mai ab revenue ka data change nahi hoga kiyuki ab vo private property ban gaya hai 

# agar private variable ko acess karna hai to ek method mai aapko pass kar dene ka phir us method ko object ke through call kara dene ka