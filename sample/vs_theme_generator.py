# import curses
import os
import re
import json

class FileManager:
    def __init__(self):
        self.sourcePath = input("Insert path to theme .json file: ")
        self.openSourceFile()
        self.createGeneratedFile()
        self.getStyles()
        self.generateFile()

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
        with open(self.sourceFolder + "/styles.json") as stylesFile:
            self.styles = json.load(stylesFile)
        
    def updateFileWithStyles(self, file):
        for name, value in self.styles.items():
            file = file.replace(name, value)
        return file

    def generateFile(self):
        self.openSourceFile()
        self.getStyles()

        print("Opening generated file!")
        generatedFile = open(self.generatedURI, "w")

        generatedFile.write(self.updateFileWithStyles(self.sourceFile))

        generatedFile.close()
        print("File generated!")
        print("")

    def createDir(self, path):
        # create directory if it doesnt exist
        if not os.path.exists(path):
            os.makedirs(path)

fileManager = FileManager()

try:
    while True:
        input("Hit enter to refresh!")

        fileManager.generateFile()

except KeyboardInterrupt:
    print('interrupted!')