import argparse
import json
import sys

# Parse CLI flags
parser = argparse.ArgumentParser(description="Spoof file signatures")
parser.add_argument("inputFile", help="Input file")
parser.add_argument("outputFile", help="Output file")
parser.add_argument("fileType", help="Signature to spoof")
args = parser.parse_args()

inPath = args.inputFile
outPath = args.outputFile

# Create file handlers
inFile = open(inPath, 'rb')
if outPath == "-":
    outFile = sys.stdout
else:
    outFile = open(outPath, 'wb')

# Parse sigs.json
sigs = {}
with open("sigs.json", "r") as sigFile:
    sigs = json.loads(sigFile.read())

# Generate new file with additional signature
magicSig = sigs[args.fileType].replace(' ', '').decode("hex")
outFile.write(magicSig)
outFile.write(inFile.read())

# Close file handlers
inFile.close()
outFile.close()