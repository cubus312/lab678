import argparse
import json
import yaml
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Input file path")
parser.add_argument("output_file", help="Output file path")
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

input_extension = os.path.splitext(input_file)[1].lower()
output_extension = os.path.splitext(output_file)[1].lower()

if input_extension == ".json":
    with open(input_file, "r") as file:
        data = json.load(file)