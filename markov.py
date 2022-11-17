import numpy as np
from itertools import product
from copy import deepcopy
import random
import time

# Note = (pitch, beat)

# File format beat -> duration (*64)
def F2T(beat):
    if(beat > 0): return 64 // beat
    beat = -beat
    return 32 // beat * 3

def T2F(dur):
    if(dur % 3 == 0):
        beat = 32 // (dur // 3)
        return -beat
    return 64 // dur

# rem, slen take 1/64 note as a unit 

def Init(_order):
    random.seed(int(time.time()*1000000))
    global order
    global pre
    order = _order
    pre = []
    global PitchMat, BeatMat
    PitchMat = {}
    BeatMat = {}

def NewSong():
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
    # if not curBeat in BeatMat: return None
    pitch = RandChoice(PitchMat[curPitch])
    global rem, slen
    remBeat = {}
    for k, v in BeatMat[curBeat].items():
        if(rem >= F2T(k)):
            remBeat[k] = v
    # print(remBeat)
    beat = T2F(rem)
    if(len(remBeat) > 0):
        beat = RandChoice(remBeat)
    # print(rem, beat)
    rem -= F2T(beat)
    if(abs(rem) < 1e-2):
        # print("Align")
        rem = slen
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

def RandHead(_slen):
    global PitchMat, BeatMat
    pitch, beat = (), ()
    global slen, rem
    _slen *= 64
    slen, rem = _slen, _slen
    while True:
        pitch = RandChoice(SumHead(PitchMat))
        beat = RandChoice(SumHead(BeatMat))
        sum = 0
        for bt in beat: sum += F2T(bt)
        if sum > slen: continue
        if(sum == slen): sum = 0
        rem -= sum
        break    
    return list(zip(*[pitch, beat]))