import ntpath 
import os
import sys
import re


r = re.compile('\{.*\}')

def main(path):
    base, name = ntpath.split(path)
    srt = open(path, 'r')
    target = open(os.path.join(base, 'new.srt'), 'w')
    for line in srt:
        n = r.sub('', line)
        target.write(n)
    srt.close()
    target.close()

if __name__ == "__main__":
    main(sys.argv[1])
