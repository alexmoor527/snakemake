from biobb_vs.utils.extract_model_pdbqt import extract_model_pdbqt

# Input and output paths
input_docking_path = snakemake.input.docking  # e.g., results/output_vina.pdbqt
output_structure_path = snakemake.output.structure  # e.g., results/output_structure.pdbqt

# Debugging: Print paths
print(f"Input docking file: {input_docking_path}")
print(f"Output structure file: {output_structure_path}")

# Call extract_model_pdbqt
extract_model_pdbqt(
    input_pdbqt_path=input_docking_path,
    output_pdbqt_path=output_structure_path,
    properties={}
)

