# -*- coding: utf-8 -*-
"""

Example of how the edit distance function works.

"""

from nltk.metrics import edit_distance


def partially_randomly_permute_phrase(s, distortion):
    """
    s : any string or list
    distortion : how many letters to swap
    """
    import numpy as np
    permute_these = np.random.permutation(len(s))[:distortion]
    final_position = np.random.permutation(len(permute_these))
    the_permutation = list(range(len(s)))   
    for j in range(len(permute_these)):
        the_permutation[permute_these[j]] = permute_these[final_position[j]]   
    s_permuted = ''.join([s[j] for j in the_permutation])
    return s_permuted
    
    
   
s = "This is the most vanilla sentence you can imagine."

x = []
for i in range(4):       
    x.append(partially_randomly_permute_phrase(s, distortion = 3*i))
print(x)

for j in range(len(x)):
    d = edit_distance(x[0],x[j], transpositions=False)
    dt = edit_distance(x[0],x[j], transpositions=True)
    print(0,j,d,dt)

