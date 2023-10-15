from pathlib import Path


def load_tables(path: Path):
    print(f'Loading tables from path = {path}')
    # import numpy #  TODO numpy is not importable from the newly created interpreter
    # from pdtable.io import read_csv
    # from pdtable import BlockType
    
    # block_iterator = read_csv(source=path)
    # return [
    #     table for block_type, table in block_iterator
    #     if block_type == BlockType.TABLE
    # ]
