from ItemHandler import rank

obj1 = ({'name': 'QFC',
         'distance': 1.3,
         'markup': 1.5
         },
        7.50)

obj2 = ({'name': 'Target',
         'distance': 2.0,
         'markup': 1.2
         },
        5.00)

store_data = [obj1, obj2]

ranks = rank(store_data)

expected_qfc_rank = 0.7*(7.50/7.50) + 0.3*(1.3/2.0)
expected_target_rank = 0.7*(5.00/7.50) + 0.3*(2.0/2.0)

assert expected_qfc_rank == ranks['QFC']
assert expected_target_rank == ranks['Target']
print('Tests passed')

