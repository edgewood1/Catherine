#importing a file called random that includes randint
import random
#setting mylist as an empty list
mylist = []

number_of_trials = 1000

#creating a for loop to add a random 1 or 0 to my list a thousand times
for i in range(0, number_of_trials):
	mylist.append(random.randint(0, 1))

one_count=0
zero_count=0

if 1 in mylist:
	one_count= mylist.count(1)
else:
	one_count=0
if 0 in mylist:
	zero_count= mylist.count(0)
else:
	zero_count=0
#printing mylist now a list of a thousand random numbers of 1 or 0
print(mylist)
print("Random ones:", one_count)
print("Random zeros:", zero_count)

def percentage_of_ones(one_count, number_of_trials):
	result = one_count/number_of_trials * 100
	return result
print ("Percentage of ones: " + str(percentage_of_ones(one_count, number_of_trials)) + "%")
def percentage_of_ones(zero_count, number_of_trials):
	result = zero_count/number_of_trials * 100
	return result
print ("Percentage of zeros: " + str(percentage_of_ones(zero_count, number_of_trials)) + "%")