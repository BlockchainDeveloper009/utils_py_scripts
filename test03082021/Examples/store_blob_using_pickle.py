import pickle
import math

import os

scores = {} # scores is an empty dict already
"""
if os.path.getsize(target) > 0:      
    with open(target, "rb") as f:
        unpickler = pickle.Unpickler(f)
        # if file is not empty scores will be equal
        # to the value unpickled
        scores = unpickler.load()
        """
object_pi = ["asdfsdfasdfsds", "adfsfsdfsdfsdf", "adfsadfsfsdfs sfsdds"]
file_pi = open('filename_pi.obj', 'wb')
pickle.dump(object_pi, file_pi)

if os.path.getsize('filename_pi.obj') > 0:
    file_pi2 = open('filename_pi.obj', 'rb')
    object_pi2 = pickle.load(file_pi2)

    print(object_pi2)
else:
    print('nothing to print')