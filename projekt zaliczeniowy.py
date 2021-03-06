import platform as pl
import sys
import os

numbers = [15972490, 80247910, 92031257, 75940266,
           97986012, 87599664, 75231321, 11138524,
           68870499, 11872796, 79132533, 40649382,
           63886074, 53146293, 36914087, 62770938]

author = 'Mateusz Basiak'
python_ve = pl.python_version()
python_interpreter = pl.python_implementation()
interpreter_version = sys.version
operation_system = pl.system()
os_release = pl.release()
cpu = pl.processor()
cpu_count = os.cpu_count()


# print(f"Python version: {python_ve}")
# print(f"Interpreter: {python_interpreter}")
# print(f"Interpreter version: {interpreter_version}")
# print(f"Operating system: {operation_system}")
# print(f"Operating system version: {os_release}")
# print(f"Processor: {cpu}")
# print(f"CPUs: {cpu_count}")
# print(f"App author{author}")

def fn_sum(n):
    result = 0
    for i in range(1, n):
        result += (n - i) * i
    return result


def write_to_file():
    with open("report.html", 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
    <html>
    <head>
    <style>
        body {background-color :lightblue;}
        p{font-size:12px;
        font-weight: bold;}
    </style>
    <head>
    <body>'''
                )
        f.write(f'<p>Python version: {python_ve}</p> \n')
        f.write(f'<p>Interpreter: {python_interpreter}</p>\n')
        f.write(f'<p>Interpreter version: {interpreter_version}</p>\n')
        f.write(f'<p>Operating system: {operation_system}</p>\n')
        f.write(f'<p>Operating system version: {os_release}</p>\n')
        f.write(f'<p>Processor: {cpu}</p>\n')
        f.write(f'<p>CPUs: {cpu_count}</p>\n')
        f.write(f'<p>App author: {author}</p>\n')
        f.write(f'</body>\n</html>')


def main():
    pass


if __name__ == '__main__':
    main()
