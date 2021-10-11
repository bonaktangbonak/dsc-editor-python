# This Program works ONLY from any Project Diva Versions except FT to Project Diva PSPimport re
# If you want to convert FT to F, contact Kawaseru

import re # regex

def TrimDSC(input, star, chance):
    infile = open(input, "r")
    infiletrimmed = ""
    for command in infile:
        test = re.findall("^MUSIC_PLAY|^TARGET\(|^TIME|^END|^PV_END", command) # Might add MODE_SELECT but still haven't got chancetime working
        if test == []: continue
        elif "TARGET(" in test:
            sn = re.search("12", command); cn = re.search("15", command)
            if sn != None and sn.start() == 7: command = re.sub("12", str(star), command, 1)
            elif cn != None and sn.start() == 7: command = re.sub("15", str(chance), command, 1)
        infiletrimmed += command
    infile.close()
    outfile = open(input, "w"); outfile.write(infiletrimmed); outfile.close()

if __name__ == "__main__":
    InputDirectory = "P:/lease/enter/the/file/path" # Place the file path of the file you want to edit
    StarNote = 0 # Replace 0 with the numbers between 0-3
    ChanceNote = 0 # Same procedure as the Star Notes
    TrimDSC(InputDirectory, StarNote, ChanceNote)
    