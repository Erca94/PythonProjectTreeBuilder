import sys
from PyQt5.QtWidgets import QApplication
from ui.window import BuilderWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BuilderWindow()
    sys.exit(app.exec_())