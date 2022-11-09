import matplotlib.pyplot as plt
import numpy as np

with open('Sensor_1.txt') as f:
    lines_1 = f.readlines()
    arr_1 = np.zeros((2, len(lines_1)))
    for i, line in enumerate(lines_1):
        tindex_s = line.index("time: ") + 6
        tindex_e = line.index(" moved: ")
        arr_1[0, i] = float(line[tindex_s:tindex_e])
        if line[tindex_e + 8:tindex_e + 12] == "True":
            arr_1[1, i] = 1
        else:
            arr_1[1, i] = 0


with open('Sensor_2.txt') as f:
    lines_2 = f.readlines()
    arr_2 = np.zeros((2, len(lines_2)))
    for i, line in enumerate(lines_2):
        tindex_s = line.index("time: ") + 6
        tindex_e = line.index(" moved: ")
        arr_2[0, i] = float(line[tindex_s:tindex_e])
        if line[tindex_e + 8:tindex_e + 12] == "True":
            arr_2[1, i] = 1
        else:
            arr_2[1, i] = 0

with open('Sensor_3.txt') as f:
    lines_3 = f.readlines()
    arr_3 = np.zeros((2, len(lines_3)))
    for i, line in enumerate(lines_3):
        tindex_s = line.index("time: ") + 6
        tindex_e = line.index(" moved: ")
        arr_3[0, i] = float(line[tindex_s:tindex_e])
        if line[tindex_e + 8:tindex_e + 12] == "True":
            arr_3[1, i] = 1
        else:
            arr_3[1, i] = 0

with open('Sensor_4.txt') as f:
    lines_4 = f.readlines()
    arr_4 = np.zeros((2, len(lines_4)))
    for i, line in enumerate(lines_4):
        tindex_s = line.index("time: ") + 6
        tindex_e = line.index(" moved: ")
        arr_4[0, i] = float(line[tindex_s:tindex_e])
        if line[tindex_e + 8:tindex_e + 12] == "True":
            arr_4[1, i] = 1
        else:
            arr_4[1, i] = 0

with open('Sensor_5.txt') as f:
    lines_5 = f.readlines()
    arr_5 = np.zeros((2, len(lines_5)))
    for i, line in enumerate(lines_5):
        tindex_s = line.index("time: ") + 6
        tindex_e = line.index(" moved: ")
        arr_5[0, i] = float(line[tindex_s:tindex_e])
        if line[tindex_e + 8:tindex_e + 12] == "True":
            arr_5[1, i] = 1
        else:
            arr_5[1, i] = 0

fig, ax = plt.subplots()
plt.scatter(arr_1[0], arr_1[1], c='green')
plt.scatter(arr_2[0], arr_2[1], c='red')
plt.scatter(arr_3[0], arr_3[1], c='blue')
plt.scatter(arr_4[0], arr_4[1], c='cyan')
plt.scatter(arr_5[0], arr_5[1], c='yellow')
ax.xaxis.set_ticks(np.arange(90, 180, 10))
plt.legend(['Sensor_1: Kitchen (left)', 'Sensor_2: Kitchen (right)', 'Sensor_3: Bedroom', 'Sensor_4: TV/Computer Room', 'Sensor_5: Bathroom'])
plt.xlabel("Sensor Reading Time of Simulation in Seconds")
plt.ylabel("Movement Detected: 1.0 indicates movement")
plt.savefig("Sensor Graph")
plt.show()
