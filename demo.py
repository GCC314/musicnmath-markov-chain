import markov
import pysynth_e
import musicio

markov.Init(2, 1 * 64)

samples = ['row_ur_boat.xlsx',
            'yoake.xlsx',
            'karakara.xlsx']

for sname in samples:
    sample = musicio.Read_from_xlsx(sname)
    markov.ClearPre()
    for note in sample:
        markov.Insert(note)

music = markov.RandHead()

for n in range(60):
    newnote = markov.Next(music[-2:])
    if newnote == None: break 
    music.append(newnote)

musicio.Save_to_xlsx(music, '00.xlsx')

pysynth_e.make_wav(music, fn = '00.wav', silent = True)