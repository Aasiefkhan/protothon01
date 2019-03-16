import math
sep_values = []
int_list = []
userinput= str(input("enter the string "))
sep_values = userinput.split(',')
len_values = len(sep_values)
square_sum = 0
for i in range (0,len_values):
    temp = float(sep_values[i])
    print(temp)
    temp = temp*temp
    int_list.append(temp)
    square_sum = square_sum+temp
print(int_list)
print(square_sum)
mean_sum = square_sum/float(len_values)
print(mean_sum)
root_mean_square = math.sqrt(mean_sum)
print(root_mean_square)