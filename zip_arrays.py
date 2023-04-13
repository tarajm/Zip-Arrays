#ZIP Arrays into dictionary
# Dictionaries are sometimes called maps because a key (string) maps to a value. Given two arrays, 
# create an associative array (map) containing keys of the first, and values of the second. 
# For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.

def zip_arrays(arr1,arr2):
    dictionary = {}
    count = 0
    for i in arr1:
        dictionary[i] = arr2[count]
        count += 1
        
    return dictionary
print(zip_arrays(['abc', 3, 'yo'],[42, 'wassap',True]))




# def zip_arrays_into_dictionary(arr_1, arr_2):
#     d = {}
#     for key, val in arr_1:
#         for val in arr_2:
#             d[key] = val
#     return d

# print(zip_arrays_into_dictionary(['abc', 3, 'yo'],[42, 'wassap',True]))