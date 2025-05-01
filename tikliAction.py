from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Checkable Menu Example")
        
        # Menü çubuğu oluştur
        menu_bar = self.menuBar()
        
        # "Ayarlamalar" menüsü
        settings_menu = menu_bar.addMenu("Ayarlamalar")
        
        # "Ses aç/kapa" action'ı
        sound_action = QAction("Ses Aç/Kapa", self, checkable=True)
        sound_action.triggered.connect(self.toggle_sound)
        settings_menu.addAction(sound_action)
        
        # İçerik widget'ı
        self.label = QLabel("Ses durumu: Kapalı", self)
        self.setCentralWidget(self.label)

    def toggle_sound(self, checked):
        if checked:
            self.label.setText("Ses durumu: Açık")
        else:
            self.label.setText("Ses durumu: Kapalı")

# Uygulama başlatma
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
