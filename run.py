import sys
import os

# Ensure src is in path if needed, though local import should work
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui import main

if __name__ == "__main__":
    main()
