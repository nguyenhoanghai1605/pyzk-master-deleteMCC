# -*- coding: utf-8 -*-
import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK


conn = None
#zk = ZK('192.168.18.101', port=4370)
zk = ZK('192.168.18.101', port=4370)
try:
    conn = zk.connect()
    users = [1000, 10001]
    for user in users:
        #conn.delete_user(uid=10000)
        #print ('  User  ID   : {}'.format(user.user_id))
        conn.delete_user(user_id=user)
        conn.test_voice()
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()