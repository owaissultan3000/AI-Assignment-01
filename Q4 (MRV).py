import string
import random

colors = ['1', '2', '3']

provinces = ['P', 'B', 'N', 'S', 'K']  #sorted according to highest values of incoming nodes to lowest

neighbors = {
    'B': ['N', 'P', 'S'],
    'K': ['N', 'P'],
    'N': ['B', 'K', 'P'],
    'P': ['B', 'K', 'N', 'S'],
    'S': ['B', 'P']
}

string.colors = '123'

ProvinceColors = {'B': '', 'K': '', 'N': '', 'P': '', 'S': ''}

def ColorChecking(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = ProvinceColors.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True


def GetColor(state):
    while (1):

        choosed_color = random.choices(string.colors)
        choosed_color = ''.join(choosed_color)
        if ColorChecking(state, choosed_color):
            return choosed_color


for x in provinces:
    ProvinceColors[x] = GetColor(x)

print(ProvinceColors)
