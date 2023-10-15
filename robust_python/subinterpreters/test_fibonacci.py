# import datetime
import datetime
import extrainterpreters
import fibonacci

print(f'Subinterpreters setup started, time = {datetime.datetime.now()}')
interpreters = [
    extrainterpreters.Interpreter(target=fibonacci.fibonacci_with_time, kwargs={'n': 40}),
    extrainterpreters.Interpreter(target=fibonacci.fibonacci_with_time, kwargs={'n': 41})
]

for interpreter in interpreters:
    interpreter.start()

print(f'Subinterpreters run started, time = {datetime.datetime.now()}')
for interpreter in interpreters:
    interpreter.join()
    print(interpreter.result())
