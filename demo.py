import markov
import pysynth_e

markov.Init(2)

markov.Insert(("c4", 4))
markov.Insert(("c4", 4))
markov.Insert(("c4", 4))
markov.Insert(("d4", 8))
markov.Insert(("e4", 4))
markov.Insert(("e4", 4))
markov.Insert(("d4", 8))
markov.Insert(("e4", 4))
markov.Insert(("f4", 8))
markov.Insert(("g4", 2))

markov.Insert(("c4", 8))
markov.Insert(("c4", 8))
markov.Insert(("c4", 8))

markov.Insert(("g4", 8))
markov.Insert(("g4", 8))
markov.Insert(("g4", 8))

markov.Insert(("e4", 8))
markov.Insert(("e4", 8))
markov.Insert(("e4", 8))

markov.Insert(("c4", 8))
markov.Insert(("c4", 8))
markov.Insert(("c4", 8))

markov.Insert(("g4", 4))
markov.Insert(("f4", 8))
markov.Insert(("e4", 4))
markov.Insert(("d4", 8))
markov.Insert(("c4", 2))


music = [("c4", 4), ("c4", 4)]

for n in range(40):
    newnote = markov.Next(music[-2:])
    if newnote == None: break 
    music.append(newnote)

with open("00.music", "w") as fp:
    print(music, file = fp)

pysynth_e.make_wav(music, fn = '00.wav')