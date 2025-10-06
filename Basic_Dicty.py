bike = {
    'brand':'bajaj',
    'model':'avenger',
    'year':'2019',
    'engine':"220cc"
}

"""
def Search_Dict():
    
    SEARCH = input("Enter key to be searched: ") 
    
    if SEARCH in bike.values():
        print("Yes",SEARCH,"is in the bike dictionary")
    
    else:
        print("No",SEARCH,"is not in the bike dictionary")   

Search_Dict()
"""


employees = [
        {"Sub": "CSC0001", "Cat": "Mega", "PF": "CBR1"},
        {"Sub": "CSC0002", "Cat": "Mega", "PF": "CBR2"},
        {"Sub": "CSC0003", "Cat": "Mega", "PF": "CBR3"}
    ]


def print_row1():
    for sub in employees:
        print(sub)

print_row1()


#----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT
#exit()


def print_row2():
    for sub in employees:
        result = {"sub": sub}
        print(result)


print_row2()





#----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT----EXIT
#exit()

employees2 = []


def print_dict():
    if len(employees2)>0:
        print(employees2)
    else:
        print('no employees')

print_dict()



