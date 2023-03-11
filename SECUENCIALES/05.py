# 1 KB = 1024 BYTES
# 1 MB = 1024 KB
# 1 GB =1024 MB
import os
os.system("cls")

gigabytes= int (input("gigabytes: "))

megabytes = gigabytes * 1024
kilobytes = megabytes * 1024
bytes = kilobytes * 1024

print( f"megabytes = {megabytes}")
print( f"kilobytes = {kilobytes}")
print( f"bytes = {bytes}")
print()

