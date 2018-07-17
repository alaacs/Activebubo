"""
/***************************************************************************
 ActiveBubo
                                 A QGIS plugin
 ActiveBubo is a python coding project developed as the final assignment for the Python in GIS course. The data provided for the project contained a large dataset of GPS tracks, surveilling the movement of more than 20 Eagle Owls over a time span of several years. Browsing through the available data, it was decided by the group to investigate and answer the following research questions: Which is the month and the season in which the owls are most/least active? Does the temporal scope of owl activity change for different regions? For different owl genders? Which owl is the most active?
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2018-07-10
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Univerity of Muenster
        email                : y_qama01@uni-muenster.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
#from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QFileDialog
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .Active_Bubo_dialog import ActiveBuboDialog
import os
from qgis.core import *
from qgis.gui import QgsMessageBar
import qgis.utils
import ogr
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QPushButton
from sys import path
path.append(os.path.dirname(__file__))
from core import *
from plot import *


fieldsName_list = []
fieldsType_list = []
picutresLisit = []
i = 0
class ActiveBubo:

    def __init__(self, iface):

        # Save reference to the QGIS interface
        self.iface = iface
        self.deleteChartImagesDirectory()
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ActiveBubo_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = ActiveBuboDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Active Bubo')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'ActiveBubo')
        self.toolbar.setObjectName(u'ActiveBubo')
        #/////////////////////////
        self.dlg.lineEdit.clear()
        self.dlg.lineEdit_2.clear()
        self.dlg.openShapefile_button.clicked.connect(self.open_shapefile)
        self.dlg.exportAsReport_button.clicked.connect(self.exportAsReport)
        self.dlg.process_button.clicked.connect(self.process)
        self.dlg.addExpression_button.clicked.connect(self.addExpression)
        self.dlg.previousPicture_button.clicked.connect(self.previousPicture)
        self.dlg.nextPicture_button.clicked.connect(self.nextPicture)
        self.dlg.btn_equals.clicked.connect(self.equalsButtonHandler)
        self.dlg.btn_lessThan.clicked.connect(self.lessThanButtonHandler)
        self.dlg.btn_greaterThan.clicked.connect(self.greaterThanButtonHandler)
        self.dlg.btn_in.clicked.connect(self.inButtonHandler)
        self.dlg.btn_like.clicked.connect(self.likeButtonHandler)
        self.dlg.btn_and.clicked.connect(self.andButtonHandler)
        self.dlg.btn_or.clicked.connect(self.orButtonHandler)
        self.dlg.btn_not.clicked.connect(self.notButtonHandler)
    #---------------------------
    def equalsButtonHandler(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() + " = ")
    def lessThanButtonHandler(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() + " < ")
    def greaterThanButtonHandler(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() + " > ")
    def inButtonHandler(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() + " IN( ) ")
    def likeButtonHandler(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() + " LIKE ")
    def andButtonHandler(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() + " AND ")
    def orButtonHandler(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() + " OR ")
    def notButtonHandler(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() + " NOT ")
    def open_shapefile(self):
        filename = QFileDialog.getOpenFileName(self.dlg, "Open shapefile ","", '*.shp')
        self.dlg.lineEdit.setText(str(filename[0]))
        in_path = (str(filename[0]).replace('/','\\\\'))
        # get the correct driver
        driver = ogr.GetDriverByName('ESRI Shapefile')
        # 0 means read-only. 1 means writeable.
        data_source = driver.Open(in_path, 0)
        # get the Layer class object
        layer = data_source.GetLayer(0)
        self.in_path = in_path
        global fieldsName_list
        global fieldsType_list
        attributes = layer.GetLayerDefn()
        for i in range(attributes.GetFieldCount()):
            fieldsName_list.append(attributes.GetFieldDefn(i).GetName())
            fieldsType_list.append(attributes.GetFieldDefn(i).GetTypeName())
        self.dlg.comboBox.addItems(fieldsName_list)
        #self.dlg.lineEdit.setText(testFun())

    def exportAsReport(self):
        return
        ###ADD content
        ######get pictures saves of plots and display first one

            #i = i+1




    def process(self):
        directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
        if not os.path.exists(directory):
            os.makedirs(directory)
        owlData = getOwlsAggregateData(self.in_path, "timestamp", "speed", "tag_ident","tag_ident in ('1750', '1751', '1753', '1754', '3899', '4045', '5158', '4846', '4848') AND speed > 1.5", group_by = "month" )
        #print(parseOwlDataToByMonth(owlData))
        print(owlData)

        boxplotDistanceData = parseOwlDataForBoxplots(owlData, "totalDistance")
        boxplotAvgSpeedData = parseOwlDataForBoxplots(owlData, "averageSpeed")
        #print(boxplotDistanceData)
        boxplot_distance(boxplotDistanceData)
        #print(boxplotAvgSpeedData)
        boxplot_speed(boxplotAvgSpeedData)
        averageDataPerMonth = parseOwlDataToAverageByMonth(owlData)
        #print(averageDataPerMonth)
        graph_speed_distance(averageDataPerMonth)

        graphDistancePerOwlData = parseOwlDataToAvgPerOwlPerMonth(owlData)
        print(graphDistancePerOwlData)
        graph_speed(graphDistancePerOwlData)
        graph_distance(graphDistancePerOwlData)

        global picutresLisit
        global i
        picutresLisit = os.listdir(directory)
        if (len(picutresLisit) >= 0 ):
            pixmap = QPixmap(os.path.join(directory, picutresLisit[i]))
            self.dlg.plotLabel.setPixmap(pixmap)


    def addExpression(self):
        self.dlg.lineEdit_2.setText(self.dlg.lineEdit_2.text() +" "+ self.dlg.comboBox.currentText())


    def previousPicture(self):
        directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
        global i
        if(i-1 < 0):
            i = len(picutresLisit)-1
        else: i = i-1
        pixmap = QPixmap(os.path.join(directory, picutresLisit[i]))
        self.dlg.plotLabel.setPixmap(pixmap)



    def nextPicture(self):
        directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
        global i
        if(i+1 > len(picutresLisit)-1):
            i = 0
        else: i = i+1
        pixmap = QPixmap(os.path.join(directory, picutresLisit[i]))
        self.dlg.plotLabel.setPixmap(pixmap)


    #####################----------------------####################
    # noinspection PyMethodMayBeStatic
    def tr(self, message):

        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ActiveBubo', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Active_Bubo/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Active Bubo'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Active Bubo'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def deleteChartImagesDirectory(self):
        directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
        if os.path.exists(directory):
            for file in os.listdir(directory):
                os.remove(os.path.join(directory, file))
        return True
    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            self.deleteChartImagesDirectory()
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
