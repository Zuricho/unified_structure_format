import numpy as np
import matplotlib.pyplot as plt
import pickle

# INPUT
FILE_PATH = "example/Rockbridgeite.usf"
FILE_NAME = "Rockbridgeite"



color_dict = {
    "C": "black",
    "O": "red",
    "N": "blue",
    "P": "orange",
    "S": "yellow",
    "Fe": "green",
    "Ni": "green",
    "Mn": "green",
}

size_dict = {
    "C": 70,
    "O": 60,
    "N": 65,
    "P": 100,
    "S": 100,
    "Fe": 140,
    "Ni": 135,
    "Mn": 135,
}

usf_dict = pickle.load(open(FILE_PATH, "rb"))


# 3D visualization of atom coordiates
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='3d')
ax.scatter(usf_dict["coordinate"][:,0], 
           usf_dict["coordinate"][:,1], 
           usf_dict["coordinate"][:,2], 
           c=[color_dict[i] for i in usf_dict["atom_type"]],
           s=[size_dict[i] for i in usf_dict["atom_type"]],
           marker='o',
           alpha=1)


for i in range(len(usf_dict["bond"])):
    plt.plot([usf_dict["coordinate"][usf_dict["bond"][i][0]][0], usf_dict["coordinate"][usf_dict["bond"][i][1]][0]],
             [usf_dict["coordinate"][usf_dict["bond"][i][0]][1], usf_dict["coordinate"][usf_dict["bond"][i][1]][1]],
             [usf_dict["coordinate"][usf_dict["bond"][i][0]][2], usf_dict["coordinate"][usf_dict["bond"][i][1]][2]], 'b')
    
plt.show()

