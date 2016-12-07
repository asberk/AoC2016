import hashlib


def _decrypt1(pzinput, pwlen=8, compare='0'*5, start_idx=0, verbose=0):
    idx = start_idx  # initialize index
    ncompare = len(compare)
    pw = []  # empty list to hold password
    while len(pw) < pwlen:  # while we still need more characters,
        md5hash = hashlib.md5((pzinput+str(idx)).encode('utf-8')).hexdigest()
        if md5hash[:ncompare] == compare:
            pw.append(md5hash[ncompare])
            if verbose:
                print(pw)
        idx += 1
    return pw

    
def _decrypt2(pzinput, pwlen=8, compare='0'*5, start_idx=0, verbose=0):
    idx = start_idx
    ncompare = len(compare)
    pw = [None]*pwlen  # empty list to hold password
    validIdxList = [str(x) for x in range(pwlen)]
    while len(validIdxList) > 0:  # while we still need more characters,
        md5hash = hashlib.md5((pzinput+str(idx)).encode('utf-8')).hexdigest()
        if (md5hash[:ncompare] == compare) and (md5hash[ncompare] in validIdxList):
            validIdxList.remove(md5hash[ncompare])
            pw[int(md5hash[ncompare])] = md5hash[ncompare+1]
            if verbose:
                print(pw)
        idx += 1
    return pw



            
if __name__ == '__main__':
    pzinput = 'abbhdwsy'  # puzzle input
    
    password_1 = _decrypt1(pzinput)
    print('The first password is:')
    print(password_1)

    password_2 = _decrypt2(pzinput)
    print('The second password is:')
    print(password_2)
