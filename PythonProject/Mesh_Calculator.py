# Mesh Calculator

print()
def Permanent_Money(MoneyName, ParticipantNum):
    varib = int(input(f"Please Enter Total {MoneyName} : "))
    Per_hed_flat = varib//ParticipantNum
    print(f"Per Hed {MoneyName}", Per_hed_flat)
    return Per_hed_flat

Number = int(input(f"Please Enter the totel number of man participants in Flat: ")) 

# FLAT MONEY
Per_hed_flat = Permanent_Money('FLAT MONEY', Number)


# Electric bil
Per_hed_Electric = Permanent_Money('Electric bil', Number)


# News paper
Per_hed_Newspaper = Permanent_Money('News paper', Number)


# Furs cleaning
Per_hed_furs = Permanent_Money('Furs cleaning money', Number)


Total_Permanent_Money = Per_hed_flat + Per_hed_Electric + Per_hed_Newspaper + Per_hed_furs


Listof_Mans = []
def OurName():
    print("""Please Enter the Names of Man participants in WATER (Enter one by one) .
             alok
             shubham
             shailesh
             prakash
             anurag
             gautam""")
    print()
    v = list(map(str, input("             :").split()))
    print()
    for i in v:
        Listof_Mans.append(i)

OurName()

# Totel number of man participants in WATER
WNumber = len(Listof_Mans)


# Water Money
Per_hed_water = Permanent_Money('Water Money', WNumber)


# Gas Money
Per_hed_gas = Permanent_Money('Gas Money', WNumber)



print()
print("|  Mesh money calculation  |")
print()


# Mesh money calculation
def Get_Spend_Money(SName):
    # print(f"Name : {SName}")
    print(f"{SName}, please Enter all money spent in mesh (with Seprated by Comma [,]) .")
    varab = list(map(int, input(": ").split(",")))
    totalmoney = sum(varab)
    print(f"Total {SName} spend money : {totalmoney}")
    return totalmoney



# Alok sir
Alok_spent_money = 0
if 'alok' in Listof_Mans:
    Alok_spent_money = Get_Spend_Money("Alok sir")

# Shubham sir
Shubham_spent_money = 0
if 'shubham' in Listof_Mans:
    Shubham_spent_money = Get_Spend_Money("Shubham sir")


# Shailesh pandit
Shailesh_spent_money = 0
if 'shailesh' in Listof_Mans:
    Shailesh_spent_money = Get_Spend_Money("Shailesh")

# Prakash
Prakash_spent_money = 0
if 'prakash' in Listof_Mans:
    Prakash_spent_money = Get_Spend_Money("Prakash")


# Anurag civil
Anurag_spent_money = 0
if 'anurag' in Listof_Mans:
    Anurag_spent_money = Get_Spend_Money("Anurag")


# Gautam civil
Gautam_spent_money = 0
if 'gautam' in Listof_Mans:
    Gautam_spent_money = Get_Spend_Money("Gautam")

# Total mesh money calculation
print("---------------------------------------------------------------------------------")
Total_mesh_money = Alok_spent_money + Shubham_spent_money + Shailesh_spent_money + Prakash_spent_money + Anurag_spent_money + Gautam_spent_money
print("Total_mesh_money:", Total_mesh_money)


# Per hed mesh money calculation
Per_hed_mesh = Total_mesh_money//WNumber
print("Per_hed_mesh:", Per_hed_mesh)


# men mesh money calculation.
Alokmesh = Alok_spent_money-Per_hed_mesh
Shubhammesh = Shubham_spent_money-Per_hed_mesh
Shaileshmesh = Shailesh_spent_money-Per_hed_mesh
Prakashmesh = Prakash_spent_money-Per_hed_mesh
Anuragmesh = Anurag_spent_money-Per_hed_mesh
Gautammesh = Gautam_spent_money-Per_hed_mesh

print("")
print("")
print(" Final Results:::")
print()

def Result(Name, finalmesh):
    if Name in Listof_Mans:
        if finalmesh<0:
            T = finalmesh - (Total_Permanent_Money + Per_hed_water + Per_hed_gas)
            print(Name," sir :     ", T)

        elif finalmesh>0 :
            T = finalmesh - (Total_Permanent_Money + Per_hed_water + Per_hed_gas)
            print(Name," sir :     ", T)

        else:
            T = finalmesh - (Total_Permanent_Money + Per_hed_water + Per_hed_gas)
            print(Name," sir :     ", T)
    else:
        T = Total_Permanent_Money
        print(Name," sir :     -",T)


Result('alok', Alokmesh)
Result('shubham', Shubhammesh)
Result('shailesh', Shaileshmesh)
Result('prakash', Prakashmesh)
Result('anurag', Anuragmesh)
Result('gautam', Gautammesh)

