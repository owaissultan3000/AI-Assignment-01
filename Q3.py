import string
import random

string.ascii_letters = '123'
Provinces = {
    'B': '',
    'K': '',
    'N': '',
    'P': '',
    'S': ''
}
Visited = []
Open = ['B','K','N','P','S']
Provinces_Neighbour = { #Dictionary of province with their neighbour
    'B':['N','P','S'],
    'K':['N','P'],
    'N':['B','K','P'],
    'P':['B','K','N','S'],
    'S':['B','P']
}
Colors = ['1','2','3'] #colors to be assigned

def MRV(name,data):
    # while(len(Open) > 0):
    #     if(len(Open) == 0):
    #         return
    
    Visited.append(name)
    Open.pop(Open.index(name))
    print(Visited.top())
    

# print(Provinces)
Provinces['B'] = random.choice(string.ascii_letters)
MRV('B',Provinces['B'])
