from biobb_structure_utils.utils.extract_molecule import extract_molecule

extract_molecule(
    input_structure_path=snakemake.input[0],
    output_molecule_path=snakemake.output[0],
    properties={"remove_water": True, "remove_heteroatoms": True}
)

