from PyQt5.QtWidgets import QMessageBox


def get_info_box():
    """
    Get the message box for building the tree (everything ok)
    
    Returns
    -------
    message
        the message window that reports everything went well
    """
    message = QMessageBox()
    message.setIcon(QMessageBox.Information)
    message.setText("Tree built!")
    message.setWindowTitle("Created")
    return message


def get_error_box(e):
    """
    Get the error box for building the tree (something went wrong)
    
    Parameters
    ----------
    e : Exception
        the exception returned from the building process;
        something went wrong
    
    Returns
    -------
    error
        the error window that reports something went wrong
    """
    error = QMessageBox()
    error.setIcon(QMessageBox.Critical)
    error.setText("Something went wrong...")
    error.setInformativeText(str(e))
    error.setWindowTitle("Error")
    return error
