from pathlib import Path
import _xxsubinterpreters as interpreters

# TODO finish when numpy will be importable
bundle_file_path = Path(__file__).parent / 'bundle.csv'
interpreter_id = interpreters.create()
interpreters.run_string(interpreter_id, "import numpy")
