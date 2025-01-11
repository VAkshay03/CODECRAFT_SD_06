#TASK 4....
a=1,2,3,4,5
print(a) #here output = (1,2,3,4,5) it is tuple concept.........
b=d=e=100
print(b,d,e) #output = 100 100 100
f,g,h=1,2,3
print(f,g,h) # 1 stores int and 2 stores in g 3 stores in h........
sathwik=100
print(sathwik) # we will get output as 100

# RULES TO FOLLOW FOR VARIABLES.....
#A VARIABLE NAME START WITH A ((((LETTER OR UNDERSCORE......))))
#Kiran=100 this is correct
_1=12
print(_1) # see here the code executes as VARIABLE STARTED WITH THE (((UNDERSCORE....)))
#A VARIABLE NAME CANNOT START WITH THE NUMBER
#NO SPECIAL CHARACTERS ARE ((USED BEFORE VARAIBLES))
sathwik="raju"
print(sathwik) #for string we can use double quotes....
#((VARIABLES NAMES ARE CASE SENSITIVE....))
#every uppercase and lower case is matter in python 
#name="sathwik"
#print(Name) # (((((here we will get error as in print statemnet the letter is in capital N so case is different...)))
#(((KEYWORDS ARE NOT USED INN NAMING VARIABLES...)))))) like int,float,return.....etc
#THERE ARE 35 KEYWORDS IN PYTHON AND 32 IN C..
#there are three types of variable cases in python>>
#1.CAMELCASE = camelCase
#2.SNAKECASE = snake_case
#3.PASCALCASE = PascalCase
print(id(_1)) #gives the address of any variable.....ID IS ADDRESS IN PYTHON...
#if two different variables have same value then we will get same address for both the variables....
#in above at line 6 the adress of F,G,H HAVE THE SAME ADRESS AS IT HAVE SAME VALUE=100
print(int(f))
print(float(f))
_2=0
print(bool(_2)) #type conersion.............. if 0 means false else true
#THERE ARE TWO TYPES OF CONVERSION
#1.implict =  no data loss EXAMPLE = FROM INT TO FLOAT
#2.explicit = data loss .. HERE FROM FLOAT TO INT
