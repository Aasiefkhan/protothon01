user_ip = input("enter the string")
print(user_ip)

#upper case
print(user_ip.upper())

#lower case
print(user_ip.lower())

#to title case
split_list = []
split_list = user_ip.split(' ')
len_split = len(split_list)
append_string= str("")
for i in range (0,len_split):
    temp = split_list[i].capitalize()
    append_string = str(append_string)+str(" ")+str(temp)  
print(append_string)
    
#to start case
temp1 = split_list[0].capitalize()
start_case = str(temp1)
for i in range (1,len_split):
    start_case = str(start_case)+str(" ")+str(split_list[i]) 
print(start_case)