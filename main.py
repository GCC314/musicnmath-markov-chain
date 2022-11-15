import markov
import pysynth_e
import musicio

# 注释的地方为可以修改的参数

Order = 2 # 参数为markov链阶数
markov.Init(Order)

samples = ['row_ur_boat.xlsx',
            'yoake.xlsx',
            'karakara.xlsx']
# 样本文件名

for sname in samples:
    sample = musicio.Read_from_xlsx(sname)
    markov.NewSong(4 / 4) # a / b -> a分音符为1拍，每小节b拍。
    for note in sample:
        markov.Insert(note)

music = markov.RandHead()

SongLength = 60
for n in range(SongLength):
    newnote = markov.Next(music[-Order:])
    if newnote == None: break 
    music.append(newnote)

musicio.Save_to_xlsx(music, '00.xlsx') # 指定输出文件名字

pysynth_e.make_wav(music, fn = '00.wav', silent = True) # 输出音频文件名字