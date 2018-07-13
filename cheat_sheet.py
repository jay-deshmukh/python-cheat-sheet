print("Hello World")

#Comment 

'''
Multi-Line Comment 
'''

'''
DataTypes :-
    Number 
    Sting 
    Lists -> Arrays  
    Tuples -> Use It When You Have Data And You Do Not Want It To Be Easily Changed
    Dictionaries
'''

print(5 ** 3) # ** for Exponential Calculation (Reasult :- 125)
print(5 // 2) # ** for Exponential Calculation (Reasult :- 2)

multi_line_quotes = '''
    Hello 
    World 
'''


string1 = "Avengers"
string2 = "Earth's Mightiest Heroes"

print("%s %s %s" %('I Like ' ,string1 , string2) ) 


# Dicrionaries and operations on it 
print("----------------Dicrionaries and operations on it----------------")
# Dictionary
super_heroes = {
    'Iron Man' : 'Toney Stark',
    'Hulk' : 'Bruce Banner',
    'Captain America ' : 'Syteve Roggers',
    'Loki' : 'idk and idc'
    }

print(len(super_heroes)) #Length of a dictionary
print(super_heroes['Iron Man']) 
del super_heroes['Loki'] #Deleting a wrong Record 
print(len(super_heroes))
print(super_heroes.keys()) #Printing Keys 
print(super_heroes.values()) #Printing Values 

# Conditional statements 

print("----------------Conditional statements----------------")

age = 16
if age >= 16 and age <18 :
    print("You Can Drive Moped")
elif age >= 18:
    print("You Can Drive Bike")
else :
    print("Figureout For Yourself")



# Loops
print("----------------Looping----------------")
dummy_list = ['apple','samsung','banana']

for x in dummy_list:
    print(x) 



x = 0
while (x<=20):
    if x%2 == 0:
        print(x)
    x+=1

#Functions
print("----------------Functions----------------")

def addNum(n1,n2):
    sum = n1 + n2
    return sum
 
print(addNum(1,4)) 

print("----------------String Operations----------------")

some_string = "Let's not forget to have fun along the way !"

print(some_string[0:28])
print(some_string[-5:])
print(some_string.find('fun'))

print("----------------File Operations----------------")

#writing
test_file = open('temp.txt' ,'wb')
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Hello World!!!!","UTF-8")) 
test_file.close()

#read
test_file = open('temp.txt' ,'r+')
data_from_file = test_file.read()
print(data_from_file) 

# ====================================================OOP====================================================

print("----------------Object Orientation  ----------------")


class Animal:
    __name = "" # use __ (double underscore to make properties private)
    __breed = ""
    def __init__(self,name,breed): #constructor
        self.__name=name
        self.__breed=breed

    def set_name(self,name): #self acts as this 
        self.__name=name

    def get_name(self):
        return self.__name
    
    def set_breed(self,breed): #self acts as this 
        self.__breed=breed

    def get_breed(self):
        return self.__breed

    def toString(self):
        return "The Name Of The Animal is {} and its breed is {}".format(self.__name,self.__breed)

dog = Animal("Bruno","Pug")

dog.get_name()
dog.get_breed()
print(dog.toString())
dog.set_name("Alph")
dog.set_breed("Lab")
print(dog.toString())
