'''
This file is to test that the keysight libraries
 have been installed correctly.
'''

import pyvisa

print("check 1")

rm = pyvisa.ResourceManager() # use the default backend configs

print ("check 2")

print(rm.list_resources()) # print the resources available

print ("check 3")