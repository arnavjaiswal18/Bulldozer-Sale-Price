import json
import sys

try:
    with open('Bulldozer.ipynb', 'r') as f:
        nb = json.load(f)
    
    print(f"Total cells: {len(nb['cells'])}")
    print(f"Notebook version: {nb['nbformat']}.{nb['nbformat_minor']}")
    
    # Check for problematic cells
    large_cells = []
    for i, cell in enumerate(nb['cells']):
        if 'outputs' in cell:
            output_count = len(cell['outputs'])
            if output_count > 0:
                total_output_size = sum(len(str(o)) for o in cell['outputs'])
                if total_output_size > 1000000:
                    large_cells.append((i, total_output_size))
                    print(f"Cell {i}: Has large output ({total_output_size} bytes)")
    
    if not large_cells:
        print("No cells with outputs larger than 1MB found")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
