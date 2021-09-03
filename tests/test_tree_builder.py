import sys
sys.path.append('..')
import unittest
from src.tree.tree_builder import TreeBuilder

class TestTreeBuilder(unittest.TestCase):

    def test_get_color_struct_directory(self):
        tree_builder = TreeBuilder()
        col = tree_builder._get_color('src', 'dir', 1)
        self.assertEqual(col, 'green3')
        
    def test_get_color_normal_directory(self):
        tree_builder = TreeBuilder()
        col = tree_builder._get_color('dunno', 'dir', 2)
        self.assertEqual(col, 'white')
        
    def test_get_color_struct_file(self):
        tree_builder = TreeBuilder()
        col = tree_builder._get_color('__init__.py', 'file', 2)
        self.assertEqual(col, 'cornflowerblue')
        
    def test_get_color_py_file(self):
        tree_builder = TreeBuilder()
        col = tree_builder._get_color('module.py', 'file', 2)
        self.assertEqual(col, 'gold1')
        
    def test_get_color_normal_file(self):
        tree_builder = TreeBuilder()
        col = tree_builder._get_color('normal_file.txt', 'file', 2)
        self.assertEqual(col, 'grey79')
        
    def test_get_elements_empty(self):
        tree_builder = TreeBuilder()
        dirs, files, dir_path = tree_builder._get_elements('./empty_folder/')
        self.assertEqual(dirs, [])
        self.assertEqual(files, [])
        
    def test_get_elements_filled(self):
        tree_builder = TreeBuilder()
        dirs, files, dir_path = tree_builder._get_elements('./filled_folder/')
        self.assertEqual(sorted(files), ['file1.txt', 'file2.txt', 'file3.txt'])
        self.assertEqual(sorted(dirs), ['subfolder1', 'subfolder2', 'subfolder3'])
        
        
if __name__ == '__main__':
    unittest.main()
