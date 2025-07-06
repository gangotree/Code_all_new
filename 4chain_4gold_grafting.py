from ase import Atoms
from ase.io import read, write
import numpy as np

# Load gold NP input structures
gold = read("gold.pdb")

# Import the filenames of all input polymers
polymer_input = ["1pnipam_2L_S_Au.pdb", "2pnipam_2L_S_Au.pdb", "3pnipam_2L_S_Au.pdb", "4pnipam_2L_S_Au.pdb"]

# Target gold atom indices
gold_index = [28, 30, 170, 172]		# In gold.pdb it will be atom number 29, 31, 171, 173

# calculate the center of nanoparticle
center = gold.get_center_of_mass()

# Empty array to store the coordinate of translated polymer after shifting
all_polymers = []

# Now important section: execute a for loop which iterate over all the aforementioned polymers and gold indices 
for poly_files, Au_idx in zip(polymer_input, gold_index):
	polymers = read(poly_files)		# read all the input polymers
	gold_pos = gold[Au_idx].position	# store the coordinate of targeted gold atoms at {1 1 1} surface
	# unit vector pointing outward from the center of the NP to the each gold atom at Au_index (i.e., gold_index)
	normal = gold_pos - center 	# gives the vector from the NP center to the selected gold atom
	normal /= np.linalg.norm(normal)  # compute the magnitude of the above vector and make it unit vector	 

	# Specify the graft point: 0.23 nm = 2.3 Å away from gold atom along normal
	graft_point = gold_pos + normal * 2.30

	# Find sulfur anchor in all polymers
	anchor_idx = [i for i, atom in enumerate(polymers) if atom.symbol == 'S'][-1]
	anchor_pos = polymers[anchor_idx].position
	
	# Find bonded neighbor of S (for S–C bond direction)
	positions = polymers.get_positions()
	dists = np.linalg.norm(positions - anchor_pos, axis=1)
	dists[anchor_idx] = np.inf
	neighbor_idx = np.argmin(dists)
	neighbor_pos = positions[neighbor_idx]
	bond_vec = neighbor_pos - anchor_pos
	bond_vec /= np.linalg.norm(bond_vec)

	# Align S–C bond with respective gold surface normal
	rotation_axis = np.cross(bond_vec, normal)
	angle = np.arccos(np.clip(np.dot(bond_vec, normal), -1.0, 1.0))
	angle_deg = np.degrees(angle)

	if np.linalg.norm(rotation_axis) > 1e-6:
    		polymers.rotate(angle_deg, v=rotation_axis, center=anchor_pos)
    	
    	# Apply fixed tilt angle (same for all chains)
	tilt_angle_deg = 3  # or any fixed number you want
	if tilt_angle_deg != 0:
    		polymers.rotate(tilt_angle_deg, v=normal, center=anchor_pos)

	# Translate polymer so sulfur sits at the graft point (2.3 Å away from gold atom)
	shift = graft_point - polymers[anchor_idx].position
	polymers.translate(shift)
	# Additional translation along x by 0.144 nm (1.44 Å) so that Au-S-C angle should be 
	#polymers.translate([1.44, 0.0, 0.0])
	
	# now store the updated polymer coordinates in aforementioned empty array
	all_polymers.append(polymers)

# Combine coordinates (C) of all polymers and gold 
combined = gold.copy()
for C in all_polymers:
    combined += C

# Now write the coordinate into output file
write("test.pdb", combined)


