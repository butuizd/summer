import sys
from PyQt5.QtWidgets import QApplication
from AllWindows import login

if __name__=='__main__':
    app = QApplication(sys.argv)
    main=""
    Login = login()
    sys.exit(app.exec_())