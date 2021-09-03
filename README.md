# PythonProjectTreeBuilder

This desktop application helps to understand the structure of a Python project, producing a visual layer; 
this can be done building a tree of the project structure using the library Graphviz and representing it with a PDF file. 

As example, into the repository there is a fake Python project whom root folder name is "project_root_example"; let's suppose that this is a real Python project; the internal structure of the project is as follows (of course, the content of the files is empty!):

    project_root_example
    ├── src
    │   ├── __main__.py
    │   ├── launch.py
    │   ├── module1
    │   │   ├── file1.py
    │   │   ├── file2.py
    │   ├── module2
    │   │   ├── file3.py
    ├── src
    │   ├── test1.py
    │   ├── test2.py
    │   ├── test3.py
    ├── conf
    │   ├── file.json
    ├── README.md
    └── requirements.txt

The tool is able to build a tree structure as follows: 

![alt text](https://github.com/Erca94/PythonProjectTreeBuilder/blob/main/example_tree/structure.png)

Btw, the tool can be used for building the structure of any folder, not only Python projects!
However, it's been thought to build the structure of Python projects.
