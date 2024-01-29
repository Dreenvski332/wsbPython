from main import *

def calculatePrice():
    if 'Netflix' in componentsList:
        fixedTMPmem.append(60)
    if 'HBO MAX' in componentsList:
        fixedTMPmem.append(35)
    if 'Amazon Prime' in componentsList:
        fixedTMPmem.append(30)
    if 'Hulu' in componentsList:
        fixedTMPmem.append(25)
    if 'Disney+' in componentsList:
        fixedTMPmem.append(29)
    if 'YouTube premium' in componentsList:
        fixedTMPmem.append(35)
    if 'Spotify premium' in componentsList:
        fixedTMPmem.append(30)
    if 'Tidal' in componentsList:
        fixedTMPmem.append(25)
    if 'Discord Nitro' in componentsList:
        fixedTMPmem.append(20)