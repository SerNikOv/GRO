import re
from builtins import print
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5 import uic
from PyQt5.Qt import QApplication, QSettings, QMainWindow, QLineEdit, QCheckBox, QVBoxLayout, QWidget
import configparser
from pathlib import Path, PurePath, PurePosixPath
from os.path import abspath, dirname, exists
import shutil

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


def save_form(file=None):
    config2 = configparser.ConfigParser()
    config2.read_file(open(file))
    # Объект
    if not config2.has_section('Объект'):
        config2.add_section('Объект')
    config2.set('Объект', 'object', form.object.toPlainText())
    config2.set('Объект', 'msk', form.msk.text())
    config2.set('Объект', 'naimobj', form.naimobj.toPlainText())
    config2.set('Объект', 'uchastok', form.uchastok.toPlainText())
    config2.set('Объект', 'kodstr', form.kodstr.text())
    config2.set('Объект', 'adres', form.adres.toPlainText())
    # Заказчик
    if not config2.has_section('Заказчик'):
        config2.add_section('Заказчик')
    config2.set('Заказчик', 'zakazchik', form.zakazchik.toPlainText())
    config2.set('Заказчик', 'zakazchikrekviz', form.zakazchikrekviz.toPlainText())
    config2.set('Заказчик', 'zakazchikadres', form.zakazchikadres.toPlainText())
    config2.set('Заказчик', 'zakazchiksro', form.zakazchiksro.toPlainText())
    config2.set('Заказчик', 'zakazchikdolzhn', form.zakazchikdolzhn.toPlainText())
    config2.set('Заказчик', 'zakazchikfio', form.zakazchikfio.toPlainText())
    config2.set('Заказчик', 'zakazchikprikaz', form.zakazchikprikaz.toPlainText())
    # Стройконтроль
    if not config2.has_section('Стройконтроль'):
        config2.add_section('Стройконтроль')
    config2.set('Стройконтроль', 'SKrekviz', form.SKrekviz.toPlainText())
    config2.set('Стройконтроль', 'SKadres', form.SKadres.toPlainText())
    config2.set('Стройконтроль', 'SKdolzhnost', form.SKdolzhnost.toPlainText())
    config2.set('Стройконтроль', 'SKfio', form.SKfio.toPlainText())
    config2.set('Стройконтроль', 'SKprikaz', form.SKprikaz.toPlainText())

    # Генподрядчик
    if not config2.has_section('Генподрядчик'):
        config2.add_section('Генподрядчик')
    config2.set('Генподрядчик', 'genpodryadchik', form.genpodryadchik.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikrekviz', form.genpodryadchikrekviz.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikadres', form.genpodryadchikadres.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchiksro', form.genpodryadchiksro.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikdolzhn', form.genpodryadchikdolzhn.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikfio', form.genpodryadchikfio.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikprikaz', form.genpodryadchikprikaz.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikSKdolzhnost', form.genpodryadchikSKdolzhnost.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikSKfio', form.genpodryadchikSKfio.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikSKprikaz', form.genpodryadchikSKprikaz.toPlainText())
    config2.set('Генподрядчик', 'genpodryadchikSKreestr', form.genpodryadchikSKreestr.toPlainText())
    # Субподрядчик
    if not config2.has_section('Субподрядчик'):
        config2.add_section('Субподрядчик')
    config2.set('Субподрядчик', 'stroitel', form.stroitel.toPlainText())
    config2.set('Субподрядчик', 'stroiteldolzhn', form.stroiteldolzhn.toPlainText())
    config2.set('Субподрядчик', 'stroitelfio', form.stroitelfio.toPlainText())
    config2.set('Субподрядчик', 'stroitelprikaz', form.stroitelprikaz.toPlainText())
    # АН
    if not config2.has_section('АН'):
        config2.add_section('АН')
    config2.set('АН', 'proekt', form.proekt.toPlainText())
    config2.set('АН', 'proektrekviz', form.proektrekviz.toPlainText())
    config2.set('АН', 'proektadres', form.proektadres.toPlainText())
    config2.set('АН', 'proektsro', form.proektsro.toPlainText())
    config2.set('АН', 'GIP', form.GIP.toPlainText())
    config2.set('АН', 'proektdolzhn', form.proektdolzhn.toPlainText())
    config2.set('АН', 'proektfio', form.proektfio.toPlainText())
    config2.set('АН', 'proektprikaz', form.proektprikaz.toPlainText())
    # ГРО
    if not config2.has_section('ГРО'):
        config2.add_section('ГРО')
    config2.set('ГРО', 'GRO', form.GRO.toPlainText())
    config2.set('ГРО', 'GROrekviz', form.GROrekviz.toPlainText())
    config2.set('ГРО', 'GROadres', form.GROadres.toPlainText())
    config2.set('ГРО', 'GROdolzhn', form.GROdolzhn.toPlainText())
    config2.set('ГРО', 'GROfio', form.GROfio.toPlainText())
    config2.set('ГРО', 'GROprikaz', form.GROprikaz.toPlainText())

    # Акты
    if not config2.has_section('Акты'):
        config2.add_section('Акты')
    config2.set('Акты', 'nActOGS', form.nActOGS.text())
    config2.set('Акты', 'nActOtvod', form.nActOtvod.text())
    config2.set('Акты', 'allrp', str(form.allrp.value()))
    config2.set('Акты', 'allnr', str(form.allnr.value()))
    config2.set('Акты', 'l_shem_ogs', str(form.l_shem_ogs.value()))
    config2.set('Акты', 'l_kat_ogs', str(form.l_kat_ogs.value()))
    config2.set('Акты', 'ShifrGP', form.ShifrGP.text())
    config2.set('Акты', 'tchk_otvod', str(form.tchk_otvod.value()))
    config2.set('Акты', 'l_shem_otvod', str(form.l_shem_otvod.value()))
    config2.set('Акты', 'l_kat_otvod', str(form.l_kat_otvod.value()))
    config2.set('Акты', 'ShifrPPO', form.ShifrPPO.text())
    config2.set('Акты', 'ActOs_1', form.ActOs_1.toPlainText())
    config2.set('Акты', 'ActOs_2', form.ActOs_2.toPlainText())
    config2.set('Акты', 'ActOs_3', form.ActOs_3.toPlainText())
    config2.set('Акты', 'ActOs_4', form.ActOs_4.toPlainText())
    config2.set('Акты', 'ActOs_5', form.ActOs_5.toPlainText())
    config2.set('Акты', 'ActOs_6', form.ActOs_6.toPlainText())
    config2.set('Акты', 'ActOs_7', form.ActOs_7.toPlainText())
    config2.set('Акты', 'ActOs_8', form.ActOs_8.toPlainText())
    config2.set('Акты', 'ActOs_9', form.ActOs_9.toPlainText())
    config2.set('Акты', 'ActOs_10', form.ActOs_10.toPlainText())
    config2.set('Акты', 'ActOs_11', form.ActOs_11.toPlainText())
    config2.set('Акты', 'ActOs_12', form.ActOs_12.toPlainText())
    config2.set('Акты', 'ActOs_13', form.ActOs_13.toPlainText())
    config2.set('Акты', 'ActOs_14', form.ActOs_14.toPlainText())
    config2.set('Акты', 'ActOs_15', form.ActOs_15.toPlainText())

    config2.set('Акты', 'nActOs_1', form.nActOs_1.toPlainText())
    config2.set('Акты', 'nActOs_2', form.nActOs_2.toPlainText())
    config2.set('Акты', 'nActOs_3', form.nActOs_3.toPlainText())
    config2.set('Акты', 'nActOs_4', form.nActOs_4.toPlainText())
    config2.set('Акты', 'nActOs_5', form.nActOs_5.toPlainText())
    config2.set('Акты', 'nActOs_6', form.nActOs_6.toPlainText())
    config2.set('Акты', 'nActOs_7', form.nActOs_7.toPlainText())
    config2.set('Акты', 'nActOs_8', form.nActOs_8.toPlainText())
    config2.set('Акты', 'nActOs_9', form.nActOs_9.toPlainText())
    config2.set('Акты', 'nActOs_10', form.nActOs_10.toPlainText())
    config2.set('Акты', 'nActOs_11', form.nActOs_11.toPlainText())
    config2.set('Акты', 'nActOs_12', form.nActOs_12.toPlainText())
    config2.set('Акты', 'nActOs_13', form.nActOs_13.toPlainText())
    config2.set('Акты', 'nActOs_14', form.nActOs_14.toPlainText())
    config2.set('Акты', 'nActOs_15', form.nActOs_15.toPlainText())

    config2.set('Акты', 'rp_1', str(form.rp_1.value()))
    config2.set('Акты', 'rp_2', str(form.rp_2.value()))
    config2.set('Акты', 'rp_3', str(form.rp_3.value()))
    config2.set('Акты', 'rp_4', str(form.rp_4.value()))
    config2.set('Акты', 'rp_5', str(form.rp_5.value()))
    config2.set('Акты', 'rp_6', str(form.rp_6.value()))
    config2.set('Акты', 'rp_7', str(form.rp_7.value()))
    config2.set('Акты', 'rp_8', str(form.rp_8.value()))
    config2.set('Акты', 'rp_9', str(form.rp_9.value()))
    config2.set('Акты', 'rp_10', str(form.rp_10.value()))
    config2.set('Акты', 'rp_11', str(form.rp_11.value()))
    config2.set('Акты', 'rp_12', str(form.rp_12.value()))
    config2.set('Акты', 'rp_13', str(form.rp_13.value()))
    config2.set('Акты', 'rp_14', str(form.rp_14.value()))
    config2.set('Акты', 'rp_15', str(form.rp_15.value()))

    config2.set('Акты', 'nr_1', str(form.nr_1.value()))
    config2.set('Акты', 'nr_2', str(form.nr_2.value()))
    config2.set('Акты', 'nr_3', str(form.nr_3.value()))
    config2.set('Акты', 'nr_4', str(form.nr_4.value()))
    config2.set('Акты', 'nr_5', str(form.nr_5.value()))
    config2.set('Акты', 'nr_6', str(form.nr_6.value()))
    config2.set('Акты', 'nr_7', str(form.nr_7.value()))
    config2.set('Акты', 'nr_8', str(form.nr_8.value()))
    config2.set('Акты', 'nr_9', str(form.nr_9.value()))
    config2.set('Акты', 'nr_10', str(form.nr_10.value()))
    config2.set('Акты', 'nr_11', str(form.nr_11.value()))
    config2.set('Акты', 'nr_12', str(form.nr_12.value()))
    config2.set('Акты', 'nr_13', str(form.nr_13.value()))
    config2.set('Акты', 'nr_14', str(form.nr_14.value()))
    config2.set('Акты', 'nr_15', str(form.nr_15.value()))

    config2.set('Акты', 'tos_1', str(form.tos_1.value()))
    config2.set('Акты', 'tos_2', str(form.tos_2.value()))
    config2.set('Акты', 'tos_3', str(form.tos_3.value()))
    config2.set('Акты', 'tos_4', str(form.tos_4.value()))
    config2.set('Акты', 'tos_5', str(form.tos_5.value()))
    config2.set('Акты', 'tos_6', str(form.tos_6.value()))
    config2.set('Акты', 'tos_7', str(form.tos_7.value()))
    config2.set('Акты', 'tos_8', str(form.tos_8.value()))
    config2.set('Акты', 'tos_9', str(form.tos_9.value()))
    config2.set('Акты', 'tos_10', str(form.tos_10.value()))
    config2.set('Акты', 'tos_11', str(form.tos_11.value()))
    config2.set('Акты', 'tos_12', str(form.tos_12.value()))
    config2.set('Акты', 'tos_13', str(form.tos_13.value()))
    config2.set('Акты', 'tos_14', str(form.tos_14.value()))
    config2.set('Акты', 'tos_15', str(form.tos_15.value()))

    config2.set('Акты', 'lshem_1', str(form.lshem_1.value()))
    config2.set('Акты', 'lshem_2', str(form.lshem_2.value()))
    config2.set('Акты', 'lshem_3', str(form.lshem_3.value()))
    config2.set('Акты', 'lshem_4', str(form.lshem_4.value()))
    config2.set('Акты', 'lshem_5', str(form.lshem_5.value()))
    config2.set('Акты', 'lshem_6', str(form.lshem_6.value()))
    config2.set('Акты', 'lshem_7', str(form.lshem_7.value()))
    config2.set('Акты', 'lshem_8', str(form.lshem_8.value()))
    config2.set('Акты', 'lshem_9', str(form.lshem_9.value()))
    config2.set('Акты', 'lshem_10', str(form.lshem_10.value()))
    config2.set('Акты', 'lshem_11', str(form.lshem_11.value()))
    config2.set('Акты', 'lshem_12', str(form.lshem_12.value()))
    config2.set('Акты', 'lshem_13', str(form.lshem_13.value()))
    config2.set('Акты', 'lshem_14', str(form.lshem_14.value()))
    config2.set('Акты', 'lshem_15', str(form.lshem_15.value()))

    config2.set('Акты', 'lkat_1', str(form.lkat_1.value()))
    config2.set('Акты', 'lkat_2', str(form.lkat_2.value()))
    config2.set('Акты', 'lkat_3', str(form.lkat_3.value()))
    config2.set('Акты', 'lkat_4', str(form.lkat_4.value()))
    config2.set('Акты', 'lkat_5', str(form.lkat_5.value()))
    config2.set('Акты', 'lkat_6', str(form.lkat_6.value()))
    config2.set('Акты', 'lkat_7', str(form.lkat_7.value()))
    config2.set('Акты', 'lkat_8', str(form.lkat_8.value()))
    config2.set('Акты', 'lkat_9', str(form.lkat_9.value()))
    config2.set('Акты', 'lkat_10', str(form.lkat_10.value()))
    config2.set('Акты', 'lkat_11', str(form.lkat_11.value()))
    config2.set('Акты', 'lkat_12', str(form.lkat_12.value()))
    config2.set('Акты', 'lkat_13', str(form.lkat_13.value()))
    config2.set('Акты', 'lkat_14', str(form.lkat_14.value()))
    config2.set('Акты', 'lkat_15', str(form.lkat_15.value()))

    config2.set('Акты', 'ShifrRD_1', form.ShifrRD_1.toPlainText())
    config2.set('Акты', 'ShifrRD_2', form.ShifrRD_2.toPlainText())
    config2.set('Акты', 'ShifrRD_3', form.ShifrRD_3.toPlainText())
    config2.set('Акты', 'ShifrRD_4', form.ShifrRD_4.toPlainText())
    config2.set('Акты', 'ShifrRD_5', form.ShifrRD_5.toPlainText())
    config2.set('Акты', 'ShifrRD_6', form.ShifrRD_6.toPlainText())
    config2.set('Акты', 'ShifrRD_7', form.ShifrRD_7.toPlainText())
    config2.set('Акты', 'ShifrRD_8', form.ShifrRD_8.toPlainText())
    config2.set('Акты', 'ShifrRD_9', form.ShifrRD_9.toPlainText())
    config2.set('Акты', 'ShifrRD_10', form.ShifrRD_10.toPlainText())
    config2.set('Акты', 'ShifrRD_11', form.ShifrRD_11.toPlainText())
    config2.set('Акты', 'ShifrRD_12', form.ShifrRD_12.toPlainText())
    config2.set('Акты', 'ShifrRD_13', form.ShifrRD_13.toPlainText())
    config2.set('Акты', 'ShifrRD_14', form.ShifrRD_14.toPlainText())
    config2.set('Акты', 'ShifrRD_15', form.ShifrRD_15.toPlainText())

    with open(file, 'w+') as configfile2:
        config2.write(configfile2)


#     ini_form_cfg.setValue('ON_Bybit', int(form.ON_Bybit.isChecked()))
#     ini_form_cfg.setValue('Hedge', int(form.Hedge.isChecked()))
#     ini_form_cfg.setValue('leverage', int(form.leverage.value()))
#     ini_form_cfg.setValue('percent_margin', float(form.percent_margin.value()))
#     ini_form_cfg.setValue('fix_margin', int(form.fix_margin.value()))
#
#     ini_form_cfg.setValue('max_margin', int(form.max_margin.value()))
#     ini_form_cfg.setValue('panicsell', int(form.panicsell.value()))
#     ini_form_cfg.setValue('rb_set_percent', int(form.rb_set_percent.isChecked()))
#     ini_form_cfg.setValue('rb_set_margin', int(form.rb_set_margin.isChecked()))
#
#     ini_form_cfg.setValue('poluorder', int(form.poluorder.value()))
#     ini_form_cfg.setValue('LMT_1st', int(form.LMT_1st.value()))
#     ini_form_cfg.setValue('LMT_2nd', int(form.LMT_2nd.value()))
#
#     ini_form_cfg.setValue('TP_1st', int(form.TP_1st.value()))
#     ini_form_cfg.setValue('TP_2nd', int(form.TP_2nd.value()))
#
#     ini_form_cfg.setValue('VIP1', int(form.VIP1.isChecked()))
#     ini_form_cfg.setValue('VIP2', int(form.VIP2.isChecked()))
#     ini_form_cfg.setValue('VIP3', int(form.VIP3.isChecked()))
#     ini_form_cfg.setValue('VIP4', int(form.VIP4.isChecked()))
#     ini_form_cfg.setValue('VIP5', int(form.VIP5.isChecked()))
#     ini_form_cfg.setValue('VIP6', int(form.VIP6.isChecked()))
#     ini_form_cfg.setValue('VIP7', int(form.VIP7.isChecked()))
#     ini_form_cfg.setValue('no_vip', int(form.no_vip.isChecked()))
#     ini_form_cfg.setValue('test_ch', int(form.test_ch.isChecked()))
#
#     if not config.has_section('Telegram'):
#         config.add_section('Telegram')
#     if not config.has_section('Bybit'):
#         config.add_section('Bybit')
#         config.set('Bybit', 'endpoint', 'https://api.bybit.com')
#     if not config.has_section('Binance'):
#         config.add_section('Binance')
#     if not config.has_section('Criptonec'):
#         config.add_section('Criptonec')
#         config.set('Criptonec', 'id_vip_1', '-1001475114696')
#         config.set('Criptonec', 'id_vip_2', '-1001632167278')
#         config.set('Criptonec', 'id_vip_3', '-1001528138841')
#         config.set('Criptonec', 'id_vip_4', '-1001630776206')
#         config.set('Criptonec', 'id_vip_5', '-1001674027602')
#         config.set('Criptonec', 'id_vip_6', '-1001650167630')
#         config.set('Criptonec', 'id_vip_7', '-1001707100944')
#         config.set('Criptonec', 'indicator_by_cryptonec', '-1001266391544')
#     if not config.has_section('MY_CHANNEL'):
#         config.add_section('MY_CHANNEL')
#
#     if form.checkApi_Bybit.isChecked():
#         config.set('Bybit', 'api_key_bybit', form.API_KEY_Bybit.text())
#         config.set('Bybit', 'api_secret_bybit', form.API_SECRET_Bybit.text())
#
#     config.set('MY_CHANNEL', 'my_channel', form.MY_CHANNEL.text())
#     config.set('MY_CHANNEL', 'test_ch', form.MY_CHANNEL_2.text())
#
#     config.set('Telegram', 'api_token', form.api_token.text())
#     config.set('Telegram', 'api_id', form.api_id.text())
#     config.set('Telegram', 'api_hash', form.api_hash.text())
#     config.set('Telegram', 'session_string', form.session_string.text())
#     with open(file_config, 'w') as configfile:
#         config.write(configfile)
#     print('save complited')


def ini_form(file=None):
    try:
        if file != "":
            config = configparser.ConfigParser()
            config.read_file(open(file))

            # Папка объекта
            if settings.contains("objFolder"):
                objFolder = settings.value('objFolder')
            else:
                settings.setValue('objFolder', '')
                objFolder = ''

            if objFolder != '':
                window.statusBar().showMessage(objFolder)
            if objFolder == '':
                window.statusBar().showMessage('Папка не задана!!!')

            # Объект
            window.setWindowTitle(config.get('Объект', 'object'))
            form.object.setText(config.get('Объект', 'object'))
            form.msk.setText(config.get('Объект', 'msk'))
            form.naimobj.setText(config.get('Объект', 'naimobj'))
            form.uchastok.setText(config.get('Объект', 'uchastok'))
            form.kodstr.setText(config.get('Объект', 'kodstr'))
            form.adres.setText(config.get('Объект', 'adres'))
            # Заказчик
            form.zakazchik.setText(config.get('Заказчик', 'zakazchik'))
            # form.zakazchik2.setText(config.get('Заказчик', 'zakazchik2'))
            form.zakazchikrekviz.setText(config.get('Заказчик', 'zakazchikrekviz'))
            form.zakazchikadres.setText(config.get('Заказчик', 'zakazchikadres'))
            form.zakazchiksro.setText(config.get('Заказчик', 'zakazchiksro'))
            form.zakazchikdolzhn.setText(config.get('Заказчик', 'zakazchikdolzhn'))
            form.zakazchikfio.setText(config.get('Заказчик', 'zakazchikfio'))
            form.zakazchikprikaz.setText(config.get('Заказчик', 'zakazchikprikaz'))
            # Стройконтроль
            form.SKrekviz.setText(config.get('Стройконтроль', 'SKrekviz'))
            form.SKadres.setText(config.get('Стройконтроль', 'SKadres'))
            form.SKdolzhnost.setText(config.get('Стройконтроль', 'SKdolzhnost'))
            form.SKfio.setText(config.get('Стройконтроль', 'SKfio'))
            form.SKprikaz.setText(config.get('Стройконтроль', 'SKprikaz'))
            # form.SKreestr.setText(config.get('General', 'SKreestr'))
            # Генподрядчик
            form.genpodryadchik.setText(config.get('Генподрядчик', 'genpodryadchik'))
            form.genpodryadchikrekviz.setText(config.get('Генподрядчик', 'genpodryadchikrekviz'))
            form.genpodryadchikadres.setText(config.get('Генподрядчик', 'genpodryadchikadres'))
            form.genpodryadchiksro.setText(config.get('Генподрядчик', 'genpodryadchiksro'))
            form.genpodryadchikdolzhn.setText(config.get('Генподрядчик', 'genpodryadchikdolzhn'))
            form.genpodryadchikfio.setText(config.get('Генподрядчик', 'genpodryadchikfio'))
            form.genpodryadchikprikaz.setText(config.get('Генподрядчик', 'genpodryadchikprikaz'))
            form.genpodryadchikSKdolzhnost.setText(config.get('Генподрядчик', 'genpodryadchikSKdolzhnost'))
            form.genpodryadchikSKfio.setText(config.get('Генподрядчик', 'genpodryadchikSKfio'))
            form.genpodryadchikSKprikaz.setText(config.get('Генподрядчик', 'genpodryadchikSKprikaz'))
            form.genpodryadchikSKreestr.setText(config.get('Генподрядчик', 'genpodryadchikSKreestr'))
            # Субподрядчик
            form.stroitel.setText(config.get('Субподрядчик', 'stroitel'))
            form.stroiteldolzhn.setText(config.get('Субподрядчик', 'stroiteldolzhn'))
            form.stroitelfio.setText(config.get('Субподрядчик', 'stroitelfio'))
            form.stroitelprikaz.setText(config.get('Субподрядчик', 'stroitelprikaz'))
            # АН
            form.proekt.setText(config.get('АН', 'proekt'))
            form.proektrekviz.setText(config.get('АН', 'proektrekviz'))
            form.proektadres.setText(config.get('АН', 'proektadres'))
            form.proektsro.setText(config.get('АН', 'proektsro'))
            form.GIP.setText(config.get('АН', 'GIP'))
            form.proektdolzhn.setText(config.get('АН', 'proektdolzhn'))
            form.proektfio.setText(config.get('АН', 'proektfio'))
            form.proektprikaz.setText(config.get('АН', 'proektprikaz'))
            # ГРО
            form.GRO.setText(config.get('ГРО', 'GRO'))
            form.GROrekviz.setText(config.get('ГРО', 'GROrekviz'))
            form.GROadres.setText(config.get('ГРО', 'GROadres'))
            form.GROdolzhn.setText(config.get('ГРО', 'GROdolzhn'))
            form.GROfio.setText(config.get('ГРО', 'GROfio'))
            form.GROprikaz.setText(config.get('ГРО', 'GROprikaz'))
            # Акты
            form.nActOGS.setText(config.get('Акты', 'nActOGS'))
            form.nActOtvod.setText(config.get('Акты', 'nActOtvod'))
            form.allrp.setValue(int(config.get('Акты', 'allrp')))
            form.allnr.setValue(int(config.get('Акты', 'allnr')))
            form.l_shem_ogs.setValue(int(config.get('Акты', 'l_shem_ogs')))
            form.l_kat_ogs.setValue(int(config.get('Акты', 'l_kat_ogs')))
            form.ShifrGP.setText(config.get('Акты', 'ShifrGP'))
            form.tchk_otvod.setValue(int(config.get('Акты', 'tchk_otvod')))
            form.l_shem_otvod.setValue(int(config.get('Акты', 'l_shem_otvod')))
            form.l_kat_otvod.setValue(int(config.get('Акты', 'l_kat_otvod')))
            form.ShifrPPO.setText(config.get('Акты', 'ShifrPPO'))
            form.ActOs_1.setText(config.get('Акты', 'ActOs_1'))
            form.ActOs_2.setText(config.get('Акты', 'ActOs_2'))
            form.ActOs_3.setText(config.get('Акты', 'ActOs_3'))
            form.ActOs_4.setText(config.get('Акты', 'ActOs_4'))
            form.ActOs_5.setText(config.get('Акты', 'ActOs_5'))
            form.ActOs_6.setText(config.get('Акты', 'ActOs_6'))
            form.ActOs_7.setText(config.get('Акты', 'ActOs_7'))
            form.ActOs_8.setText(config.get('Акты', 'ActOs_8'))
            form.ActOs_9.setText(config.get('Акты', 'ActOs_9'))
            form.ActOs_10.setText(config.get('Акты', 'ActOs_10'))
            form.ActOs_11.setText(config.get('Акты', 'ActOs_11'))
            form.ActOs_12.setText(config.get('Акты', 'ActOs_12'))
            form.ActOs_13.setText(config.get('Акты', 'ActOs_13'))
            form.ActOs_14.setText(config.get('Акты', 'ActOs_14'))
            form.ActOs_15.setText(config.get('Акты', 'ActOs_15'))

            form.nActOs_1.setText(config.get('Акты', 'nActOs_1'))
            form.nActOs_2.setText(config.get('Акты', 'nActOs_2'))
            form.nActOs_3.setText(config.get('Акты', 'nActOs_3'))
            form.nActOs_4.setText(config.get('Акты', 'nActOs_4'))
            form.nActOs_5.setText(config.get('Акты', 'nActOs_5'))
            form.nActOs_6.setText(config.get('Акты', 'nActOs_6'))
            form.nActOs_7.setText(config.get('Акты', 'nActOs_7'))
            form.nActOs_8.setText(config.get('Акты', 'nActOs_8'))
            form.nActOs_9.setText(config.get('Акты', 'nActOs_9'))
            form.nActOs_10.setText(config.get('Акты', 'nActOs_10'))
            form.nActOs_11.setText(config.get('Акты', 'nActOs_11'))
            form.nActOs_12.setText(config.get('Акты', 'nActOs_12'))
            form.nActOs_13.setText(config.get('Акты', 'nActOs_13'))
            form.nActOs_14.setText(config.get('Акты', 'nActOs_14'))
            form.nActOs_15.setText(config.get('Акты', 'nActOs_15'))

            form.rp_1.setValue(int(config.get('Акты', 'rp_1')))
            form.rp_2.setValue(int(config.get('Акты', 'rp_2')))
            form.rp_3.setValue(int(config.get('Акты', 'rp_3')))
            form.rp_4.setValue(int(config.get('Акты', 'rp_4')))
            form.rp_5.setValue(int(config.get('Акты', 'rp_5')))
            form.rp_6.setValue(int(config.get('Акты', 'rp_6')))
            form.rp_7.setValue(int(config.get('Акты', 'rp_7')))
            form.rp_8.setValue(int(config.get('Акты', 'rp_8')))
            form.rp_9.setValue(int(config.get('Акты', 'rp_9')))
            form.rp_10.setValue(int(config.get('Акты', 'rp_10')))
            form.rp_11.setValue(int(config.get('Акты', 'rp_11')))
            form.rp_12.setValue(int(config.get('Акты', 'rp_12')))
            form.rp_13.setValue(int(config.get('Акты', 'rp_13')))
            form.rp_14.setValue(int(config.get('Акты', 'rp_14')))
            form.rp_15.setValue(int(config.get('Акты', 'rp_15')))

            form.nr_1.setValue(int(config.get('Акты', 'nr_1')))
            form.nr_2.setValue(int(config.get('Акты', 'nr_2')))
            form.nr_3.setValue(int(config.get('Акты', 'nr_3')))
            form.nr_4.setValue(int(config.get('Акты', 'nr_4')))
            form.nr_5.setValue(int(config.get('Акты', 'nr_5')))
            form.nr_6.setValue(int(config.get('Акты', 'nr_6')))
            form.nr_7.setValue(int(config.get('Акты', 'nr_7')))
            form.nr_8.setValue(int(config.get('Акты', 'nr_8')))
            form.nr_9.setValue(int(config.get('Акты', 'nr_9')))
            form.nr_10.setValue(int(config.get('Акты', 'nr_10')))
            form.nr_11.setValue(int(config.get('Акты', 'nr_11')))
            form.nr_12.setValue(int(config.get('Акты', 'nr_12')))
            form.nr_13.setValue(int(config.get('Акты', 'nr_13')))
            form.nr_14.setValue(int(config.get('Акты', 'nr_14')))
            form.nr_15.setValue(int(config.get('Акты', 'nr_15')))

            form.tos_1.setValue(int(config.get('Акты', 'tos_1')))
            form.tos_2.setValue(int(config.get('Акты', 'tos_2')))
            form.tos_3.setValue(int(config.get('Акты', 'tos_3')))
            form.tos_4.setValue(int(config.get('Акты', 'tos_4')))
            form.tos_5.setValue(int(config.get('Акты', 'tos_5')))
            form.tos_6.setValue(int(config.get('Акты', 'tos_6')))
            form.tos_7.setValue(int(config.get('Акты', 'tos_7')))
            form.tos_8.setValue(int(config.get('Акты', 'tos_8')))
            form.tos_9.setValue(int(config.get('Акты', 'tos_9')))
            form.tos_10.setValue(int(config.get('Акты', 'tos_10')))
            form.tos_11.setValue(int(config.get('Акты', 'tos_11')))
            form.tos_12.setValue(int(config.get('Акты', 'tos_12')))
            form.tos_13.setValue(int(config.get('Акты', 'tos_13')))
            form.tos_14.setValue(int(config.get('Акты', 'tos_14')))
            form.tos_15.setValue(int(config.get('Акты', 'tos_15')))

            form.lshem_1.setValue(int(config.get('Акты', 'lshem_1')))
            form.lshem_2.setValue(int(config.get('Акты', 'lshem_2')))
            form.lshem_3.setValue(int(config.get('Акты', 'lshem_3')))
            form.lshem_4.setValue(int(config.get('Акты', 'lshem_4')))
            form.lshem_5.setValue(int(config.get('Акты', 'lshem_5')))
            form.lshem_6.setValue(int(config.get('Акты', 'lshem_6')))
            form.lshem_7.setValue(int(config.get('Акты', 'lshem_7')))
            form.lshem_8.setValue(int(config.get('Акты', 'lshem_8')))
            form.lshem_9.setValue(int(config.get('Акты', 'lshem_9')))
            form.lshem_10.setValue(int(config.get('Акты', 'lshem_10')))
            form.lshem_11.setValue(int(config.get('Акты', 'lshem_11')))
            form.lshem_12.setValue(int(config.get('Акты', 'lshem_12')))
            form.lshem_13.setValue(int(config.get('Акты', 'lshem_13')))
            form.lshem_14.setValue(int(config.get('Акты', 'lshem_14')))
            form.lshem_15.setValue(int(config.get('Акты', 'lshem_15')))

            form.lkat_1.setValue(int(config.get('Акты', 'lkat_1')))
            form.lkat_2.setValue(int(config.get('Акты', 'lkat_2')))
            form.lkat_3.setValue(int(config.get('Акты', 'lkat_3')))
            form.lkat_4.setValue(int(config.get('Акты', 'lkat_4')))
            form.lkat_5.setValue(int(config.get('Акты', 'lkat_5')))
            form.lkat_6.setValue(int(config.get('Акты', 'lkat_6')))
            form.lkat_7.setValue(int(config.get('Акты', 'lkat_7')))
            form.lkat_8.setValue(int(config.get('Акты', 'lkat_8')))
            form.lkat_9.setValue(int(config.get('Акты', 'lkat_9')))
            form.lkat_10.setValue(int(config.get('Акты', 'lkat_10')))
            form.lkat_11.setValue(int(config.get('Акты', 'lkat_11')))
            form.lkat_12.setValue(int(config.get('Акты', 'lkat_12')))
            form.lkat_13.setValue(int(config.get('Акты', 'lkat_13')))
            form.lkat_14.setValue(int(config.get('Акты', 'lkat_14')))
            form.lkat_15.setValue(int(config.get('Акты', 'lkat_15')))

            form.ShifrRD_1.setText(config.get('Акты', 'ShifrRD_1'))
            form.ShifrRD_2.setText(config.get('Акты', 'ShifrRD_2'))
            form.ShifrRD_3.setText(config.get('Акты', 'ShifrRD_3'))
            form.ShifrRD_4.setText(config.get('Акты', 'ShifrRD_4'))
            form.ShifrRD_5.setText(config.get('Акты', 'ShifrRD_5'))
            form.ShifrRD_6.setText(config.get('Акты', 'ShifrRD_6'))
            form.ShifrRD_7.setText(config.get('Акты', 'ShifrRD_7'))
            form.ShifrRD_8.setText(config.get('Акты', 'ShifrRD_8'))
            form.ShifrRD_9.setText(config.get('Акты', 'ShifrRD_9'))
            form.ShifrRD_10.setText(config.get('Акты', 'ShifrRD_10'))
            form.ShifrRD_11.setText(config.get('Акты', 'ShifrRD_11'))
            form.ShifrRD_12.setText(config.get('Акты', 'ShifrRD_12'))
            form.ShifrRD_13.setText(config.get('Акты', 'ShifrRD_13'))
            form.ShifrRD_14.setText(config.get('Акты', 'ShifrRD_14'))
            form.ShifrRD_15.setText(config.get('Акты', 'ShifrRD_15'))

        # form.ON_Bybit.setChecked(bool(int(ini_form_cfg.value('ON_Bybit', 0))))
        # if form.ON_Bybit.isChecked():
        #     form.ON_Bybit.setText('ВКЛ')
        #     form.ON_Bybit.setStyleSheet("color: Green;")
        # else:
        #     form.ON_Bybit.setText('ВЫКЛ')
        #     form.ON_Bybit.setStyleSheet("color: Red;")
        # form.Hedge.setChecked(bool(int(ini_form_cfg.value('Hedge', 0))))
        # if form.Hedge.isChecked():
        #     form.Hedge.setText('Режим хэджирования включен')
        #     form.Hedge.setStyleSheet("color: Green;")
        # else:
        #     form.Hedge.setText('Установлен односторонний режим')
        #     form.Hedge.setStyleSheet("color: Red;")
        # form.leverage.setValue(int(ini_form_cfg.value('leverage')))
        # form.percent_margin.setValue(float(ini_form_cfg.value('percent_margin')))
        # form.fix_margin.setValue(int(ini_form_cfg.value('fix_margin')))
        # form.rb_set_percent.setChecked(bool(int(ini_form_cfg.value('rb_set_percent', 0))))
        # form.rb_set_margin.setChecked(bool(int(ini_form_cfg.value('rb_set_margin', 0))))
        # form.margin_Bybit.setText(strategy_config.value('margin'))
        #
        # form.max_margin.setValue(int(ini_form_cfg.value('max_margin')))
        # form.panicsell.setValue(int(ini_form_cfg.value('panicsell')))
        #
        # form.poluorder.setValue(int(ini_form_cfg.value('poluorder')))
        # form.LMT_1st.setValue(int(ini_form_cfg.value('LMT_1st')))
        # form.LMT_2nd.setValue(int(ini_form_cfg.value('LMT_2nd')))
        # #
        # form.TP_1st.setValue(int(ini_form_cfg.value('TP_1st')))
        # form.TP_2nd.setValue(int(ini_form_cfg.value('TP_2nd')))
        #
        # form.MY_CHANNEL.setText(config.get('MY_CHANNEL', 'my_channel'))
        # form.MY_CHANNEL_2.setText(config.get('MY_CHANNEL', 'test_ch'))
        #
        # form.VIP1.setChecked(bool(int(ini_form_cfg.value('VIP1', 0))))
        # if form.VIP1.isChecked():
        #     form.VIP1.setStyleSheet("color: Green;")
        # else:
        #     form.VIP1.setStyleSheet("color: Red;")
        # form.VIP2.setChecked(bool(int(ini_form_cfg.value('VIP2', 0))))
        # if form.VIP2.isChecked():
        #     form.VIP2.setStyleSheet("color: Green;")
        # else:
        #     form.VIP2.setStyleSheet("color: Red;")
        # form.VIP3.setChecked(bool(int(ini_form_cfg.value('VIP3', 0))))
        # if form.VIP3.isChecked():
        #     form.VIP3.setStyleSheet("color: Green;")
        # else:
        #     form.VIP3.setStyleSheet("color: Red;")
        # form.VIP4.setChecked(bool(int(ini_form_cfg.value('VIP4', 0))))
        # if form.VIP4.isChecked():
        #     form.VIP4.setStyleSheet("color: Green;")
        # else:
        #     form.VIP4.setStyleSheet("color: Red;")
        # form.VIP5.setChecked(bool(int(ini_form_cfg.value('VIP5', 0))))
        # if form.VIP5.isChecked():
        #     form.VIP5.setStyleSheet("color: Green;")
        # else:
        #     form.VIP5.setStyleSheet("color: Red;")
        # form.VIP6.setChecked(bool(int(ini_form_cfg.value('VIP6', 0))))
        # if form.VIP6.isChecked():
        #     form.VIP6.setStyleSheet("color: Green;")
        # else:
        #     form.VIP6.setStyleSheet("color: Red;")
        # form.VIP7.setChecked(bool(int(ini_form_cfg.value('VIP7', 0))))
        # if form.VIP7.isChecked():
        #     form.VIP7.setStyleSheet("color: Green;")
        # else:
        #     form.VIP7.setStyleSheet("color: Red;")
        # form.no_vip.setChecked(bool(int(ini_form_cfg.value('no_vip', 0))))
        # if form.no_vip.isChecked():
        #     form.no_vip.setStyleSheet("color: Green;")
        # else:
        #     form.no_vip.setStyleSheet("color: Red;")
        # form.test_ch.setChecked(bool(int(ini_form_cfg.value('test_ch', 0))))
        # if form.test_ch.isChecked():
        #     form.test_ch.setStyleSheet("color: Green;")
        # else:
        #     form.test_ch.setStyleSheet("color: Red;")
        # form.api_token.setText(config.get('Telegram', 'api_token'))
        # form.api_id.setText(config.get('Telegram', 'api_id'))
        # form.api_hash.setText(config.get('Telegram', 'api_hash'))
        # form.session_string.setText(config.get('Telegram', 'session_string'))
    except:
        pass


# def change_form(mode):
#     if mode == 'setBybit':
#         config_bybit.setValue("ON_Bybit", int(form.ON_Bybit.isChecked()))
#         if form.ON_Bybit.isChecked():  # BYBIT
#             form.ON_Bybit.setText('ВКЛ')
#             form.ON_Bybit.setStyleSheet("color: Green;")
#         else:
#             form.ON_Bybit.setText('ВЫКЛ')
#             form.ON_Bybit.setStyleSheet("color: Red;")
#     if mode == 'Hedge':
#         if form.Hedge.isChecked():  # BYBIT
#             mode_bybit = 'BothSide'
#             strategy_config.setValue("Hedge", mode_bybit)
#             form.Hedge.setText('Режим хэджирования включен')
#             form.Hedge.setStyleSheet("color: Green;")
#         else:
#             mode_bybit = 'MergedSingle'
#             strategy_config.setValue("Hedge", mode_bybit)
#             form.Hedge.setText('Установлен односторонний режим')
#             form.Hedge.setStyleSheet("color: Red;")
#         if form.checkApi_Bybit.isChecked():
#             if Bybit.position_mode_switch(mode_bybit):
#                 form.statusBar.showMessage(f'Установлен {mode_bybit} режим')
#     if mode == 'leverage':
#         leverage = int(form.leverage.value())
#         strategy_config.setValue("leverage", leverage)
#     if mode == 'fix_margin':
#         fix_margin = int(form.fix_margin.value())
#         if fix_margin != 0:
#             form.rb_set_margin.setChecked(True)
#             percent_margin = 0
#             margin = round(fix_margin)
#             strategy_config.setValue("percent_margin", percent_margin)
#             strategy_config.setValue("margin", margin)
#             form.percent_margin.setValue(percent_margin)
#             form.margin_Bybit.setText(str(margin))
#         strategy_config.setValue("fix_margin", fix_margin)
#         set_min_margin()
#     if mode == 'percent_margin':
#         percent_margin = float(form.percent_margin.value())
#         if percent_margin != 0:
#             form.rb_set_percent.setChecked(True)
#             strategy_config.setValue("percent_margin", percent_margin)
#             fix_margin = 0
#             strategy_config.setValue("fix_margin", fix_margin)
#             margin = Utils.set_margin()
#             form.fix_margin.setValue(fix_margin)
#             form.margin_Bybit.setText(str(margin))
#         strategy_config.setValue("percent_margin", percent_margin)
#         set_min_margin()
#     if mode == 'max_margin':
#         max_margin = int(form.max_margin.value())
#         strategy_config.setValue("maxmargin", max_margin)
#     if mode == 'panicsell':
#         panicsell = int(form.panicsell.value())
#         strategy_config.setValue("panicsell", panicsell)
#     if mode == 'TP1':
#         TP_1st = int(form.TP_1st.value())
#         strategy_config.setValue("TP_1st", TP_1st)
#         set_min_margin()
#     if mode == 'TP2':
#         TP_2nd = int(form.TP_2nd.value())
#         strategy_config.setValue("TP_2nd", TP_2nd)
#         set_min_margin()
#     if mode == 'LMT':
#         poluorder = int(form.poluorder.value())
#         strategy_config.setValue("poluorder", poluorder)
#     if mode == 'LMT1':
#         LMT_1st = int(form.LMT_1st.value())
#         # form.LMT_1st.setMaximum(LMT_1stmax)
#         strategy_config.setValue("LMT_1st", LMT_1st)
#     if mode == 'LMT2':
#         LMT_2nd = int(form.LMT_2nd.value())
#         strategy_config.setValue("LMT_2nd", LMT_2nd)
#     if mode == 'MY_CHANNEL':
#         try:
#             my = form.MY_CHANNEL.text()
#             m = [int(s) for s in re.findall(r'-?\d+\.?\d*', my)][0]
#             # tst = form.MY_CHANNEL_2.text()
#             # t = [int(x) for x in re.findall(r'-?\d+\.?\d*', tst)][0]
#             config.set('MY_CHANNEL', 'my_channel', str(m))
#             # config.set('MY_CHANNEL', 'test_ch', str(t))
#             with open(file_config, 'w') as configfile:
#                 config.write(configfile)
#         except:
#             form.statusBar.showMessage(f'неверный формат id канала')
#     if mode == 'Telega':
#         api_token = str(form.api_token.text())
#         api_id = str(form.api_id.text())
#         api_hash = str(form.api_hash.text())
#         session_string = str(form.session_string.text())
#         config.set('Telegram', 'api_token', api_token)
#         config.set('Telegram', 'api_id', api_id)
#         config.set('Telegram', 'api_hash', api_hash)
#         config.set('Telegram', 'session_string', session_string)
#         with open(file_config, 'w') as configfile:
#             config.write(configfile)
#     if mode == 'VIP1':
#         if form.VIP1.isChecked():  # BYBIT
#             form.VIP1.setStyleSheet("color: Green;")
#         else:
#             form.VIP1.setStyleSheet("color: Red;")
#         strategy_config.setValue("VIP1", int(form.VIP1.isChecked()))
#         Utils.add_channel()
#     if mode == 'VIP2':
#         if form.VIP2.isChecked():  # BYBIT
#             form.VIP2.setStyleSheet("color: Green;")
#         else:
#             form.VIP2.setStyleSheet("color: Red;")
#         strategy_config.setValue("VIP2", int(form.VIP2.isChecked()))
#         Utils.add_channel()
#     if mode == 'VIP3':
#         if form.VIP3.isChecked():  # BYBIT
#             form.VIP3.setStyleSheet("color: Green;")
#         else:
#             form.VIP3.setStyleSheet("color: Red;")
#         strategy_config.setValue("VIP3", int(form.VIP3.isChecked()))
#         Utils.add_channel()
#     if mode == 'VIP4':
#         if form.VIP4.isChecked():  # BYBIT
#             form.VIP4.setStyleSheet("color: Green;")
#         else:
#             form.VIP4.setStyleSheet("color: Red;")
#         strategy_config.setValue("VIP4", int(form.VIP4.isChecked()))
#         Utils.add_channel()
#     if mode == 'VIP5':
#         if form.VIP5.isChecked():  # BYBIT
#             form.VIP5.setStyleSheet("color: Green;")
#         else:
#             form.VIP5.setStyleSheet("color: Red;")
#         strategy_config.setValue("VIP5", int(form.VIP5.isChecked()))
#         Utils.add_channel()
#     if mode == 'VIP6':
#         if form.VIP6.isChecked():  # BYBIT
#             form.VIP6.setStyleSheet("color: Green;")
#         else:
#             form.VIP6.setStyleSheet("color: Red;")
#         strategy_config.setValue("VIP6", int(form.VIP6.isChecked()))
#         Utils.add_channel()
#     if mode == 'VIP7':
#         if form.VIP7.isChecked():  # BYBIT
#             form.VIP7.setStyleSheet("color: Green;")
#         else:
#             form.VIP7.setStyleSheet("color: Red;")
#         strategy_config.setValue("VIP7", int(form.VIP7.isChecked()))
#         Utils.add_channel()
#     if mode == 'no_vip':
#         if form.no_vip.isChecked():  # BYBIT
#             form.no_vip.setStyleSheet("color: Green;")
#         else:
#             form.no_vip.setStyleSheet("color: Red;")
#         strategy_config.setValue("no_vip", int(form.no_vip.isChecked()))
#         Utils.add_channel()
#     if mode == 'test_ch':
#         if form.test_ch.isChecked():  # BYBIT
#             form.test_ch.setStyleSheet("color: Green;")
#         else:
#             form.test_ch.setStyleSheet("color: Red;")
#         strategy_config.setValue("test_ch", int(form.test_ch.isChecked()))
#         tst = form.MY_CHANNEL_2.text()
#         t = [int(x) for x in re.findall(r'-?\d+\.?\d*', tst)][0]
#         config.set('MY_CHANNEL', 'test_ch', str(t))
#         with open(file_config, 'w') as configfile:
#             config.write(configfile)
#         Utils.add_channel()


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


def save111():
    objFolder = settings.value('objFolder')
    if objFolder != '':
        file = objFolder + '/Карточка объекта - ' + form.object.toPlainText() + '.gro'
    else:
        nfile = dirname(last_form) + '/Карточка объекта - ' + form.object.toPlainText() + '.gro'
        file = \
            QFileDialog().getSaveFileName(window, 'Выберите путь для карточки объекта', nfile, filter="*.gro")[0]
        objFolder = dirname(file)
        settings.setValue("objFolder", objFolder)
    if file != '':
    #     my_file = open(file, "w+")
    #     my_file.close()
    #     save_form(file)
        print(exists(file))
        shutil.copyfile('.\Shablon\!промежуточный.docx', f'{objFolder}\copyz.docx')


if __name__ == '__main__':
    Form, Window = uic.loadUiType("./form/GRO.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)

    window.show()
    # ini_form(last_form)
    openini('last')

    # форма
    form.pushButtonOpenini.clicked.connect(lambda: openini('open'))
    form.pushButtonOpenCopy.clicked.connect(lambda: openini('copy'))
    form.pushButtonClear.clicked.connect(lambda: ini_form(defoult_form))
    form.pushButtonSave.clicked.connect(save111)
    form.pushButtonClose.clicked.connect(window.close)

    #
    # # Установка плечей
    # form.leverage.valueChanged.connect(lambda: change_form('leverage'))
    # form.set_Leverage_Bybit.clicked.connect(set_leverage_bybit)
    # # Установка маржи
    # form.fix_margin.valueChanged.connect(lambda: change_form('fix_margin'))
    # # Установка маржи %
    # form.percent_margin.valueChanged.connect(lambda: change_form('percent_margin'))
    # form.refresh_rec_ch.clicked.connect(lambda: change_form('MY_CHANNEL'))
    # # change_vip
    # form.VIP1.stateChanged.connect(
    #     lambda: change_form('VIP1'))
    # form.VIP2.stateChanged.connect(
    #     lambda: change_form('VIP2'))
    # form.VIP3.stateChanged.connect(
    #     lambda: change_form('VIP3'))
    # form.VIP4.stateChanged.connect(
    #     lambda: change_form('VIP4'))
    # form.VIP5.stateChanged.connect(
    #     lambda: change_form('VIP5'))
    # form.VIP6.stateChanged.connect(
    #     lambda: change_form('VIP6'))
    # form.VIP7.stateChanged.connect(
    #     lambda: change_form('VIP7'))
    # form.no_vip.stateChanged.connect(
    #     lambda: change_form('no_vip'))
    # form.test_ch.stateChanged.connect(
    #     lambda: change_form('test_ch'))
    # form.max_margin.valueChanged.connect(
    #     lambda: change_form('max_margin'))  # Установка максимальной маржи в открытых позах
    # form.panicsell.valueChanged.connect(
    #     lambda: change_form('panicsell'))  # Установка максимальной просадки "ПАНИКСЕЛЛ"
    # form.TP_1st.valueChanged.connect(
    #     lambda: change_form('TP1'))  # Установка первого тейка
    # form.TP_2nd.valueChanged.connect(
    #     lambda: change_form('TP2'))  # Установка второго тейка
    # form.poluorder.valueChanged.connect(
    #     lambda: change_form('LMT'))  # Установка первого размера ордера
    # form.LMT_1st.valueChanged.connect(
    #     lambda: change_form('LMT1'))  # Установка первого добора позиции
    # form.LMT_2nd.valueChanged.connect(
    #     lambda: change_form('LMT2'))  # Установка первого добора позиции
    # form.apply_telega.clicked.connect(
    #     lambda: change_form('Telega'))  # Установка ключей телеги
    app.exec()
    # save_form()
