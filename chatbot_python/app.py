from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Predefined questions and responses
responses = {
    "what is a variable in python": "A variable in Python is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name.",
    "how do you create a function in python": "In Python, you can create a function using the 'def' keyword. Example:\n\ndef my_function():\n    print('Hello from my function!')",
    "what is a list in python": "A list in Python is a collection of items that are ordered and mutable. Example: my_list = [1, 2, 3, 4]",
    "how do you handle exceptions in python": "In Python, you handle exceptions using try-except blocks. Example:\n\ntry:\n    # code that might cause an exception\nexcept Exception as e:\n    print(f'An error occurred: {e}')",
    "what is a dictionary in python": "A dictionary in Python is an unordered collection of items. Each item is a key-value pair. Example: my_dict = {'name': 'John', 'age': 30}",
    "how do you create a class in python": "In Python, you can create a class using the 'class' keyword. Example:\n\nclass MyClass:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print(f'Hello, {self.name}!')",
    "what is a loop in python": "A loop in Python is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. The two main types of loops are 'for' loops and 'while' loops.",
    "how do you create a loop in python": "You can create a loop in Python using either 'for' or 'while'. Example of a 'for' loop:\n\nfor i in range(5):\n    print(i)\n\nExample of a 'while' loop:\n\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1",
    "what is a tuple in python": "A tuple in Python is an immutable, ordered collection of items. Example: my_tuple = (1, 2, 3)",
    "how do you write a comment in python": "In Python, you can write a comment by starting the line with a hash symbol (#). Example:\n\n# This is a comment",
    "what is a module in python": "A module in Python is a file containing Python code (functions, classes, variables) that can be included in other Python programs. You can import a module using the 'import' statement.",
    "how do you import a module in python": "You can import a module in Python using the 'import' keyword. Example:\n\nimport math\n\nprint(math.sqrt(16))",
    "what is a lambda function in python": "A lambda function in Python is a small anonymous function defined using the 'lambda' keyword. Example:\n\nsum = lambda x, y: x + y\nprint(sum(5, 10))",
    "how do you read a file in python": "You can read a file in Python using the 'open' function. Example:\n\nwith open('file.txt', 'r') as file:\n    content = file.read()\n    print(content)",
    "what is a set in python": "A set in Python is an unordered collection of unique items. Example: my_set = {1, 2, 3, 4}",
    "how do you create a set in python": "You can create a set in Python using curly braces or the 'set' function. Example:\n\nmy_set = {1, 2, 3}\n\nor\n\nmy_set = set([1, 2, 3])",
    "how do you handle multiple exceptions in python": "You can handle multiple exceptions in Python using a single try-except block by specifying multiple exceptions in a tuple. Example:\n\ntry:\n    # code that might cause multiple exceptions\nexcept (TypeError, ValueError) as e:\n    print(f'An error occurred: {e}')",
    "what is a list comprehension in python": "A list comprehension in Python is a concise way to create lists. Example:\n\nsquares = [x**2 for x in range(10)]",
    "how do you create a generator in python": "You can create a generator in Python using a function with 'yield' statements or using generator expressions. Example:\n\ndef my_generator():\n    yield 1\n    yield 2\n    yield 3\n\nor\n\nmy_gen = (x**2 for x in range(10))",
    "what is the difference between list and tuple in python": "The main difference between a list and a tuple in Python is that a list is mutable (can be changed) while a tuple is immutable (cannot be changed).",
    "how do you create a virtual environment in python": "You can create a virtual environment in Python using the 'venv' module. Example:\n\npython -m venv myenv\n\nTo activate it:\n\nOn Windows: myenv\\Scripts\\activate\nOn Unix or MacOS: source myenv/bin/activate",
    "what is pip in python": "pip is the package installer for Python. You can use pip to install packages from the Python Package Index (PyPI) and other indexes.",
    "how do you install a package in python using pip": "You can install a package in Python using pip by running the command:\n\npip install package_name",
    "how do you create a list in python": "You can create a list in Python using square brackets []. Example: my_list = [1, 2, 3, 4]",
    "how do you check the length of a list in python": "You can check the length of a list in Python using the 'len' function. Example:\n\nmy_list = [1, 2, 3, 4]\nprint(len(my_list))",
    "what is an if statement in python": "An 'if' statement in Python is used to test a condition. If the condition is true, the code block under the 'if' statement is executed. Example:\n\nif x > 0:\n    print('x is positive')",
    "how do you write an else statement in python": "An 'else' statement in Python is used to execute a block of code if the condition in the 'if' statement is false. Example:\n\nif x > 0:\n    print('x is positive')\nelse:\n    print('x is non-positive')",
    "how do you write an elif statement in python": "An 'elif' statement in Python allows you to check multiple conditions. Example:\n\nif x > 0:\n    print('x is positive')\nelif x == 0:\n    print('x is zero')\nelse:\n    print('x is negative')",
    "how do you concatenate strings in python": "You can concatenate strings in Python using the '+' operator. Example:\n\nstring1 = 'Hello'\nstring2 = 'World'\nresult = string1 + ' ' + string2\nprint(result)",
    "what is slicing in python": "Slicing in Python is a way to extract a subset of elements from sequences like lists, tuples, or strings. Example:\n\nmy_list = [1, 2, 3, 4, 5]\nsliced_list = my_list[1:4]",
    "how do you reverse a list in python": "You can reverse a list in Python using the 'reverse()' method or slicing. Example:\n\nmy_list = [1, 2, 3, 4]\nmy_list.reverse()\n\nor\n\nreversed_list = my_list[::-1]",
    "what is a decorator in python": "A decorator in Python is a function that takes another function and extends its behavior without explicitly modifying it. Example:\n\n@decorator_function\ndef my_function():\n    pass",
    "how do you create a decorator in python": "You can create a decorator in Python by defining a function that takes another function as an argument and returns a new function. Example:\n\ndef my_decorator(func):\n    def wrapper():\n        print('Something before the function')\n        func()\n        print('Something after the function')\n    return wrapper",
    "what is inheritance in python": "Inheritance in Python is a mechanism where a new class inherits attributes and methods from an existing class. Example:\n\nclass Parent:\n    def greet(self):\n        print('Hello from Parent')\n\nclass Child(Parent):\n    pass",
    "how do you use super() in python": "You use 'super()' in Python to call a method from the parent class. Example:\n\nclass Parent:\n    def __init__(self, name):\n        self.name = name\n\nclass Child(Parent):\n    def __init__(self, name, age):\n        super().__init__(name)\n        self.age = age",
    "what is a method in python": "A method in Python is a function that is defined inside a class and is associated with the objects of that class. Example:\n\nclass MyClass:\n    def my_method(self):\n        print('Hello')",
    "how do you write a docstring in python": "A docstring in Python is a string literal that appears as the first statement in a module, function, class, or method definition. Example:\n\ndef my_function():\n    '''This is a docstring.'''\n    pass",
    "how do you create a package in python": "You can create a package in Python by organizing modules into directories and adding an __init__.py file in each directory. Example:\n\nmy_package/\n    __init__.py\n    module1.py\n    module2.py",
    "how do you iterate over a dictionary in python": "You can iterate over a dictionary in Python using a for loop. Example:\n\nmy_dict = {'a': 1, 'b': 2}\nfor key, value in my_dict.items():\n    print(key, value)",
    "how do you merge two dictionaries in python": "You can merge two dictionaries in Python using the update() method or the ** unpacking operator. Example:\n\n# Using update()\ndict1.update(dict2)\n\n# Using ** unpacking\nmerged_dict = {**dict1, **dict2}",
    "what is recursion in python": "Recursion in Python is a process where a function calls itself as a subroutine. Example:\n\ndef factorial(n):\n    if n == 1:\n        return 1\n    else:\n        return n * factorial(n-1)",
    "how do you measure the execution time of code in python": "You can measure the execution time of code in Python using the time module. Example:\n\nimport time\nstart_time = time.time()\n# code to measure\ntime_taken = time.time() - start_time\nprint(f'Time taken: {time_taken} seconds')",
    "how do you use map() in python": "The map() function in Python applies a function to all items in an input list. Example:\n\ndef square(x):\n    return x**2\nnumbers = [1, 2, 3, 4]\nsquares = list(map(square, numbers))",
    "how do you use filter() in python": "The filter() function in Python filters items out of a list based on a function that returns a boolean value. Example:\n\ndef is_even(x):\n    return x % 2 == 0\nnumbers = [1, 2, 3, 4]\neven_numbers = list(filter(is_even, numbers))",
    "what is a comprehension in python": "A comprehension in Python is a concise way to create lists, sets, or dictionaries. Example:\n\n# List comprehension\nsquares = [x**2 for x in range(10)]\n\n# Set comprehension\nunique_squares = {x**2 for x in range(10)}\n\n# Dictionary comprehension\nsquare_dict = {x: x**2 for x in range(10)}",
    "how do you create a dictionary comprehension in python": "You can create a dictionary comprehension in Python using the following syntax:\n\n{key: value for key, value in iterable}",
    "how do you convert a list to a set in python": "You can convert a list to a set in Python using the set() function. Example:\n\nmy_list = [1, 2, 2, 3]\nmy_set = set(my_list)",
    "how do you convert a string to an integer in python": "You can convert a string to an integer in Python using the int() function. Example:\n\nmy_string = '123'\nmy_int = int(my_string)",
    "how do you convert an integer to a string in python": "You can convert an integer to a string in Python using the str() function. Example:\n\nmy_int = 123\nmy_string = str(my_int)",
    "how do you remove duplicates from a list in python": "You can remove duplicates from a list in Python by converting the list to a set and then back to a list. Example:\n\nmy_list = [1, 2, 2, 3]\nunique_list = list(set(my_list))",
    "how do you check if a key exists in a dictionary in python": "You can check if a key exists in a dictionary in Python using the 'in' keyword. Example:\n\nmy_dict = {'a': 1, 'b': 2}\nif 'a' in my_dict:\n    print('Key exists')",
    "how do you delete a key from a dictionary in python": "You can delete a key from a dictionary in Python using the 'del' keyword. Example:\n\nmy_dict = {'a': 1, 'b': 2}\ndel my_dict['a']",
    "how do you handle command line arguments in python": "You can handle command line arguments in Python using the 'sys' module. Example:\n\nimport sys\nprint(sys.argv)",
    "what is the difference between a shallow copy and a deep copy in python": "A shallow copy in Python creates a new object, but inserts references into it to the objects found in the original. A deep copy creates a new object and recursively copies all objects found in the original.",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    question = request.json.get('question').lower()
    answer = responses.get(question, "Sorry, I don't have an answer for that question.")
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)
