from biobb_io.api.ideal_sdf import ideal_sdf

ideal_sdf(
    output_sdf_path=snakemake.output[0],
    properties={"ligand_code": snakemake.config["ligand_code"]}
)

