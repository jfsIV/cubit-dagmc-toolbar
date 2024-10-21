import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QApplication, QDockWidget

def get_qapp():
    return QApplication.instance()

# I'm not sure why findChild doesn't work
def find_claro():
    qApp = get_qapp()
    widgets = qApp.allWidgets()
    for w in widgets:
        if "Claro" in w.objectName() and type(w).__name__ == 'QMainWindow':
            return w
    return None

if __name__ == "__coreformcubit__":
    qApp = qApp = get_qapp()
    claro = find_claro()
    ccp = claro.findChild(QDockWidget, "CubitCommandPanel")
    ccl = claro.findChild(QDockWidget, "ClaroCommandWindow")
