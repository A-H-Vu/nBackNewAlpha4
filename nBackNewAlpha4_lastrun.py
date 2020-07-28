#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 27, 2020, at 19:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'nBackNewAlpha4'  # from the Builder filename that created this script
expInfo = {'participant': '', 'taskVer': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\nBackNewAlpha4\\nBackNewAlpha4_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1088, 614], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text=None,
    font='Arial',
    pos=(-0.3,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrResp = keyboard.Keyboard()
instrImg = visual.ImageStim(
    win=win,
    name='instrImg', 
    image=None, mask=None,
    ori=0, pos=[0,0], size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialResp = keyboard.Keyboard()
trialGrid = visual.ImageStim(
    win=win,
    name='trialGrid', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trialSquare = visual.Rect(
    win=win, name='trialSquare',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
greenGrid = visual.ImageStim(
    win=win,
    name='greenGrid', 
    image='gridGreen.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
redGrid = visual.ImageStim(
    win=win,
    name='redGrid', 
    image='gridRed.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='This is the end of the experiment. Thank you for your time. Please remember to return to the questionnaire to carry on with the study. Press ‘space’ to exit.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endResp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
taskLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('taskCond.xlsx'),
    seed=None, name='taskLoop')
thisExp.addLoop(taskLoop)  # add the loop to the experiment
thisTaskLoop = taskLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTaskLoop.rgb)
if thisTaskLoop != None:
    for paramName in thisTaskLoop:
        exec('{} = thisTaskLoop[paramName]'.format(paramName))

for thisTaskLoop in taskLoop:
    currentLoop = taskLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTaskLoop.rgb)
    if thisTaskLoop != None:
        for paramName in thisTaskLoop:
            exec('{} = thisTaskLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    instrText.setText('')
    instrResp.keys = []
    instrResp.rt = []
    _instrResp_allKeys = []
    instrImg.setPos((0, 0))
    if condsFile == "nBack1Cond.xlsx":
        instrImg.pos = (0.5, -0.3)
        instrImg.image = '1back.png'
        instrText.text = "In this task you will be required to press ‘space’ if the white square appeared in the same location as the location on the last trial. For example if the square was in the left down corner on trial 1 and then it appeared in the same location on trial 2, press ‘space’. Otherwise, do not respond. Press ‘s’ to continue."
    elif condsFile == "nBack2Cond.xlsx":
        instrImg.pos = (0.5, -0.15)
        instrImg.image = '2back.png'
        instrText.text = "This is the end of 1-back trials. You are about to start 2-back trials. This means that instead of pressing ‘space’ whenever the square appears in the same position as on the position on one trial before, you are required to press ‘space’ whenever the square appears in the same position as on the position two trials before. For example if the square appeared in left down corner on trial 1, you should press ‘space’ if the square appears in the left down corner on trial 3. Press ‘s’ to continue."
    elif condsFile == "nBack3Cond.xlsx":
        instrImg.pos = (0.5, 0)
        instrImg.image = '3back.png'
        instrText.text = "This is the end of 2-back trials. You are about to start 3-back trials. This means that instead of pressing ‘space’ whenever the square appears in the same position as on the position on two trials before, you are required to press ‘space’ whenever the square appears in the same position as on the position three trials before. For example if the square appeared in left down corner on trial 1, you should press ‘space’ if the square appears in the left down corner on trial 4. Press ‘s’ to continue."
    else: 
        instrImg.pos = (0.5, 0)
        instrImg.image = '3back.png'
        instrText.text = "This is the end of 2-back trials. You are about to start 3-back trials. This means that instead of pressing ‘space’ whenever the square appears in the same position as on the position on two trials before, you are required to press ‘space’ whenever the square appears in the same position as on the position three trials before. For example if the square appeared in left down corner on trial 1, you should press ‘space’ if the square appears in the left down corner on trial 4. Press ‘s’ to continue."
    # keep track of which components have finished
    instrComponents = [instrText, instrResp, instrImg]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrText* updates
        if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrText.frameNStart = frameN  # exact frame index
            instrText.tStart = t  # local t and not account for scr refresh
            instrText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
            instrText.setAutoDraw(True)
        
        # *instrResp* updates
        waitOnFlip = False
        if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrResp.frameNStart = frameN  # exact frame index
            instrResp.tStart = t  # local t and not account for scr refresh
            instrResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
            instrResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instrResp.status == STARTED and not waitOnFlip:
            theseKeys = instrResp.getKeys(keyList=['s'], waitRelease=False)
            _instrResp_allKeys.extend(theseKeys)
            if len(_instrResp_allKeys):
                instrResp.keys = _instrResp_allKeys[-1].name  # just the last key pressed
                instrResp.rt = _instrResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *instrImg* updates
        if instrImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrImg.frameNStart = frameN  # exact frame index
            instrImg.tStart = t  # local t and not account for scr refresh
            instrImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrImg, 'tStartRefresh')  # time at next scr refresh
            instrImg.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    taskLoop.addData('instrText.started', instrText.tStartRefresh)
    taskLoop.addData('instrText.stopped', instrText.tStopRefresh)
    taskLoop.addData('instrImg.started', instrImg.tStartRefresh)
    taskLoop.addData('instrImg.stopped', instrImg.tStopRefresh)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condsFile),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        trialResp.keys = []
        trialResp.rt = []
        _trialResp_allKeys = []
        trialSquare.setPos((loc1, loc2))
        gridOpac = 1
        greenOpac = 0
        redOpac = 0
        
        
        # keep track of which components have finished
        trialComponents = [trialResp, trialGrid, trialSquare, trialFix, greenGrid, redGrid]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trialResp* updates
            waitOnFlip = False
            if trialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialResp.frameNStart = frameN  # exact frame index
                trialResp.tStart = t  # local t and not account for scr refresh
                trialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
                trialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialResp.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialResp.tStop = t  # not accounting for scr refresh
                    trialResp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trialResp, 'tStopRefresh')  # time at next scr refresh
                    trialResp.status = FINISHED
            if trialResp.status == STARTED and not waitOnFlip:
                theseKeys = trialResp.getKeys(keyList=['space'], waitRelease=False)
                _trialResp_allKeys.extend(theseKeys)
                if len(_trialResp_allKeys):
                    trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                    trialResp.rt = _trialResp_allKeys[-1].rt
            
            # *trialGrid* updates
            if trialGrid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialGrid.frameNStart = frameN  # exact frame index
                trialGrid.tStart = t  # local t and not account for scr refresh
                trialGrid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialGrid, 'tStartRefresh')  # time at next scr refresh
                trialGrid.setAutoDraw(True)
            if trialGrid.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialGrid.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    trialGrid.tStop = t  # not accounting for scr refresh
                    trialGrid.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trialGrid, 'tStopRefresh')  # time at next scr refresh
                    trialGrid.setAutoDraw(False)
            if trialGrid.status == STARTED:  # only update if drawing
                trialGrid.setOpacity(gridOpac, log=False)
            
            # *trialSquare* updates
            if trialSquare.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialSquare.frameNStart = frameN  # exact frame index
                trialSquare.tStart = t  # local t and not account for scr refresh
                trialSquare.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialSquare, 'tStartRefresh')  # time at next scr refresh
                trialSquare.setAutoDraw(True)
            if trialSquare.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialSquare.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialSquare.tStop = t  # not accounting for scr refresh
                    trialSquare.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trialSquare, 'tStopRefresh')  # time at next scr refresh
                    trialSquare.setAutoDraw(False)
            
            # *trialFix* updates
            if trialFix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialFix.frameNStart = frameN  # exact frame index
                trialFix.tStart = t  # local t and not account for scr refresh
                trialFix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(True)
            if trialFix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialFix.tStop = t  # not accounting for scr refresh
                    trialFix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                    trialFix.setAutoDraw(False)
            
            # *greenGrid* updates
            if greenGrid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                greenGrid.frameNStart = frameN  # exact frame index
                greenGrid.tStart = t  # local t and not account for scr refresh
                greenGrid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(greenGrid, 'tStartRefresh')  # time at next scr refresh
                greenGrid.setAutoDraw(True)
            if greenGrid.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > greenGrid.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    greenGrid.tStop = t  # not accounting for scr refresh
                    greenGrid.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(greenGrid, 'tStopRefresh')  # time at next scr refresh
                    greenGrid.setAutoDraw(False)
            if greenGrid.status == STARTED:  # only update if drawing
                greenGrid.setOpacity(greenOpac, log=False)
            
            # *redGrid* updates
            if redGrid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                redGrid.frameNStart = frameN  # exact frame index
                redGrid.tStart = t  # local t and not account for scr refresh
                redGrid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(redGrid, 'tStartRefresh')  # time at next scr refresh
                redGrid.setAutoDraw(True)
            if redGrid.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > redGrid.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    redGrid.tStop = t  # not accounting for scr refresh
                    redGrid.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(redGrid, 'tStopRefresh')  # time at next scr refresh
                    redGrid.setAutoDraw(False)
            if redGrid.status == STARTED:  # only update if drawing
                redGrid.setOpacity(redOpac, log=False)
            if corrAns == 'space' and (trialResp.keys == 'space'):
                gridOpac = 0
                greenOpac = 1
            if not(corrAns == 'space') and (trialResp.keys == 'space'):
                gridOpac = 0
                redOpac = 1
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if trialResp.keys in ['', [], None]:  # No response was made
            trialResp.keys = None
        trials.addData('trialResp.keys',trialResp.keys)
        if trialResp.keys != None:  # we had a response
            trials.addData('trialResp.rt', trialResp.rt)
        trials.addData('trialResp.started', trialResp.tStartRefresh)
        trials.addData('trialResp.stopped', trialResp.tStopRefresh)
        trials.addData('trialGrid.started', trialGrid.tStartRefresh)
        trials.addData('trialGrid.stopped', trialGrid.tStopRefresh)
        trials.addData('trialSquare.started', trialSquare.tStartRefresh)
        trials.addData('trialSquare.stopped', trialSquare.tStopRefresh)
        trials.addData('trialFix.started', trialFix.tStartRefresh)
        trials.addData('trialFix.stopped', trialFix.tStopRefresh)
        trials.addData('greenGrid.started', greenGrid.tStartRefresh)
        trials.addData('greenGrid.stopped', greenGrid.tStopRefresh)
        trials.addData('redGrid.started', redGrid.tStartRefresh)
        trials.addData('redGrid.stopped', redGrid.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'taskLoop'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
endResp.keys = []
endResp.rt = []
_endResp_allKeys = []
# keep track of which components have finished
endComponents = [endText, endResp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    
    # *endResp* updates
    waitOnFlip = False
    if endResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResp.frameNStart = frameN  # exact frame index
        endResp.tStart = t  # local t and not account for scr refresh
        endResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResp, 'tStartRefresh')  # time at next scr refresh
        endResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endResp.status == STARTED and not waitOnFlip:
        theseKeys = endResp.getKeys(keyList=['space'], waitRelease=False)
        _endResp_allKeys.extend(theseKeys)
        if len(_endResp_allKeys):
            endResp.keys = _endResp_allKeys[-1].name  # just the last key pressed
            endResp.rt = _endResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
