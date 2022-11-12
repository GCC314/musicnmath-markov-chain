import markov
import pysynth_e
import musicio

markov.Init(2)
markov.ClearPre()

sample = musicio.Read_from_xlsx('row_ur_boat.xlsx')
for note in sample:
    markov.Insert(note)

music = [("c4", 4), ("c4", 4)]

for n in range(40):
    newnote = markov.Next(music[-2:])
    if newnote == None: break 
    music.append(newnote)

musicio.Save_to_xlsx(music, '00.xlsx')

pysynth_e.make_wav(music, fn = '00.wav', silent = True)