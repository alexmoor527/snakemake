Snakemake Workflow: Protein-Ligand Docking Pipeline

This repository contains a Snakemake workflow for automating a protein-ligand docking process. It fetches a protein structure, prepares it, identifies cavities, downloads and prepares a ligand, and performs docking using AutoDock Vina.
Workflow Overview
Workflow Steps:

    Fetch PDB Structure
    Download the protein structure file in PDB format using a PDB code.

    Extract Protein Structure
    Extract the protein portion from the PDB file.

    Compute Cavities
    Use the PDBe API to identify cavities within the protein.

    Generate Cavity Box
    Create a docking box around the identified cavity.

    Download Ligand
    Download the ligand structure file in SDF format using a ligand code.

    Prepare Ligand for Docking
    Convert and prepare the ligand file in PDBQT format.

    Prepare Protein for Docking
    Prepare the protein structure for docking in PDBQT format.

    Run Docking
    Perform docking using AutoDock Vina and save the results.

    Extract Docking Pose
    Extract the best docking pose from the docking results.

    Convert to PDB Format
    Convert the docking pose to a PDB file for visualization.
