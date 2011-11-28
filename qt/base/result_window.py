# Created By: Virgil Dupras
# Created On: 2009-04-25
# Copyright 2011 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from PyQt4.QtCore import Qt, SIGNAL, QUrl, QRect
from PyQt4.QtGui import (QMainWindow, QMenu, QLabel, QMessageBox, QInputDialog, QLineEdit,
    QDesktopServices, QFileDialog, QMenuBar, QWidget, QVBoxLayout, QAbstractItemView, QStatusBar,
    QDialog)

from hscommon.plat import ISOSX, ISLINUX
from hscommon.trans import trget
from hscommon.util import nonone
from qtlib.util import moveToScreenCenter

from .results_model import ResultsView
from .stats_label import StatsLabel
from .util import createActions
from .prioritize_dialog import PrioritizeDialog

tr = trget('ui')

class ResultWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self, None)
        self.app = app
        self._last_filter = None
        self._setupUi()
        self.resultsModel = app.RESULT_MODEL_CLASS(self.app, self.resultsView)
        self.stats = StatsLabel(app, self.statusLabel)
        self._update_column_actions_status()
        
        self.connect(self.menuColumns, SIGNAL('triggered(QAction*)'), self.columnToggled)
        self.connect(self.resultsView, SIGNAL('doubleClicked()'), self.resultsDoubleClicked)
        self.connect(self.resultsView, SIGNAL('spacePressed()'), self.resultsSpacePressed)
        self.app.willSavePrefs.connect(self.appWillSavePrefs)
    
    def _setupActions(self):
        # (name, shortcut, icon, desc, func)
        ACTIONS = [
            ('actionDetails', 'Ctrl+I', '', tr("Details"), self.detailsTriggered),
            ('actionActions', '', '', tr("Actions"), self.actionsTriggered),
            ('actionPowerMarker', 'Ctrl+1', '', tr("Show Dupes Only"), self.powerMarkerTriggered),
            ('actionDelta', 'Ctrl+2', '', tr("Show Delta Values"), self.deltaTriggered),
            ('actionDeleteMarked', 'Ctrl+D', '', tr("Send Marked to Recycle Bin"), self.deleteTriggered),
            ('actionHardlinkMarked', 'Ctrl+Shift+D', '', tr("Delete Marked and Replace with Hardlinks"), self.hardlinkTriggered),
            ('actionMoveMarked', 'Ctrl+M', '', tr("Move Marked to..."), self.moveTriggered),
            ('actionCopyMarked', 'Ctrl+Shift+M', '', tr("Copy Marked to..."), self.copyTriggered),
            ('actionRemoveMarked', 'Ctrl+R', '', tr("Remove Marked from Results"), self.removeMarkedTriggered),
            ('actionReprioritize', '', '', tr("Re-Prioritize Results..."), self.reprioritizeTriggered),
            ('actionRemoveSelected', 'Ctrl+Del', '', tr("Remove Selected from Results"), self.removeSelectedTriggered),
            ('actionIgnoreSelected', 'Ctrl+Shift+Del', '', tr("Add Selected to Ignore List"), self.addToIgnoreListTriggered),
            ('actionMakeSelectedReference', 'Ctrl+Space', '', tr("Make Selected Reference"), self.makeReferenceTriggered),
            ('actionOpenSelected', 'Ctrl+O', '', tr("Open Selected with Default Application"), self.openTriggered),
            ('actionRevealSelected', 'Ctrl+Shift+O', '', tr("Open Containing Folder of Selected"), self.revealTriggered),
            ('actionRenameSelected', 'F2', '', tr("Rename Selected"), self.renameTriggered),
            ('actionMarkAll', 'Ctrl+A', '', tr("Mark All"), self.markAllTriggered),
            ('actionMarkNone', 'Ctrl+Shift+A', '', tr("Mark None"), self.markNoneTriggered),
            ('actionInvertMarking', 'Ctrl+Alt+A', '', tr("Invert Marking"), self.markInvertTriggered),
            ('actionMarkSelected', '', '', tr("Mark Selected"), self.markSelectedTriggered),
            ('actionClearIgnoreList', '', '', tr("Clear Ignore List"), self.clearIgnoreListTriggered),
            ('actionApplyFilter', 'Ctrl+F', '', tr("Apply Filter"), self.applyFilterTriggered),
            ('actionCancelFilter', 'Ctrl+Shift+F', '', tr("Cancel Filter"), self.cancelFilterTriggered),
            ('actionExport', '', '', tr("Export To HTML"), self.exportTriggered),
            ('actionSaveResults', 'Ctrl+S', '', tr("Save Results..."), self.saveResultsTriggered),
            ('actionInvokeCustomCommand', 'Ctrl+Alt+I', '', tr("Invoke Custom Command"), self.app.invokeCustomCommand),
        ]
        createActions(ACTIONS, self)
        self.actionDelta.setCheckable(True)
        self.actionPowerMarker.setCheckable(True)
        
        if (not ISOSX) and (not ISLINUX):
            self.actionHardlinkMarked.setVisible(False)
    
    def _setupMenu(self):
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 630, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setTitle(tr("File"))
        self.menuMark = QMenu(self.menubar)
        self.menuMark.setTitle(tr("Mark"))
        self.menuActions = QMenu(self.menubar)
        self.menuActions.setTitle(tr("Actions"))
        self.menuColumns = QMenu(self.menubar)
        self.menuColumns.setTitle(tr("Columns"))
        self.menuView = QMenu(self.menubar)
        self.menuView.setTitle(tr("View"))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setTitle(tr("Help"))
        self.setMenuBar(self.menubar)
        
        self.menuActions.addAction(self.actionDeleteMarked)
        self.menuActions.addAction(self.actionHardlinkMarked)
        self.menuActions.addAction(self.actionMoveMarked)
        self.menuActions.addAction(self.actionCopyMarked)
        self.menuActions.addAction(self.actionRemoveMarked)
        self.menuActions.addAction(self.actionReprioritize)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionRemoveSelected)
        self.menuActions.addAction(self.actionIgnoreSelected)
        self.menuActions.addAction(self.actionMakeSelectedReference)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionOpenSelected)
        self.menuActions.addAction(self.actionRevealSelected)
        self.menuActions.addAction(self.actionInvokeCustomCommand)
        self.menuActions.addAction(self.actionRenameSelected)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionApplyFilter)
        self.menuActions.addAction(self.actionCancelFilter)
        self.menuMark.addAction(self.actionMarkAll)
        self.menuMark.addAction(self.actionMarkNone)
        self.menuMark.addAction(self.actionInvertMarking)
        self.menuMark.addAction(self.actionMarkSelected)
        self.menuView.addAction(self.actionPowerMarker)
        self.menuView.addAction(self.actionDelta)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionDetails)
        self.menuView.addAction(self.app.actionPreferences)
        self.menuHelp.addAction(self.app.actionShowHelp)
        self.menuHelp.addAction(self.app.actionRegister)
        self.menuHelp.addAction(self.app.actionCheckForUpdate)
        self.menuHelp.addAction(self.app.actionOpenDebugLog)
        self.menuHelp.addAction(self.app.actionAbout)
        self.menuFile.addAction(self.actionSaveResults)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionClearIgnoreList)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.app.actionQuit)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMark.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuColumns.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        # Columns menu
        menu = self.menuColumns
        self._column_actions = []
        for index, (display, visible) in enumerate(self.app.model.result_table.columns.menu_items()):
            action = menu.addAction(display)
            action.setCheckable(True)
            action.setChecked(visible)
            action.item_index = index
            self._column_actions.append(action)
        menu.addSeparator()
        action = menu.addAction(tr("Reset to Defaults"))
        action.item_index = -1
        
        # Action menu
        actionMenu = QMenu(tr("Actions"), self.menubar)
        actionMenu.addAction(self.actionDeleteMarked)
        actionMenu.addAction(self.actionHardlinkMarked)
        actionMenu.addAction(self.actionMoveMarked)
        actionMenu.addAction(self.actionCopyMarked)
        actionMenu.addAction(self.actionRemoveMarked)
        actionMenu.addSeparator()
        actionMenu.addAction(self.actionRemoveSelected)
        actionMenu.addAction(self.actionIgnoreSelected)
        actionMenu.addAction(self.actionMakeSelectedReference)
        actionMenu.addSeparator()
        actionMenu.addAction(self.actionOpenSelected)
        actionMenu.addAction(self.actionRevealSelected)
        actionMenu.addAction(self.actionInvokeCustomCommand)
        actionMenu.addAction(self.actionRenameSelected)
        self.actionActions.setMenu(actionMenu)
    
    def _setupUi(self):
        self.setWindowTitle(tr("{} Results").format(self.app.NAME))
        self.resize(630, 514)
        self.centralwidget = QWidget(self)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setMargin(0)
        self.resultsView = ResultsView(self.centralwidget)
        self.resultsView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.resultsView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.resultsView.setSortingEnabled(True)
        self.resultsView.verticalHeader().setVisible(False)
        h = self.resultsView.horizontalHeader()
        h.setHighlightSections(False)
        h.setMovable(True)
        h.setStretchLastSection(False)
        h.setDefaultAlignment(Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.resultsView)
        self.setCentralWidget(self.centralwidget)
        self._setupActions()
        self._setupMenu()
        self.statusbar = QStatusBar(self)
        self.statusbar.setSizeGripEnabled(True)
        self.setStatusBar(self.statusbar)
        self.statusLabel = QLabel(self)
        self.statusbar.addPermanentWidget(self.statusLabel, 1)
        
        if self.app.prefs.resultWindowIsMaximized:
            self.setWindowState(self.windowState() | Qt.WindowMaximized)
        else:
            if self.app.prefs.resultWindowRect is not None:
                self.setGeometry(self.app.prefs.resultWindowRect)
            else:
                moveToScreenCenter(self)
    
    #--- Private
    def _update_column_actions_status(self):
        # Update menu checked state
        menu_items = self.app.model.result_table.columns.menu_items()
        for action, (display, visible) in zip(self._column_actions, menu_items):
            action.setChecked(visible)
    
    #--- Actions
    def actionsTriggered(self):
        self.actionsButton.showMenu()
    
    def addToIgnoreListTriggered(self):
        self.app.model.add_selected_to_ignore_list()
    
    def applyFilterTriggered(self):
        title = tr("Apply Filter")
        msg = tr("Type the filter you want to apply on your results. See help for details.")
        text = nonone(self._last_filter, '[*]')
        answer, ok = QInputDialog.getText(self, title, msg, QLineEdit.Normal, text)
        if not ok:
            return
        answer = str(answer)
        self.app.model.apply_filter(answer)
        self._last_filter = answer
    
    def cancelFilterTriggered(self):
        self.app.model.apply_filter('')
    
    def clearIgnoreListTriggered(self):
        title = tr("Clear Ignore List")
        count = len(self.app.model.scanner.ignore_list)
        if not count:
            QMessageBox.information(self, title, tr("Nothing to clear."))
            return
        msg = tr("Do you really want to remove all %d items from the ignore list?") % count
        if self.app.confirm(title, msg, QMessageBox.No):
            self.app.model.scanner.ignore_list.Clear()
            QMessageBox.information(self, title, tr("Ignore list cleared."))
    
    def copyTriggered(self):
        self.app.copy_or_move_marked(True)
    
    def deleteTriggered(self):
        count = self.app.model.results.mark_count
        if not count:
            return
        title = tr("Delete duplicates")
        msg = tr("You are about to send %d files to Trash. Continue?") % count
        if self.app.confirm(title, msg):
            self.app.model.delete_marked()
    
    def deltaTriggered(self):
        self.resultsModel.delta_values = self.actionDelta.isChecked()
    
    def detailsTriggered(self):
        self.app.show_details()
    
    def exportTriggered(self):
        h = self.resultsView.horizontalHeader()
        column_ids = []
        for i in range(len(self.app.model.COLUMNS)):
            if not h.isSectionHidden(i):
                column_ids.append(str(i))
        exported_path = self.app.model.export_to_xhtml(column_ids)
        url = QUrl.fromLocalFile(exported_path)
        QDesktopServices.openUrl(url)
    
    def hardlinkTriggered(self):
        count = self.app.model.results.mark_count
        if not count:
            return
        title = tr("Delete and hardlink duplicates")
        msg = tr("You are about to send %d files to Trash (and hardlink them afterwards). Continue?") % count
        if self.app.confirm(title, msg):
            self.app.model.delete_marked(replace_with_hardlinks=True)
    
    def makeReferenceTriggered(self):
        self.app.model.make_selected_reference()
    
    def markAllTriggered(self):
        self.app.model.mark_all()
    
    def markInvertTriggered(self):
        self.app.model.mark_invert()
    
    def markNoneTriggered(self):
        self.app.model.mark_none()
    
    def markSelectedTriggered(self):
        self.app.model.toggle_selected_mark_state()
    
    def moveTriggered(self):
        self.app.copy_or_move_marked(False)
    
    def openTriggered(self):
        self.app.model.open_selected()
    
    def powerMarkerTriggered(self):
        self.resultsModel.power_marker = self.actionPowerMarker.isChecked()
    
    def preferencesTriggered(self):
        self.app.show_preferences()
    
    def removeMarkedTriggered(self):
        count = self.app.model.results.mark_count
        if not count:
            return
        title = tr("Remove duplicates")
        msg = tr("You are about to remove %d files from results. Continue?") % count
        if self.app.confirm(title, msg):
            self.app.model.remove_marked()
    
    def removeSelectedTriggered(self):
        self.app.model.remove_selected()
    
    def renameTriggered(self):
        self.resultsView.edit(self.resultsView.selectionModel().currentIndex())
    
    def reprioritizeTriggered(self):
        dlg = PrioritizeDialog(self, self.app)
        result = dlg.exec()
        if result == QDialog.Accepted:
            dlg.model.perform_reprioritization()
    
    def revealTriggered(self):
        self.app.model.reveal_selected()
    
    def saveResultsTriggered(self):
        title = tr("Select a file to save your results to")
        files = tr("dupeGuru Results (*.dupeguru)")
        destination = QFileDialog.getSaveFileName(self, title, '', files)
        if destination:
            if not destination.endswith('.dupeguru'):
                destination = '{}.dupeguru'.format(destination)
            self.app.model.save_as(destination)
            self.app.recentResults.insertItem(destination)
    
    #--- Events
    def appWillSavePrefs(self):
        prefs = self.app.prefs
        prefs.resultWindowIsMaximized = self.isMaximized()
        prefs.resultWindowRect = self.geometry()
    
    def columnToggled(self, action):
        index = action.item_index
        if index == -1:
            self.app.model.result_table.columns.reset_to_defaults()
            self._update_column_actions_status()
        else:
            visible = self.app.model.result_table.columns.toggle_menu_item(index)
            action.setChecked(visible)
    
    def contextMenuEvent(self, event):
        self.actionActions.menu().exec_(event.globalPos())
    
    def resultsDoubleClicked(self):
        self.app.model.open_selected()
    
    def resultsSpacePressed(self):
        self.app.model.toggle_selected_mark_state()
    
