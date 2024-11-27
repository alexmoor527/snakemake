from biobb_chemistry.babelm.babel_convert import babel_convert

babel_convert(
    input_path=snakemake.input[0],
    output_path=snakemake.output[0],
    properties={"input_format": "sdf", "output_format": "pdbqt", "binary_path": "obabel"}
)

