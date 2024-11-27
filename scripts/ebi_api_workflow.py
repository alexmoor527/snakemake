import sys
import json
from biobb_chemistry.chemistry.vs import LigandFiltering, LigandSimilarity, GetMolecule

if len(sys.argv) < 3:
    raise ValueError("Specify the step (filter, similarity, retrieve) and input/output files.")

step = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

if step == "filter":
    properties = {
        "num_molecules": 1  # Only filter one molecule for testing
    }
    LigandFiltering(input_file=input_file, output_file=output_file, properties=properties).launch()

elif step == "similarity":
    properties = {
        "max_similar_molecules": 5  # Retrieve 5 similar molecules
    }
    LigandSimilarity(input_file=input_file, output_file=output_file, properties=properties).launch()

elif step == "retrieve":
    properties = {
        "compound_format": "sdf"
    }
    GetMolecule(input_file=input_file, output_file=output_file, properties=properties).launch()

else:
    raise ValueError("Unknown step provided. Use 'filter', 'similarity', or 'retrieve'.")

