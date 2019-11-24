# -*- coding:utf-8 -*-
"""
Created on 2019/11/23 22:38
@author: Leo
@file:test_gj.py
@desc:
"""
import tempfile

import pywinauto

from easytrader import helpers


def startup_app(exe_path='C:\\app\\全能行证券交易终端\\xiadan.exe'):
    app=pywinauto.application.Application()
    app.start(exe_path)
    # app.top_window().Edit1.key_
def verify_code(app):
    edit3 = app.top_window().window(control_id=0x3eb)
    c = app.top_window().window(control_id=0x5db).click()
    import time
    time.sleep(0.2)
    file_path = tempfile.mktemp() + ".jpg"
    c.capture_as_image().save(file_path)
    time.sleep(0.2)
    vcode = helpers.recognize_verify_code(file_path, "gj_client")
    return vcode

