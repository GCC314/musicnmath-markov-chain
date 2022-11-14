import numpy as np
from itertools import product
from copy import deepcopy
import random

# Note = (pitch, beat)

def __init__():
    global Pitch, Beat

    Pitch = ['g3','g#3','a3','a#3','b3','c4','c#4','d4','d#4','e4','f4','f#4','g4','g#4','a4','a#4','b4','c5','c#5','d5','d#5','e5','f5']
    Beat = [1, 2, 4, 8, 16, 32]

# rem, slen take 1/192 note as a unit 

def Init(_order, _slen):
    global order
    global pre
    global slen, rem
    order, slen, rem = _order, _slen, _slen
    pre = []
    global PitchMat, BeatMat
    PitchMat = {}
    BeatMat = {}

def ClearPre():
    global pre
    pre = []

def Insert(note):
    global pre, order
    if len(pre) < order:
        pre.append(note)
        return
    global PitchMat, BeatMat
    prePitch = tuple(zip(*pre))[0]
    preBeat = tuple(zip(*pre))[1]
    if not prePitch in PitchMat:
        PitchMat[prePitch] = {}
    if not note[0] in PitchMat[prePitch]:
        PitchMat[prePitch][note[0]] = 0
    PitchMat[prePitch][note[0]] += 1
    if not preBeat in BeatMat:
        BeatMat[preBeat] = {}
    if not note[1] in BeatMat[preBeat]:
        BeatMat[preBeat][note[1]] = 0
    BeatMat[preBeat][note[1]] += 1
    pre.append(note)
    pre = pre[1:]

def Next(cur):
    global PitchMat, BeatMat
    curPitch = tuple(zip(*cur))[0]
    curBeat = tuple(zip(*cur))[1]
    if not curPitch in PitchMat: return None
    if not curBeat in BeatMat: return None
    pitch = RandChoice(PitchMat[curPitch])
    global rem, slen
    remBeat = {}
    for k, v in curBeat.items():
        if(rem >= 192 / k):
            remBeat[k] = v
    beat = 192 / rem
    if(len(remBeat) > 0):
        beat = RandChoice(remBeat)
    rem -= 192 / beat
    if(rem == 0): rem = slen
    return (pitch, beat)

def RandChoice(dic):
    global PitchMat, BeatMat
    sum = 0
    for k in dic: sum += dic[k]
    id = random.randint(1, sum)
    for k in dic:
        if id > dic[k]: id -= dic[k]
        else: return k
    # Control should never reach here

def SumHead(totDic):
    dic = {}
    for k, v in totDic.items():
        dic[k] = 0
        for kk, cnt in v.items():
            dic[k] += cnt
    return dic

def RandHead():
    global PitchMat, BeatMat
    pitch = RandChoice(SumHead(PitchMat))
    beat = RandChoice(SumHead(BeatMat))
    return list(zip(*[pitch, beat]))