from biobb_structure_utils.utils.str_check_add_hydrogens import str_check_add_hydrogens

str_check_add_hydrogens(
    input_structure_path=snakemake.input[0],
    output_structure_path=snakemake.output[0],
    properties={"charges": True}
)

