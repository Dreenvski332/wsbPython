from tkinter import *
from packages.calculatePrice import calculatePrice

# Create window object
app = Tk()
componentsList = []
customTMPmem = []
fixedTMPmem = []

def addToList():
    # adds to the list
    componentsList.append(componentEntryName.get()) # adds component to the list
    componentsListToDisplay = '\n'.join(componentsList) # adds new line between components on display

    global componentEntryPriceInt
    componentEntryPriceInt = int(componentEntryPrice.get())# converts string to int

    componentsPrintList.delete('1.0', END) # clears the displayed list
    componentsPrintList.insert(END, componentsListToDisplay) # displays list in textbox

    # adds to dictionary (important when calculation price)
    componentsPrintedInDictionary.update({componentEntryName.get(): componentEntryPriceInt})

    # clear both entries
    componentEntryName.delete(0, 'end')
    componentEntryPrice.delete(0, 'end')

    customTMPmem.append(componentEntryPriceInt)

def selectComponent(event):
    # select component from listbox
    widget = event.widget
    selection=widget.curselection()
    global picked
    picked = widget.get(selection[0])
    
    # add it to dictionary bellow
    componentsList.append(picked)
    componentsListToDisplay = '\n'.join(componentsList) #adds new line between components on display
    componentsPrintList.delete('1.0', END)
    componentsPrintList.insert(END, componentsListToDisplay)

    if not componentEntryPrice.get():
        global finalCustom
        finalCustom = 0
    else:
        finalCustom = componentEntryPriceInt

def clearList():
    componentsPrintList.delete('1.0', END)
    finalPriceNumber.delete('1.0', END)
    fixedTMPmem.clear()
    customTMPmem.clear()
    componentsList.clear()

def saveListToFile():
    file=open('twojaKombinacja.txt', 'w')
    for element in componentsList:
        file.write(element+'\n')
    file.write('\n'+ 'Final price: ')
    file.write(str(sumFinal))

def loadSavedList():
    file = open('twojaKombinacja.txt', 'r')
    fileContent = file.read()
    file.close()
    componentsPrintList.delete('1.0', END)
    componentsPrintList.insert(END, fileContent)

def displaySum():
    calculatePrice()
    global sumFinal
    sumFinal = sum(fixedTMPmem) + sum(customTMPmem)

    finalPriceNumber.delete('1.0', END) # clears the displayed list
    finalPriceNumber.insert(END, sumFinal) # displays list in textbox
    print(fixedTMPmem)
    print(customTMPmem)

    fixedTMPmem.clear()

# Stuff really
nameButtonText = StringVar()
buttonLabelName = Label(app, text='Subscription name:', font=('bold', 10), pady=2, padx = 12); buttonLabelName.grid(row=1, column=0, sticky=W)
componentEntryName = Entry(app, textvariable=nameButtonText); componentEntryName.grid(row=1, column=0)

# More stuff
priceButtonInt = StringVar()
buttonLabelPrice = Label(app, text='Subscription price:', font=('bold', 10), pady=2, padx = 12); buttonLabelPrice.grid(row=2, column=0, sticky=W)
componentEntryPrice = Entry(app, textvariable=priceButtonInt); componentEntryPrice.grid(row=2, column=0)

# Buttons
addToListButton = Button(app, text='Add to list', width=15, command=addToList); addToListButton.grid(row=3, column=0, pady=5)
clearListButton = Button(app, text='Clear list', width=15, command=clearList); clearListButton.grid(row=4, column=0, pady=5)
saveListButton = Button(app, text='Save to .txt', width=15, command=saveListToFile); saveListButton.grid(row=5, column=0, pady=(20, 5))
loadListButton = Button(app, text='Load from .txt', width=15, command=loadSavedList); loadListButton.grid(row=6, column=0, pady=5)
addUpButton = Button(app, text='Sum it up', width=15, command=displaySum); addUpButton.grid(row=11, column=0, pady=5)

# Lists
componentsPrintList = Text(app, height=10, width=60, border=2); componentsPrintList.grid(row=7, column=0, pady=10, padx=10)
componentsListToChooseFrom = Listbox(app, height=10, width=80, border=0); componentsListToChooseFrom.grid(row=0, column=0, pady=10, padx=10)
componentsListToChooseFrom.bind('<<ListboxSelect>>', selectComponent)

# Even more stuff!
finalPriceLabel = Label(app, text='Final price:', font=('bold', 10), pady=2, padx = 12); finalPriceLabel.grid(row=10, column=0, sticky=W)
finalPriceNumber = Text(app, height=1, width=8, border=2); finalPriceNumber.grid(row=10, column=0, pady=20, padx=20)

# Add components to Dictionary
componentsPrintedInDictionary = {
    'Netflix': 60, 
    'HBO MAX':35, 
    'Amazon Prime':30, 
    'Hulu':25, 
    'Disney+':29, 
    'YouTube premium':35, 
    'Spotify premium':30, 
    'Tidal':25, 
    'Discord Nitro':20
    }
for components in componentsPrintedInDictionary:
    componentsListToChooseFrom.insert(END,components)


app.title('Subscription manager')
app.geometry('505x690')

# Start program
app.mainloop()