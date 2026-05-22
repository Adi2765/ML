import numpy as np
#element wise comparison
marks=np.array([90,80,100,95,84])
print(marks==100)
print(marks>=85)
marks[marks<85]=0
print(marks)