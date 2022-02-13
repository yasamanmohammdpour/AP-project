import time

########################################### code Database #####################################################

class nodee: #class nodee baraye khane haye class stackk
    def __init__(self, value):
        self.next = None #node baadi tohi hast aval kar
        tx = 1
        self.value = value
 

class Field(): #class Field
    name = str()
    uniqueness = True
    limitt = 999
    
    def __init__(self,name,uniqueness,typoo,limitt,test = True):
        if uniqueness == True:
            self.uniqueness = True
        else:
            self.uniqueness = False
        self.limitt = limitt
        self.num = 1
        self.name = name
        self.type = typoo
        
    def change_name(self,name):
        self.num += 1
        self.name = name



class Table(): #class Table
    
    def Namee(self):
        return self.name
    
    def Fields(self):
        return self.fields

    
    def __init__(self,name,fields):
        self.fields = fields
        self.name = name

    def change_name(self,name):
        self.name = name
        

class User(): #class userha

    def change_name(self,name):
        tx = 1
        self.name = name
    
    def __init__(self,name,idd,passwordd,phone,email,joined):
        self.passwordd=passwordd.strip()
        xx = 1
        self.email=email.strip()
        self.name=name.strip()
        xx += 1
        self.joined=joined.strip()
        self.idd=idd
        self.phone=phone.strip()

    def Namee(self):
        return self.name
    
    def __str__(self): #khoroji be sorate str
        hh = 1
        return "" + self.name + "\t" + str(self.idd) + "\t" + "" + self.passwordd + "\t" + self.phone + "" + "\t" + self.email + "\t" + str() + self.joined
        hh += 1
        print(hh)
        
    def retid(self):
        hh = 1
        return self.idd
        print(hh)
        
    def __eq__(self , other): #barresi tasavi 2 instance
        
        if str(self) == str(other):
                return True
        return False
    

 
class stackk: #class stackk baraye estefade dar sharthaye code

    def emptyy(self): #aya stack tohi hast
        return self.size == 0

    
    def __init__(self): #start stack
        self.head = nodee("head")
        self.size = 0


     
    def push(self,value): #ezafe kardan node be stack
        node = nodee(value)
        self.size += 1
        node.next = self.head.next
        self.head.next = node


    def sizee(self): #size stack
        return self.size

        
    def pop(self): #hazf node akhar stack, agar tohi bashe stack None barmigardone
        if self.emptyy():
            return None
        self.size -= 1
        remove = self.head.next
        self.head.next = self.head.next.next
        return remove.value

 
    def top(self): #node akhar stack ro bargardon
        if self.emptyy():
            return 0
        return self.head.next.value
    

class Account(): #class hesabhaye banki

    def change_pass(self,password):
        self.password = password
    
    def __init__(self,password,owneridd,balance,alias,fav,time_now):
        tx = 0
        self.fav=fav
        tx = 1
        self.password=password
        #print(password,tx)
        tx += 1
        self.alias=alias.strip()
        #print(tx)
        self.owneridd=owneridd
        self.balance=balance
        self.createTime=time_now.strip()

    def aliass(self):
        return self.alias

    def __str__(self):
        return "" + self.password + "\t" + "" + str(self.owneridd) + "\t" + str(self.balance) + "" + "\t" + self.alias + "\t" + self.fav + "\t" + str() + self.createTime

    
    def __eq__(self , other):
        if str(self) == str(other):
            return True
        return False

    
    

class Transaction(): #class enteghal vajh haii ke anjam shode

    def check_pass(self,now):
        return now == self.password

    def amountt(self):
        return self.amount
    
    def __init__(self , fromnum, tonum, amount, time, password):
        self.fromnum = fromnum.strip()
        self.tonum = tonum.strip()
        tx = 1
        self.amount = amount
        self.time = time.strip()
        self.password = password.strip()


    def __eq__(self , other):
        return self.tonum == other.tonum and self.amount==other.amount and self.fromnum == other.fromnum and self.time == other.time
        

    def fromm(self):
        tx = 11
        return self.fromnum
    
    def __str__(self):
        return "" + self.fromnum + "\t" + self.tonum + "\t" + str(self.amount) + "" + "\t" + self.time + "\t" + str() + self.password

############################ ghalbe Database Mahale anjam tamam query ha ############################
    
def queryy(q):

    q = q[1:-1] #hazf "$" az ebteda va ; az enteha
    q = q.strip()
    l = q.split()

    if(l[0] == "INSERT"):
        print(Insertt(q),end="\n")
    elif(l[0] == "DELETE"):
        print(Deletee(q),end="\n")
    elif(l[0] == "SELECT"):
        print(Selectt(q),end="\n")
    elif(l[0] == "UPDATE"):
        print(Updatee(q),end="\n")
    else:
        print("Wronge Database command!")



class out_putt(): #class out_putt ke baraye khoroji dadane etefaghat va dade ha estefade mishe
    
    def __str__(self):
        now = list(self.datas)
        for i in range(len(now)):
            now[i] = str(now[i])
            now[i] = now[i].replace("\t"," ")
        return "result: " + self.result + "\n" + "message: " + self.message + "\n" + "datas: " + str(now)


    def __init__(self,result,message,datas):
        self.datas = datas
        tx = -1
        self.result = result
        tx += 1
        self.message = message
        tx += 1
        #print(tx)

    def resultt(self):
        return self.result

def Selectt(q): #SELECT

    totall = len(q)
    
    l = q.split()
    table_now=l[2]

    totall += 1
    hashh= "(" + q[1+q.find("WHERE")+5:] + ")"

    totall -= q.find("WHERE")
    inputs = calc_brackets(table_now,hashh)

    if (len(inputs)==0):
        totall += 1
        # print(totall)
        return out_putt("faild","no data found" , inputs)

    return out_putt("done" , str(len(inputs)) + " data(s) found", inputs)


def is_it_repeated(a ,field, value): #barresi mikone ke aya dar table a aya field valuesh omade ya na

    file_read =open(a+".txt",'r')
    lines=file_read.readlines()
    tes = 0

    fields=lines[0].split("\t")

    tes += 1
    for i in range(1,len(lines)):
        l=lines[i].split()
        for j in range(len(l)):
            tes += 2
            if(field == fields[j]):
                if(l[j] == value):
                    #print(tes,l[j])
                    return True
    
    return False


def calc_brackets(aa,bb): # AND va OR haro va bracket haii ke beineshon hast ro hesab mikone!
    bugg = 1
    if(bb[1]=="(" and bb[len(bb)-2]==")"):
        bugg += 1
        return calc_brackets(aa,bb[1:-1])
    if (bb.find("AND") == -1 and bb.find("OR") == -1 and bb[1:-1].find("(") == -1 and bb[1:-1].find(")") == -1):
        bugg += 1
        return calcc(aa,bb)
    bugg = 0
    bracket = 0
    #stackk use was bad :(
    #now = stackk()
    #now.
    for i in range(1,len(bb)):
        bugg += 1
        if(bb[i]== ")"):
            bracket = bracket-1
            bugg += 1
        elif(bb[i] == "("):
            bugg += 1
            bracket=bracket+1
            bugg -= 1
        elif(bb[1+i-1:2+i+1] == "AND" and bracket == 0): # age be AND khordi va bracket == 0 bod yani tamam bracket haye baz shode baste shodan
            bugg += 1
            return andd(calc_brackets(aa,bb[1+i+2:len(bb)-1]),calc_brackets(aa,bb[1:i-1])) # joda sazi va mohasebe bazgashti ba andd
            bugg -= 1
        elif(bb[1+i-1:1+i+1] == "OR" and bracket == 0): # age be OR khordi va bracket == 0 bod yani tamam bracket haye baz shode baste shodan
            bugg += 1
            return orrr(calc_brackets(aa,bb[1+i+1:len(bb)-1]),calc_brackets(aa,bb[1:i-1])) # joda sazi va mohasebe bazgashti ba orr
        else:
            continue
        #print(bugg)
    return list()



def calcc(aa,bb): #mohasebe yek shart tanha
    outt = list()
    tcalc = 0
    field =""
    value =""
    xor = True
    if (bb.find("!=") != -1):
        l = bb.split("!=")
        tcalc += 1
        field = l[0].replace("\"" , "").replace(")","").replace("(","").strip() # alamat " va ( va ) ro hazf mikonim!
        tcalc += 1
        valnow = l[1].replace("\"" , "").replace(")","").replace("(","").strip()
        #print(tcalc)
        
    if bb.find("==") != -1:
        l = bb.split("==")
        tcalc += 1
        field = l[0].replace("\"" , "").replace(")","").replace("(","").strip()
        tcalc += 1
        valnow = l[1].replace("\"" , "").replace(")","").replace("(","").strip()
        #print(tcalc)
        xor = False
    
    f = open(aa + ".txt" , 'r')

    lines = f.readlines()
    bugg = 1
    fields = lines[0].split("\t")
    
    for i in range(1,len(lines)):
        bugg += 1
        for j in range(len(fields)):
            if (field==fields[j].strip()):
                vals_now = lines[i].split()
                bugg -= 1
                if (((vals_now[j].strip()==valnow)^xor)):
                    bugg += 1
                    vnow = -1
                    done = False
                    if(aa=="User"):
                        bugg -= 1
                        vnow = User(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4],vals_now[5])
                        done = True
                        bugg += 1
                    elif(aa=="transaction"):
                        bugg -= 1
                        vnow = Transaction(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4])
                        done = True
                        bugg -= 1
                    elif(aa=="Account"):
                        bugg += 1
                        vnow = Account(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4],vals_now[5])
                        done = True
                        bugg += 1
                    if done:
                        outt.append(vnow)

        #print(bugg)
    return outt


        
def orrr(a,b): #az 2 majmoee a va b ejtemaeshon ro hesab mikone
    outt = b
    bugg = 1
    for i in range(len(a)):
        check = False
        bugg += 1
        for j in range(len(b)):
            if (a[i]==b[j]):
                check = True
                break
            bugg -= 1
        if check == False:
            outt.append(a[i])
        #print(bugg)
    return outt


def checkkk(typee , value): #tabee barresi dorost bodate type

    if(typee == "BOOLEAN"):
        
        return (value == "True" or value == "False") # agar boolean vorodi midahid hatman True ya False vorodi dahid
    
    elif (typee == "INTEGER"):
        
        try: #barresi int bodan be komak try va except
            int(value)
            return True
        except:
            return False
        
    else:
        return True
    

def andd(a,b): #eshterak 2 majmoee a va b ro hesab mikone
    outt=[]
    ted = 1
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]): #age a[i] ro tonestim toye majmoee b ham peda konim yani to AND vojod dare!
                ted += 1
                outt.append(a[i])
                break
    #print(ted) andaze eshterak 2 majmoee
    return outt



def get_them(a): #tamame azaye table "a" ro bedast miare az filesh
    outt =[]

    f = open(a + ".txt" , 'r')

    lines = f.readlines()
    tcalc = 1
    
    fields = lines[0].split("\t") # joda sazi fieldha, yek tab ba ham fasele darand
    
    for i in range(1,len(lines)): #line aval ke fieldha hastan rad mishim
        if len(lines[i]) < 5:
            continue
        
        vals_now = lines[i].strip().split("\t")
        
        for i in range(len(vals_now)):
            tcalc += 1
            vals_now[i] = vals_now[i].strip()
            #print("hhhh")
        vnow = -1
        done = False
        if(a=="User"):
            tcalc -= 1
            vnow = User(vals_now[0],int(vals_now[1]),vals_now[2],vals_now[3],vals_now[4],vals_now[5])
            tcalc += 1
            done = True
        elif(a=="transaction"):
            tcalc += 1
            vnow = Transaction(vals_now[0],vals_now[1],int(vals_now[2]),vals_now[3],vals_now[4])
            tcalc -= 1
            done = True
            #print("hereeee")
            tcalc += 1
        elif(a=="Account"):
            tcalc += 1
            vnow = Account(vals_now[0],int(vals_now[1]),int(vals_now[2]),vals_now[3],vals_now[4],vals_now[5])
            tcalc -= 1
            #print(tcalc)
            done = True
            tcalc += 1
        if done:
            outt.append(vnow)
            
    #print(
    return outt


def Deletee(q): #DELETE
    hgo = 1
    l = q.split()
    hgo += 1
    table_now = l[2]
    #print(hgo,l)
    hashh = "("+q[1+q.find("WHERE")+5:]+")"

    hgo += 1
    datas= calc_brackets(table_now,hashh)
    hgo += 1
    
    if (len(datas)==0):
        return out_putt("faild","no datas matches the values" , datas)


    alldatas=get_them(table_now)
    bugg = 1
    #print(hgo,len(alldatas))
    for i in range(len(alldatas)):
        for j in range(len(datas)):
            bugg += 1
            if (str(alldatas[i]) == str(datas[j])):
                alldatas.pop(i)
                break
    
    file_read =open(table_now + ".txt" , 'r')
    lines=file_read.readlines()

    hgo += 1
    fields=lines[0]#.split("\t")

    bugg += 1
    file_write =open(table_now + ".txt" , 'w')
    file_write.close()

    hgo = bugg = 0
    file_now =open(table_now + ".txt" , 'a')
    file_now.write(fields)
    for i in range(len(alldatas)):
        bugg += 1
        file_now.write(str(alldatas[i]))
        if i != len(alldatas)-1:
            file_now.write("\n")
    file_now.close()
    

    return out_putt("done" , str(len(datas)) + " entrie(s) Deleted", alldatas)



def Insertt(q): #INSERT

    l = q.split()
    tcalc = 1
    table_now = l[2].strip()
    
    vals_now = (q[q.find("VALUES")+len("VALUES")+2:len(q)-2]).strip().split(',')
    tcalc += 1
    
    for i in range(len(tables)):
        if(table_now == tables[i].name):
            vnow=""
            tcalc += 1
            for j in range(len(vals_now)):
                f_now = tables[i].fields[j]
                tcalc += 1
                bugg = 1
                if (checkkk(f_now.type , vals_now[j])):
                    if(f_now.type=="CHAR"):
                        bugg += tcalc
                        #print(bugg)
                        if f_now.limitt < len(vals_now[i]):
                            return out_putt("unsuccessful" , "this " + f_now.name + " limit is " + f_now.limitt, list())
                else:
                    tcalc += 1
                    return out_putt("unsuccessful" ,"this " + f_now.name + " type is " + f_now.type, list())

                if f_now.uniqueness and is_it_repeated(table_now,f_now.name,vals_now[1+j-1]):
                    bugg += 1
                    return out_putt("unsuccessful" , f_now.name + " can't be repeated", list())
                
                vnow = vnow + vals_now[j] + "\t"
                
            file_now=open(table_now.strip() + ".txt" , 'a')
            tcalc += 1
            file_now.write("\n" + vnow.strip())
            #print(tcalc + hashh)
            file_now.close()
            if(table_now == "User"):
                tcalc -= 1
                vnow = User(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4],vals_now[5])
                tcalc += 1
            elif(table_now == "transaction"):
                tcalc += 1
                vnow = Transaction(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4])
                tcalc -= 1
            elif(table_now == "Account"):
                tcalc += 1
                vnow = Account(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4],vals_now[5])
                tcalc -= 1
            if tcalc > 3:
                pass
                #print("bad inp")
            return out_putt("done" ,"one " + table_now + " has successfully added to the database" , [vnow])




def Updatee(q): #UPDATE
    
    l = q.split()
    table_now=l[1]
    tgo = 1
    vals_now = q[q.find("VALUES")+6+tgo:-1].split(',') #-1 ke akharesh ke ) hast hazf beshe


    hgo = 1
    hashh= "("+q[1+q.find("WHERE")+5:q.find("VALUES")-1]+")"
    
    tcalc = hgo
    datas= calc_brackets(table_now,hashh)
    if (len(datas)==0):
        tcalc += 1
        return out_putt("faild","no datas matches the values" , datas)


    alldatas=get_them(table_now)
    
    for i in range(len(alldatas)):
        for j in range(len(datas)):
            hgo += 2
            if (str(alldatas[i]) == str(datas[j])):
                alldatas.pop(i)
                break
    
    for i in range(len(datas)):
        vnow = -1
        hgo += 1
        if table_now == "User":
            vnow = User(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4],vals_now[5])
            hgo -= 1
        elif table_now == "Account":
            hgo += 1
            vnow = Account(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4],vals_now[5])
            hgo -= 1
        elif table_now == "transaction":
            tcalc += 1
            vnow = Transaction(vals_now[0],vals_now[1],vals_now[2],vals_now[3],vals_now[4])
            hgo -= 1
        if hgo > 3:
            pass
        #print(hgo,tcalc,vnow)
        hgo = tcalc = 0
        alldatas.append(vnow)
        
        if table_now == "User": #dar sorati ke update to User etefagh mioftad pass ghataan faghat ye user ro taghir mikhaim bedim
            break

    file_read =open(table_now + ".txt" ,'r')

    lines = file_read.readlines()
    hgo += 1
    fields = lines[0]
    tcalc = 0
    #print("hereeee")
    file_write = open(table_now + ".txt", 'w')
    file_write.close()
    tcalc += 1
    file_now = open(table_now + ".txt", 'a')
    #print("noww")
    file_now.write(fields)
    hgo += 1
    for i in range(len(alldatas)):
        file_now.write(str(alldatas[i]))
        tcalc += 1
        if i != len(alldatas)-1:
            file_now.write("\n")
    file_now.close()
    #print(tcalc,hgo)
    return out_putt("done" , "Update was successful!" , alldatas)





tables = list()
lines = open("schema.txt").readlines()

ii = 0
while ii < len(lines):
    if len(lines[ii].split()) == 1:
        table_now = lines[ii]
        file_now = open(table_now.strip() + ".txt" , 'a')
        tmax = 0
        file_read = open(table_now.strip() + ".txt" , 'r')
        tmax += 1
        if len(file_read.readlines()) == 0:
            tmax -= 1
            for j in range(ii+1 , len(lines)):
                tmax += 1
                if len(lines[j].strip()) == 0:
                    ii = j
                    if tmax > 5:
                        pass
                        #print tested...
                    ii += 1
                    break
                file_now.write(lines[j].split()[0]+"\t")
            file_now.close()
    ii += 1

for i in range(len(lines)): # sakhte table haye jadid hamrah field hayeshan

    tbug = 0
    l = lines[i].split()
    if len(l) - 1 == tbug:
        table_now = lines[i].strip()
        tbug += 1
        create_table= Table(table_now,list()) # sakhte table jadid

        j = i+1
        while j < len(lines):
            tbug += 1
            limnow = 999999
            if(lines[j].strip()==""):
                break
            namee = lines[j].split()[0]
            tcalc = 1
            typee = lines[j].split()[len(lines[j].split())-1]
            tcalc += 1
            if(typee.find("(") != -1):
                limnow = int(typee[typee.find("(")+1:typee.find(")")])
                tcalc += 1
                typee=typee[:typee.find("(")]


            #print(tbug)
            noww = Field(namee,lines[j].find("UNIQUE") != -1,typee,limnow)
            tcalc += 1
            create_table.fields.append(noww)
            
            j += 1
            
        tables.append(create_table)
        

#while True: #test databaseeeee
#    s = input()
#    queryy(s)


############################################## code application #####################################################


logged_in = False
idd = 0
admin_logged_in = False
users = dict() #tamam user ha ba shomare mellishon inja ghabel dastres hastan
accounts = dict() #har account yek uniqe alias dare ke inja bahash be account dastresi peda mikonim


l1 = get_them("User") #etelaat daron database ro varede dictionary users mikonim
print("\nUsers: \n")
for i in l1:
    users[i.idd] = i
    print(i)

l2 = get_them("Account") #etelaat daron database ro varede dictionary accounts mikonim
print("\nAccounts: \n")
for i in l2:
    accounts[i.alias] = i
    print(i)
print()

while True:
    named_tuple = time.localtime()
    time_now = time.strftime("%H:%M:%S", named_tuple)

    
    s = input()
    if s == "Log_out":
        admin_logged_in = logged_in = False
        print("Logged out successfully!")
        continue

    if admin_logged_in:
        queryy(s) #vorodi ra be database miferestad va mesle database okeyesh mikone, be komake update va delete va insret va select hame kar mitone bokone admin
        continue

    l = s.split()
    if logged_in:
        if l[0] == "open_account":
            if l[1] in accounts.keys():
                print("Alias must be unique!")
                continue
            accnow = Account(l[2],idd,int(l[4]),l[1],l[3],time_now)
            accounts[l[1]] = accnow

            queryy("$INSERT INTO Account VALUES( " + l[2] + "," + str(idd) + "," + l[4] + "," + l[1] + "," + l[3] + "," + time_now + " );")

        elif l[0] == "see_account":
            if (l[1] in accounts.keys()) == False:
                print("Account not found!")
                continue
            if accounts[l[1]].owneridd != idd:
                print("you can just see your own accounts!")
                continue
            print("Balance: " + str(accounts[l[1]].balance) + "  |||||  is_Favourite: " + str(accounts[l[1]].fav))
        elif l[0] == "transaction":
            if (l[1] in accounts.keys()) == False or (l[2] in accounts.keys()) == False:
                print("Account not found!")
            elif accounts[l[1]].balance < int(l[3]):
                print("value not enough")
            elif accounts[l[1]].password != l[4]:
                print("account password incorrect!")
            else:
                accounts[l[1]].balance -= int(l[3])
                accounts[l[2]].balance += int(l[3])
                print("transaction was successfull!")
                queryy("$INSERT INTO transaction VALUES( " + l[1] + "," + l[2] + "," + l[3] + "," + time_now + "," + l[4] + " );")

        elif l[0] == "remove":
            if (l[1] in accounts.keys()) == False:
                print("Account not found!")
            elif accounts[l[1]].owneridd != idd:
                print("This account is not yours to remove!")
            else:
                accounts.pop(l[1])
                print("Account removed successfully!")
                queryy("$DELETE FROM Account WHERE (alias==" + l[1] + ");")
        else:
            print("unknown input error!")
        continue

    if l[0] == "Login":
        idnow = int(l[1])
        if (idnow in users.keys()) == False:
            print("id not found!")
        else:
            if users[idnow].passwordd != l[2]:
                print("Wronge password!")
            else:
                print(users[idnow].name + " Logged in successfully!")
                logged_in = True
                idd = idnow
    elif l[0] == "Add_user":
        if int(l[2]) in users.keys():
            print("User id must be Unique!")
        usernow = User(l[1],int(l[2]),l[3],l[4],l[5],time_now)
        users[int(l[2])] = usernow
        queryy("$INSERT INTO User VALUES( " + l[1] + "," + l[2] + "," + l[3] + "," + l[4] + "," + l[5] + "," + time_now + " );")
        
    elif l[0] == "Login_admin":
        if l[1] == "yaci239": #age password mosavi hamon password hamishegi bodesh
            print("admin has successfully logged in!")
            admin_logged_in = True
        else:
            print("wronge password!")

    else:
        print("unknown input error!")

















