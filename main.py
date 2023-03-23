import urllib
urllib.request.urlretrieve('https://raw.githubusercontent.com/techguy16/LegacyUpdateUpdater/main/latestver.txt', './latestver.txt')

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

with open('latestver.txt', 'r') as file:
    latestver = file.read().replace('\n', '')
    
latestverdownload = 'https://github.com/kirb/LegacyUpdate/releases/download/v', latestver, '.0/LegacyUpdate-', latestver, '.exe'
latestverdown1 = convertTuple(latestverdownload)
latestverdown = latestverdown1.strip(" ")

latestverdownload2 = './LegacyUpdate-', latestver, '.exe /S'
latestverdown12 = convertTuple(latestverdownload2)
latestverdown2 = latestverdown12.strip(" ")

urllib.request.urlretrieve(latestverdown)

import subprocess
FNULL = open(os.devnull, 'w')
args = latestverdown2
subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

