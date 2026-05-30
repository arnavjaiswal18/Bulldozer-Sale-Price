import json

# Read notebook
with open('Bulldozer.ipynb', 'r') as f:
    nb = json.load(f)

# Remove Google Colab cell and clear outputs
cells_to_keep = []
for i, cell in enumerate(nb['cells']):
    source = ''.join(cell.get('source', []))
    
    # Skip the Google Colab cell entirely
    if 'google.colab' in source or 'drive.mount' in source:
        print(f"Removing Cell {i} (Google Colab code)")
        continue
    
    # Clear outputs from code cells to reduce file size and avoid rendering issues
    if cell['cell_type'] == 'code':
        cell['outputs'] = []
        cell['execution_count'] = None
    
    cells_to_keep.append(cell)

nb['cells'] = cells_to_keep

# Write back
with open('Bulldozer.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)

print(f"Cleaned notebook: {len(cells_to_keep)} cells remaining")
print("- Removed Google Colab code")
print("- Cleared all cell outputs")
