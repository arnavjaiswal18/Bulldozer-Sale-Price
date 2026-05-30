import json

with open('Bulldozer.ipynb', 'r') as f:
    nb = json.load(f)

# Check for problematic cells
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell.get('source', []))
        
        # Check for Google Colab references
        if 'google.colab' in source or 'drive.mount' in source:
            print(f"Cell {i}: Contains Google Colab code")
            print(f"  Source: {source[:100]}")
            
        # Check for problematic output types
        for output in cell.get('outputs', []):
            if output.get('output_type') in ['display_data', 'execute_result']:
                if 'data' in output:
                    data_types = list(output['data'].keys())
                    if any(dt in data_types for dt in ['image/png', 'image/jpeg', 'application/javascript']):
                        size = sum(len(str(v)) for v in output['data'].values())
                        print(f"Cell {i}: Contains {data_types} output ({size} bytes)")
