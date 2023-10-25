import os 

cwd = os.getcwd()

print(f"CWD: {cwd}")

import sys

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("A virtual environment is activated.")
    print("Virtual environment path:", sys.prefix)
else:
    print("No virtual environment is activated.")
