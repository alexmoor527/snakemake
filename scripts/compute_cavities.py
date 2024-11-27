from biobb_io.api.api_binding_site import api_binding_site

api_binding_site(
    output_json_path=snakemake.output[0],
    properties={"pdb_code": snakemake.config["pdb_code"]}
)

