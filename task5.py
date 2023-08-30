'''
input_list=["sakthi","dhoni","dravid"]
for i in input_list:
    print(sorted(i))
'''

input_list=["dhoni","dravid","sakthi"]
n=len(input_list)
for i in range(n):
    for j in range(0,n-i-1):
        if input_list[j]>input_list[j+1]:
            input_list[j],input_list[j+1]=input_list[j+1],input_list[j]
print(input_list)
            
        
