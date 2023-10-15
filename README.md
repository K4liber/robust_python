# robust_python
Python best practices with examples.

1. Parametrized `pytest` fixtures ([link](robust_python/test/test_parametrized_fixture.py))

2. Counting lines of code per package ([link](robust_python/script/lines_of_code.py))

3. Protobuf typing with Python Interface file `*.pyi` ([link](robust_python/functionality/protobuf))

- `protoc -I=. --python_out=. --pyi_out=. person.proto`

4. Subinterpreters (python 3.12 required) ([link](robust_python/subinterpreters)) 
- `python -m pip install extrainterpreters`  
- `python robust_python/subinterpreters/test_fibonacci.py`

5. [TODO] `pre-commit` setup for static analysis
6. [TODO] VSCode example setup
7. [TODO] decorate all public methods
