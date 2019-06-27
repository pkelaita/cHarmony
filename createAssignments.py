import numpy as np
import json

num_items = 5

stores = ["Target", "QFC", "Trader Joe's", "Whole Foods", "Fred Meyers "]

lists = []

for i in range(num_items):
    num_stores = np.random.randint(2, 5 + 1)
    choices = np.random.choice(range(len(stores)), num_stores, replace=False)
    lists.append([stores[index] for index in choices])

with open('assignments.json', 'w') as f:
    json.dump(lists, f, indent=4)

print('done')



