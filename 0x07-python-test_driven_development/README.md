# Python
## 0x07-python-test_driven_development

### Author
- [Berhane Zerabruk Desta](https://github.com/berhanez)

## Tasks :page_with_curl:

* **0. Integers addition**
  * [0-add_integer.py](./0-add_integer.py): Python function that returns the integer addition
  of two numbers.
  * PROTOTYPE: ``` xx ```
  
* **1. Divide a matrix**
  * [2-matrix_divided.py](./2-matrix_divided.py): Python function that divides all
  elements of a matrix by a common divisor.
  * PROTOTYPE:

* **2. Say my name**
  * [3-say_my_name.py](./3-say_my_name.py): Python function that prints a name in
  the format `My name is <first_name> <last_name>`.
  * PROTOTYPE:
  
* **3. Print square**
  * [4-print_square.py](./4-print_square.py): Python function that prints a square using
  the `#` character.
  * PROTOTYPE:
  
* **4. Text indentation**
  * [5-text_indentation.py](./5-text_indentation.py): Python function that prints text with
  indentation.
  * PROTOTYPE:
  
* **5. Max integer - Unittest**
  * [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): Python class/script
  that runs unittests for the function `def max_integer(list=[]):`
  * PROTOTYPE:

* **6. Matrix multiplication**
  * [100-matrix_mul.py](./100-matrix_mul.py): Python function that multiplies two matrices.
  * PROTOTYPE:
* **7. Lazy matrix multiplication**
  * [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py): Python function that multiplies
  two matrices using the module `NumPy`.
  * Identical in function to [100-matrix_mul.py](./100-matrix_mul.py).
  * PROTOTYPE:
* **8. CPython #3: Python Strings**
  * [102-python.c](./102-python.c): C function that prints basic information about Python
  string objects.
  * PROTOTYPE: 
## Tests :check_mark:

* [tests](./tests): Folder of test files. Includes both Holberton-provided ones as well as the
following eight independently-developed:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |
| `102-python.c`           | `void print_python_string(PyObject *p);`     |
