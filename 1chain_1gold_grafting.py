from ase import Atoms
from ase.io import read, write
import numpy as np

# Load structures
gold = read("gold.pdb")
polymer = read("1pnipam_2L_S_Au.pdb")

# Target gold atom index
gold_index = 46
gold_pos = gold[gold_index].position

# Compute outward normal from NP center to gold atom
center = gold.get_center_of_mass()
normal = gold_pos - center
normal /= np.linalg.norm(normal)

# Graft point: 0.23 nm = 2.3 Å away from gold atom along normal
graft_point = gold_pos + normal * 2.30

# Find sulfur anchor in polymer
anchor_idx = [i for i, atom in enumerate(polymer) if atom.symbol == 'S'][-1]
anchor_pos = polymer[anchor_idx].position

# Find bonded neighbor of S (for S–C bond direction)
positions = polymer.get_positions()
dists = np.linalg.norm(positions - anchor_pos, axis=1)
dists[anchor_idx] = np.inf
neighbor_idx = np.argmin(dists)
neighbor_pos = positions[neighbor_idx]
bond_vec = neighbor_pos - anchor_pos
bond_vec /= np.linalg.norm(bond_vec)

# Align S–C bond to the surface normal
rotation_axis = np.cross(bond_vec, normal)
angle = np.arccos(np.clip(np.dot(bond_vec, normal), -1.0, 1.0))
angle_deg = np.degrees(angle)

if np.linalg.norm(rotation_axis) > 1e-6:
    polymer.rotate(angle_deg, v=rotation_axis, center=anchor_pos)

# Translate polymer so sulfur sits at the graft point (23.0 Å away from gold atom)
shift = graft_point - polymer[anchor_idx].position
polymer.translate(shift)

# Combine and write structure
combined = polymer + gold
write("test.pdb", combined)

# Optional: confirm distance
print("Final S–Au distance:", np.linalg.norm(polymer[anchor_idx].position - gold_pos) / 10, "nm")

