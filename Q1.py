import random 
import time
import matplotlib.pyplot as plt 








def input_info():
    while True:
        length=input("Enter Length Of Chromosome: ")
        if(int(length)>=8):
            break
    while True:
        population = input("Enter Population Size: ")
        if(int(population)>3 and int(population)%2==0):
            break
        else:
            print("Enter Even Population greater than 3")
    return int(length),int(population)


def populate(chromosome,length,population):
    #Population Generation
    ###########Initial Population##################
    
    for j in range(population):
        chrm = ''
        for i in range(length):
            chrm=chrm+str(random.randrange(0,2))#genrate character 0 or 1
        chromosome.append(chrm) #Append Complete string in array



def sort_upon_fitness(chromosome,length,population):

    int_arr =[]
    for i in range(population):
        int_arr.append(int(chromosome[i],2)) #Genrate NUmbers from each string fot evaluation 

############Fitness Funtion#################
    for i in range(population-1):#Sort chromosome array on bases of evaluation that is greatest integer
        for j in range(i+1,population):
            if(int_arr[i]<int_arr[j]):
                int_arr[i],int_arr[j]=int_arr[j],int_arr[i]
                chromosome[i],chromosome[j]=chromosome[j],chromosome[i]
    #Remove 25% of lower Population and fill with random of remianing 75%
    Lower=int(population*25/100)
    for i in range(population-Lower,population):
        chromosome[i] = random.choice(chromosome[:population-Lower-1])
    int_arr =[]
   
def cross_over(chromosome,length,population):
########## CrossOver ###################
    for i in range(0,population,2):
        num1 = random.randrange(0,length-1)
        time.sleep(0.06)
        p1 = chromosome[i][num1:]
        c1 = chromosome[i][:num1]
        p2 = chromosome[i+1][num1:]
        c2 = chromosome[i+1][:num1]
    
        chromosome[i]=c1+p2
        chromosome[i+1]=c2+p1


def mutate(chromosome,length,population):
#########Mutation##############
    print("\n")
    for i in range(population):
        num = random.randrange(0,2)
        num1 =random.randrange(0,length)
        if(num==1):
            p1=chromosome[i][:num1]
            p2 = chromosome[i][num1+1:]
            chromosome[i]=p1+'1'+p2


def check_result(chromosome,population,length):
    ideal = pow(2,length)-1
    for i in range(population):
        if(int(chromosome[i],2)==ideal):
            return True
    return False


def graph_generator():
    f1 = open("file1.txt",'r')
    f2 = open("file2.txt",'r')
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for x in f1:
        val = x.split(' ')
        x1.append(float(val[0]))
        y1.append(float(val[1]))
    for x in f2:
        val = x.split(' ')
        x2.append(float(val[0]))
        y2.append(float(val[1]))
    
    plt.plot(x1, y1) 
    plt.xlabel('Population Size') 
    plt.ylabel('No Of Generations') 
    plt.title('POPULATION VS GENERATIONS') 
    plt.show() 
    plt.plot(x2, y2) 
    plt.xlabel('Chromosome Length') 
    plt.ylabel('No Of Generations') 
    plt.title('Chromosome Length VS GENERATIONS') 
    plt.show() 

while True:
    choice = input("Enter 1 Run Algorithm\nEnter 2 To Run From Scratch\nEnter 3 To Generate Graph from Preprocessed Data\n")
    if(int(choice) in [1,2,3]):
        break
    else:
        print("Retry With Correct Input")
if int(choice)==3:
    graph_generator()
elif(int(choice)==1):
    chromosome = []
    length,population = input_info()
    populate(chromosome,length,population)
    result = False
    counter=0
    while not result:
        counter+=1
        sort_upon_fitness(chromosome,length,population)
        cross_over(chromosome,length,population)
        mutate(chromosome,length,population)
        result=check_result(chromosome,population,length)
        print(chromosome)
    print("\n")
    print(chromosome)
    print("Genetic Algorithm Took {} steps for max1 Problem".format(counter))
else:
    length = 8
    f=open("file1.txt",'w')
    for population in range(4,31,2):# for even number of population after 4 and Chromosome length 8 run Algo
        chromosome = []
        populate(chromosome,length,population)
        result = False
        counter=0
        while not result:
            counter+=1
            sort_upon_fitness(chromosome,length,population)
            cross_over(chromosome,length,population)
            mutate(chromosome,length,population)
            result=check_result(chromosome,population,length)
            print(chromosome)
        print("\n")
        print(chromosome)
        f.write("{} {}\n".format(population,counter))
        print("Population Size: {}".format(population))
        print("Genetic Algorithm Took {} steps for max1 Problem".format(counter))
    f.close()
    f = open("file2.txt",'w')
    population = 4
    for length in range(8,41,2): #for population 4 and even chromosome length from 8 to 40 run Algo
        chromosome = []
        populate(chromosome,length,population)
        result = False
        counter=0
        while not result:
            counter+=1
            sort_upon_fitness(chromosome,length,population)
            cross_over(chromosome,length,population)
            mutate(chromosome,length,population)
            result=check_result(chromosome,population,length)
            print(chromosome)
        print("\n")
        f.write("{} {}\n".format(length,counter))
        print("Length Of Chromosome: {}".format(length))
        print("Genetic Algorithm Took {} steps for max1 Problem".format(counter))
    f.close() 
    graph_generator()

