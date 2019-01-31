import numpy as np

ran = np.random.random((3, 4))

print(np.max(ran, axis=0))
print(np.max(ran, axis=1))
print(np.min(ran, axis=0))
print(np.min(ran, axis=1))
print()

new_arr = np.reshape(ran, (12))
print(new_arr)
print()

new_arr_two = np.reshape(ran, (12, 1))
print(new_arr_two)


