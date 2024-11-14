import numpy as np
import matplotlib.pyplot as plt
import pickle

# INPUT
FILE_PATH = "example/6zk6_core.usf"
FILE_NAME = "6zk6_core"


usf_dict = pickle.load(open(FILE_PATH, "rb"))


# 3D visualization of atom coordiates
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='3d')
ax.scatter(usf_dict["coordinate"][:,0], usf_dict["coordinate"][:,1], usf_dict["coordinate"][:,2], c='r', marker='o')

for i in range(len(usf_dict["bond"])):
    plt.plot([usf_dict["coordinate"][usf_dict["bond"][i][0]][0], usf_dict["coordinate"][usf_dict["bond"][i][1]][0]],
             [usf_dict["coordinate"][usf_dict["bond"][i][0]][1], usf_dict["coordinate"][usf_dict["bond"][i][1]][1]],
             [usf_dict["coordinate"][usf_dict["bond"][i][0]][2], usf_dict["coordinate"][usf_dict["bond"][i][1]][2]], 'b')
    
plt.show()
