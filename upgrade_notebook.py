import json
import nbformat

# Read the notebook
with open('Bulldozer.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Write it back with the latest format
with open('Bulldozer.ipynb', 'w') as f:
    nbformat.write(nb, f)

print(f"Upgraded notebook to nbformat {nb.nbformat}.{nb.nbformat_minor}")
