import re

keyword = {"if":"if","switch":"switch","choice":"choice","crack":"crack","default":"default","although":"although",
        "then":"then","otherwise":"otherwise","subject":"subject","retaliate":"retaliate",
          "digit":"DT","point":"DT","char":"DT","word":"DT","bool":"DT","function":"function","implicit":"implicit", 
          'new': 'new','array':'array','continue':'continue',"none":"none","inherit":"inherit", "public":"public", "private":"private",
          "protected":"protected", "self":"self", "super":"super"}

opr = {"+":"PM","-":"PM","*":"MDM","/":"MDM","%":"MDM","!":"NOT","~":"NOT","&&":"&&","||":"||","and":"and","or":"or",
      "<":"RO",">":"RO","<=":"RO",">=":"RO","!=":"RO","==":"RO","=":"Assign","<<":"shiftOp",">>":"shiftOp","+=":"AssignOp",
       "*=":"AssignOp","/=":"AssignOp","%==":"AssignOp","<<=":"AssignOp",">>=":"AssignOp","++":"IncDec","--":"IncDec",
      "**":"Power"}
      
punc = {",":"," , ";":";" , ":":":" , ".":"." , "{":"{" , "}":"}" , "(":"(" , ")":")" ,
        "[":"[" , "]":"]" }

def token(text):
    if text in keyword:

        for key,value in keyword.items():

            if text == key:#a is class part and y is value part
                if value==text:
                    y=value
                    a=key
                #sfghjkl
                else:

                    y=value
                    a = text
    elif text in punc:

        for key,value in punc.items():

            if text ==key:
                if value==text:
                        y=value
                        a="punctuator"
                else:

                    y=value
                    a = text

    elif text in opr:

        for key,value in opr.items():
              if text ==key:
                    if value==text:
                            y=value
                            a=key
                    else:

                        y=value
                        a = text
                      
                      
    elif text == '\n':

        y =text
        a =" "
    elif re.match(r'^[+-]?[0-9]+$',text):
        y=text
        a="INTEGER CONSTANT"
    elif re.match(r"([+|-][0-9]*[.][0-9]+)|([0-9]*[.][0-9]+)",text):
        y=text
        a="FLOAT CONSTANT"
    elif re.match(r'^_+[a-zA-Z_0-9]*[A-Za-z0-9]$|^[A-Za-z]+[A-Za-z_0-9]*[A-Za-z0-9]$|^[A-Za-z]+$',text):
        y=text
        a="IDENTIFIER" 

    elif re.match(r"[\w\W]$",text):
        y=text
        a="CHAR CONSTANT"
    elif re.match(r"[\w\W]*",text):
        y=text
        a="STRING CONSTANT"

    else:
        y="Invalid Token"
        a = text
    
        
    return a,y

all_tokens=[]
eq=["="]
op=['+','-','*','/',"band" ,'!']
sh=['<<','<','>','>>']
do=['!','%']
sym=[';','#','\t']
punct=[',',':','}','{','[',']','(',')']
result = []
#dot=['.']
all_tokens = []
num=['0','1','2','3','4','5','6','7','8','9']
le=''
sp=' '
c = 1
key=op+sym+eq+punct+do+sh
# def listToString(s): 
#     # initialize an empty string 
#     str1 = " " 
#     # return string  
#     return (str1.join(s))

# with open("E:/Compiler-Construction/program.txt", 'r') as f:
#     string = f.readlines()

# string = listToString(string)
# print(string)
string="digit result = 10000;\ndigit result = 150;\npoint v2 = 1.0.65;\nword w = 'aaaa';\na.fn()\nchar ch = a;\nif\n{\nresult\n}"
#string="alpha a = b \nfunc void sum(alpha a,alpha b){alpha a=b\n}\nd=2+c\nif(a<b){r=t * 4\n}\nelse{a=2+a\n}\nspan(a==b){s=5 * c\n}\na=2\niterate i in range(a)\na=3\niterate i in range(5){\nia new b()\n}\na++\na+=b\nfunc dec mul(alpha a=b,dec c=2){a.b.c.fn(2)\n}\n"

for a,i in enumerate(string):
    if i == '\n':
        le+=i
        #temp=le
#         toke = token(le)
        n=token(le)
        for t in n:
            result.append(t)
        result.append(c)
        all_tokens.append(result)
        print(result)
        c+=1
        result=[]
        le=le.strip()#for newline
        #temp=le
    try:
        if i !=sp and i not in sym:#checking and appending into le
            if le.startswith('\"'):
                le+=i
            elif le.startswith('\''):
                le+=i
            elif i in op or i in sh:
                try:
                    if string[a+1] in eq:
                        le=i+string[a+1]
                    elif i==string[a+1] and i!=string[a-1]:
                        le=i+string[a+1]
                    elif i==string[a+1] and i==string[a-1]:
                        le+=i
                    elif i==string[a-1]:
                        pass
                    elif string[a+1] in num :
                        le=i+string[a+1]
                    
                    else:
                        le+=i
                except:
                    le+=i
            elif i in num and string[a-1] in op:
                pass
            elif i in eq:
                try:
                    if string[a+1] in op :
                        pass
                    elif string[a-1] in op :
                        pass
                    elif i==string[a+1] and i!=string[a-1]:
                        le=i+string[a+1]
                    elif i==string[a+1] and i==string[a-1]:
                        le+=i
                    elif i==string[a-1] and string[a-2]in op:
                        le+=i
                    elif i==string[a-1] and string[a-2]not in op:
                        pass
                   
                    else:
                        le+=i
                except:
                    le+=i
            #elif i=="." and string [a+1]  in num:
             #   le+=i
            #le.replace('.','')
                #le= le.strip(".")
           # elif i==".":
            #    le="."
            else:
                le+=i
    except IndexError:
        print("END OF FILE")
    if(a+1<=len(string)):
        try:
            if le.startswith('\"'):
            
                if le=="\"":
                    pass
                elif le.endswith('\"'):
                    if le != '':
                        #le=le.strip("\"")
#                         toke = token(le)
                        n=token(le)
                        for t in n:
                            result.append(t)
                        result.append(c)     
                        all_tokens.append(result)
                        print(result)
                        result = []
                        le=''
            elif le.startswith('\''):
            
                if le=='\'':
                    pass
                elif le.endswith('\''):
                    if le != '':
#                         toke = token(le)
                        n=token(le)
                        for t in n:
                            result.append(t)
                        result.append(c)     
                        all_tokens.append(result)
                        print(result)
                        result = []
                        le=''     
            
            elif string[a+1] == sp or string[a+1] in key or le in key or string[a+1] == '\n':#checking the next word(breaker)
                
                if le != '':
                   
                        
                    if '\n' in le:
                        le=le.strip()
                        #print(le.replace('\n',''))
#                         toke = token(le)
                        n=token(le)
                        for t in n:
                            result.append(t)
                        result.append(c)    
                        all_tokens.append(result)
                        print(result)
                        result = [] 
                            #temp=le
                        le=''
                   
                    else:  
#                         toke = token(le)
                        n=token(le)
                        for t in n:
                            result.append(t)
                        result.append(c)     
                        all_tokens.append(result)
                        print(result)
                        result = []               
                        #temp=le
                        le=''
                        #or  (string[a+1]=='.' and i not in num)
          #  elif  string[a+1] == "."and string[a+2] not in num or '.' in le  :#(breakforalpha)
            elif string[a+1] =='.' and i not in num  :
                if le != '':
                   # le=le.strip(".")
#                     toke = token(le)
                    n=token(le)
                    for t in n:
                        result.append(t)
                    result.append(c)     
                    all_tokens.append(result)
                    print(result)
                    result = []               
                        #temp=le
                    le=''
                   # le=le.strip(".")
                   # print(le.replace('\n','\n\r'))
                    #le=""
            elif i=='.' and string[a+1]not in num and '.' in le:
                 if le != '':
                   # le=le.strip(".")
#                     toke = token(le)
                    n=token(le)
                    for t in n:
                        result.append(t)
                    result.append(c)     
                    all_tokens.append(result)
                    print(result)
                    result = []               
                        #temp=le
                    le=''
            
            elif i in num and string[a+1]=='.' and '.' in le:
           # elif string[a+1] in '.'and string[a+2]  in num and '.' in le: 
                if le != '':
#                     toke = token(le)
                    n=token(le)
                    for t in n:
                        result.append(t)
                    result.append(c)     
                    all_tokens.append(result)
                    print(result)
                    result = []               
                        #temp=le
                    le=''
                    print(le.replace('\n','\n\r'))
                    le=""
        except:
            print("end of file")