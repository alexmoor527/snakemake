import json
from biobb_vs.utils.box_residues import box_residues

# Correctly access the JSON input file
with open(snakemake.input[0]) as json_file:
    data = json.load(json_file)

# Ensure the PDB code exists in the JSON data
pdb_code = snakemake.config["pdb_code"].lower()
if pdb_code not in data:
    raise KeyError(f"PDB code '{pdb_code}' not found in residues.json.")

# Ensure there are binding sites for the given PDB code
if not data[pdb_code]:
    raise ValueError(f"No binding sites found for PDB code '{pdb_code}'.")

# Select the desired binding site (default to the first one)
binding_site_index = 0  # Modify if a specific binding site index is required
if binding_site_index >= len(data[pdb_code]):
    raise IndexError(f"Binding site index {binding_site_index} out of range. Available sites: {len(data[pdb_code])}.")

# Extract residue list from the selected binding site
residue_list = [
    res["author_residue_number"]
    for res in data[pdb_code][binding_site_index]["site_residues"]
]

# Define properties for box_residues
properties = {
    "resid_list": residue_list,
    "offset": 12,  # Box size offset
    "box_coordinates": True  # Enable output of box coordinates
}

# Generate the cavity box
box_residues(
    input_pdb_path=snakemake.input[1],  # Use the protein PDB file as input
    output_pdb_path=snakemake.output[0],
    properties=properties
)

