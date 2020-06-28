# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:26:51 2020

@author: rlawl
"""

import pyautogui as pag
import harr as h

#print(pag.confirm('{0}{1}'.format(mX,mY),buttons=['go','stop']))
#print('{0}{1}'.format(screenWidth,screenHeight))

#print("click",pag.click(1,1))

key = pag.confirm('select',
            buttons=['start','cancel','mute'])
changeTab = pag.prompt('Input Task Tab Number (change Tab)')
originTab = pag.prompt('Input origin Tab Number (return Tab)')



while True:
    screenWidth, screenHeight = pag.size()
    mX, mY = pag.position()
    
    if key=='cancel':
        break
    elif key == 'a':
        print(pag.alert('{0}{1}'.format(mX, mY)))
        
    elif key == 'start':
        mX, mY = pag.position()
        h.bodyDetect(changeTab, originTab)
        break;
        #pag.hotkey(['win','2'])
            
    elif key == 's':
        pag.screenshot('a.png')
        
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