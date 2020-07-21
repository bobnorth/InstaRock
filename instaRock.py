# instaRock by Rob North (www.robnorth.co.uk)

import maya.cmds as cmds
import random
import math
import functools

windowName='InstaRock'

def createUI(pWindowTitle, pApplyCallback):
    
    def cancelCallback( *pArgs ):
            if cmds.window( windowName, exists=True ):
               cmds.deleteUI( windowName ) 
               
    if cmds.window(windowName, exists=True):
        cmds.deleteUI(windowName)
    
    cmds.window(windowName, t=pWindowTitle, s=False, rtf=True)
    cmds.rowColumnLayout(nc=2, cw=[(1,100), (2,50)], co=[(1, 'right', 3)])
    
    
    cmds.text(label='Number Of Rocks:')
    noOfRocksField=cmds.intField(min=1, s=1)
    
    cmds.text(label='Scale Multiplier')
    scaleMultiplierField=cmds.intField(min=1, s=1)
    
    cmds.button(label='Done', bgc=(0,1,0), c=functools.partial(pApplyCallback, noOfRocksField, scaleMultiplierField))
      
    cmds.button(label='Cancel', bgc=(1,0,0), c=cancelCallback)
    
    cmds.showWindow()
    
def applyCallback(noOfRocksField, scaleMultiplierField, *pArgs):
    noOfRocks=cmds.intField(noOfRocksField, q=True, v=True)     
    scaleMultiplier=cmds.intField(scaleMultiplierField, q=True, v=True)
    
    for i in range(noOfRocks):
        rock = cmds.polyPlatonic( r=random.uniform(7.5, 12.5), primitive=random.choice([3,4])),  cmds.rename('rock_#')
    
        cmds.polyReduce( ver=1, trm=1, vct=random.choice([4,5,7,8,9]), p=random.uniform(40, 75), shp=random.uniform(0,1), kqw=random.uniform(0,1), kev=random.choice([True, False]), kmw=random.uniform(0,1))
        
        if noOfRocks>1:
            x = random.uniform( -10*noOfRocks, 10*noOfRocks )*scaleMultiplier
            y = 0
            z = random.uniform( -10*noOfRocks, 10*noOfRocks )*scaleMultiplier 
        
            cmds.move( x, y, z)
        
        allEdges = cmds.ls('.e[:]', flatten=1)
        cmds.select(allEdges )
        cmds.polyBevel3( n='rockBevel_#', mv=True, ch=True, sa=180, sn=True, sg=random.choice([2,3,4]), d=random.uniform(0.25, 1), o=random.uniform(0.5, 1.5))
        
        cmds.select(rock)
        cmds.polySmooth(c=random.uniform(0,1), kb=random.choice([True, False]), khe=random.choice([True, False]), mth=random.choice([1,2]), ro=random.uniform(0,1))
        
        cmds.select(rock)
        cmds.scale(random.uniform(0.3, 1.3)*scaleMultiplier, random.uniform(0.75, 1.25)*scaleMultiplier, random.uniform(0.75, 1.25)*scaleMultiplier, r=True, a=True)
        cmds.manipPivot(r=True)
        
    cmds.deleteUI(windowName) 
        
createUI(windowName, applyCallback)        

#Created By Rob North (www.robnorth.co.uk)         