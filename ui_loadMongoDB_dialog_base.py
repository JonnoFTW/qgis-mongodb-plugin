# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadMongoDB_dialog_base.ui'
#
# Created: Wed Jul 15 20:36:43 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loadMongoDBDialogBase(object):
    def setupUi(self, loadMongoDBDialogBase):
        loadMongoDBDialogBase.setObjectName(_fromUtf8("loadMongoDBDialogBase"))
        loadMongoDBDialogBase.resize(689, 489)
        self.tabWidget = QtGui.QTabWidget(loadMongoDBDialogBase)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 671, 471))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(20, 410, 511, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.Close_button = QtGui.QPushButton(self.tab)
        self.Close_button.setGeometry(QtCore.QRect(550, 410, 114, 32))
        self.Close_button.setObjectName(_fromUtf8("Close_button"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 611, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.dbName = QtGui.QComboBox(self.layoutWidget)
        self.dbName.setEditable(True)
        self.dbName.setObjectName(_fromUtf8("dbName"))
        self.gridLayout.addWidget(self.dbName, 1, 1, 1, 4)
        self.serverName = QtGui.QComboBox(self.layoutWidget)
        self.serverName.setEditable(True)
        self.serverName.setObjectName(_fromUtf8("serverName"))
        self.gridLayout.addWidget(self.serverName, 0, 1, 1, 4)
        self.geom_field = QtGui.QComboBox(self.layoutWidget)
        self.geom_field.setEditable(True)
        self.geom_field.setObjectName(_fromUtf8("geom_field"))
        self.gridLayout.addWidget(self.geom_field, 2, 1, 1, 4)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 180, 641, 221))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.createFile = QtGui.QPushButton(self.groupBox)
        self.createFile.setGeometry(QtCore.QRect(10, 20, 114, 32))
        self.createFile.setObjectName(_fromUtf8("createFile"))
        self.load_collection = QtGui.QPushButton(self.groupBox)
        self.load_collection.setGeometry(QtCore.QRect(120, 20, 114, 32))
        self.load_collection.setObjectName(_fromUtf8("load_collection"))
        self.listCol = QtGui.QTreeWidget(self.groupBox)
        self.listCol.setGeometry(QtCore.QRect(10, 50, 621, 161))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listCol.sizePolicy().hasHeightForWidth())
        self.listCol.setSizePolicy(sizePolicy)
        self.listCol.setObjectName(_fromUtf8("listCol"))
        self.listCol.headerItem().setText(1, _fromUtf8("Geometry"))
        self.listCol.header().setDefaultSectionSize(210)
        self.listCol.header().setMinimumSectionSize(200)
        self.listCol.header().setStretchLastSection(False)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(450, 20, 21, 20))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setCheckable(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.load_field = QtGui.QComboBox(self.groupBox)
        self.load_field.setGeometry(QtCore.QRect(480, 20, 151, 26))
        self.load_field.setEditable(False)
        self.load_field.setObjectName(_fromUtf8("load_field"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.view_all = QtGui.QListWidget(self.tab_2)
        self.view_all.setEnabled(False)
        self.view_all.setGeometry(QtCore.QRect(10, 10, 221, 371))
        self.view_all.setObjectName(_fromUtf8("view_all"))
        self.distinct_button = QtGui.QPushButton(self.tab_2)
        self.distinct_button.setEnabled(False)
        self.distinct_button.setGeometry(QtCore.QRect(120, 380, 111, 41))
        self.distinct_button.setObjectName(_fromUtf8("distinct_button"))
        self.view_distinct = QtGui.QListWidget(self.tab_2)
        self.view_distinct.setEnabled(False)
        self.view_distinct.setGeometry(QtCore.QRect(240, 10, 171, 181))
        self.view_distinct.setObjectName(_fromUtf8("view_distinct"))
        self.set_button = QtGui.QPushButton(self.tab_2)
        self.set_button.setEnabled(False)
        self.set_button.setGeometry(QtCore.QRect(300, 190, 114, 41))
        self.set_button.setObjectName(_fromUtf8("set_button"))
        self.view_button = QtGui.QPushButton(self.tab_2)
        self.view_button.setEnabled(False)
        self.view_button.setGeometry(QtCore.QRect(10, 380, 111, 41))
        self.view_button.setObjectName(_fromUtf8("view_button"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label = QtGui.QLabel(loadMongoDBDialogBase)
        self.label.setGeometry(QtCore.QRect(560, 0, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(loadMongoDBDialogBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.Close_button, QtCore.SIGNAL(_fromUtf8("clicked()")), loadMongoDBDialogBase.close)
        QtCore.QMetaObject.connectSlotsByName(loadMongoDBDialogBase)
        loadMongoDBDialogBase.setTabOrder(self.serverName, self.dbName)
        loadMongoDBDialogBase.setTabOrder(self.dbName, self.geom_field)
        loadMongoDBDialogBase.setTabOrder(self.geom_field, self.createFile)
        loadMongoDBDialogBase.setTabOrder(self.createFile, self.load_collection)
        loadMongoDBDialogBase.setTabOrder(self.load_collection, self.listCol)
        loadMongoDBDialogBase.setTabOrder(self.listCol, self.Close_button)

    def retranslateUi(self, loadMongoDBDialogBase):
        loadMongoDBDialogBase.setWindowTitle(_translate("loadMongoDBDialogBase", "Load MongoDB Points", None))
        self.Close_button.setText(_translate("loadMongoDBDialogBase", "Close", None))
        self.label_3.setText(_translate("loadMongoDBDialogBase", "Database:", None))
        self.label_5.setText(_translate("loadMongoDBDialogBase", "Server:", None))
        self.label_6.setText(_translate("loadMongoDBDialogBase", "Geometry field:", None))
        self.createFile.setText(_translate("loadMongoDBDialogBase", "Connect", None))
        self.load_collection.setText(_translate("loadMongoDBDialogBase", "Load", None))
        self.listCol.headerItem().setText(0, _translate("loadMongoDBDialogBase", "Items", None))
        self.listCol.headerItem().setText(2, _translate("loadMongoDBDialogBase", "Count", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("loadMongoDBDialogBase", "Connection", None))
        self.distinct_button.setText(_translate("loadMongoDBDialogBase", "Distinct", None))
        self.set_button.setText(_translate("loadMongoDBDialogBase", "Set", None))
        self.view_button.setText(_translate("loadMongoDBDialogBase", "View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("loadMongoDBDialogBase", "Settings", None))
        self.label.setText(_translate("loadMongoDBDialogBase", "MongoDB Loader", None))

