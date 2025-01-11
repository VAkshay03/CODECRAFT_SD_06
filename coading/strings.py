#a string is a sequence of character 26 alphabets are all characters.'python'or collection/combination/group of characters
#"10" is a string,"kiran" is string
#string is declared in '',"",''' '''
#STRINGS METHODS
''' 
count()
endswith()
find() or found
format()
index()
isalnum()
isalpha()
join()
lower()
Istrip()
replace()
rstrip()
split()
startswith()
strip()
title()
upper()
'''
#syntax= variable.method
#1.UPPER() FUNCTION
sathwik="python"
print(sathwik.upper())#upper is used to convert the letters to capital alphabets
#similarly lower() is used for converting to small alphabets 
#2.COUNT() FUNCTION
james="my fav hero is prabhas"
print(james.count("prabhas"))#counts the words present in the main string
#((((in strings topic the count variable is used for counting the words but not letters in the word))))
#3.INDEX()  FUNCCTION
print(james.index("my"))#((shows the index of the my)))----->>>implies the index of first letter
#4.FIND() FUNCTION
print(james.index("prabhas"))#includes the space also
#difference between find and index is if there in no string present in the main string.
#index will give the (error) but the find function gives always (-1)
# print(james.index("sathwik"))#GIVES ERROR IN THE CODE
# print(james.find("sathwik"))#GIVES (-1)
#5.STARTSWITH() FUNCTION
s="sathwik is good boy"
print(s.startswith("sathwik"))#output is True
#6.ENDSWITH() FUNCTION
print(s.endswith("boy"))#output is true
#example code with using endswith()
in_websites=[]
for i in ["sathwik.in","raju.com","sandhya.in","akshay.com"]:
    if i.endswith("in"):
        in_websites.append(i)
    print(in_websites)#gives the output as sathwik.in and sandhya.in
#7.FORMAT() FUNCTION
raju="he is {} son".format("my")
print(raju)#format() is used to add a string by replacing the {} we can take multiple letters...
#example--------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
for i in ["sathwik","ayman","layakrishna","rithwik","ganesh"]:
    print("hii {} dont waste time. concentrate on your goals".format(i))
#8.ISALNUM() FUNNCTION
satya="10"
print(satya.isalnum())#it shows true as it satisfies both alphabets and numericals
#if we take float values like 2.2 then it is false the string reads its data type without any change in this function
#9.ISALPHA() FUNCTION
_2="12"
print(_2.isalpha())#false as the string contains numbers
#10.STRIP() FUNCTION
data=" this is book  "
print(len(data))#includes space also
s=data.strip()
print(len(s))#justifies the length excluding the spaces.but includes the middle spaces...
s=data.lstrip()#excludes only left side of space...
print(len(s))
s=data.rstrip()
print(len(s))#exludes the right side of the spaces....
#11.TITLE() FUNNCTION
f="na book na istam"
print(f.title())#the basic rule of title is first letter is capital in each word.. so output comes in same format
#12.>REPLACE() FUNCTION
shaik="these is my books"
new=shaik.replace("is","are")
print(new)#output comes by replacing the is by are.....
#13.>SPLIT() FUNNCTION
#with an example
d="this is my work"
f=d.split()
print(f)#output comes in list format and we can operate the list operations
n=[]
for i in f:
    if i=="is":
        i="are"
    else:   
        n.append(i)
print(n)
#14.>join() function
a="sathwik is good boy"
print(a)
b=a.split()
print(b)
c=" ".join(b)
print(c)#join is used to get into again in string format 

