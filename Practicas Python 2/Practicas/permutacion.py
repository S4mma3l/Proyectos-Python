from itertools import permutations

palabra = input("Palabra a permutar: ")

permutations_list = [''.join(p) for p in permutations(palabra)]

print(f'{palabra} -> {", ".join(permutations_list)}')

# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])
 
# Print the obtained permutations
for i in list(perm):
    print (i)