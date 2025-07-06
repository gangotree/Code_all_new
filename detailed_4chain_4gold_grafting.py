from ase import Atoms
from ase.io import read, write
import numpy as np

# Load structures (gold NP and all polymer chains)
gold = read("gold.pdb")
polymer1 = read("1pnipam_2L_S_Au.pdb")
polymer2 = read("2pnipam_2L_S_Au.pdb")
polymer3 = read("3pnipam_2L_S_Au.pdb")
polymer4 = read("4pnipam_2L_S_Au.pdb")

# Target gold atom index and store it's coordinate in different variables
gold_index = [28, 30, 44, 172]
gold_pos1 = gold[gold_index[0]].position
print (gold_pos1)
gold_pos2 = gold[gold_index[1]].position
gold_pos3 = gold[gold_index[2]].position
gold_pos4 = gold[gold_index[3]].position

# Compute outward normal from NP center to gold atom
center = gold.get_center_of_mass()
# unit vector pointing outward from the center of the NP to the gold atom at gold_index.
normal1 = gold_pos1 - center
normal1 /= np.linalg.norm(normal1)  
normal2 = gold_pos2 - center
normal2 /= np.linalg.norm(normal2) 
normal3 = gold_pos3 - center
normal3 /= np.linalg.norm(normal3)
normal4 = gold_pos4 - center
normal4 /= np.linalg.norm(normal4)  

# Graft point: 0.23 nm = 2.3 Å away from gold atom along normal
graft_point1 = gold_pos1 + normal1 * 2.30
graft_point2 = gold_pos2 + normal2 * 2.30
graft_point3 = gold_pos3 + normal3 * 2.30
graft_point4 = gold_pos4 + normal4 * 2.30

# Find sulfur anchor in polymer
anchor_idx1 = [i for i, atom in enumerate(polymer1) if atom.symbol == 'S'][-1]
anchor_pos1 = polymer1[anchor_idx1].position
anchor_idx2 = [i for i, atom in enumerate(polymer2) if atom.symbol == 'S'][-1]
anchor_pos2 = polymer2[anchor_idx2].position
anchor_idx3 = [i for i, atom in enumerate(polymer3) if atom.symbol == 'S'][-1]
anchor_pos3 = polymer3[anchor_idx3].position
anchor_idx4 = [i for i, atom in enumerate(polymer4) if atom.symbol == 'S'][-1]
anchor_pos4 = polymer4[anchor_idx4].position

# Find bonded neighbor of S (for S–C bond direction)
positions1 = polymer1.get_positions()
dists1 = np.linalg.norm(positions1 - anchor_pos1, axis=1)
dists1[anchor_idx1] = np.inf
neighbor_idx1 = np.argmin(dists1)
neighbor_pos1 = positions1[neighbor_idx1]
bond_vec1 = neighbor_pos1 - anchor_pos1
bond_vec1 /= np.linalg.norm(bond_vec1)

positions2 = polymer2.get_positions()
dists2 = np.linalg.norm(positions2 - anchor_pos2, axis=1)
dists2[anchor_idx2] = np.inf
neighbor_idx2 = np.argmin(dists2)
neighbor_pos2 = positions2[neighbor_idx2]
bond_vec2 = neighbor_pos2 - anchor_pos2
bond_vec2 /= np.linalg.norm(bond_vec2)

positions3 = polymer3.get_positions()
dists3 = np.linalg.norm(positions3 - anchor_pos3, axis=1)
dists3[anchor_idx3] = np.inf
neighbor_idx3 = np.argmin(dists3)
neighbor_pos3 = positions3[neighbor_idx3]
bond_vec3 = neighbor_pos3 - anchor_pos3
bond_vec3 /= np.linalg.norm(bond_vec3)

positions4 = polymer4.get_positions()
dists4 = np.linalg.norm(positions4 - anchor_pos4, axis=1)
dists4[anchor_idx4] = np.inf
neighbor_idx4 = np.argmin(dists4)
neighbor_pos4 = positions4[neighbor_idx4]
bond_vec4 = neighbor_pos4 - anchor_pos4
bond_vec4 /= np.linalg.norm(bond_vec4)


# Align S–C bond to the surface normal
rotation_axis1 = np.cross(bond_vec1, normal1)
angle1 = np.arccos(np.clip(np.dot(bond_vec1, normal1), -1.0, 1.0))
angle_deg1 = np.degrees(angle1)

rotation_axis2 = np.cross(bond_vec2, normal2)
angle2 = np.arccos(np.clip(np.dot(bond_vec2, normal2), -1.0, 1.0))
angle_deg2 = np.degrees(angle2)

rotation_axis3 = np.cross(bond_vec3, normal3)
angle3 = np.arccos(np.clip(np.dot(bond_vec3, normal3), -1.0, 1.0))
angle_deg3 = np.degrees(angle3)

rotation_axis4 = np.cross(bond_vec4, normal4)
angle4 = np.arccos(np.clip(np.dot(bond_vec4, normal4), -1.0, 1.0))
angle_deg4 = np.degrees(angle4)

if np.linalg.norm(rotation_axis1) > 1e-6:
    polymer1.rotate(angle_deg1, v=rotation_axis1, center=anchor_pos1)
    
if np.linalg.norm(rotation_axis2) > 1e-6:
    polymer2.rotate(angle_deg2, v=rotation_axis2, center=anchor_pos2)
    
if np.linalg.norm(rotation_axis3) > 1e-6:
    polymer3.rotate(angle_deg3, v=rotation_axis3, center=anchor_pos3)

if np.linalg.norm(rotation_axis4) > 1e-6:
    polymer4.rotate(angle_deg4, v=rotation_axis4, center=anchor_pos4)

# Translate polymer so sulfur sits at the graft point (23.0 Å away from gold atom)
shift1 = graft_point1 - polymer1[anchor_idx1].position
polymer1.translate(shift1)

shift2 = graft_point2 - polymer2[anchor_idx2].position
polymer2.translate(shift2)

shift3 = graft_point3 - polymer3[anchor_idx3].position
polymer3.translate(shift3)

shift4 = graft_point4 - polymer4[anchor_idx4].position
polymer4.translate(shift4)

# Combine and write structure
combined = polymer1 + polymer2 + polymer3 + polymer4 + gold
write("test.pdb", combined)


