# def twoSum(nums:list[int], target: int) -> list[int]:
#     for i in range(len(nums)):
#         for j in range(i+1, len (nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
            

# run = twoSum([2,7,11,15], 9)
# print(run)







# prefix = []

# # Loop through the indices of the FIRST word ('f', 'l', 'o', 'w', 'e', 'r')
# for char_idx in range(len(strs[0])):
#     char_to_match = strs[0][char_idx]
    
#     # Check this character against the same position in all other words
#     for word_idx in range(1, len(strs)):
#         # If the current word is too short, or the character doesn't match, stop!
#         if char_idx >= len(strs[word_idx]) or strs[word_idx][char_idx] != char_to_match:
#             print("".join(prefix))
#             return # Or break/exit
            
#     # If every word matched, add it to our prefix
#     prefix.append(char_to_match)

# print("".join(prefix))