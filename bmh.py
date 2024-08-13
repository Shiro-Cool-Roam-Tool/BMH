import os, sys
try:
    __import__("BMH").approveme()
except Exception as e:
    exit(str(e))
