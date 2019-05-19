import ctypes
import os

lpBuffer = ctypes.create_string_buffer(78)
ctypes.windll.kernel32.GetLogicalDriveStringsA(ctypes.sizeof(lpBuffer), lpBuffer)
vol = lpBuffer.raw.split('\x00')
for i in vol:
    print i