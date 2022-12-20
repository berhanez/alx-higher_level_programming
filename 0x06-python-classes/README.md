# :snake: *PYTHON
# 0x06. Python - Classes

### This directory contains files done as part of ALX-SE program, Sprint 2 - PYTHON


## Execution
All programs are executed using 
```
./x-main.py
```
where x is the task number.

## :wrench: TASKS
List of Tasks in this directory
```
0-square.py - my first square
```
* An empty class Square that defines a square.


```
1-square.py - Square with size
```
* A class Square that defines a square by: (based on 0-square.py).
* Private instance attribute: size
* Instantiation with size (no type/value verification)


```
2-square.py - Size validation
```
* A class Square that defines a square by: (based on 1-square.py).
* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
	- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
	- if size is less than 0, raise a ValueError exception with the message size must be >= 0


```
3-square.py - Area of a square
```
* A class Square that defines a square by: (based on 2-square.py).
* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
	- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
	- if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Public instance method: def area(self): that returns the current square area


```
4-square.py - Access and update private attribute
```
* A class Square that defines a square by: (based on 3-square.py).
* Private instance attribute: size:
	- property def size(self): to retrieve it
	- property setter def size(self, value): to set it:
		* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
		* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
	#### GETTER AND SETTER:
** Why a getter and setter? ** 
	> - Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.


```
5-square.py - printing a square
```
* A class Square that defines a square by: (based on 4-square.py).
* Private instance attribute: size:
	- property def size(self): to retrieve it
	- property setter def size(self, value): to set it:
		* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
		* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
	- if size is equal to 0, print an empty line


```
6-square.py - Coordinates of a square
```
* A class Square that defines a square by: (based on 5-square.py).
* Private instance attribute: size
	* property def size(self): to retrieve it
	* property setter def size(self, value): to set it 
* Private instance attribute: position:
	* property def position(self): to retrieve it
	* property setter def position(self, value): to set it
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:

## :100: *ADVANCED TASKS* :100:

The following is a list of advanced tasks done in this project:

```
100-singly_linked_list.py - Singly Linked List
```
* a class Node that defines a node of a singly linked list by:
	- Private instance attribute: data
	- Private instance attribute: next_node
	- Instantiation with data and next_node: def __init__(self, data, next_node=None):
* a class SinglyLinkedList that defines a singly linked list by:
	- Private instance attribute: head (no setter or getter)
	- Simple instantiation: def __init__(self):
		* print the entire list in stdout & one node number by line
	- Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)

```
101-square.py - Print Square Instance
```
* a class Square that defines a square by: (based on 6-square.py)


```
102-square.py - Compare two squares
```
*  a class Square that defines a square by: (based on 4-square.py)


```
103-magic_class.py - ByteCode -> Python #5
```
* the Python class MagicClass that does exactly the same as the Python bytecode given in the project page:
[Python Bytecode Tip/Resource](https://docs.python.org/3.4/library/dis.html)
	

## :blue_book: Author

* **Berhane Zerabruk Desta** - [@berhanez](https://github.com/berhanez)


## :mega: Acknowledgments
* ALX + Holberton School for giving us these challenges to grow and providing us with guidance in this program.
