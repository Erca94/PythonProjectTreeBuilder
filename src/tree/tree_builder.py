import os
import graphviz


class TreeBuilder():
    """
    This class is used for handling the tree builder. 
    
    Attributes
    ----------
    tree: graphviz.Digraph
        the tree object
    structure_files: list
        the list of files that have a particular meaning in python
    structure_dirs: list
        the list of directories that have a particular meaning in python
    
    Methods
    -------
    _get_color(name, tp, level)
        Get the color for the element in the python project. 
        
    _get_elements(directory)
        Given a directory, get the list of files, the list of directories and the path.
        
    build(directory, level, parent)
        Recursive function for building the python project tree.
    
    save(fn)
        Save the tree object as a pdf file.
    """
    
    def __init__(self):
        self.tree = graphviz.Digraph()
        self.structure_files =  [
            'README.rst', 'README.md', 'LICENSE', 'pyproject.toml', 
            'setup.py', 'setup.cfg', 'requirements.txt', '__init__.py', '__main__.py'
        ]
        self.structure_dirs = ['tests', 'src', 'docs']
        
        
    def _get_color(self, name, tp, level):
        """
        Get the color to be used in the tree for a particular object.
        
        Parameters
        ----------
        name: str
            name the of element for which get the color
        tp: str
            type of the element, either file or directory 
        level: int
            depth level
        
        Returns
        -------
        fc
            the color
        """
        if tp == 'dir':
            if level == 1 and name in self.structure_dirs:
                fc = 'green3'
            else:
                fc = 'white'
        else: 
            if name in self.structure_files:
                fc = 'cornflowerblue'                
            elif name.endswith('.py'):
                fc = 'gold1'
            else:
                fc = 'grey79'
        return fc
    
    
    def _get_elements(self, directory):
        """
        Get the list of files and directories inside a directory and the absolute path to it.
        
        Parameters
        ----------
        directory: str
            path to the directory
        
        Returns
        -------
        (dirs, files, dir_path)
            (list of subdirectories, list of files, absolute path to the current directory)
        """
        dirs = []
        files = []
        for (dirpath, dirnames, filenames) in os.walk(directory):        
            dir_path = dirpath
            dirs.extend(dirnames)
            files.extend(filenames)
            break
        return (dirs, files, dir_path)
    
    
    def build(self, directory, level, parent):
        """
        Build the tree of a python project.
        
        Parameters
        ----------
        directory: str
            path to the directory
        level: int
            depth level
        parent: str
            name of the parent directory
        """
        dirs, files, dir_path = self._get_elements(directory)
        try:
            dir_name = os.path.basename(os.path.normpath(dir_path))
        except:
            dir_name = "/"
        fc = self._get_color(dir_name, 'dir', level)
        self.tree.node('{}-{}'.format(level,dir_name), dir_name, shape='folder', style='filled',fillcolor=fc)
        if parent:
            self.tree.edge('{}-{}'.format(level-1,parent), '{}-{}'.format(level,dir_name), constraint='true')
        for f in files:
            fc = self._get_color(f, 'file', None)
            self.tree.node('{}-{}'.format(level+1,f), f, style='filled',fillcolor=fc)
            self.tree.edge('{}-{}'.format(level,dir_name), '{}-{}'.format(level+1,f), constraint='true')
        for d in dirs:
            self.build(os.path.join(dir_path, d), level+1, dir_name)
            
            
    def save(self, fn):
        """
        Save the tree as a pdf.
        
        Parameters
        ----------
        fn: str
            destination directory and file
        """
        self.tree.render(filename=fn)
        