import tkinter as tk
import json
from pathlib import Path
from random import randint

thisFolderPath = Path(__file__).absolute().parent
parentFolderPath = thisFolderPath.parent
saveFilePath = Path(thisFolderPath / "config.json")

class App:
    def __init__(self):
        global cAction
        global cWindow
        cAction = Action()
        cWindow = Window()
        ##
        cWindow.nameCreation()
        cWindow.flagCreation()
        cWindow.descriptionCreation()
        ##
        cWindow.init_mainloop()
        

class Window:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gender Creator")
        self.window.geometry("350x350")
        self.master = self.window
        appIcon = tk.PhotoImage(file="icon.png")
        self.window.iconphoto(False, appIcon)

    def init_mainloop(self):
        self.window.mainloop()

#--------------------------------------
    def nameCreation(self):
        nameFrame = tk.Frame(self.window)
        self.nameString = tk.StringVar()
        tk.Label(text="My totally new gender is:").pack()
        tk.Entry(nameFrame, textvariable = self.nameString).pack()
        tk.Button(nameFrame, text = "Random", command =self.nameSubmit).pack()
        nameFrame.pack()

    def nameSubmit(self):
        self.nameString.set(cAction.createGenderName())  
#--------------------------------------
    def generateFlag(self):
        self.flagColors = [str(cAction.randomHexadecimal()),str(cAction.randomHexadecimal()),'''str(cAction.randomHexadecimal())'''] #Third color disabled
        self.flagColorsPack = ["#ff0066", "#3366ff", "#00ffff", "#00ff00", "#00ff00", "#333300", "#663300", "#ffffff"]
         
        self.flagParts = []
        lastDecision = 0
        exceptionHappened = 1
        while exceptionHappened:
            try:    
                for i in range(5):
                    randomNumber = randint(0,1)
                    while randomNumber == lastDecision:
                        randomNumber = randint(0,1)          
                    lastDecision = randomNumber
                    rectangleColor = self.flagColors[randomNumber]
                    self.flagParts.append(self.flag.create_rectangle(10,10+i*10,100,20+i*10, fill=rectangleColor, outline=rectangleColor))
                exceptionHappened = 0

            except:
                self.flagColors = [str(cAction.randomHexadecimal()),str(cAction.randomHexadecimal()),str(cAction.randomHexadecimal())]

    def flagCreation(self):
        self.flagCreationFrame = tk.Frame(self.window)
        
        self.flag = tk.Canvas(self.flagCreationFrame, width = 100, height= 100)
        self.flag.pack()
        
        self.generateFlag()

        tk.Button(self.flagCreationFrame, text="Generate new flag", command=self.generateFlag).pack()

        self.flagCreationFrame.pack(fill="both")
#--------------------------------------
    def descriptionCreation(self):
        self.descriptionFrame = tk.Frame(self.window)
        tk.Label(self.descriptionFrame, text="Description").pack()
        descriptionString=cAction.randomDescriptions()
        textField = tk.Text(self.descriptionFrame, height = 5, width = 52)
        textField.insert(tk.END, descriptionString)
        textField.pack()
        self.descriptionFrame.pack()

class Action:

    def __init__(self):
        self.loadFromLocal(saveFilePath)

    def loadFromLocal(self, path):
        with open(path, 'r') as jsonFile:
            self.data = json.load(jsonFile)
 
        self.prefixes = self.data["prefix"]
        self.suffixes = self.data["suffix"]
        self.descriptions = self.data["description"]
        self.dataArray = [self.prefixes, self.suffixes]

    def createGenderName(self):
        genderName = ""
        
        prefixCount = len(self.prefixes)-1
        suffixCount = len(self.suffixes)-1
        togetherCount = [prefixCount, suffixCount]
        for i in range(2):
            coef = randint(0, togetherCount[i])
            genderName += self.dataArray[i][coef]

        return genderName

    def randomDescriptions(self):
        descCount = len(self.descriptions)-1
        descriptionIndex = randint(0,descCount)
        description = self.descriptions[descriptionIndex]
        return description


    def randomHexadecimal(self):

        theNumber = randint(0,16777215)
        hex_number = "#" + str(hex(theNumber))[2:]
        return hex_number

cApp = App()