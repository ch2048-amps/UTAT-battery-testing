'''
This file is to test the installation of pyVISA. 

If the output requests IVI binary or pyvisa-py installation, then pyVISA is 
installed backend configuration files (including the defaults) are not installed.

Move onto downloading the keysight libraries.
'''

import pyvisa

print("check 1")

rm = pyvisa.ResourceManager() # use the default backend configs

# print ("check 2")

# print(rm.list_resources()) # print the resources available

# print ("check 3")