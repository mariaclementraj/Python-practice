import pymongo
count=0
count1=0
con=pymongo.MongoClient("mongodb://localhost:27017/")
db=con["mcq_project"]
col=db["mcq"]
list1=[{"_id":1,"question":"Who developed Python Programming Language","op1":"a) Wick van Rossum","op2":"b) Rasmus Lerdorf","op3":"c) Guido van Rossum","op4":"d) Niene Stom","ans":"c"},
       {"_id":2,"question":"Which type of Programming does Python support","op1":"a) object-oriented programming","op2":"b) structured programming","op3":"c) functional programming","op4":"d) all of the mentioned","ans":"d"},
       {"_id":3,"question":"Is Python case sensitive when dealing with identifiers","op1":"a) no","op2":"b) yes","op3":"c) machine dependent","op4":"d) none of the mentioned","ans":"b"},
       {"_id":4,"question":"Which of the following is the correct extension of the Python file","op1":"a).python","op2":"b).pl","op3":"c).py","op4":"d).p","ans":"c"},
       {"_id":5,"question":"Is Python code compiled or interpreted","op1":"a) Python code is both compiled and interpreted","op2":"b) Python code is neither compiled nor interpreted","op3":"c) Python code is only compiled","op4":"d) Python code is only interpreted","ans":"a"}]
x=col.insert_many(list1)


for x in col.find():
    print(x["question"])
    print(x["op1"])
    print(x["op2"])
    print(x["op3"])
    print(x["op4"])
    answer=x["ans"]
    userinput=input("Enter the option ")
    if userinput==answer:
        count+=1
    else:
        count1+=1
    print()

print("You have answerd for", count,"questions")
print("You have not answerd for", count1,"questions")
    

