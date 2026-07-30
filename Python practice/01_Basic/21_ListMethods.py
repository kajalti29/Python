
# Common List Methods 
# append() :- List ke end me ek item add kar deta hai.
nums = [1, 2, 3]
nums.append(4)
print(nums)  # Output: [1, 2, 3, 4]

# insert() :- List ke specified index par ek item add kar deta hai.
nums = [1, 2, 3]
nums.insert(1, 1.5)
print(nums)  # Output: [1, 1.5, 2, 3]

# pop() :- List ke end se ya specified index se item remove kar deta hai.
nums = [1, 2, 3, 4]
removed_item = nums.pop()
print(removed_item)  # Output: 4