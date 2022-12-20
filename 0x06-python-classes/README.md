# :snake: PYTHON
# 0x05. Python - Exceptions

## This directory contains files done as part of ALX-SE program, Sprint 2 - PYTHON


## Execution
All programs are executed using 
```
./x-main.py
```
where x is the task number.

## :wrench: ERRORS and EXCEPTIONS
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
	## GETTER AND SETTER:
	* Why a getter and setter?
	- Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

```
5-square.py - printing a square
```
	* A class Square that defines a square by: (based on 4-square.py).
```
6-square.py - Coordinates of a square
```
	A class Square that defines a square by: (based on 5-square.py).	


## :blue_book: Author

* **Berhane Zerabruk Desta** - [@berhanez](https://github.com/berhanez)


## :mega: Acknowledgments
* ALX + Holberton School for giving us these challenges to grow and providing us with guidance in this program.
