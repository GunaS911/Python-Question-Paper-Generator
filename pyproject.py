import sqlite3
import random

noq = int(input("Enter the number of questions you want in your question paper: "))
DB_NAME = "python_mcq_100.db"
questions = [
    ("Which keyword is used to define a function in Python?",
     "func", "def", "function", "define", "b"),

    ("Which data type is immutable in Python?",
     "list", "set", "dictionary", "tuple", "d"),

    ("What is the output of: print(type([])) ?",
     "<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>", "a"),

    ("Which operator is used for exponentiation in Python?",
     "^", "**", "pow", "exp", "b"),

    ("How do you start a single-line comment in Python?",
     "/*", "//", "#", "<!--", "c"),

    ("What is the correct file extension for Python files?",
     ".py", ".python", ".pt", ".p", "a"),

    ("Which built-in function returns the length of an object?",
     "size()", "count()", "len()", "length()", "c"),

    ("Which method adds an element to the end of a list?",
     "add()", "append()", "insert()", "extend()", "b"),

    ("How do you create a dictionary in Python?",
     "{}", "[]", "()","<>", "a"),

    ("Which keyword is used for exception handling?",
     "try", "catch", "handle", "exceptonly", "a"),

    ("Which statement is used to stop a loop?",
     "break", "stop", "exit", "end", "a"),

    ("What is the result of 3 // 2 in Python?",
     "1.5", "1", "2", "Error", "b"),

    ("Which collection type stores unique, unordered items?",
     "list", "tuple", "set", "dict", "c"),

    ("Which keyword is used to create a class?",
     "class", "struct", "object", "type", "a"),

    ("How to create an empty set?",
     "set()", "{}", "[]", "()", "a"),

    ("Which function converts a string to an integer?",
     "int()", "str()", "float()", "to_int()", "a"),

    ("Which of these is a mutable type?",
     "int", "str", "list", "tuple", "c"),

    ("What will '5' + 3 produce?",
     "8", "58", "TypeError", "'53'", "c"),

    ("Which keyword is used to create an anonymous function?",
     "lambda", "anon", "def", "func", "a"),

    ("Which method removes and returns the last item from list?",
     "pop()", "remove()", "del()", "discard()", "a"),

    ("Which operator checks for identity (same object)?",
     "==", "!=", "is", "in", "c"),

    ("How do you open a file for writing (overwrite) in Python?",
     "open('file','r')", "open('file','w')", "open('file','a')", "open('file','x')", "b"),

    ("Which module is used for regular expressions?",
     "re", "regex", "pyregex", "regexp", "a"),

    ("What is a correct way to create a list comprehension?",
     "[x for x in range(5)]", "(x for x in range(5))", "{x for x in range(5)}", "list(x for x in range(5))", "a"),

    ("Which statement is used to handle multiple exceptions?",
     "except Exception1, Exception2:", "except (Exception1, Exception2):", "except Exception1 | Exception2:", "except Exception1 and Exception2:", "b"),

    ("What does PEP stand for?",
     "Python Enhancement Proposal", "Python Enforced Policy", "Programming Enhancement Proposal", "Python Example Proposal", "a"),

    ("Which built-in can iterate over two lists in parallel?",
     "map()", "filter()", "zip()", "enumerate()", "c"),

    ("What does the 'self' keyword represent inside a class?",
     "A global variable", "Instance of the class", "Class method", "A decorator", "b"),

    ("Which method returns a view object of dict's keys?",
     "items()", "keys()", "get()", "values()", "b"),

    ("Which keyword makes a function generator?",
     "yield", "return", "generate", "async", "a"),

    ("What will len('hello') return?",
     "4", "5", "6", "Error", "b"),

    ("Which built-in sorts a list in place?",
     "sorted()", "sort()", "order()", "arrange()", "b"),

    ("Which of these raises when accessing missing dict key?",
     "KeyError", "IndexError", "ValueError", "TypeError", "a"),

    ("How do you create a virtual environment using venv module?",
     "python -m venv env", "python venv create env", "virtualenv env", "venv create env", "a"),

    ("Which import style imports all names into current namespace?",
     "import module", "from module import name", "from module import *", "import *", "c"),

    ("Which of these is NOT a valid variable name?",
     "var_1", "1_var", "_var", "var1", "b"),

    ("Which is the correct way to check if x in list L?",
     "if x in L:", "if x contained L:", "if L has x:", "if x within L:", "a"),

    ("What is the output of bool('') ?",
     "True", "False", "None", "Error", "b"),

    ("Which function returns the maximum of arguments?",
     "max()", "biggest()", "highest()", "top()", "a"),

    ("Which built-in creates an immutable sequence?",
     "list()", "dict()", "tuple()", "set()", "c"),

    ("Which of the following statements is true about Python integers?",
     "Fixed 32-bit", "Unlimited precision", "Fixed 64-bit", "Depends on platform", "b"),

    ("Which method adds elements from an iterable to a set?",
     "add()", "append()", "update()", "extend()", "c"),

    ("What is the output of list(range(0)) ?",
     "[]", "[0]", "None", "Error", "a"),

    ("Which statement is used to define an asynchronous function?",
     "async def", "await def", "def async", "async function", "a"),

    ("Which library is used for HTTP requests commonly?",
     "urllib", "requests", "httpclient", "httplib2", "b"),

    ("Which keyword is used to import a module under a different name?",
     "import ... as ...", "alias", "importas", "as", "a"),

    ("How do you check the type of a variable x?",
     "type(x)", "typeof x", "checktype(x)", "gettype(x)", "a"),

    ("Which function is used to convert a list into a tuple?",
     "tuple()", "list()", "set()", "convert()", "a"),

    ("Which statement is used to continue to the next iteration?",
     "pass", "continue", "break", "next", "b"),

    ("Which method returns substring count in a string?",
     "count()", "find()", "index()", "substr()", "a"),

    ("What is the output of: bool(0) ?",
     "True", "False", "0", "None", "b"),

    ("Which built-in returns an iterator of pairs (index, value)?",
     "zip()", "enumerate()", "pair()", "index()", "b"),

    ("Which of these is used for byte sequences?",
     "str", "bytes", "int", "float", "b"),

    ("Which operator is used to concatenate strings?",
     "+", "&", "concat()", "*", "a"),

    ("Which function is used to get help/documentation for objects?",
     "help()", "doc()", "info()", "describe()", "a"),

    ("Which typing indicates a function returns nothing?",
     "-> None", "-> void", "-> empty", "-> null", "a"),

    ("Which of the following is used to check if an object is iterable?",
     "hasattr(obj, '__iter__')", "callable(obj)", "isinstance(obj, Iterable)", "obj.iterable", "a"),

    ("Which of the following creates a shallow copy of a list?",
     "list.copy()", "copy.deepcopy()", "list[:]", "Both a and c", "d"),

    ("What does the 'with' statement ensure when working with files?",
     "Faster IO", "Automatic resource cleanup", "Concurrent access", "File encryption", "b"),

    ("Which method converts all characters in string to lowercase?",
     "lower()", "casefold()", "downcase()", "tolower()", "a"),

    ("Which of these statements will raise an IndentationError?",
     "def f():\nprint('hi')", "def f():\n\tprint('hi')", "def f():\n    print('hi')", "def f():\n  print('hi')", "a"),

    ("Which collection preserves insertion order as of Python 3.7?",
     "set", "dict", "list", "tuple", "b"),

    ("Which module would you use for JSON parsing?",
     "xml", "yaml", "json", "pickle", "c"),

    ("Which of these can be used to create partial function application?",
     "functools.partial", "itertools.partial", "functools.reduce", "operator.partial", "a"),

    ("Which built-in raises StopIteration when exhausted?",
     "list", "generator", "dict", "set", "b"),

    ("Which keyword do you use to pause coroutine until awaitable completes?",
     "await", "yield", "pause", "wait", "a"),

    ("What is the output of: 3 == 3.0 ?",
     "False", "True", "TypeError", "Depends", "b"),

    ("Which operator tests membership in a sequence?",
     "in", "has", "contains", "member", "a"),

    ("Which of these is used to create a class method?",
     "@staticmethod", "@classmethod", "def classmethod()", "@bindmethod", "b"),

    ("Which function maps a function across iterable and returns iterator in Py3?",
     "map()", "imap()", "map_it()", "apply()", "a"),

    ("Which of these will check equality of lists by value?",
     "is", "==", "equals()", "cmp()", "b"),

    ("Which module helps with working with dates?",
     "calendar", "datetime", "timeit", "os", "b"),

    ("Which is correct way to clone a list L?",
     "L2 = L", "L2 = list(L)", "L2 = L.copy()", "Both b and c", "d"),

    ("Which statement is used to import only specific names from a module?",
     "import module", "from module import name", "import module.name", "include module.name", "b"),

    ("Which function will convert an iterable to a list?",
     "list()", "iter()", "tuple()", "collect()", "a"),

    ("Which of the following is true about Python memory management?",
     "Manual malloc/free required", "Garbage collected", "No memory management", "Only stack allocated", "b"),

    ("Which of these will create a bytes object from a string s?",
     "bytes(s)", "s.encode()", "bytearray(s)", "Both a and b", "d"),

    ("Which of these is used to run unit tests in standard library?",
     "pytest", "unittest", "nose", "tox", "b"),

    ("Which function formats strings using placeholders?",
     "format()", "printf()", "sprintf()", "place()", "a"),

    ("Which of the following statements creates a set with one element 1?",
     "{1}", "set([1])", "set(1)", "Both a and b", "d"),

    ("Which expression will create a dictionary comprehension?",
     "{k:v for k,v in pairs}", "[k:v for k,v in pairs]", "(k:v for k,v in pairs)", "dictcomp(k:v)", "a"),

    ("What does the __init__ method do in a class?",
     "Deletes object", "Initializes object", "Represents class as string", "Compares two objects", "b"),

    ("Which of the following is a correct generator expression?",
     "(x*x for x in range(5))", "[x*x for x in range(5)]", "{x*x for x in range(5)}", "x*x for x in range(5)", "a"),

    ("Which built-in can be used to create an iterator from a function?",
     "iter()", "callable()", "next()", "generator()", "a"),

    ("Which of these effectively makes a shallow copy of a dict?",
     "dict.copy()", "{**d}", "d.copy()", "Both a and b", "d"),

    ("Which operator can be overridden by __add__?",
     "+", "-", "*", "/", "a"),

    ("Which method is used to join a list of strings with a separator?",
     "concat()", "join()", "sep()", "merge()", "b"),

    ("Which module provides high-level file operations (shutil)?",
     "os", "sys", "shutil", "file", "c"),

    ("What does '__name__ == \"__main__\"' check for?",
     "If module is imported", "If script is run directly", "If function exists", "If class defined", "b"),

    ("Which of these types supports slicing?",
     "int", "list", "float", "bool", "b"),

    ("Which function will return ASCII code of a character?",
     "ord()", "chr()", "ascii()", "code()", "a"),

    ("Which built-in will convert ASCII code to character?",
     "ord()", "chr()", "char()", "tochar()", "b"),

    ("Which of the following is NOT a valid JSON type?",
     "number", "boolean", "set", "string", "c"),

    ("Which of the following is used to create context managers?",
     "__enter__ and __exit__", "__start__ and __end__", "__open__ and __close__", "__init__ and __del__", "a"),

    ("Which of these will raise ValueError when converting 'abc' to int?",
     "int('abc')", "float('abc')", "str('abc')", "bool('abc')", "a"),

    ("Which function is used to get the next item from an iterator?",
     "next()", "iterator()", "get()", "fetch()", "a"),

    ("Which package manager is used to install Python packages?",
     "apt", "yum", "pip", "npm", "c"),

    ("Which of these is used to create a bytes array that is mutable?",
     "bytes()", "bytearray()", "memoryview()", "array()", "b"),

    ("Which method checks if string starts with a prefix?",
     "startswith()", "startswithwith()", "starts()", "hasprefix()", "a"),

    ("Which of the following statements creates a new list from an old list multiplying by 2 each element?",
     "[x*2 for x in L]", "map(lambda x: x*2, L)", "for x in L: x*2", "Both a and b", "d")
]

def create_and_populate(db_name=DB_NAME):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        A TEXT NOT NULL,
        B TEXT NOT NULL,
        C TEXT NOT NULL,
        D TEXT NOT NULL,
        correct_option CHAR(1) NOT NULL
    );
    """)

    cur.execute("DELETE FROM questions;")

    cur.executemany("""
    INSERT INTO questions (question, A, B, C, D, correct_option)
    VALUES (?, ?, ?, ?, ?, ?);
    """, questions)

    conn.commit()

    cur.execute("SELECT id, question, A, B, C, D, correct_option FROM questions ORDER BY RANDOM() LIMIT {} ;".format(noq))
    rows = cur.fetchall()
    for r in rows:
        for j in range (1,len(r)):
            print(r[j])

    conn.close()

if __name__ == "__main__":
    create_and_populate()


