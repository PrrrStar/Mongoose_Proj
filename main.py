# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:26:51 2020

@author: rlawl
"""

import pyautogui as pag
import lbpDetector as lbp

#print(pag.confirm('{0}{1}'.format(mX,mY),buttons=['go','stop']))
#print('{0}{1}'.format(screenWidth,screenHeight))

#print("click",pag.click(1,1))

key = pag.confirm('select',
            buttons=['Start','Quit'])



while True:
    screenWidth, screenHeight = pag.size()
    mX, mY = pag.position()
    mute = False
    
    if key=='Quit':
        break
       
    elif key == 'Start':
        cascade = pag.confirm('select cascade method',
                      buttons = ['lbpcascade','haarcascade'])
        changeTab = pag.prompt('Input Task Tab Number (change Tab)')
        originTab = pag.prompt('Input origin Tab Number (return Tab)')
        if pag.confirm('Select Mute Mode\nWhen people detect, do you want to change Mute On?',
                       buttons = ['Yes', 'No']) == 'Yes':
            mute = True
            pag.alert('Mute Mode ON!!\nPlease Change your state, Volume On')
        print("Mute Mode = ",mute)
        lbp.bodyDetect(cascade, changeTab, originTab, mute)
        break;
        #pag.hotkey(['win','2'])
            
        
    else:
        print('wrong Key')
        pass
        
'''
while  True:    
    print('{0}{1}'.format(mX, mY))
'''

    
    

#pag.moveTo(300,100,1)


#pag.hotkey('win','2')


#pag.hotkey('volumemute')