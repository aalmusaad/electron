#!/usr/bin/env python

import atexit
import os
import subprocess
import sys

from dbusmock import DBusTestCase

from lib.config import is_verbose_mode

def stop():
    print('In dbus_mock stop')
    DBusTestCase.stop_dbus(DBusTestCase.system_bus_pid)
    print('In dbus_mock stop, stopped system bus')
    DBusTestCase.stop_dbus(DBusTestCase.session_bus_pid)
    print('In dbus_mock stop, stopped session bus')

def start():
    log = sys.stdout
    print('In dbus_mock start')
    DBusTestCase.start_system_bus()
    print('In dbus_mock start, started system bus')
    DBusTestCase.spawn_server_template('logind', None, log)
    print('In dbus_mock start, spawned logind')
    DBusTestCase.start_session_bus()
    print('In dbus_mock start, started session bus')
    DBusTestCase.spawn_server_template('notification_daemon', None, log)
    print('In dbus_mock start, spawned notification_daemon')

if __name__ == '__main__':
    start()
    try:
        print 'About to call {}'.format(sys.argv)
        subprocess.check_call(sys.argv[1:])
        print 'Done calling {}'.format(sys.argv)
    finally:
        stop()
