# AirBnB_clone

 ![AirBnB project](illustrations/hbnb.png)

<h1 align="center">HBnB</h1>

<h3 align="center">AN AirBnB clone</h3>


 The goal of the Air_BnB clone project is to deploy on a server a simple copy
 of the [AirBnB website](https://alx-intranet.hbtn.io/rltoken/m8g02HcD2ovrl_K-zulYBw).
 By the end of this project timeline, the complete web application will be composed of:
- A command interpreter to manipulate data without a visual interface, like a Shell
- A website (front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data=objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them, i.e., CRUD)

## Final product

 ![AirBnB clone homepage](illustrations/homepage.png)

## The console

 This is the first step towards building a full web application: the AirBnB clone.

 ![Application design](illustrations/application_design.png)

## Tasks :page_with_curl:

- A parent class (`BaseModel`) will be put in place to take care of the initialization, serialization and deserialization of future instances.
- Creation of a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Creation of all classes used by AirBnB (`User`, `State`, `City`, `Place`...) that inherit from the `BaseModel`.
- Creation of the first abstracted storage engine of the project: File storage.
- Creation of all unittests to validate all classes and storage engine.

### Aim of the console

 On the whole, the console has a single use function: a command line interface (CLI) from which one can create, modify and delete objects in the file storage.
 It will serve as a tool; a sandbox where one can play around with ideas, see what does and does not work in storage before building out the rest of the application.

 For the purpose of this project, we want to be able to manage objects in the following way:

1. Create a new object(ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc.
3. Do operations on objects (count, compute stats, etc.)
4. Update attributes of an object
5. Destroy an object

## Execution

 The shell works like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

 In non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
