# # return list with common elenents from 2 different list
# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))

def common_elements(list1, list2):
    common_list = []
    list1 = list(set(list1))
    list2 = list(set(list2))
    [common_list.append(i) for i in list1 if i in list2]
    return common_list
    
print(common_elements([1,2,3,3],[3,4,5]))

