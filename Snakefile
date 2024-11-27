configfile: "config.yaml"

# Define the workflow output
rule all:
    input:
        "results/output_structure.pdb"


# Rule to fetch PDB structure
rule fetch_pdb:
    output:
        "data/{config[pdb_code]}.pdb"
    script:
        "scripts/fetch_pdb.py"

# Rule to extract the protein structure
rule extract_protein:
    input:
        "data/{config[pdb_code]}.pdb"
    output:
        "data/{config[pdb_code]}_protein.pdb"
    script:
        "scripts/extract_protein.py"

# Rule to compute cavities using PDBe API
rule compute_cavities:
    input:
        "data/{config[pdb_code]}_protein.pdb"
    output:
        "data/residues.json"
    script:
        "scripts/compute_cavities.py"

# Rule to generate the cavity box
rule generate_cavity_box:
    input:
        json="data/residues.json",
        pdb="data/{config[pdb_code]}_protein.pdb"
    output:
        "data/box.pdb"
    script:
        "scripts/generate_cavity_box.py"

# Rule to download the ligand
rule download_ligand:
    output:
        "data/{config[ligand_code]}.sdf"
    script:
        "scripts/download_ligand.py"

# Rule to prepare the ligand for docking
rule prepare_ligand:
    input:
        "data/{config[ligand_code]}.sdf"
    output:
        "data/{config[ligand_code]}.pdbqt"
    script:
        "scripts/prepare_ligand.py"

# Rule to prepare the protein for docking
rule prepare_protein:
    input:
        "data/{config[pdb_code]}_protein.pdb"
    output:
        "data/{config[pdb_code]}_protein.pdbqt"
    script:
        "scripts/prepare_protein.py"

# Rule to run the docking process
rule run_docking:
    input:
        ligand="data/{config[ligand_code]}.pdbqt",
        protein="data/{config[pdb_code]}_protein.pdbqt",
        box="data/box.pdb"
    output:
        docking="results/output_vina.pdbqt",
        log="results/output_vina.log"
    params:
        config=config
    script:
        "scripts/run_docking.py"


rule extract_docking_pose:
    input:
        docking="results/output_vina.pdbqt"
    output:
        structure="results/output_structure.pdbqt"
    script:
        "scripts/extract_docking_pose.py"

rule convert_to_pdb:
    input:
        pdbqt="results/output_structure.pdbqt"
    output:
        pdb="results/output_structure.pdb"
    shell:
        "obabel {input.pdbqt} -O {output.pdb}"  # Ensure Open Babel is installed


