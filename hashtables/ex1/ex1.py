#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

'''
FOR LOOP VARIANT
'''
# def get_indices_of_item_weights(weights, length, limit):
#     for i in range(length):
#         for j in range(length):
#             if weights[i] + weights[j] == limit and i != j:
#                 if i > j:
#                     return (i, j)
#                 else:
#                     return (j, i)

'''
HASH TABLE VARIANT
'''
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        hash_table_insert(ht, weights[i], i)

        index = hash_table_retrieve(ht, (limit - weights[i]))
        second_index = weights.index(weights[i])

        if index is not None and index != second_index:
            if second_index > index:
                return (second_index, index)
            else: 
                return (index, second_index)



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([4, 4], 2, 8))