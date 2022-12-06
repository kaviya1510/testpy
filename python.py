from math import sqrt
import random
#Is_Prime Function to check if given value is Prime or not
def is_prime(n):
	flag = 0
	if(n > 1):
		for i in range(2, int(sqrt(n)) + 1):
			if (n % i == 0):
				flag = 1
				break
		if (flag == 0):
			return("True")
		else:
			return("False")
	else:
		return("False")

#generate_random_number function to provide all prime values within a range
def generate_random_number(n1,n2):
	g_list=[]
	for num in range(n1, n2 + 1):
		if num > 1:
			for i in range(2, int(sqrt(num)) + 1):
				if (num % i) == 0:
					break
			else:
				glist=num
				g_list.append(int(glist))
	return(g_list)
#number_of_primes_in_the_range Function to provide count of prime numbers within a range
def number_of_primes_in_the_range(n1,n2):
	cnt=0
	for num in range(n1, n2 + 1):
		if num > 1:
			for i in range(2, int(sqrt(num)) + 1):
				if (num % i) == 0:
					break
			else:
				cnt=cnt+1
	return(cnt)

def mainfunction():

	print('Provide inputs of 3 integers from the keyboard:')
	print('\tThe 1st is the number of unique prime numbers to be created:')
	print('\tThe 2nd and 3rd define the range of those prime number.')
	ip = input('Enter those 3 integers seperated by space:')
	print("\n")
	value_list = ip.split()
	for i in range(len(value_list)):
		value_list[i] = int(value_list[i])
	first_value=value_list[0]
	range_check=number_of_primes_in_the_range(value_list[1],value_list[2])
	if range_check >= first_value:
		r_list=[]
		m_list=[]
		for i in range(first_value):
			random_list = generate_random_number(value_list[1], value_list[2])
		print("The generated random number list:")
		print(random_list)
		print("The Sorted Order:")
		s_list=sorted(random_list)
		print(s_list)
		len_slist=len(s_list)
		lenn=int(len_slist)
		print ("The Minimum and Maximum prime numbers are:" ,s_list[0],s_list[lenn-1])
	else:
		print ("**** Improper input was provided;try again!****")
		mainfunction()

mainfunction()
