import os

def openAndCount(name):
    fh = open(name)
    try:
        t = fh.readlines()
    except:
        return None
    fileBefore = len(t)
    # print('name '  ,name)

    # get name (replaced to support linux and win )
    # ll  = re.split('[\/]' , name)
    # name =ll[-1]  # get last part which is file name

    # print('ll' , ll)
    # of = open(name +'1'+'.txt' , 'wb') # OUTPUT file
    # toWrite = ''
    nAfter = 0  # number of lines after cleaning blank lines
    for line in t:
        if len(line.strip()) > 0:
            nAfter += 1
            #   toWrite += line

    # of.write(toWrite.encode())
    # of.close()
    fh.close()
    return name, fileBefore, fileBefore - nAfter, nAfter

def list_files1(dir):
    r = []
    nn = dict()
    for root, _, files in os.walk(dir):
        for name in files:
            p = os.path.join(root, name)
            r.append(p)
            a = nn.get(p, name)
            nn[p] = a
    return r, nn

def evaluate(files):
    totals = dict()
    print('PLease wait untill finishing Summary....^_^')
    for f in files:
        if openAndCount(f) is not None:
            name, _ , blank, nAfter = openAndCount(f)
        else:
            continue
        ext = name[name.find('.') + 1:]
        c = totals.get(ext, (0, 0))
        # print(type(c))
        pure, blankTotal = c
        pure += nAfter
        blankTotal += blank
        totals[ext] = (pure, blankTotal)

    from beautifultable import BeautifulTable
    table = BeautifulTable()
    table.column_headers = ["Extension", "Blank Line", "Pure Code"]
    for ext, c in totals.items():
        pure, blank = c
        if len(ext) > 10: continue
        table.append_row([ext, blank, pure])
    if len(table) == 0 :
        print('No Code Files Found')
        return
    print(table)

def doSummary(path):
    if len(path) < 2:
        print('invalid path')
        return
    files, _ = list_files1(path)
    evaluate(files)    






