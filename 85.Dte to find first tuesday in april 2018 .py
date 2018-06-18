#Date to find first tuesday

import numpy as np
print("First tuesday in April 2018: ")
print(np.busday_offset('2018-04',0, roll='forward', weekmask='Tue'))