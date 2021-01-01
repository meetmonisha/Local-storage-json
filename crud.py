import json 
  
def read():
   
    f = open("data.json","r") 
    data = json.load(f) 
    for i in data['stu_details']: 
        print(i) 
    f.close() 
def create():
    a='{"stu_name": "Bob", "roll_num": "1"}'
    y = json.loads(a)   
    print("JSON string = ", y) 
    print() 
    f = open ('data.json', "r+")  
    data = json.loads(f.read()) 
    for i in data['stu_details']: 
        print(i) 
    f.close()
def delete():
    json_lines = []
    with open("data.json", 'r+') as open_file:
        for line in open_file.readlines():
            j = json.loads(line)
            if not j["stu_name"] == "Monisha":
                json_lines.append(line)

    with open("data.json", 'r+') as open_file:
        open_file.writelines('\n'.join(json_lines))
        
print("Welcome! Select a option to perform to your json data store")
print("\n1.Create \n2.Read \n3.Delete \n4.exit")
print("Enter your option")
n=int(input())
if(n==1):
    
    create()
   
if(n==2):
    print("The data store has following data")
    read()
if(n==3):
    
    delete();








