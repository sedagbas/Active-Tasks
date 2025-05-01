import sys
import serial
import serial.tools.list_ports
import os
import threading
import subprocess
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton, QAction, QVBoxLayout, QHBoxLayout,
                            QLabel, QTextEdit)

class portsGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Serial Ports Application')
        self.setGeometry(300,300,1200,700)

        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&File')
        exit = QAction('Exit', self)
        fileMenu.addAction(exit)

        portsMenu = menubar.addMenu('&Ports')

        #self.ports = serial.tools.list_ports.comports()
        self.ports = ["COM3", "COM4", "COM5"]
        self.statusBar().showMessage(f"Number of Available Port(s): {len(self.ports)}")

        layout_textEdit = QHBoxLayout()

        widget = QWidget(self)
        widget.setLayout(layout_textEdit)
        self.setCentralWidget(widget)

        for port in self.ports:
            port = QAction(f"{port}", self, checkable=True)
            port.setChecked(True)
            portsMenu.addAction(port)
            
            port_layout = QVBoxLayout()

            label = QLabel(f"Port: {port}", self)
            port_layout.addWidget(label)
            
            text_edit = QTextEdit(self)
            port_layout.addWidget(text_edit)

            layout_textEdit.addLayout(port_layout)

            if port.isChecked():
                thread = threading.Thread(target=self.read_from_port, args=(port, ))



def read_from_port(self, port, text_edit):
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = portsGUI()
    window.show()
    sys.exit(app.exec_())
