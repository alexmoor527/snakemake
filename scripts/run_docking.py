from biobb_vs.vina.autodock_vina_run import autodock_vina_run

# Define input and output paths and properties
input_ligand_pdbqt_path = snakemake.input.ligand  # e.g., data/{config[ligand_code]}.pdbqt
input_receptor_pdbqt_path = snakemake.input.protein  # e.g., data/{config[pdb_code]}_protein.pdbqt
input_box_path = snakemake.input.box  # e.g., data/box.pdb
output_pdbqt_path = snakemake.output.docking  # e.g., results/output_vina.pdbqt
output_log_path = snakemake.output.log  # e.g., results/output_vina.log
properties = snakemake.params.config  # Additional configuration passed via Snakefile

# Debugging: Print paths and properties
print(f"Input ligand: {input_ligand_pdbqt_path}")
print(f"Input receptor: {input_receptor_pdbqt_path}")
print(f"Input box: {input_box_path}")
print(f"Output docking file: {output_pdbqt_path}")
print(f"Output log file: {output_log_path}")
print(f"Properties: {properties}")

# Call autodock_vina_run
autodock_vina_run(
    input_ligand_pdbqt_path=input_ligand_pdbqt_path,
    input_receptor_pdbqt_path=input_receptor_pdbqt_path,
    input_box_path=input_box_path,
    output_pdbqt_path=output_pdbqt_path,
    output_log_path=output_log_path,
    properties=properties
)

