# PythonProjectTreeBuilder

This desktop application helps to understand the structure of a Python project, producing a visual layer; 
this can be done building a tree of the project structure and representing it in a PDF file. 

As example, into the repository there is a fake python project whom root folder name is "project_root_example"; let's suppose that this is a real Python project; the internal structure of the project is as follows:

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

The tree structure build by the tool is the following: 
![alt text](https://github.com/Erca94/PythonProjectTreeBuilder/blob/main/example_tree/structure.png)
