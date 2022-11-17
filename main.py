import markov
import pysynth_e
import musicio
from markov import F2T, T2F

# 注释的地方为可以修改的参数

Order = 2 # 参数为markov链阶数
markov.Init(Order)

samples = ['Lebal.xlsx']
# 样本文件名

for sname in samples:
    sample = musicio.Read_from_xlsx(sname)
    markov.NewSong()
    for note in sample:
        markov.Insert(note)

A, B = 4, 4 # A / B -> B分音符为1拍，每小节A拍。
music = markov.RandHead(A / B)

BarNum = 16 # 小节数
curptr = 0
for note in music: curptr += F2T(note[1])

# for note in music: print(note)

while(curptr < BarNum * 64):
    newnote = markov.Next(music[-Order:])
    if newnote == None: break 
    music.append(newnote)
    print(newnote)
    curptr += F2T(newnote[1])
    print("#", curptr, BarNum * 64)

musicio.Save_to_xlsx(music, '00.xlsx') # 指定输出文件名字

pysynth_e.make_wav(music, fn = '00.wav', silent = True) # 输出音频文件名字