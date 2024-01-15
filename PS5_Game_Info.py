# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

#++++++++++Modules++++++++++
from PyQt6 import QtCore, QtGui, QtWidgets
import json, os
from pathlib import Path
import webbrowser
#++++++++++GlobalVariables++++++++++
gPath=''
gVer=''
region=''
gname=''
sVer=''
Fcheck=''
Fsize=''
NO_SLCT="NO CONTENT SELECTED"
game_info_lbl="<html><head/><body><p align=\"center\">Game {Fcheck} ({region}) - {gVer} - RSSV: v{sVer} - {Fsize}</p></body></html>"
game_title_lbl="<html><head/><body><p align=\"center\">{gname}</p></body></html>"
basedir = os.path.dirname(__file__)
#++++++++++Defs++++++++++
def region_convertor(R):
        if R == "UP":
                return "US"
        elif R == "EP":
                return "EU"
        else:
                return R

def version_corrector(v):
        return v[:2]+"."+v[2:4]+"."+v[4:6]+"."+v[6:8]

def convert_bytes(size):
        for x in ['bytes','KB','MB','GB','TB']:
                if size < 1024.0:
                        return'%3.1f%s'%(size,x)
                size/=1024.0
        return size

def Param_Table_Inputer():
        global gVer,region,gname,sVer
        with open(gPath+"/sce_sys/param.json","r") as f:
                dict_param= json.load(f)
        #-------------------------------"titleName"
        if "localizedParameters" in dict_param.keys():
                title_name = dict_param["localizedParameters"]["en-US"]["titleName"].replace("â€“","-")
                gname=title_name
        #-------------------------------"contentVersion"
        if "contentVersion" in dict_param.keys():
                content_version = dict_param["contentVersion"]
                gVer = content_version
                dict_param.pop("contentVersion")
        #-------------------------------"titleId"
        if "titleId" in dict_param.keys():
                title_id=dict_param["titleId"]
                dict_param.pop("titleId")
        #-------------------------------"contentId"
        if "contentId" in dict_param.keys():
                content_id=dict_param["contentId"]
                region=region_convertor(content_id[:2])
                dict_param.pop("contentId")
        #-------------------------------"requiredSystemSoftwareVersion"
        if "requiredSystemSoftwareVersion" in dict_param.keys():
                sys_ver=version_corrector(dict_param["requiredSystemSoftwareVersion"][2:])
                sVer=sys_ver[:5]
                dict_param.pop("requiredSystemSoftwareVersion")
        #-------------------------------"sdkVersion"
        if "sdkVersion" in dict_param.keys():
                sdk_ver=version_corrector(dict_param["sdkVersion"][2:])
                dict_param.pop("sdkVersion")
        if Fcheck=='(<span style=\" color:#55aa00;\">Fake</span>)':
                Fake_Self="True"
        else:
                Fake_Self="False"
        #-------------------------------
        main_dict={
                "Title Name" : title_name,
                "Content Version" : content_version,
                "Title ID" : title_id,
                "Title Name" : title_name,
                "Content ID" : content_id,
                "Required System Software Version" : sys_ver,
                "SDK Version" : sdk_ver,
                "Fake Self":Fake_Self
        }
        #-------------------------------["addcont"]["serviceIdForSharing"]
        if "addcont" in dict_param.keys():
                txtaddcont=''
                for i in dict_param["addcont"]["serviceIdForSharing"]:
                        QtWidgets.QApplication.processEvents()
                        if " " not in i:
                                txtaddcont=txtaddcont+i+", "
                main_dict["(Add Cont)Service ID For Sharing"] = txtaddcont[:-2]
                dict_param.pop("addcont")
        #-------------------------------["savedata"]["titleIdForTransferringPs4"]
        if "savedata" in dict_param.keys():
                txtsavedata=''
                for i in dict_param["savedata"]["titleIdForTransferringPs4"]:
                        QtWidgets.QApplication.processEvents()
                        if " " not in i:
                                txtsavedata=txtsavedata+i+", "
                main_dict["(Save Data)Title ID For Transferring Ps4"] = txtsavedata[:-2]
                dict_param.pop("savedata")
        #-------------------------------["gameIntent"]["permittedIntents"]
        if "gameIntent" in dict_param.keys():
                txtintentType=''
                for i in dict_param["gameIntent"]["permittedIntents"]:
                        QtWidgets.QApplication.processEvents()
                        for y in i.values():
                                if "intentType" in i.keys():
                                        txtintentType=txtintentType+y+", "
                main_dict["Intent Type"] = txtintentType[:-2]
                dict_param.pop("gameIntent")
        #-------------------------------"ageLevel"
        if "ageLevel" in dict_param.keys():
                for x,y in dict_param["ageLevel"].items():
                        QtWidgets.QApplication.processEvents()
                        main_dict["Age Level_"+x] = str(y)
                dict_param.pop("ageLevel")
        #-------------------------------"localizedParameters"
        if "localizedParameters" in dict_param.keys():
                for x,y in dict_param["localizedParameters"].items():
                        QtWidgets.QApplication.processEvents()
                        if x == "defaultLanguage":
                                main_dict[x] = str(y)
                        else:
                                main_dict[x+":Title Name"] = y["titleName"].replace("â€“","-")
                dict_param.pop("localizedParameters")
        #-------------------------------"pubtools"
        if "pubtools" in dict_param.keys():
                for x,y in dict_param["pubtools"].items():
                        QtWidgets.QApplication.processEvents()
                        main_dict[x] = str(y)
                dict_param.pop("pubtools")
        #-------------------------------"All"
        link=dict_param["versionFileUri"].replace(" ","")
        dict_param.pop("versionFileUri")
        for x,y in dict_param.items():
                QtWidgets.QApplication.processEvents()
                main_dict[x] = str(y)
        main_dict["Version File URI"] = link
        #-------------------------------Printer
        c1=0
        ui.tw_param.setRowCount(len(main_dict))
        __sortingEnabled = ui.tw_param.isSortingEnabled()
        ui.tw_param.setSortingEnabled(False)
        for x,y in main_dict.items():
                QtWidgets.QApplication.processEvents()
                item = QtWidgets.QTableWidgetItem()
                ui.tw_param.setItem(c1, 0, item)
                item.setText(x)
                item = QtWidgets.QTableWidgetItem()
                ui.tw_param.setItem(c1, 1, item)
                item.setText(y)
                c1+=1
        ui.tw_param.setSortingEnabled(__sortingEnabled)
#++++++++++UI++++++++++
class Ui_PS5_Game_Info(object):
    def setupUi(self, PS5_Game_Info):
        PS5_Game_Info.setObjectName("PS5_Game_Info")
#============================================================================centralwidget
        PS5_Game_Info.resize(312, 673)
        PS5_Game_Info.setMinimumSize(QtCore.QSize(312, 693))
        PS5_Game_Info.setMaximumSize(QtCore.QSize(312, 693))
        PS5_Game_Info.setBaseSize(QtCore.QSize(312, 0))
        self.centralwidget = QtWidgets.QWidget(parent=PS5_Game_Info)
        self.centralwidget.setObjectName("centralwidget")
#============================================================================lbl_icon0
        self.lbl_icon0 = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_icon0.setGeometry(QtCore.QRect(28, 24, 256, 256))
        self.lbl_icon0.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lbl_icon0.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lbl_icon0.setPixmap(QtGui.QPixmap(os.path.join('images/Nothing.png')))
        self.lbl_icon0.setScaledContents(True)
        self.lbl_icon0.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon0.setObjectName("lbl_icon0")
#============================================================================le_game_path
        self.le_game_path = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.le_game_path.setGeometry(QtCore.QRect(10, 330, 268, 20))
        self.le_game_path.setObjectName("le_game_path")
        self.le_game_path.returnPressed.connect(self.le_path)
#============================================================================btn_game_path
        self.btn_game_path = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_game_path.setGeometry(QtCore.QRect(280, 330, 21, 21))
        self.btn_game_path.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Folder_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_game_path.setIcon(icon)
        self.btn_game_path.setObjectName("btn_game_path")
        self.btn_game_path.clicked.connect(self.Game_location)
#============================================================================lbl_game_info
        self.lbl_game_info = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_game_info.setGeometry(QtCore.QRect(0, 310, 311, 20))
        self.lbl_game_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_game_info.setObjectName("lbl_game_info")
#============================================================================lbl_game_title
        self.lbl_game_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_game_title.setGeometry(QtCore.QRect(10, 280, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.lbl_game_title.setFont(font)
        self.lbl_game_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lbl_game_title.setWordWrap(True)
        self.lbl_game_title.setObjectName("lbl_game_title")
#============================================================================tw_param
        self.tw_param = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tw_param.setGeometry(QtCore.QRect(10, 360, 301, 320))
        self.tw_param.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.tw_param.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tw_param.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tw_param.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tw_param.setTabKeyNavigation(True)
        self.tw_param.setDragEnabled(False)
        self.tw_param.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tw_param.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tw_param.setShowGrid(True)
        self.tw_param.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tw_param.setWordWrap(False)
        self.tw_param.setCornerButtonEnabled(True)
        self.tw_param.setColumnCount(2)
        self.tw_param.setObjectName("tw_param")
        item = QtWidgets.QTableWidgetItem()
        self.tw_param.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_param.setHorizontalHeaderItem(1, item)
        self.tw_param.horizontalHeader().setDefaultSectionSize(141)
        self.tw_param.horizontalHeader().setHighlightSections(True)
        self.tw_param.horizontalHeader().setMinimumSectionSize(42)
        self.tw_param.horizontalHeader().setSortIndicatorShown(False)
        self.tw_param.horizontalHeader().setStretchLastSection(True)
        self.tw_param.verticalHeader().setVisible(False)
        self.tw_param.verticalHeader().setDefaultSectionSize(20)
        self.tw_param.verticalHeader().setHighlightSections(False)
        self.tw_param.verticalHeader().setMinimumSectionSize(15)
#==================================================================lblSinajet
        self.lblSinajet = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(7)
        font.setItalic(True)
        self.lblSinajet.setFont(font)
        self.lblSinajet.setObjectName("lblSinajet")
#============================================================================menubar
        PS5_Game_Info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PS5_Game_Info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1323, 22))
        self.menubar.setObjectName("menubar")
#==========================================================================================mnus
        self.mnuFiles = QtWidgets.QMenu(self.menubar)
        self.mnuFiles.setObjectName("mnuFiles")
        self.mnuAbout = QtWidgets.QMenu(self.menubar)
        self.mnuAbout.setObjectName("mnuAbout")
#==========================================================================================statusbar
        PS5_Game_Info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PS5_Game_Info)
        self.statusbar.setObjectName("statusbar")
#==========================================================================================actGithub
        PS5_Game_Info.setStatusBar(self.statusbar)
        self.actGithub = QtGui.QAction(PS5_Game_Info)
        self.actGithub.setObjectName("actGithub")
        iconGithub=QtGui.QIcon()
        iconGithub.addPixmap(QtGui.QPixmap(os.path.join('images/GitHub_logo.png')),QtGui.QIcon().Mode.Normal)
        self.actGithub.setIcon(iconGithub)
#==========================================================================================actTelegram
        self.actTelegram = QtGui.QAction(PS5_Game_Info)
        self.actTelegram.setObjectName("actTelegram")
        iconTelegram=QtGui.QIcon()
        iconTelegram.addPixmap(QtGui.QPixmap(os.path.join('images/Telegram_logo.png')),QtGui.QIcon().Mode.Normal)
        self.actTelegram.setIcon(iconTelegram)
#==========================================================================================actYoutube
        self.actYoutube = QtGui.QAction(PS5_Game_Info)
        self.actYoutube.setObjectName("actYoutube")
        iconYoutube=QtGui.QIcon()
        iconYoutube.addPixmap(QtGui.QPixmap(os.path.join('images/YT_logo.png')),QtGui.QIcon().Mode.Normal)
        self.actYoutube.setIcon(iconYoutube)
#==========================================================================================acOpen
        self.acOpen = QtGui.QAction(PS5_Game_Info)
        self.acOpen.setCheckable(False)
        self.acOpen.setObjectName("acOpen")
        self.acOpen.setShortcut("Ctrl+F")
        iconOpen=QtGui.QIcon()
        iconOpen.addPixmap(QtGui.QPixmap(os.path.join('images/Folder_icon.png')),QtGui.QIcon().Mode.Normal)
        self.acOpen.setIcon(iconOpen)
#==========================================================================================acClear
        self.acClear = QtGui.QAction(PS5_Game_Info)
        self.acClear.setObjectName("acClear")
        self.acClear.setShortcut("Ctrl+D")
        acClear=QtGui.QIcon()
        acClear.addPixmap(QtGui.QPixmap(os.path.join('images/Clear_icon.png')),QtGui.QIcon().Mode.Normal)
        self.acClear.setIcon(acClear)
#============================================================================menubar
        PS5_Game_Info.setCentralWidget(self.centralwidget)
        self.mnuFiles.addAction(self.acOpen)
        self.mnuFiles.addAction(self.acClear)
        self.mnuAbout.addAction(self.actGithub)
        self.mnuAbout.addAction(self.actTelegram)
        self.mnuAbout.addAction(self.actYoutube)
        self.menubar = QtWidgets.QMenuBar(parent=PS5_Game_Info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 22))
        self.menubar.setObjectName("menubar")
        self.menubar.addAction(self.mnuFiles.menuAction())
        self.menubar.addAction(self.mnuAbout.menuAction())
        self.mnuFiles.triggered[QtGui.QAction].connect(self.dMnuFiles)
        self.mnuAbout.triggered[QtGui.QAction].connect(self.dMnuAbout)
#==================================================================statusbar
        self.statusbar = QtWidgets.QStatusBar(PS5_Game_Info)
        self.statusbar.showMessage("", 0) # حذف متن پیش‌فرض
        self.statusbar.addPermanentWidget(self.lblSinajet)
        self.statusbar.setObjectName("statusbar")
        PS5_Game_Info.setStatusBar(self.statusbar)

        self.retranslateUi(PS5_Game_Info)
        QtCore.QMetaObject.connectSlotsByName(PS5_Game_Info)

    def retranslateUi(self, PS5_Game_Info):
        _translate = QtCore.QCoreApplication.translate
        PS5_Game_Info.setWindowTitle(_translate("PS5_Game_Info", "PS5 Game Info - V0.90B"))
        self.lbl_game_info.setText(_translate("PS5_Game_Info",NO_SLCT))
        self.lbl_game_title.setText(_translate("PS5_Game_Info", "Select Game Folder First!"))
        self.lblSinajet.setText(_translate("Linksaz", "By Sinajet"))
        item = self.tw_param.horizontalHeaderItem(0)
        item.setText(_translate("PS5_Game_Info", "Param"))
        item = self.tw_param.horizontalHeaderItem(1)
        item.setText(_translate("PS5_Game_Info", "Value"))
        self.acOpen.setText(_translate("PS5_Game_Info", "Open Game Folder"))
        self.mnuFiles.setTitle(_translate("PS5_Game_Info", "File"))
        self.acClear.setText(_translate("PS5_Game_Info", "Clear"))
        self.mnuAbout.setTitle(_translate("PS5_Game_Info", "About"))
        self.actGithub.setText(_translate("PS5_Game_Info", "GitHub"))
        self.actTelegram.setText(_translate("PS5_Game_Info", "Telegram"))
        self.actYoutube.setText(_translate("PS5_Game_Info", "YouTube"))
#=======================================================================Game_location
    def Game_location(self):
        global gPath
        try:
                gPath = QtWidgets.QFileDialog.getExistingDirectory(None,'Select Game Folder',"")
                if gPath != "":
                        self.main_procress()
        except:
                pass
#=======================================================================Change_Icon0
    def Change_Icon0(self,p):
        path_icon=p+"/sce_sys/icon0.png"
        self.lbl_icon0.setPixmap(QtGui.QPixmap(path_icon))
#=======================================================================eboot_fake_checker
    def eboot_fake_checker(self):
        with open(gPath+"/eboot.bin","r",errors="ignore") as f:
                eboot_txt=f.read()
        if "ELF" in eboot_txt[:len("ELF")]:
                return '(<span style=\" color:#036494;\">official</span>)'
        else:
                return '(<span style=\" color:#55aa00;\">Fake</span>)'
#=======================================================================le_path
    def le_path(self):
        global gPath
        if self.le_game_path.text().replace('\\','/') != gPath and self.le_game_path.text().replace('\\','/') != "":
                gPath=self.le_game_path.text().replace("\\",'/')
                self.main_procress()
#=======================================================================main_procress
    def main_procress(self):
        global gPath,Fcheck
        self.le_game_path.setText(gPath.replace('/','\\'))
        self.Change_Icon0(gPath)
        if os.path.exists(gPath+"/eboot.bin"):
                Fcheck=self.eboot_fake_checker()
                if os.path.exists(gPath+"/sce_sys/param.json"):
                        Param_Table_Inputer()
                root_directory = Path(gPath)
                Fsize=convert_bytes(sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file()))
                self.lbl_game_info.setText(game_info_lbl.format(region=region,gVer=gVer,sVer=sVer,Fcheck=Fcheck,Fsize=Fsize))
                self.lbl_game_title.setText(game_title_lbl.format(gname=gname))
        else:
                self.lbl_game_info.setText(NO_SLCT)
                self.lbl_game_title.setText("Cant Find eboot File-Please Select Correct Path")
                self.tw_param.clearContents()
                self.lbl_icon0.setPixmap(QtGui.QPixmap(os.path.join('images/Nothing.png')))
#=======================================================================dMnuFiles
    def dMnuFiles(self,q):
        global gPath,gVer,region,gname,sVer,Fcheck,Fsize
        if q.objectName()=="acOpen":
                self.Game_location()
        elif q.objectName()=="acClear":
                self.tw_param.clearContents()
                self.lbl_game_info.setText(NO_SLCT)
                self.lbl_game_title.setText("Select Game Folder First!")
                self.lbl_icon0.setPixmap(QtGui.QPixmap(os.path.join('images/Nothing.png')))
                self.le_game_path.clear()
                gPath=''
                gVer=''
                region=''
                gname=''
                sVer=''
                Fcheck=''
                Fsize=''
#=======================================================================dMnuAbout
    def dMnuAbout(self,q):
        if q.objectName()=="actTelegram":
                webbrowser.open('https://t.me/sinajet')
        elif q.objectName()=="actYoutube":
                webbrowser.open('https://www.youtube.com/c/SinaJet')
        elif q.objectName()=="actGithub":
                webbrowser.open('https://github.com/sinajet')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PS5_Game_Info = QtWidgets.QMainWindow()
    app.setWindowIcon(QtGui.QIcon(os.path.join('Icon_ps5_info.ico')))
    ui = Ui_PS5_Game_Info()
    ui.setupUi(PS5_Game_Info)
    if len(sys.argv)>1:
            gPath=sys.argv[1].replace('\\'+os.path.basedir(sys.argv[1]),'').replace('\\','/')
            ui.main_procress()
    PS5_Game_Info.show()
    sys.exit(app.exec())
