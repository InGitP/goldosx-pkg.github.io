import sys

import Tools.util
def playtext(file):
    print(f"now playing: {file}")
def cmd(args,path):
    sys.path.append(path.rootpath(patha="bin/Tools"))
    import Tools
    flib
    a = True
    try:

        if Tools.util.array.lencheck(args,3):
            filb = args[2]
    except Exception:

        flib = input("Audio name>")
    d = Tools.player3(filb)
    while a:
        
        
        
        playtext(filb)
        b = input("psound>")
        c = b.split()
        
        
        if c[0] == "exit":
            d.unload()
            a = False
        elif c[0] == "play":
            d.play()
            
        elif c[0] == "stop":
            d.stop()
        elif c[0] == "pause":
            d.pause()
        elif c[0] == "resume":
            d.unpause()
        elif c[0] == "change":
            d.change(c[1])
        