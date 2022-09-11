# Reference of SA algorithm is taken from http://apmonitor.com/me575/index.php/Main/SimulatedAnnealing
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import math

# Creating a field of targets randomly spread on 500x500m area. The target positions change with each run
# The below function returns the position / coordinates of targets on the field
def target_sites(): 
    X = 500
    Y = 500
    targets = 17 
    tot_targets = 250000 # (500x500) possible locations to choose from
    x_coor = []; y_coor = []
    count=0
    while count < 17:
        a = random.randint(1, 500)
        if a not in x_coor: #constraints that are taken care of
            x_coor.append(a)
            count = count+1

    count = 0
    while count < 17:
        b = random.randint(1, 500)
        y_coor.append(b)
        count = count+1
    print("X_coor are:::::::: ", x_coor)
    print("Y_coor are:::::::: ", y_coor)    
    return x_coor, y_coor

#placing sensor on the field such that all the constraints are satisfied
#The below function returns the position / coordinates of all the 3 sensors 
def sen_loc(x_coor,y_coor):
    s1_coor_x = []; s1_coor_y = []
    s2_coor_x = []; s2_coor_y = []
    s3_coor_x = []; s3_coor_y = []
    
    count = 0
    while count < s1:
        c = random.randint(1, 500)
        if c not in (x_coor and s1_coor_x): #constraints to be satisfied wrt assignment
            s1_coor_x.append(c)
            count = count+1
    count = 0
    while count < s1:
        d = random.randint(1, 500)
        s1_coor_y.append(d)
        count = count+1
    
    count = 0
    while count < s2:
        d = random.randint(1, 500)
        if d not in (x_coor and s1_coor_x and s2_coor_x):
            s2_coor_x.append(d)
            count = count+1
    count = 0
    while count < s2:
        e = random.randint(1, 500)
        s2_coor_y.append(e)
        count = count+1    

    count = 0
    while count < s3:
        f = random.randint(1, 500)
        if f not in (x_coor and s1_coor_x and s2_coor_x and s3_coor_x):
            s3_coor_x.append(f)
            count = count+1

    count = 0
    while count < s3:
        e = random.randint(1, 500)
        s3_coor_y.append(e)
        count = count+1

    return s1_coor_x, s1_coor_y, s2_coor_x, s2_coor_y, s3_coor_x, s3_coor_y

#plotting the sensor field location and their range
def plotting(s1_coor_x, s1_coor_y, s2_coor_x, s2_coor_y,s3_coor_x, s3_coor_y,x_coor,y_coor,s1,s2,s3):
    plt.scatter(x_coor, y_coor, color='red', label='Targets') 
    for i, label in enumerate(range(1,18)): 
        plt.annotate(label, (x_coor[i], y_coor[i]))
    plt.scatter(s1_coor_x, s1_coor_y, color='blue', label='Sensor1', marker = 'x') 
    for i, label in enumerate(range(s1)): 
        plt.annotate(label, (s1_coor_x[i], s1_coor_y[i]))
    plt.scatter(s2_coor_x, s2_coor_y, color='green', label='Sensor2', marker = 'x') 
    for i, label in enumerate(range(s2)): 
        plt.annotate(label, (s2_coor_x[i], s2_coor_y[i]))
    plt.scatter(s3_coor_x, s3_coor_y, color='black', label='Sensor3', marker = 'x') 
    for i, label in enumerate(range(s3)): 
        plt.annotate(label, (s3_coor_x[i], s3_coor_y[i]))
    for i in range(s1):
        draw_circle = plt.Circle((s1_coor_x[i],s1_coor_y[i]), 100, fill=False) 
        plt.gcf().gca().add_artist(draw_circle)
    for i in range(s2):
        draw_circle = plt.Circle((s2_coor_x[i],s2_coor_y[i]), 70, fill=False) 
        plt.gcf().gca().add_artist(draw_circle)
    for i in range(s3):
        draw_circle = plt.Circle((s3_coor_x[i],s3_coor_y[i]), 30, fill=False) 
        plt.gcf().gca().add_artist(draw_circle)
    plt.xlim(0,510); plt.ylim(0,510)
    # plt.legend()
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.) 
    plt.draw(); plt.waitforbuttonpress(0); plt.close()


#Checking coverage of all targets in the list and then returns True if all the target positions are k covered
def Check_coverage(k,s1,s2,s3):
    Is_coverage = 17*[0]
    #s1
    for i in range(17):
        for j in range(s1):
            dist = math.sqrt((x_coor[i] - s1_coor_x[j])**2 + (y_coor[i] - s1_coor_y[j])**2 ) #finding distance
            if dist <= r1:
                Is_coverage[i] =Is_coverage[i] + 1

    #s2
    for i in range(17):
        for j in range(s2):
            dist = math.sqrt((x_coor[i] - s2_coor_x[j])**2 + (y_coor[i] - s2_coor_y[j])**2 )
            if dist <= r2:
                Is_coverage[i] =Is_coverage[i] + 1

    #s3
    for i in range(17):
        for j in range(s3):
            dist = math.sqrt((x_coor[i] - s3_coor_x[j])**2 + (y_coor[i] - s3_coor_y[j])**2 )
            if dist <= r3:
                Is_coverage[i] =Is_coverage[i] + 1

    if k ==1:
        for i in range(17):
            if Is_coverage[i] <1:
                return False
    
    if k ==2:
        for i in range(17):
            if Is_coverage[i] <2:
                return False

    if k ==3:
        for i in range(17):
            if Is_coverage[i] <3:
                return False
    print("IS_coverage", Is_coverage) #prints the list of length 17 with values showing the number of sensors that covers that particular target
    
    return True

s1 = 20; s2 = 20; s3 = 10 #initial number of sensors which changes in the following code wrt the cost
r1 = 100; r2 = 70; r3 = 30 #range of sensors
#cost of sensors
c1 = 300
c2 = 170
c3 = 65
cost = s1*r1 + s2*r2 + s3*r3 #initial cost
x_coor, y_coor = target_sites() #position of targets
initial_cost  = cost
iterations = 50 #each cycle has 50 iterations
cycles = 1500   #cycles which is a parameter that can be altered by the user
temp1 = -1.0/math.log(0.7); temp50 = -1.0/math.log(0.001) #inital temp and final temp
fraction = (temp50/temp1)**(1.0/(cycles-1.0))
temp = temp1
deltaAvg = 0.0
best_cost = initial_cost #choosing best cost as initial cost
na = 1 #no_of_acceptable_solutions
all_cost = [] #list to store all costs
all_approved_costs = [] #list to store all accepted cost
all_cost.append(cost)

#SIMULATED ANNEALING
for i in range(cycles+1):
    coverage = False    
    for j in range(iterations):
        while(coverage == False):
            #choosing sensors randomly between 1 to 50 
            s1 = random.randint(1,50)
            s2 = random.randint(1, 50)
            s3 = random.randint(1,25)
            
            s1_coor_x, s1_coor_y, s2_coor_x, s2_coor_y,s3_coor_x, s3_coor_y = sen_loc(x_coor, y_coor) #finding sensor locations
            k=3 #value of k
            coverage = Check_coverage(k,s1,s2,s3) #check if a target is k-connected 
            #if targets are k connected find the cost, compare with best cost, if new cost is less than best cost replace the best cost with 
            #new cost, else accept the worst cost based on the probablity function of acceptance
            if coverage==True:
                new_cost = s1*r1 + s2*r2 + s3*r3
                all_cost.append(new_cost)    #history
                print("Best cost: ", best_cost, " New cost: ", new_cost)
                if (best_cost > new_cost):
                    delta = abs(best_cost-new_cost)
                    best_cost = new_cost
                    #storing the best location of sensors for our plot
                    final_s1_x = s1_coor_x; final_s1_y = s1_coor_y
                    final_s2_x = s2_coor_x; final_s2_y = s2_coor_y
                    final_s3_x = s3_coor_x; final_s3_y = s3_coor_y
                    sen_1 = s1; sen_2 = s2; sen_3 = s3
                    all_approved_costs.append(best_cost)                    
                    na = na+1
                else:
                    # print("New cost is worse :(")
                    delta = abs(best_cost - new_cost)
                    if deltaAvg == 0:
                        deltaAvg = delta
                    probab_of_acceptance = math.exp(-delta/(deltaAvg * temp)) #probablity of acceptance of worst cost
                    random_num = random.uniform(0, 1) #generating a random number
                    
                    if random_num > probab_of_acceptance: #if random_num > prob_of_acceptance, donot accept the worst solution                        
                        continue
                    else: #accept worst cost
                        #accept worst cost
                        best_cost = new_cost #replacing best cost with new cost
                        
                        final_s1_x = s1_coor_x; final_s1_y = s1_coor_y
                        final_s2_x = s2_coor_x; final_s2_y = s2_coor_y
                        final_s3_x = s3_coor_x; final_s3_y = s3_coor_y
                        sen_1 = s1; sen_2 = s2; sen_3 = s3                        
                        all_approved_costs.append(best_cost)                        
                        na = na+1
    deltaAvg = (deltaAvg * (na-1.0) + delta) / (na)  #updating delta avg    
    #lower temp
    temp = fraction* temp 
print("All approved costs are: ", all_approved_costs)
plt.title("Cost vs no. of accepted costs and the sensors\n s1 = %d, s2 = %d, s3 = %d, k = %d, cost at the end =%d \n" %(sen_1, sen_2, sen_3, k,all_approved_costs[-1]))
plt.xlabel("Accepted costs"); plt.ylabel("Costs")
plt.plot(all_approved_costs)
plt.draw() 
plt.waitforbuttonpress(0) 
plt.close()
print(len(all_approved_costs))
plt.title("Sensor field for cost = %d \n s1 = %d, s2 = %d, s3 =%d with k = %d" %(all_approved_costs[-1], sen_1, sen_2, sen_3, k))
plott = plotting(final_s1_x, final_s1_y, final_s2_x, final_s2_y, final_s3_x, final_s3_y, x_coor, y_coor,sen_1,sen_2,sen_3)        

                        





    







