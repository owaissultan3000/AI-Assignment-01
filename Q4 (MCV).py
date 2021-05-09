import string
import random

colors = ['1', '2', '3']

provinces = ['B', 'K', 'N', 'S', 'P']

neighbors = {
    'B': ['N', 'P', 'S'],
    'K': ['N', 'P'],
    'N': ['B', 'K', 'P'],
    'P': ['B', 'K', 'N', 'S'],
    'S': ['B', 'P']
}

string.ascii_letters = '123'
string.province = 'BKNPS'

Open = ['B', 'K', 'N', 'P', 'S']

ProvinceColors = {'B': '', 'K': '', 'N': '', 'P': '', 'S': ''}


def ColorChecking(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = ProvinceColors.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True


def GetColor(state):
    for color in colors:
        if ColorChecking(state, color):
            return color


while (len(Open) > 0):
    val = random.choices(string.province)
    val = ''.join(val)
    if (val in Open):
        Open.pop(Open.index(val))

        ProvinceColors[val] = GetColor(val)

print(ProvinceColors)
