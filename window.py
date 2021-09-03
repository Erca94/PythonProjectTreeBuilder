import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGridLayout, QDialog,
                             QPushButton, QLabel,
                             QLineEdit, QDesktopWidget,
                             QFileDialog)
from tree_builder import TreeBuilder
from utils import get_info_box, get_error_box


class BuilderWindow(QDialog):
    """
    This class is used for handling the tree builder. 
    
    Attributes
    ----------
    tree_builder: TreeBuilder
        the class that builds the project tree
    layout: PyQt5.QtWidgets.QGridLayout
        the layout that contains all the widgets
    destination_label: PyQt5.QtWidgets.QLabel
        the label for the destination
    destination_box: PyQt5.QtWidgets.QLineEdit
        the text box for the destination folder, uneditable
    destination_button: PyQt5.QtWidgets.QPushButton
        the button for browsing the filesystem
    root_label: PyQt5.QtWidgets.QLabel
        the label for the root folder of the project
    root_box: PyQt5.QtWidgets.QLineEdit
        the text box for the root folder, uneditable
    root_button: PyQt5.QtWidgets.QPushButton
        the button for browsing the filesystem
    tree_button: PyQt5.QtWidgets.QPushButton
        the button for building the tree and saving it as a pdf
    
    Methods
    -------
    _center()
        Center the window in the screen.
        
    _init_ui()
        Initialize the window and set the layout and the widgets.
        
    _choose_destination()
        Action executed when the button for browsing the filesystem is clicked;
        it allows to browse the filesystem and choose the destination directory.
    
    _choose_root()
        Action executed when the button for browsing the filesystem is clicked;
        it allows to browse the filesystem and choose the project root directory.
    
    _create_tree()
        Action executed when the button for building the tree is clicked;
        it allows to start the create a tree and to save it as a pdf.        
    """
    
    def __init__(self):
        super().__init__()
        self._init_ui()
        
    
    def _center(self):
        """
        Center the window in the screen.
        """
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        #move the window in the center of the screen
        self.move(qt_rectangle.topLeft())
        
    
    def _init_ui(self):
        """
        Initialize the window and set the layout and the widgets.
        """
        title = 'Python Project Tree Builder'
        left = 10
        top = 10
        width = 700
        height = 80
        
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowCloseButtonHint, True)
        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.destination_label = QLabel("Destination:")
        self.layout.addWidget(self.destination_label, 0, 0)
        
        self.destination_box = QLineEdit(self)
        self.destination_box.setText(os.getcwd())
        self.destination_box.setReadOnly(True)
        self.layout.addWidget(self.destination_box, 0, 1)
        
        self.destination_button = QPushButton('Choose destination', self)
        self.layout.addWidget(self.destination_button, 0, 2)
        
        self.root_label = QLabel("Project root:")
        self.layout.addWidget(self.root_label, 1, 0)
        
        self.root_box = QLineEdit(self)
        self.root_box.setText(os.getcwd())
        self.root_box.setReadOnly(True)
        self.layout.addWidget(self.root_box, 1, 1)
        
        self.root_button = QPushButton('Select root', self)
        self.layout.addWidget(self.root_button, 1, 2)
            
        self.tree_button = QPushButton('Create tree', self)
        self.layout.addWidget(self.tree_button, 2, 0, 3, 3)
        
        self.destination_button.clicked.connect(self._choose_destination)
        self.root_button.clicked.connect(self._choose_root)
        self.tree_button.clicked.connect(self._create_tree)
        self._center()
        self.show()
        
    
    def _choose_destination(self):
        """
        Action executed when the button for browsing the filesystem is clicked;
        it allows to browse the filesystem and choose the destination directory.
        """
        path = QFileDialog.getExistingDirectory(self, 'Choose a destination')
        if path:
            self.destination_box.setText(path)
            
            
    def _choose_root(self):
        """
        Action executed when the button for browsing the filesystem is clicked;
        it allows to browse the filesystem and choose the project root directory.
        """
        path = QFileDialog.getExistingDirectory(self, 'Choose project root')
        if path:
            self.root_box.setText(path)
            
                
    def _create_tree(self):
        """
        Action executed when the button for building the tree is clicked;
        it allows to start the create a tree and to save it as a pdf.
        """
        destination = self.destination_box.text().strip()
        root = self.root_box.text().strip()
        try:
            self.tree_builder = TreeBuilder()
            self.tree_builder.build(root, 0, None)
            fn = os.path.basename(os.path.normpath(root))
            self.tree_builder.save(os.path.join(destination, fn))
            message = get_info_box()
            #show the message that everything went well
            message.exec_()
        except Exception as e:
            error = get_error_box(e)
            #show the message that an error occurred
            error.exec_()
