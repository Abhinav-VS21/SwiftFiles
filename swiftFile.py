from PySide6.QtWidgets import QApplication , QMainWindow ,QWidget , QVBoxLayout , QSplitter , QTreeView , QMenuBar
from PySide6.QtCore import Qt
from fileTreeView import FileTreeViewWidget
from iconviewerWidget import IconViewer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Swift File")
        self.resize(823, 727)
        
        self.centralwidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        
        # using qsplitter 
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setOrientation(Qt.Horizontal)
        
        # adding the file tree view widget to the splitter
        self.fileTreeVew = FileTreeViewWidget()
        self.fileTreeVew.setObjectName(u"FiletreeView")
        self.fileTreeVew.fileTreeUI.fileTreeView.hideColumn(1)
        self.fileTreeVew.fileTreeUI.fileTreeView.hideColumn(2)
        self.fileTreeVew.fileTreeUI.fileTreeView.hideColumn(3)
        
        self.fileTreeVew.fileTreeUI.fileTreeView.header().setStretchLastSection(False)
        self.fileTreeVew.fileTreeUI.fileTreeView.setColumnWidth(0, self.fileTreeVew.width())
        
        
        # Set the maximum width of the fileTreeVew widget
        self.fileTreeVew.setMaximumWidth(300)  # Set the desired maximum width in pixels
        
        
        
        # creating 
        self.iconViewer = IconViewer(self.fileTreeVew.homeDirectory)
        self.iconViewer.setObjectName(u"iconViewer")
        
        
        self.splitter.addWidget(self.fileTreeVew)
        self.splitter.addWidget(self.iconViewer)



        self.verticalLayout.addWidget(self.splitter)

        self.setCentralWidget(self.centralwidget)

        # Create the QMenuBar
        self.menubar = QMenuBar(self)
        self.setMenuBar(self.menubar)

        # Add menus to the menubar
        self.fileMenu = self.menubar.addMenu("File")
        self.editMenu = self.menubar.addMenu("Edit")
        self.viewMenu = self.menubar.addMenu("View")
        self.helpMenu = self.menubar.addMenu("Help")
        
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()