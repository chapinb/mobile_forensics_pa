#!/usr/bin/env python

from physical import *						
import urllib2
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import MessageBox

def find_OUI (MAC):
	url = 'http://api.macvendors.com/'
	try:
		vendor = urllib2.urlopen(url + MAC).read()
	except urllib2.HTTPError:
		vendor = 'No Vendor Found'
	return vendor


if __name__ == "<module>" or __name__ == "__main__":
	count = 0
	for device in ds.Models[BluetoothDevice]:
		device.Info.Value = find_OUI(str(device.MACAddress))
		print count
		count += 1
	MessageBox.Show('Successfuly added ' + str(count) + ' items to the DataStore.', 'Success!')
