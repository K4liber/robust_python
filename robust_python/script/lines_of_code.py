from collections import defaultdict
import os
import sys


def count_lines_of_code(file_path: str) -> int:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except (IOError, UnicodeDecodeError):
        return 0


def find_python_modules(
        directory,
        max_depth: int | None,
        prefix: str | None
    ) -> list[tuple[str, int]]:
    python_modules = defaultdict(int)
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and not file.startswith('test'):
                module_path = os.path.join(root, file)

                if prefix is not None:
                    if not module_path.startswith(prefix):
                        continue

                lines = count_lines_of_code(module_path)
                
                if lines > 0:
                    module_key = os.path.join(*module_path.split(os.sep)[:max_depth]) \
                        if max_depth else module_path
                    python_modules[module_key] += lines

    return [
        (k, v) for k, v in python_modules.items()
    ]


if __name__ == "__main__":
    directory = sys.argv[1]
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else None
    prefix = sys.argv[3] if len(sys.argv) > 3 else None
    python_modules = find_python_modules(
        directory=directory,
        max_depth=max_depth,
        prefix=prefix
    )
    python_modules.sort(key=lambda v: v[1], reverse=False)
    total_lines = 0
    total_modules = len(python_modules)

    if total_modules == 0:
        print(f'Nothing has been found')
        exit(0)

    for index, (module_path, lines) in enumerate(python_modules):
        total_lines += lines
        print(f"#{total_modules - index} {module_path}: {lines} lines")
    
    average = int(total_lines/total_modules)
    print(f"\nTotal entities: {total_modules}, total lines: {total_lines}, average: {average}")
