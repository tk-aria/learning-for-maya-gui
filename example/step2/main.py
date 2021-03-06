# -*- coding: utf-8 -*-
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile

if __name__ == "__main__":
	app = QApplication.instance()

	file = QFile("D:\workspace\Qt\HelloPySide\ui\helloworld.ui")
	file.open(QFile.ReadOnly)

	loader = QUiLoader()
	window = loader.load(file)

	window.show()

	sys.exit(app.exec_())
