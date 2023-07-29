import ppadb
from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5307)
devices = adb.devices()

print(devices)
