nums = list(range(21))
even_nums = [i for i in nums if i%2 == 0]
odd_nums = [i for i in nums if i%2 ==1]

#Merging lists
even_nums.extend(odd_nums) 
merged_lists = even_nums

#Multipling values
for i in range(21):
    merged_lists[i] *= 2

#Sorting list
merged_lists.sort()

for i in merged_lists:
    print(i)
