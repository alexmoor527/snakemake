from biobb_io.api.pdb import pdb

pdb_code = snakemake.config["pdb_code"]
pdb(output_pdb_path=snakemake.output[0], properties={"pdb_code": pdb_code})

