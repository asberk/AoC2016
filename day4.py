import numpy as np
import scipy as sp
import pandas as pd

with open('./input/day4input.txt', 'r') as fp:
    read_data = fp.read()

data = read_data.split('\n')[:-1]
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def newCountDict():
    countDict = {}
    for j in alphabet:
        countDict[j] = 0
    return countDict


def countLetterFrequency(s):
    countDict = newCountDict()
    idx = 0
    while s[idx] is not '[':
        if s[idx] in alphabet:
            countDict[s[idx]] += 1
        idx += 1
    return countDict


def highestFrequencies(letter_frequencies):
    highest = np.max(list(letter_frequencies.values()))
    sorted_lf = [ sorted([x for x,y in letter_frequencies.items() if y==n]) for
                  n in range(highest, -1, -1)]
    sorted_lf_flat = [item for sublist in sorted_lf for item in sublist]
    return ''.join(sorted_lf_flat[:5])


def fetchChecksum(s):
    idx = -2
    checksum = []
    while s[idx] is not '[':
        checksum.append(s[idx])
        idx -= 1
    return ''.join(checksum[-1::-1])


def fetchSectorID(s):
    return int(s[-10:-7])


def checksumIsValid(s):
    s_hash = highestFrequencies(countLetterFrequency(s))
    checksum = fetchChecksum(s)
    return s_hash == checksum


def fetchValidSectorID(s):
    if checksumIsValid(s):
        return fetchSectorID(s)
    else:
        return 0


# Day 4: Part I
sectorID_total = 0
for string in data:
    sectorID_total += fetchValidSectorID(string)

print(sectorID_total)


# Day 4: Part II
def fetchEncrypted(s):
    retstring = []
    idx = 0
    strdigits = [str(x) for x in range(10)]
    while s[idx] not in strdigits:
        retstring.append(s[idx])
        idx += 1
    return retstring


def getLetterPositions():
    retDict = {}
    for ij, j in enumerate(alphabet):
        retDict[j] = ij
    return getLetterPositions


letter_positions = getLetterPositions()


def letterToPosition(ell):
    if ell is '-':
        return ' '
    else:
        if ell in alphabet:
            return alphabet.index(ell)
        else:
            raise Exception('not a letter')


def positionToLetter(p):
    return alphabet[p]


def decodeLetter(ell, sid):
    if ell is '-':
        return ' '
    else:
        return positionToLetter((letterToPosition(ell)+sid) % 26)


def decodeValidCipher(s):
    sid = fetchValidSectorID(s)
    if sid > 0:
        decoded = [decodeLetter(x, sid) for x in fetchEncrypted(s)]
        return ''.join(decoded[:-1])


# print results
decodedStringList = [decodeValidCipher(string) for string in data]


def matchSubstring(s, sList):
    return [x for x in sList if ((x) and (s in x))]


def getFirstIndexOfMatch(s, sList):
    return sList.index(matchSubstring(s, sList)[0])


northpole_idx = getFirstIndexOfMatch('north', decodedStringList)

print('Check if this is the correct index...')
print('if the next line doesn\'t have northpole'
      ' in it, then something\'s wrong...')
print(decodeValidCipher(data[northpole_idx]))
print('answer:')
print(fetchSectorID(data[northpole_idx]))
