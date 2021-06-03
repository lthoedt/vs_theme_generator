# import curses
import os
import re
import json
from pynput import keyboard

loop = False

class FileManager:
    def __init__(self):
        self.sourcePath = input("Insert path to theme .json file: ")
        self.openSourceFile()
        self.createGeneratedFile()
        self.getStyles()
        loop = True
    
    def openSourceFile(self):
        self.sourceFile = open(self.sourcePath).read();

    def createGeneratedFile(self):
        # extract filename
        self.sourceFileName = re.search(r"[^/\\&\?]+\.\w{3,4}(?=([\?&].*$|$))", self.sourcePath).group(0)
        # source folder
        self.sourceFolder = self.sourcePath.replace(self.sourceFileName, "")

        # generated source folder
        self.generatedDir = self.sourceFolder + "generated/"
        # generated file URI
        self.generatedURI = self.generatedDir + self.sourceFileName
        
        # create generated root folder
        self.createDir(self.generatedDir)

    def getStyles(self):
        with open(self.sourceFolder + "/styles/" + self.sourceFileName) as stylesFile:
            self.styles = json.load(stylesFile)
        
    def updateFileWithStyles(self, file):
        for name, value in self.styles.items():
            file = file.replace(name, value)
        return file

    def generateFile(self):
        print("Opening generated file!")
        generatedFile = open(self.generatedURI, "w")

        generatedFile.write(self.updateFileWithStyles(self.sourceFile))

        generatedFile.close()
        print("File generated!")

    def createDir(self, path):
        # create directory if it doesnt exist
        if not os.path.exists(path):
            os.makedirs(path)

fileManager = FileManager()

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# if __name__ == '__main__':
#     try:
#         # while loop:
#         #     key = window.get_wch()

#         #     print(key);

#         #     # if key == ' ' or key == 'r':
#         #     #     print("ce")
#         #     #     fileManager.generateFile()
                
#         #     # if key == 'q' or key == 'c':
#         #     #     break
#         #     curses.flushinp()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)