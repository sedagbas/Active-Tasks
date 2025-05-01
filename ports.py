import sys
import serial
import threading
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QAction, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit)
from PyQt5.QtCore import pyqtSignal, QObject

class PortsGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Serial Ports Application')
        self.setGeometry(300, 300, 1200, 700)
        self.statusBar().showMessage("Ready")

        # Menu setup
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        portsMenu = menubar.addMenu('&Ports')

        # Example ports list
        self.ports = ["COM3", "COM4", "COM5"]
        self.statusBar().showMessage(f"Number of Available Port(s): {len(self.ports)}")

        # Layout for text fields
        layout_textEdit = QHBoxLayout()

        # Create a QWidget to hold the layout
        widget = QWidget(self)
        widget.setLayout(layout_textEdit)
        self.setCentralWidget(widget)

        # Dictionary to hold the QTextEdit widgets for each port
        self.text_edit_dict = {}

        # Create a QTextEdit for each port and add them to the layout
        for port in self.ports:
            # Create an action for the port
            port_action = QAction(f"{port}", self, checkable=True)
            port_action.setChecked(True)  # Set the port as checked by default
            portsMenu.addAction(port_action)

            # Create a container layout for each port
            port_layout = QVBoxLayout()

            # Add port label
            label = QLabel(f"Port: {port}", self)
            port_layout.addWidget(label)

            # Add QTextEdit for the port
            text_edit = QTextEdit(self)
            text_edit.setPlainText(f"Details for {port}")
            port_layout.addWidget(text_edit)

            # Add the port's layout to the main layout
            layout_textEdit.addLayout(port_layout)

            # Store the QTextEdit widget in the dictionary for easy access later
            self.text_edit_dict[port] = text_edit

            # Start a thread to read data from this port
            if port_action.isChecked():
                thread = threading.Thread(target=self.read_from_port, args=(port, text_edit))
                thread.daemon = True
                thread.start()

        self.show()

    def read_from_port(self, port, text_edit):
        try:
            # Open the serial port
            ser = serial.Serial(port, 9600, timeout=1)
            while True:
                # Read data from the serial port
                data = ser.readline().decode('utf-8').strip()
                if data:
                    self.update_text_edit(text_edit, data)
        except serial.SerialException as e:
            print(f"Error reading from {port}: {e}")

    def update_text_edit(self, text_edit, data):
        # This method will safely update the QTextEdit from a worker thread
        # We need to use `QTextEdit.append()` to update the GUI from a different thread
        text_edit.append(data)

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PortsGUI()
    sys.exit(app.exec_())
