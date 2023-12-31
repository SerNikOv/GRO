# import re
# from builtins import print
from PyQt5.QtWidgets import QApplication, QFileDialog, QButtonGroup, QAbstractButton
from PyQt5 import uic
from PyQt5.Qt import QApplication, QSettings, QMainWindow, QLineEdit, QCheckBox, QVBoxLayout, QWidget
import configparser
from pathlib import Path, PurePath, PurePosixPath
from os.path import abspath, dirname, exists
import shutil
from change_docx import changeDocx, DocxProp

defoult_form = './Config/defoult_form.ini'
# last_form = './Config/ini_form.ini'
open_form = ''
settings = QSettings('User', 'GRO')
config_data_dir = Path("User/GRO")

# Последняя форма
if settings.contains("last_form"):
    last_form = settings.value('last_form')
else:
    settings.setValue('last_form', '/home')
    last_form = '/home'
# Папка объекта
if settings.contains("objFolder"):
    objFolder = settings.value('objFolder')
else:
    settings.setValue('objFolder', '')
    objFolder = ''


def save_form():
    objFolder = settings.value('objFolder')
    objectName = form.object.toPlainText()
    form.progressBar.setValue(0)
    if objectName != '':
        settings.setValue("objectName", objectName)
        if objFolder != '':
            file = objFolder + '/Карточка объекта - ' + objectName + '.gro'
            objFolder = dirname(file)
        else:
            nfile = dirname(last_form) + '/Карточка объекта - ' + form.object.toPlainText() + '.gro'
            file = \
                QFileDialog().getSaveFileName(window, 'Выберите путь для карточки объекта', nfile, filter="*.gro")[0]
            objFolder = dirname(file)
        settings.setValue("objFolder", objFolder)
        window.statusBar().setStyleSheet("color: Black;")
        window.statusBar().showMessage(objFolder)
        if file != '':
            # my_file = open(file, "w+")
            # my_file.close()
            # save_form(file)
            config2 = configparser.ConfigParser()
            config2.read_file(open('./Config/ini_form.ini'))
            # Объект
            if not config2.has_section('Объект'):
                config2.add_section('Объект')
            config2.set('Объект', 'object', form.object.toPlainText())
            config2.set('Объект', 'msk', form.msk.text())
            config2.set('Объект', 'naimobj', form.naimobj.toPlainText())
            config2.set('Объект', 'uchastok', form.uchastok.toPlainText())
            config2.set('Объект', 'kodstr', form.kodstr.text())
            config2.set('Объект', 'objadres', form.objadres.toPlainText())
            # Заказчик
            if not config2.has_section('Заказчик'):
                config2.add_section('Заказчик')
            config2.set('Заказчик', 'zakazchiknaim', form.zakazchiknaim.toPlainText())
            config2.set('Заказчик', 'zakazchikrekviz', form.zakazchikrekviz.toPlainText())
            config2.set('Заказчик', 'zakazchikadres', form.zakazchikadres.toPlainText())
            config2.set('Заказчик', 'zakazchiksro', form.zakazchiksro.toPlainText())
            config2.set('Заказчик', 'zakazchikdolzhn', form.zakazchikdolzhn.toPlainText())
            config2.set('Заказчик', 'zakazchikfio', form.zakazchikfio.toPlainText())
            config2.set('Заказчик', 'zakazchikprikaz', form.zakazchikprikaz.toPlainText())
            # Стройконтроль
            if not config2.has_section('Стройконтроль'):
                config2.add_section('Стройконтроль')
            config2.set('Стройконтроль', 'skrekviz', form.skrekviz.toPlainText())
            config2.set('Стройконтроль', 'skadres', form.skadres.toPlainText())
            config2.set('Стройконтроль', 'skdolzhnost', form.skdolzhnost.toPlainText())
            config2.set('Стройконтроль', 'skfio', form.skfio.toPlainText())
            config2.set('Стройконтроль', 'skprikaz', form.skprikaz.toPlainText())

            # Генподрядчик
            if not config2.has_section('Генподрядчик'):
                config2.add_section('Генподрядчик')
            config2.set('Генподрядчик', 'genpodryadchiknaim', form.genpodryadchiknaim.toPlainText())
            config2.set('Генподрядчик', 'genpodryadchikrekviz', form.genpodryadchikrekviz.toPlainText())
            config2.set('Генподрядчик', 'genpodryadchikadres', form.genpodryadchikadres.toPlainText())
            config2.set('Генподрядчик', 'genpodryadchiksro', form.genpodryadchiksro.toPlainText())
            config2.set('Генподрядчик', 'genpodryadchikdolzhn', form.genpodryadchikdolzhn.toPlainText())
            config2.set('Генподрядчик', 'genpodryadchikfio', form.genpodryadchikfio.toPlainText())
            config2.set('Генподрядчик', 'genpodryadchikprikaz', form.genpodryadchikprikaz.toPlainText())
            config2.set('Генподрядчик', 'skgpdolzhnost', form.skgpdolzhnost.toPlainText())
            config2.set('Генподрядчик', 'skgpfio', form.skgpfio.toPlainText())
            config2.set('Генподрядчик', 'skgpprikaz', form.skgpprikaz.toPlainText())
            config2.set('Генподрядчик', 'skgpreestr', form.skgpreestr.toPlainText())
            # Субподрядчик
            if not config2.has_section('Субподрядчик'):
                config2.add_section('Субподрядчик')
            config2.set('Субподрядчик', 'stroitelnaim', form.stroitelnaim.toPlainText())
            config2.set('Субподрядчик', 'stroiteldolzhn', form.stroiteldolzhn.toPlainText())
            config2.set('Субподрядчик', 'stroitelfio', form.stroitelfio.toPlainText())
            config2.set('Субподрядчик', 'stroitelprikaz', form.stroitelprikaz.toPlainText())
            # АН
            if not config2.has_section('АН'):
                config2.add_section('АН')
            config2.set('АН', 'proektnaim', form.proektnaim.toPlainText())
            config2.set('АН', 'proektrekviz', form.proektrekviz.toPlainText())
            config2.set('АН', 'proektadres', form.proektadres.toPlainText())
            config2.set('АН', 'proektsro', form.proektsro.toPlainText())
            config2.set('АН', 'gip', form.gip.toPlainText())
            config2.set('АН', 'proektdolzhn', form.proektdolzhn.toPlainText())
            config2.set('АН', 'proektfio', form.proektfio.toPlainText())
            config2.set('АН', 'proektprikaz', form.proektprikaz.toPlainText())
            # ГРО
            if not config2.has_section('ГРО'):
                config2.add_section('ГРО')
            config2.set('ГРО', 'gronaim', form.gronaim.toPlainText())
            config2.set('ГРО', 'grorekviz', form.grorekviz.toPlainText())
            config2.set('ГРО', 'groadres', form.groadres.toPlainText())
            config2.set('ГРО', 'grodolzhn', form.grodolzhn.toPlainText())
            config2.set('ГРО', 'grofio', form.grofio.toPlainText())
            config2.set('ГРО', 'groprikaz', form.groprikaz.toPlainText())

            # Акты
            if not config2.has_section('Акты'):
                config2.add_section('Акты')
            config2.set('Акты', 'nactogs', form.nactogs.text())
            config2.set('Акты', 'nactotvod', form.nactotvod.text())
            config2.set('Акты', 'allrp', str(form.allrp.value()))
            config2.set('Акты', 'allnr', str(form.allnr.value()))
            config2.set('Акты', 'l_shem_ogs', str(form.l_shem_ogs.value()))
            config2.set('Акты', 'l_kat_ogs', str(form.l_kat_ogs.value()))
            config2.set('Акты', 'shifrgp', form.shifrgp.text())
            config2.set('Акты', 'tchk_otvod', str(form.tchk_otvod.value()))
            config2.set('Акты', 'l_shem_otvod', str(form.l_shem_otvod.value()))
            config2.set('Акты', 'l_kat_otvod', str(form.l_kat_otvod.value()))
            config2.set('Акты', 'shifrppo', form.shifrppo.text())
            # ОСИ
            if not config2.has_section('ОСИ'):
                config2.add_section('ОСИ')
            config2.set('ОСИ', 'iactos_1', form.iactos_1.toPlainText())
            config2.set('ОСИ', 'iactos_2', form.iactos_2.toPlainText())
            config2.set('ОСИ', 'iactos_3', form.iactos_3.toPlainText())
            config2.set('ОСИ', 'iactos_4', form.iactos_4.toPlainText())
            config2.set('ОСИ', 'iactos_5', form.iactos_5.toPlainText())
            config2.set('ОСИ', 'iactos_6', form.iactos_6.toPlainText())
            config2.set('ОСИ', 'iactos_7', form.iactos_7.toPlainText())
            config2.set('ОСИ', 'iactos_8', form.iactos_8.toPlainText())
            config2.set('ОСИ', 'iactos_9', form.iactos_9.toPlainText())
            config2.set('ОСИ', 'iactos_10', form.iactos_10.toPlainText())
            config2.set('ОСИ', 'iactos_11', form.iactos_11.toPlainText())
            config2.set('ОСИ', 'iactos_12', form.iactos_12.toPlainText())
            config2.set('ОСИ', 'iactos_13', form.iactos_13.toPlainText())
            config2.set('ОСИ', 'iactos_14', form.iactos_14.toPlainText())
            config2.set('ОСИ', 'iactos_15', form.iactos_15.toPlainText())

            config2.set('ОСИ', 'nactos_1', form.nactos_1.toPlainText())
            config2.set('ОСИ', 'nactos_2', form.nactos_2.toPlainText())
            config2.set('ОСИ', 'nactos_3', form.nactos_3.toPlainText())
            config2.set('ОСИ', 'nactos_4', form.nactos_4.toPlainText())
            config2.set('ОСИ', 'nactos_5', form.nactos_5.toPlainText())
            config2.set('ОСИ', 'nactos_6', form.nactos_6.toPlainText())
            config2.set('ОСИ', 'nactos_7', form.nactos_7.toPlainText())
            config2.set('ОСИ', 'nactos_8', form.nactos_8.toPlainText())
            config2.set('ОСИ', 'nactos_9', form.nactos_9.toPlainText())
            config2.set('ОСИ', 'nactos_10', form.nactos_10.toPlainText())
            config2.set('ОСИ', 'nactos_11', form.nactos_11.toPlainText())
            config2.set('ОСИ', 'nactos_12', form.nactos_12.toPlainText())
            config2.set('ОСИ', 'nactos_13', form.nactos_13.toPlainText())
            config2.set('ОСИ', 'nactos_14', form.nactos_14.toPlainText())
            config2.set('ОСИ', 'nactos_15', form.nactos_15.toPlainText())

            config2.set('ОСИ', 'rp_1', str(form.rp_1.value()))
            config2.set('ОСИ', 'rp_2', str(form.rp_2.value()))
            config2.set('ОСИ', 'rp_3', str(form.rp_3.value()))
            config2.set('ОСИ', 'rp_4', str(form.rp_4.value()))
            config2.set('ОСИ', 'rp_5', str(form.rp_5.value()))
            config2.set('ОСИ', 'rp_6', str(form.rp_6.value()))
            config2.set('ОСИ', 'rp_7', str(form.rp_7.value()))
            config2.set('ОСИ', 'rp_8', str(form.rp_8.value()))
            config2.set('ОСИ', 'rp_9', str(form.rp_9.value()))
            config2.set('ОСИ', 'rp_10', str(form.rp_10.value()))
            config2.set('ОСИ', 'rp_11', str(form.rp_11.value()))
            config2.set('ОСИ', 'rp_12', str(form.rp_12.value()))
            config2.set('ОСИ', 'rp_13', str(form.rp_13.value()))
            config2.set('ОСИ', 'rp_14', str(form.rp_14.value()))
            config2.set('ОСИ', 'rp_15', str(form.rp_15.value()))

            config2.set('ОСИ', 'nr_1', str(form.nr_1.value()))
            config2.set('ОСИ', 'nr_2', str(form.nr_2.value()))
            config2.set('ОСИ', 'nr_3', str(form.nr_3.value()))
            config2.set('ОСИ', 'nr_4', str(form.nr_4.value()))
            config2.set('ОСИ', 'nr_5', str(form.nr_5.value()))
            config2.set('ОСИ', 'nr_6', str(form.nr_6.value()))
            config2.set('ОСИ', 'nr_7', str(form.nr_7.value()))
            config2.set('ОСИ', 'nr_8', str(form.nr_8.value()))
            config2.set('ОСИ', 'nr_9', str(form.nr_9.value()))
            config2.set('ОСИ', 'nr_10', str(form.nr_10.value()))
            config2.set('ОСИ', 'nr_11', str(form.nr_11.value()))
            config2.set('ОСИ', 'nr_12', str(form.nr_12.value()))
            config2.set('ОСИ', 'nr_13', str(form.nr_13.value()))
            config2.set('ОСИ', 'nr_14', str(form.nr_14.value()))
            config2.set('ОСИ', 'nr_15', str(form.nr_15.value()))

            config2.set('ОСИ', 'tos_1', str(form.tos_1.value()))
            config2.set('ОСИ', 'tos_2', str(form.tos_2.value()))
            config2.set('ОСИ', 'tos_3', str(form.tos_3.value()))
            config2.set('ОСИ', 'tos_4', str(form.tos_4.value()))
            config2.set('ОСИ', 'tos_5', str(form.tos_5.value()))
            config2.set('ОСИ', 'tos_6', str(form.tos_6.value()))
            config2.set('ОСИ', 'tos_7', str(form.tos_7.value()))
            config2.set('ОСИ', 'tos_8', str(form.tos_8.value()))
            config2.set('ОСИ', 'tos_9', str(form.tos_9.value()))
            config2.set('ОСИ', 'tos_10', str(form.tos_10.value()))
            config2.set('ОСИ', 'tos_11', str(form.tos_11.value()))
            config2.set('ОСИ', 'tos_12', str(form.tos_12.value()))
            config2.set('ОСИ', 'tos_13', str(form.tos_13.value()))
            config2.set('ОСИ', 'tos_14', str(form.tos_14.value()))
            config2.set('ОСИ', 'tos_15', str(form.tos_15.value()))

            config2.set('ОСИ', 'lshem_1', str(form.lshem_1.value()))
            config2.set('ОСИ', 'lshem_2', str(form.lshem_2.value()))
            config2.set('ОСИ', 'lshem_3', str(form.lshem_3.value()))
            config2.set('ОСИ', 'lshem_4', str(form.lshem_4.value()))
            config2.set('ОСИ', 'lshem_5', str(form.lshem_5.value()))
            config2.set('ОСИ', 'lshem_6', str(form.lshem_6.value()))
            config2.set('ОСИ', 'lshem_7', str(form.lshem_7.value()))
            config2.set('ОСИ', 'lshem_8', str(form.lshem_8.value()))
            config2.set('ОСИ', 'lshem_9', str(form.lshem_9.value()))
            config2.set('ОСИ', 'lshem_10', str(form.lshem_10.value()))
            config2.set('ОСИ', 'lshem_11', str(form.lshem_11.value()))
            config2.set('ОСИ', 'lshem_12', str(form.lshem_12.value()))
            config2.set('ОСИ', 'lshem_13', str(form.lshem_13.value()))
            config2.set('ОСИ', 'lshem_14', str(form.lshem_14.value()))
            config2.set('ОСИ', 'lshem_15', str(form.lshem_15.value()))

            config2.set('ОСИ', 'lkat_1', str(form.lkat_1.value()))
            config2.set('ОСИ', 'lkat_2', str(form.lkat_2.value()))
            config2.set('ОСИ', 'lkat_3', str(form.lkat_3.value()))
            config2.set('ОСИ', 'lkat_4', str(form.lkat_4.value()))
            config2.set('ОСИ', 'lkat_5', str(form.lkat_5.value()))
            config2.set('ОСИ', 'lkat_6', str(form.lkat_6.value()))
            config2.set('ОСИ', 'lkat_7', str(form.lkat_7.value()))
            config2.set('ОСИ', 'lkat_8', str(form.lkat_8.value()))
            config2.set('ОСИ', 'lkat_9', str(form.lkat_9.value()))
            config2.set('ОСИ', 'lkat_10', str(form.lkat_10.value()))
            config2.set('ОСИ', 'lkat_11', str(form.lkat_11.value()))
            config2.set('ОСИ', 'lkat_12', str(form.lkat_12.value()))
            config2.set('ОСИ', 'lkat_13', str(form.lkat_13.value()))
            config2.set('ОСИ', 'lkat_14', str(form.lkat_14.value()))
            config2.set('ОСИ', 'lkat_15', str(form.lkat_15.value()))

            config2.set('ОСИ', 'shifrrd_1', form.shifrrd_1.toPlainText())
            config2.set('ОСИ', 'shifrrd_2', form.shifrrd_2.toPlainText())
            config2.set('ОСИ', 'shifrrd_3', form.shifrrd_3.toPlainText())
            config2.set('ОСИ', 'shifrrd_4', form.shifrrd_4.toPlainText())
            config2.set('ОСИ', 'shifrrd_5', form.shifrrd_5.toPlainText())
            config2.set('ОСИ', 'shifrrd_6', form.shifrrd_6.toPlainText())
            config2.set('ОСИ', 'shifrrd_7', form.shifrrd_7.toPlainText())
            config2.set('ОСИ', 'shifrrd_8', form.shifrrd_8.toPlainText())
            config2.set('ОСИ', 'shifrrd_9', form.shifrrd_9.toPlainText())
            config2.set('ОСИ', 'shifrrd_10', form.shifrrd_10.toPlainText())
            config2.set('ОСИ', 'shifrrd_11', form.shifrrd_11.toPlainText())
            config2.set('ОСИ', 'shifrrd_12', form.shifrrd_12.toPlainText())
            config2.set('ОСИ', 'shifrrd_13', form.shifrrd_13.toPlainText())
            config2.set('ОСИ', 'shifrrd_14', form.shifrrd_14.toPlainText())
            config2.set('ОСИ', 'shifrrd_15', form.shifrrd_15.toPlainText())

            with open('./Config/ini_form.ini', 'w') as configfile2:
                config2.write(configfile2)
            shutil.copyfile('./Config/ini_form.ini', file)
            settings.setValue('last_form', file)
    else:
        form.tabWidget.setCurrentIndex(0)
        form.object.setFocus()


def ini_form(file=None):
    try:
        if file != "":
            config = configparser.ConfigParser()
            config.read_file(open(file))
            form.progressBar.setValue(0)
            # Папка объекта
            if settings.contains("objFolder"):
                objFolder = settings.value('objFolder')
            else:
                settings.setValue('objFolder', '')
                objFolder = ''

            if objFolder != '':
                window.statusBar().setStyleSheet("color: Black;")
                window.statusBar().showMessage(objFolder)
            if objFolder == '':
                window.statusBar().setStyleSheet("color: Red;")
                window.statusBar().showMessage('Папка не задана!!!')

            # Объект
            window.setWindowTitle(config.get('Объект', 'object'))
            form.object.setText(config.get('Объект', 'object'))
            form.msk.setText(config.get('Объект', 'msk'))
            form.naimobj.setText(config.get('Объект', 'naimobj'))
            form.uchastok.setText(config.get('Объект', 'uchastok'))
            form.kodstr.setText(config.get('Объект', 'kodstr'))
            form.objadres.setText(config.get('Объект', 'objadres'))
            # Заказчик
            form.zakazchiknaim.setText(config.get('Заказчик', 'zakazchiknaim'))
            form.zakazchikrekviz.setText(config.get('Заказчик', 'zakazchikrekviz'))
            form.zakazchikadres.setText(config.get('Заказчик', 'zakazchikadres'))
            form.zakazchiksro.setText(config.get('Заказчик', 'zakazchiksro'))
            form.zakazchikdolzhn.setText(config.get('Заказчик', 'zakazchikdolzhn'))
            form.zakazchikfio.setText(config.get('Заказчик', 'zakazchikfio'))
            form.zakazchikprikaz.setText(config.get('Заказчик', 'zakazchikprikaz'))
            # Стройконтроль
            form.skrekviz.setText(config.get('Стройконтроль', 'skrekviz'))
            form.skadres.setText(config.get('Стройконтроль', 'skadres'))
            form.skdolzhnost.setText(config.get('Стройконтроль', 'skdolzhnost'))
            form.skfio.setText(config.get('Стройконтроль', 'skfio'))
            form.skprikaz.setText(config.get('Стройконтроль', 'skprikaz'))
            # form.skreestr.setText(config.get('Стройконтроль', 'skreestr'))
            # Генподрядчик
            form.genpodryadchiknaim.setText(config.get('Генподрядчик', 'genpodryadchiknaim'))
            form.genpodryadchikrekviz.setText(config.get('Генподрядчик', 'genpodryadchikrekviz'))
            form.genpodryadchikadres.setText(config.get('Генподрядчик', 'genpodryadchikadres'))
            form.genpodryadchiksro.setText(config.get('Генподрядчик', 'genpodryadchiksro'))
            form.genpodryadchikdolzhn.setText(config.get('Генподрядчик', 'genpodryadchikdolzhn'))
            form.genpodryadchikfio.setText(config.get('Генподрядчик', 'genpodryadchikfio'))
            form.genpodryadchikprikaz.setText(config.get('Генподрядчик', 'genpodryadchikprikaz'))
            form.skgpdolzhnost.setText(config.get('Генподрядчик', 'skgpdolzhnost'))
            form.skgpfio.setText(config.get('Генподрядчик', 'skgpfio'))
            form.skgpprikaz.setText(config.get('Генподрядчик', 'skgpprikaz'))
            form.skgpreestr.setText(config.get('Генподрядчик', 'skgpreestr'))
            # Субподрядчик
            form.stroitelnaim.setText(config.get('Субподрядчик', 'stroitelnaim'))
            form.stroiteldolzhn.setText(config.get('Субподрядчик', 'stroiteldolzhn'))
            form.stroitelfio.setText(config.get('Субподрядчик', 'stroitelfio'))
            form.stroitelprikaz.setText(config.get('Субподрядчик', 'stroitelprikaz'))
            # АН
            form.proektnaim.setText(config.get('АН', 'proektnaim'))
            form.proektrekviz.setText(config.get('АН', 'proektrekviz'))
            form.proektadres.setText(config.get('АН', 'proektadres'))
            form.proektsro.setText(config.get('АН', 'proektsro'))
            form.gip.setText(config.get('АН', 'gip'))
            form.proektdolzhn.setText(config.get('АН', 'proektdolzhn'))
            form.proektfio.setText(config.get('АН', 'proektfio'))
            form.proektprikaz.setText(config.get('АН', 'proektprikaz'))
            # ГРО
            form.gronaim.setText(config.get('ГРО', 'gronaim'))
            form.grorekviz.setText(config.get('ГРО', 'grorekviz'))
            form.groadres.setText(config.get('ГРО', 'groadres'))
            form.grodolzhn.setText(config.get('ГРО', 'grodolzhn'))
            form.grofio.setText(config.get('ГРО', 'grofio'))
            form.groprikaz.setText(config.get('ГРО', 'groprikaz'))
            # Акты
            form.nactogs.setText(config.get('Акты', 'nactogs'))
            form.nactotvod.setText(config.get('Акты', 'nactotvod'))
            form.allrp.setValue(int(config.get('Акты', 'allrp')))
            form.allnr.setValue(int(config.get('Акты', 'allnr')))
            form.l_shem_ogs.setValue(int(config.get('Акты', 'l_shem_ogs')))
            form.l_kat_ogs.setValue(int(config.get('Акты', 'l_kat_ogs')))
            form.shifrgp.setText(config.get('Акты', 'shifrgp'))
            form.tchk_otvod.setValue(int(config.get('Акты', 'tchk_otvod')))
            form.l_shem_otvod.setValue(int(config.get('Акты', 'l_shem_otvod')))
            form.l_kat_otvod.setValue(int(config.get('Акты', 'l_kat_otvod')))
            form.shifrppo.setText(config.get('Акты', 'shifrppo'))
            # ОСИ
            form.iactos_1.setText(config.get('ОСИ', 'iactos_1'))
            form.iactos_2.setText(config.get('ОСИ', 'iactos_2'))
            form.iactos_3.setText(config.get('ОСИ', 'iactos_3'))
            form.iactos_4.setText(config.get('ОСИ', 'iactos_4'))
            form.iactos_5.setText(config.get('ОСИ', 'iactos_5'))
            form.iactos_6.setText(config.get('ОСИ', 'iactos_6'))
            form.iactos_7.setText(config.get('ОСИ', 'iactos_7'))
            form.iactos_8.setText(config.get('ОСИ', 'iactos_8'))
            form.iactos_9.setText(config.get('ОСИ', 'iactos_9'))
            form.iactos_10.setText(config.get('ОСИ', 'iactos_10'))
            form.iactos_11.setText(config.get('ОСИ', 'iactos_11'))
            form.iactos_12.setText(config.get('ОСИ', 'iactos_12'))
            form.iactos_13.setText(config.get('ОСИ', 'iactos_13'))
            form.iactos_14.setText(config.get('ОСИ', 'iactos_14'))
            form.iactos_15.setText(config.get('ОСИ', 'iactos_15'))

            form.nactos_1.setText(config.get('ОСИ', 'nactos_1'))
            form.nactos_2.setText(config.get('ОСИ', 'nactos_2'))
            form.nactos_3.setText(config.get('ОСИ', 'nactos_3'))
            form.nactos_4.setText(config.get('ОСИ', 'nactos_4'))
            form.nactos_5.setText(config.get('ОСИ', 'nactos_5'))
            form.nactos_6.setText(config.get('ОСИ', 'nactos_6'))
            form.nactos_7.setText(config.get('ОСИ', 'nactos_7'))
            form.nactos_8.setText(config.get('ОСИ', 'nactos_8'))
            form.nactos_9.setText(config.get('ОСИ', 'nactos_9'))
            form.nactos_10.setText(config.get('ОСИ', 'nactos_10'))
            form.nactos_11.setText(config.get('ОСИ', 'nactos_11'))
            form.nactos_12.setText(config.get('ОСИ', 'nactos_12'))
            form.nactos_13.setText(config.get('ОСИ', 'nactos_13'))
            form.nactos_14.setText(config.get('ОСИ', 'nactos_14'))
            form.nactos_15.setText(config.get('ОСИ', 'nactos_15'))

            form.rp_1.setValue(int(config.get('ОСИ', 'rp_1')))
            form.rp_2.setValue(int(config.get('ОСИ', 'rp_2')))
            form.rp_3.setValue(int(config.get('ОСИ', 'rp_3')))
            form.rp_4.setValue(int(config.get('ОСИ', 'rp_4')))
            form.rp_5.setValue(int(config.get('ОСИ', 'rp_5')))
            form.rp_6.setValue(int(config.get('ОСИ', 'rp_6')))
            form.rp_7.setValue(int(config.get('ОСИ', 'rp_7')))
            form.rp_8.setValue(int(config.get('ОСИ', 'rp_8')))
            form.rp_9.setValue(int(config.get('ОСИ', 'rp_9')))
            form.rp_10.setValue(int(config.get('ОСИ', 'rp_10')))
            form.rp_11.setValue(int(config.get('ОСИ', 'rp_11')))
            form.rp_12.setValue(int(config.get('ОСИ', 'rp_12')))
            form.rp_13.setValue(int(config.get('ОСИ', 'rp_13')))
            form.rp_14.setValue(int(config.get('ОСИ', 'rp_14')))
            form.rp_15.setValue(int(config.get('ОСИ', 'rp_15')))

            form.nr_1.setValue(int(config.get('ОСИ', 'nr_1')))
            form.nr_2.setValue(int(config.get('ОСИ', 'nr_2')))
            form.nr_3.setValue(int(config.get('ОСИ', 'nr_3')))
            form.nr_4.setValue(int(config.get('ОСИ', 'nr_4')))
            form.nr_5.setValue(int(config.get('ОСИ', 'nr_5')))
            form.nr_6.setValue(int(config.get('ОСИ', 'nr_6')))
            form.nr_7.setValue(int(config.get('ОСИ', 'nr_7')))
            form.nr_8.setValue(int(config.get('ОСИ', 'nr_8')))
            form.nr_9.setValue(int(config.get('ОСИ', 'nr_9')))
            form.nr_10.setValue(int(config.get('ОСИ', 'nr_10')))
            form.nr_11.setValue(int(config.get('ОСИ', 'nr_11')))
            form.nr_12.setValue(int(config.get('ОСИ', 'nr_12')))
            form.nr_13.setValue(int(config.get('ОСИ', 'nr_13')))
            form.nr_14.setValue(int(config.get('ОСИ', 'nr_14')))
            form.nr_15.setValue(int(config.get('ОСИ', 'nr_15')))

            form.tos_1.setValue(int(config.get('ОСИ', 'tos_1')))
            form.tos_2.setValue(int(config.get('ОСИ', 'tos_2')))
            form.tos_3.setValue(int(config.get('ОСИ', 'tos_3')))
            form.tos_4.setValue(int(config.get('ОСИ', 'tos_4')))
            form.tos_5.setValue(int(config.get('ОСИ', 'tos_5')))
            form.tos_6.setValue(int(config.get('ОСИ', 'tos_6')))
            form.tos_7.setValue(int(config.get('ОСИ', 'tos_7')))
            form.tos_8.setValue(int(config.get('ОСИ', 'tos_8')))
            form.tos_9.setValue(int(config.get('ОСИ', 'tos_9')))
            form.tos_10.setValue(int(config.get('ОСИ', 'tos_10')))
            form.tos_11.setValue(int(config.get('ОСИ', 'tos_11')))
            form.tos_12.setValue(int(config.get('ОСИ', 'tos_12')))
            form.tos_13.setValue(int(config.get('ОСИ', 'tos_13')))
            form.tos_14.setValue(int(config.get('ОСИ', 'tos_14')))
            form.tos_15.setValue(int(config.get('ОСИ', 'tos_15')))

            form.lshem_1.setValue(int(config.get('ОСИ', 'lshem_1')))
            form.lshem_2.setValue(int(config.get('ОСИ', 'lshem_2')))
            form.lshem_3.setValue(int(config.get('ОСИ', 'lshem_3')))
            form.lshem_4.setValue(int(config.get('ОСИ', 'lshem_4')))
            form.lshem_5.setValue(int(config.get('ОСИ', 'lshem_5')))
            form.lshem_6.setValue(int(config.get('ОСИ', 'lshem_6')))
            form.lshem_7.setValue(int(config.get('ОСИ', 'lshem_7')))
            form.lshem_8.setValue(int(config.get('ОСИ', 'lshem_8')))
            form.lshem_9.setValue(int(config.get('ОСИ', 'lshem_9')))
            form.lshem_10.setValue(int(config.get('ОСИ', 'lshem_10')))
            form.lshem_11.setValue(int(config.get('ОСИ', 'lshem_11')))
            form.lshem_12.setValue(int(config.get('ОСИ', 'lshem_12')))
            form.lshem_13.setValue(int(config.get('ОСИ', 'lshem_13')))
            form.lshem_14.setValue(int(config.get('ОСИ', 'lshem_14')))
            form.lshem_15.setValue(int(config.get('ОСИ', 'lshem_15')))

            form.lkat_1.setValue(int(config.get('ОСИ', 'lkat_1')))
            form.lkat_2.setValue(int(config.get('ОСИ', 'lkat_2')))
            form.lkat_3.setValue(int(config.get('ОСИ', 'lkat_3')))
            form.lkat_4.setValue(int(config.get('ОСИ', 'lkat_4')))
            form.lkat_5.setValue(int(config.get('ОСИ', 'lkat_5')))
            form.lkat_6.setValue(int(config.get('ОСИ', 'lkat_6')))
            form.lkat_7.setValue(int(config.get('ОСИ', 'lkat_7')))
            form.lkat_8.setValue(int(config.get('ОСИ', 'lkat_8')))
            form.lkat_9.setValue(int(config.get('ОСИ', 'lkat_9')))
            form.lkat_10.setValue(int(config.get('ОСИ', 'lkat_10')))
            form.lkat_11.setValue(int(config.get('ОСИ', 'lkat_11')))
            form.lkat_12.setValue(int(config.get('ОСИ', 'lkat_12')))
            form.lkat_13.setValue(int(config.get('ОСИ', 'lkat_13')))
            form.lkat_14.setValue(int(config.get('ОСИ', 'lkat_14')))
            form.lkat_15.setValue(int(config.get('ОСИ', 'lkat_15')))

            form.shifrrd_1.setText(config.get('ОСИ', 'shifrrd_1'))
            form.shifrrd_2.setText(config.get('ОСИ', 'shifrrd_2'))
            form.shifrrd_3.setText(config.get('ОСИ', 'shifrrd_3'))
            form.shifrrd_4.setText(config.get('ОСИ', 'shifrrd_4'))
            form.shifrrd_5.setText(config.get('ОСИ', 'shifrrd_5'))
            form.shifrrd_6.setText(config.get('ОСИ', 'shifrrd_6'))
            form.shifrrd_7.setText(config.get('ОСИ', 'shifrrd_7'))
            form.shifrrd_8.setText(config.get('ОСИ', 'shifrrd_8'))
            form.shifrrd_9.setText(config.get('ОСИ', 'shifrrd_9'))
            form.shifrrd_10.setText(config.get('ОСИ', 'shifrrd_10'))
            form.shifrrd_11.setText(config.get('ОСИ', 'shifrrd_11'))
            form.shifrrd_12.setText(config.get('ОСИ', 'shifrrd_12'))
            form.shifrrd_13.setText(config.get('ОСИ', 'shifrrd_13'))
            form.shifrrd_14.setText(config.get('ОСИ', 'shifrrd_14'))
            form.shifrrd_15.setText(config.get('ОСИ', 'shifrrd_15'))

            # form.ON_Bybit.setChecked(bool(int(ini_form_cfg.value('ON_Bybit', 0))))
        # if form.ON_Bybit.isChecked():
        #     form.ON_Bybit.setText('ВКЛ')
        #     form.ON_Bybit.setStyleSheet("color: Green;")
        # if form.VIP7.isChecked():
        #     form.VIP7.setStyleSheet("color: Green;")
        # else:
        #     form.VIP7.setStyleSheet("color: Red;")
    except:
        pass


def openini(mode=None):
    try:
        if mode != 'last':
            file = \
                QFileDialog().getOpenFileName(window, 'Выберите файл карточки объекта', last_form, filter="*.gro")[0]
            if file != "":
                if mode == 'open':
                    objFolder = dirname(file)
                if mode == 'copy':
                    objFolder = ''
        else:
            objFolder = dirname(last_form)
            file = last_form

        # print(file)
        # if file != "":
        #     objFolder = dirname(file)
        #     # if mode == 'open':
        #     # objFolder = PurePath(file).as_posix()
        #     # objFolder = abspath(file)
        #     # print(objFolder)
        #     if mode == 'copy':
        #         objFolder = ''
        settings.setValue("objFolder", objFolder)
        settings.setValue("last_form", file)
        ini_form(file)
    except:
        pass


def saveActs():
    save_form()
    objFolder = settings.value('objFolder')
    objectName = settings.value('objectName')
    last_form = settings.value('last_form')
    if objFolder != '':
        if objectName != '':
            # print(objectName)
            # print(exists(file))
            # Промежуточный
            if form.CheckBoxPromezh.isChecked():
                myFile = f'{objFolder}\промежуточный.docx'
                d = config_to_dict(last_form, '')
                # shutil.copyfile('.\Shablon\!промежуточный.docx', myFile)
                shutil.copyfile(".\\Shablon\\!промежуточный.docx", myFile)
                changeDocx(myFile, d)
                print('промежуточный OK')
                window.statusBar().showMessage('промежуточный OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            # ОГС
            if form.CheckBoxRD1.isChecked():
                act = form.nactogs.text().replace('/', '-')
                print(act)
                myFile = f'{objFolder}\{act}(1РД1(ГРО)).docx'
                d = config_to_dict(last_form, '')
                if form.rd_new.isChecked():
                    shutil.copyfile(".\\Shablon\\1РД1(ГРО)нов.docx", myFile)
                if form.rd_old.isChecked():
                    shutil.copyfile(".\\Shablon\\1РД1(ГРО)олд.docx", myFile)
                changeDocx(myFile, d)
                print('РД ОГС OK')
                window.statusBar().showMessage('РД ОГС OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxKAT1.isChecked():
                act = form.nactogs.text().replace('/', '-')
                myFile = f'{objFolder}\{act}(Каталог координат и высот ОГС).docx'
                d = config_to_dict(last_form, '')
                shutil.copyfile(".\\Shablon\\Каталог координат и высот ОГС.docx", myFile)
                changeDocx(myFile, d)
                print('каталог ОГС OK')
                window.statusBar().showMessage('каталог ОГС OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            # Отвод
            if form.CheckBoxRD2.isChecked():
                act = form.nactotvod.text().replace('/', '-')
                print(act)
                myFile = f'{objFolder}\{act}(1РД2(землеотвод)).docx'
                d = config_to_dict(last_form, '')
                if form.rd_new.isChecked():
                    shutil.copyfile(".\\Shablon\\1РД2(землеотвод)нов.docx", myFile)
                if form.rd_old.isChecked():
                    shutil.copyfile(".\\Shablon\\1РД2(землеотвод)олд.docx", myFile)
                changeDocx(myFile, d)
                print('РД отвод OK')
                window.statusBar().showMessage('РД отвод OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxVSN2.isChecked():
                d = config_to_dict(last_form, '')
                act = form.nactotvod.text().replace('/', '-')
                myFile = f'{objFolder}\{act}(2ВСН(землеотвод)).docx'
                shutil.copyfile(".\\Shablon\\2ВСН(землеотвод).docx", myFile)
                changeDocx(myFile, d)
                print('ВСН отвод OK')
                window.statusBar().showMessage('ВСН отвод OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxSP2.isChecked():
                act = form.nactotvod.text().replace('/', '-')
                myFile = f'{objFolder}\{act}(3СП(землеотвод)).docx'
                d = config_to_dict(last_form, '')
                shutil.copyfile(".\\Shablon\\3СП(землеотвод).docx", myFile)
                changeDocx(myFile, d)
                print('СП отвод OK')
                window.statusBar().showMessage('СП отвод OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxKAT2.isChecked():
                act = form.nactotvod.text().replace('/', '-')
                myFile = f'{objFolder}\{act}(Каталог координат землеотвода).docx'
                d = config_to_dict(last_form, '')
                shutil.copyfile('.\\Shablon\\Каталог координат закрепительных знаков землеотвода.docx', myFile)
                changeDocx(myFile, d)
                print('каталог отвод OK')
                window.statusBar().showMessage('каталог отвод OK')
            # ОСИ
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_1.isChecked():
                act = form.nactos_1.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '1')
                makeActOsy(act, d)
                print('ОСИ 1 OK')
                window.statusBar().showMessage('ОСИ 1 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_2.isChecked():
                act = form.nactos_2.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '2')
                makeActOsy(act, d)
                print('ОСИ 2 OK')
                window.statusBar().showMessage('ОСИ 2 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_3.isChecked():
                act = form.nactos_3.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '3')
                makeActOsy(act, d)
                print('ОСИ 3 OK')
                window.statusBar().showMessage('ОСИ 3 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_4.isChecked():
                act = form.nactos_4.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '4')
                makeActOsy(act, d)
                print('ОСИ 4 OK')
                window.statusBar().showMessage('ОСИ 4 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_5.isChecked():
                act = form.nactos_5.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '5')
                makeActOsy(act, d)
                print('ОСИ 5 OK')
                window.statusBar().showMessage('ОСИ 5 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_6.isChecked():
                act = form.nactos_6.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '6')
                makeActOsy(act, d)
                print('ОСИ 6 OK')
                window.statusBar().showMessage('ОСИ 6 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_7.isChecked():
                act = form.nactos_7.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '7')
                makeActOsy(act, d)
                print('ОСИ 7 OK')
                window.statusBar().showMessage('ОСИ 7 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_8.isChecked():
                act = form.nactos_8.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '8')
                makeActOsy(act, d)
                print('ОСИ 8 OK')
                window.statusBar().showMessage('ОСИ 8 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_9.isChecked():
                act = form.nactos_9.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '9')
                makeActOsy(act, d)
                print('ОСИ 9 OK')
                window.statusBar().showMessage('ОСИ 9 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_10.isChecked():
                act = form.nactos_10.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '10')
                makeActOsy(act, d)
                print('ОСИ 10 OK')
                window.statusBar().showMessage('ОСИ 10 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_11.isChecked():
                act = form.nactos_11.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '11')
                makeActOsy(act, d)
                print('ОСИ 11 OK')
                window.statusBar().showMessage('ОСИ 11 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_12.isChecked():
                act = form.nactos_12.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '12')
                makeActOsy(act, d)
                print('ОСИ 12 OK')
                window.statusBar().showMessage('ОСИ 12 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_13.isChecked():
                act = form.nactos_13.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '13')
                makeActOsy(act, d)
                print('ОСИ 13 OK')
                window.statusBar().showMessage('ОСИ 13 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_14.isChecked():
                act = form.nactos_14.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '14')
                makeActOsy(act, d)
                print('ОСИ 14 OK')
                window.statusBar().showMessage('ОСИ 14 OK')
            form.progressBar.setValue(form.progressBar.value() + 5)
            if form.CheckBoxActOs_15.isChecked():
                act = form.nactos_15.toPlainText().replace('/', '-')
                print(act)
                d = config_to_dict(last_form, '15')
                makeActOsy(act, d)
                print('ОСИ 15 OK')
                window.statusBar().showMessage('ОСИ 15 OK')
            window.statusBar().setStyleSheet("color: Green;")
            form.progressBar.setValue(100)
            window.statusBar().showMessage('Акты готовы!')
        else:
            pass
    else:
        pass


def makeActOsy(act, d):
    objFolder = settings.value('objFolder')
    if form.CheckBoxRD3.isChecked():
        myFile = f'{objFolder}\{act}(1РД2(ОСИ)).docx'
        if form.rd_new.isChecked():
            shutil.copyfile(".\\Shablon\\1РД2(ОСИ)нов.docx", myFile)
        if form.rd_old.isChecked():
            shutil.copyfile('.\\Shablon\\1РД2(ОСИ)олд.docx', myFile)
        changeDocx(myFile, d)

    if form.CheckBoxVSN3.isChecked():
        myFile = f'{objFolder}\{act}(2ВСН(ОСИ)).docx'
        shutil.copyfile('.\\Shablon\\2ВСН(ОСИ).docx', myFile)
        changeDocx(myFile, d)

    if form.CheckBoxSP3.isChecked():
        myFile = f'{objFolder}\{act}(3СП(ОСИ)).docx'
        shutil.copyfile('.\\Shablon\\3СП(ОСИ).docx', myFile)
        changeDocx(myFile, d)

    if form.CheckBoxKAT3.isChecked():
        myFile = f'{objFolder}\{act}(Каталог координат осей).docx'
        shutil.copyfile('.\\Shablon\\Каталог координат закрепительных знаков осей.docx', myFile)
        changeDocx(myFile, d)


def config_to_dict(file_path, rt):
    # form.QCheckBox('CheckBoxALLKAT').setChecked(True)
    config = configparser.ConfigParser()
    config.read(file_path)
    d = {}

    # print(config['ОСИ'].keys())
    # print(config.sections())

    for section in config.sections():
        for key in config[section]:
            if section == 'ОСИ':
                k = key.split('_', 1)[-1]
                if rt == k:
                    key2 = key.replace(k, '')
                    d[key2] = config[section][key]
            else:
                d[key] = config[section][key]
    print(d)
    return d


def allACT():
    if form.CheckBoxALLACT.isChecked():
        print('check')
        form.CheckBoxALLRD.setChecked(True)
        form.CheckBoxALLVSN.setChecked(True)
        form.CheckBoxALLSP.setChecked(True)
        form.CheckBoxALLACT.setStyleSheet("color: Green;")
    else:
        form.CheckBoxALLRD.setChecked(False)
        form.CheckBoxALLVSN.setChecked(False)
        form.CheckBoxALLSP.setChecked(False)
        form.CheckBoxALLACT.setStyleSheet("color: Red;")


def allRD():
    if form.CheckBoxALLRD.isChecked():
        # form.CheckBoxRD1.setEnabled(True)
        form.CheckBoxRD1.setChecked(True)
        form.CheckBoxRD2.setChecked(True)
        form.CheckBoxRD3.setChecked(True)
        form.CheckBoxALLRD.setStyleSheet("color: Green;")
    else:
        form.CheckBoxALLACT.setChecked(False)
        form.CheckBoxRD1.setChecked(False)
        form.CheckBoxRD2.setChecked(False)
        form.CheckBoxRD3.setChecked(False)
        form.CheckBoxALLRD.setStyleSheet("color: Red;")


def allVSN():
    if form.CheckBoxALLVSN.isChecked():
        form.CheckBoxVSN2.setChecked(True)
        form.CheckBoxVSN3.setChecked(True)
        form.CheckBoxALLVSN.setStyleSheet("color: Green;")
    else:
        form.CheckBoxALLACT.setChecked(False)
        form.CheckBoxVSN2.setChecked(False)
        form.CheckBoxVSN3.setChecked(False)
        form.CheckBoxALLVSN.setStyleSheet("color: Red;")


def allSP():
    if form.CheckBoxALLSP.isChecked():
        form.CheckBoxSP2.setChecked(True)
        form.CheckBoxSP3.setChecked(True)
        form.CheckBoxALLSP.setStyleSheet("color: Green;")
    else:
        form.CheckBoxALLACT.setChecked(False)
        form.CheckBoxSP2.setChecked(False)
        form.CheckBoxSP3.setChecked(False)
        form.CheckBoxALLSP.setStyleSheet("color: Red;")


def allKAT():
    if form.CheckBoxALLKAT.isChecked():
        form.CheckBoxKAT1.setChecked(True)
        form.CheckBoxKAT2.setChecked(True)
        form.CheckBoxKAT3.setChecked(True)
        form.CheckBoxALLKAT.setStyleSheet("color: Green;")
    else:
        form.CheckBoxKAT1.setChecked(False)
        form.CheckBoxKAT2.setChecked(False)
        form.CheckBoxKAT3.setChecked(False)
        form.CheckBoxALLKAT.setStyleSheet("color: Red;")


def btngroup(btn):
    print(btn.text() + " is selected")
    # print(form.CheckBoxActOs_1.text())


if __name__ == '__main__':
    Form, Window = uic.loadUiType("./form/GRO.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)

    # form.bg = QButtonGroup()
    # form.bg.addButton(form.CheckBoxActOs_1, 1)
    # form.bg.buttonClicked[QAbstractButton].connect(btngroup)
    window.show()

    openini('last')

    # работа с формой
    form.pushButtonOpenini.clicked.connect(lambda: openini('open'))
    form.pushButtonOpenCopy.clicked.connect(lambda: openini('copy'))
    form.pushButtonClear.clicked.connect(lambda: ini_form(defoult_form))
    form.pushButtonSave.clicked.connect(save_form)
    form.pushButtonClose.clicked.connect(window.close)

    # чекбоксы актов
    form.CheckBoxALLACT.stateChanged.connect(allACT)
    form.CheckBoxALLRD.stateChanged.connect(allRD)
    form.CheckBoxALLVSN.stateChanged.connect(allVSN)
    form.CheckBoxALLSP.stateChanged.connect(allSP)
    form.CheckBoxALLKAT.stateChanged.connect(allKAT)

    # Акты
    form.pushButtonSaveAct.clicked.connect(saveActs)
    # form.pushButtonClear_2.clicked.connect(DocxProp)
    app.exec()
