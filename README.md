## Snakemake Workflow

This project automates a protein-ligand docking pipeline using **Snakemake**. Below is a high-level overview of the rules in the workflow:

1. **Fetch PDB Structure**  
   Downloads the protein structure using the PDB code.

2. **Extract Protein Structure**  
   Extracts the protein-only portion of the PDB file.

3. **Compute Cavities**  
   Identifies cavities in the protein using the PDBe API.

4. **Generate Cavity Box**  
   Creates a docking box around the identified cavity.

5. **Download Ligand**  
   Downloads the ligand structure in SDF format using the ligand code.

6. **Prepare Ligand for Docking**  
   Converts and prepares the ligand file into PDBQT format.

7. **Prepare Protein for Docking**  
   Prepares the protein structure into PDBQT format.

8. **Run Docking**  
   Performs docking using AutoDock Vina.

9. **Extract Docking Pose**  
   Extracts the best docking pose from the results.

10. **Convert to PDB Format**  
    Converts the docking pose to a PDB file for visualization.
