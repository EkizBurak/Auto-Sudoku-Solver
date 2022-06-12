import numpy
from math import ceil

sudoku=numpy.array\
(
    [
        [
            [0, 9, 0, 6, 0, 7, 8, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 7],
            [0, 0, 0, 0, 2, 0, 0, 0, 4],

            [0, 3, 0, 0, 7, 2, 0, 0, 9],
            [0, 5, 0, 0, 0, 0, 0, 2, 0],
            [4, 0, 0, 8, 6, 0, 0, 3, 0],

            [7, 0, 0, 0, 5, 0, 0, 0, 0],
            [4, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 8, 7, 0, 3, 0, 9, 0]
        ]
    ]
)

kareninAlabilecegiDegerler=numpy.array\
    (
        [
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],

                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],

                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ]
        ]
    )
yatayAlabilecegiDegerler=numpy.array\
    (
        [
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],

                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],

                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ]
        ]
    )
dikeyAlabilecegiDegerler=numpy.array\
    (
        [
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],

                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],

                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ]
        ]
    )

hucreDegerleri={}
hucreDegerlerisayac=1

for i in sudoku:
    for sayac,x in enumerate(i):
        for nsayac,n in enumerate(x):
            if n!=0:
                kareninAlabilecegiDegerler[0][sayac] = numpy.append(numpy.delete(kareninAlabilecegiDegerler[0][sayac], numpy.where(kareninAlabilecegiDegerler[0][sayac] == n)[0][0]),0)
                if sayac <3:
                    yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) - 1] = numpy.append(numpy.delete(yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) - 1],numpy.where(yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) - 1] == n)[0][0]), 0)
                elif sayac <6:
                    yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) + 2] = numpy.append(numpy.delete(yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) + 2],numpy.where(yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) + 2] == n)[0][0]), 0)
                elif sayac <9:
                    yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) + 5] = numpy.append(numpy.delete(yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) + 5],numpy.where(yatayAlabilecegiDegerler[0][ceil((nsayac + 1) / 3) + 5] == n)[0][0]), 0)

                if sayac==0 or sayac ==3 or sayac==6:
                    if nsayac==0 or nsayac==3 or nsayac==6:
                        dikeyDeger=0
                    elif nsayac == 1 or nsayac == 4 or nsayac == 7:
                        dikeyDeger=1
                    elif nsayac == 2 or nsayac == 5 or nsayac == 8:
                        dikeyDeger=2

                elif sayac == 1 or sayac == 4 or sayac == 7:
                    if nsayac == 0 or nsayac == 3 or nsayac == 6:
                        dikeyDeger=3
                    elif nsayac == 1 or nsayac == 4 or nsayac == 7:
                        dikeyDeger=4
                    elif nsayac == 2 or nsayac == 5 or nsayac == 8:
                        dikeyDeger = 5

                elif sayac == 2 or sayac == 5 or sayac == 8:
                    if nsayac == 0 or nsayac == 3 or nsayac == 6:
                        dikeyDeger=6
                    elif nsayac == 1 or nsayac == 4 or nsayac == 7:
                        dikeyDeger=7
                    elif nsayac == 2 or nsayac == 5 or nsayac == 8:
                        dikeyDeger=8

                dikeyAlabilecegiDegerler[0][dikeyDeger] = numpy.append(numpy.delete(dikeyAlabilecegiDegerler[0][dikeyDeger], numpy.where(dikeyAlabilecegiDegerler[0][dikeyDeger] == n)[0][0]),0)
            elif n ==0:
                hucreDegerleri["{0}".format(hucreDegerlerisayac)]= numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
            hucreDegerlerisayac+=1

def hucreDegeriHesapla():
    for i in kareninAlabilecegiDegerler:
        for sayac, x in enumerate(i):
            for m in range(1, 10):
                if len(numpy.where(x == m)[0]) == 0:
                    if sayac == 0:
                        for n in range(1, 10):
                            try:
                                hucreDegerleri[f"{n}"] = numpy.delete(hucreDegerleri[f"{n}"],
                                                                      numpy.where(hucreDegerleri[f"{n}"] == m))
                            except:
                                pass
                    else:
                        for z in range(sayac * 9 + 1, (sayac + 1) * 9 + 1):
                            try:
                                hucreDegerleri[f"{z}"] = numpy.delete(hucreDegerleri[f"{z}"],
                                                                      numpy.where(hucreDegerleri[f"{z}"] == m))
                            except:
                                pass
    for sayac,x in enumerate(yatayAlabilecegiDegerler[0]):
        for m in range(1,10):
            if sayac == 0:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["1"] = numpy.delete(hucreDegerleri["1"], numpy.where(hucreDegerleri["1"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["2"] = numpy.delete(hucreDegerleri["2"], numpy.where(hucreDegerleri["2"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["3"] = numpy.delete(hucreDegerleri["3"], numpy.where(hucreDegerleri["3"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["10"] = numpy.delete(hucreDegerleri["10"], numpy.where(hucreDegerleri["10"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["11"] = numpy.delete(hucreDegerleri["11"], numpy.where(hucreDegerleri["11"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["12"] = numpy.delete(hucreDegerleri["12"], numpy.where(hucreDegerleri["12"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["19"] = numpy.delete(hucreDegerleri["19"], numpy.where(hucreDegerleri["19"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["20"] = numpy.delete(hucreDegerleri["20"], numpy.where(hucreDegerleri["20"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["21"] = numpy.delete(hucreDegerleri["21"], numpy.where(hucreDegerleri["21"] == m))
                    except:
                        pass

            if sayac == 1:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["4"] = numpy.delete(hucreDegerleri["4"], numpy.where(hucreDegerleri["4"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["5"] = numpy.delete(hucreDegerleri["5"], numpy.where(hucreDegerleri["5"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["6"] = numpy.delete(hucreDegerleri["6"], numpy.where(hucreDegerleri["6"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["13"] = numpy.delete(hucreDegerleri["13"], numpy.where(hucreDegerleri["13"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["14"] = numpy.delete(hucreDegerleri["14"], numpy.where(hucreDegerleri["14"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["15"] = numpy.delete(hucreDegerleri["15"], numpy.where(hucreDegerleri["15"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["22"] = numpy.delete(hucreDegerleri["22"], numpy.where(hucreDegerleri["22"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["23"] = numpy.delete(hucreDegerleri["23"], numpy.where(hucreDegerleri["23"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["24"] = numpy.delete(hucreDegerleri["24"], numpy.where(hucreDegerleri["24"] == m))
                    except:
                        pass

            if sayac == 2:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["7"] = numpy.delete(hucreDegerleri["7"], numpy.where(hucreDegerleri["7"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["8"] = numpy.delete(hucreDegerleri["8"], numpy.where(hucreDegerleri["8"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["9"] = numpy.delete(hucreDegerleri["9"], numpy.where(hucreDegerleri["9"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["16"] = numpy.delete(hucreDegerleri["16"], numpy.where(hucreDegerleri["16"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["17"] = numpy.delete(hucreDegerleri["17"], numpy.where(hucreDegerleri["17"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["18"] = numpy.delete(hucreDegerleri["18"], numpy.where(hucreDegerleri["18"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["25"] = numpy.delete(hucreDegerleri["25"], numpy.where(hucreDegerleri["25"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["26"] = numpy.delete(hucreDegerleri["26"], numpy.where(hucreDegerleri["26"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["27"] = numpy.delete(hucreDegerleri["27"], numpy.where(hucreDegerleri["27"] == m))
                    except:
                        pass

            if sayac == 3:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["28"] = numpy.delete(hucreDegerleri["28"], numpy.where(hucreDegerleri["28"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["29"] = numpy.delete(hucreDegerleri["29"], numpy.where(hucreDegerleri["29"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["30"] = numpy.delete(hucreDegerleri["30"], numpy.where(hucreDegerleri["30"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["37"] = numpy.delete(hucreDegerleri["37"], numpy.where(hucreDegerleri["37"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["38"] = numpy.delete(hucreDegerleri["38"], numpy.where(hucreDegerleri["38"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["39"] = numpy.delete(hucreDegerleri["39"], numpy.where(hucreDegerleri["39"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["46"] = numpy.delete(hucreDegerleri["46"], numpy.where(hucreDegerleri["46"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["47"] = numpy.delete(hucreDegerleri["47"], numpy.where(hucreDegerleri["47"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["48"] = numpy.delete(hucreDegerleri["48"], numpy.where(hucreDegerleri["48"] == m))
                    except:
                        pass

            if sayac == 4:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["31"] = numpy.delete(hucreDegerleri["31"], numpy.where(hucreDegerleri["31"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["32"] = numpy.delete(hucreDegerleri["32"], numpy.where(hucreDegerleri["32"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["33"] = numpy.delete(hucreDegerleri["33"], numpy.where(hucreDegerleri["33"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["40"] = numpy.delete(hucreDegerleri["40"], numpy.where(hucreDegerleri["40"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["41"] = numpy.delete(hucreDegerleri["41"], numpy.where(hucreDegerleri["41"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["42"] = numpy.delete(hucreDegerleri["42"], numpy.where(hucreDegerleri["42"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["49"] = numpy.delete(hucreDegerleri["49"], numpy.where(hucreDegerleri["49"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["50"] = numpy.delete(hucreDegerleri["50"], numpy.where(hucreDegerleri["50"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["51"] = numpy.delete(hucreDegerleri["51"], numpy.where(hucreDegerleri["51"] == m))
                    except:
                        pass

            if sayac == 5:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["34"] = numpy.delete(hucreDegerleri["34"], numpy.where(hucreDegerleri["34"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["35"] = numpy.delete(hucreDegerleri["35"], numpy.where(hucreDegerleri["35"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["36"] = numpy.delete(hucreDegerleri["36"], numpy.where(hucreDegerleri["36"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["43"] = numpy.delete(hucreDegerleri["43"], numpy.where(hucreDegerleri["43"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["44"] = numpy.delete(hucreDegerleri["44"], numpy.where(hucreDegerleri["44"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["45"] = numpy.delete(hucreDegerleri["45"], numpy.where(hucreDegerleri["45"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["52"] = numpy.delete(hucreDegerleri["52"], numpy.where(hucreDegerleri["52"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["53"] = numpy.delete(hucreDegerleri["53"], numpy.where(hucreDegerleri["53"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["54"] = numpy.delete(hucreDegerleri["54"], numpy.where(hucreDegerleri["54"] == m))
                    except:
                        pass

            if sayac == 6:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["55"] = numpy.delete(hucreDegerleri["55"], numpy.where(hucreDegerleri["55"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["56"] = numpy.delete(hucreDegerleri["56"], numpy.where(hucreDegerleri["56"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["57"] = numpy.delete(hucreDegerleri["57"], numpy.where(hucreDegerleri["57"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["64"] = numpy.delete(hucreDegerleri["64"], numpy.where(hucreDegerleri["64"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["65"] = numpy.delete(hucreDegerleri["65"], numpy.where(hucreDegerleri["65"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["66"] = numpy.delete(hucreDegerleri["66"], numpy.where(hucreDegerleri["66"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["73"] = numpy.delete(hucreDegerleri["73"], numpy.where(hucreDegerleri["73"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["74"] = numpy.delete(hucreDegerleri["74"], numpy.where(hucreDegerleri["74"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["75"] = numpy.delete(hucreDegerleri["75"], numpy.where(hucreDegerleri["75"] == m))
                    except:
                        pass

            if sayac == 7:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["58"] = numpy.delete(hucreDegerleri["58"], numpy.where(hucreDegerleri["58"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["59"] = numpy.delete(hucreDegerleri["59"], numpy.where(hucreDegerleri["59"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["60"] = numpy.delete(hucreDegerleri["60"], numpy.where(hucreDegerleri["60"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["67"] = numpy.delete(hucreDegerleri["67"], numpy.where(hucreDegerleri["67"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["68"] = numpy.delete(hucreDegerleri["68"], numpy.where(hucreDegerleri["68"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["69"] = numpy.delete(hucreDegerleri["69"], numpy.where(hucreDegerleri["69"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["76"] = numpy.delete(hucreDegerleri["76"], numpy.where(hucreDegerleri["76"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["77"] = numpy.delete(hucreDegerleri["77"], numpy.where(hucreDegerleri["77"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["78"] = numpy.delete(hucreDegerleri["78"], numpy.where(hucreDegerleri["78"] == m))
                    except:
                        pass

            if sayac == 8:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["61"] = numpy.delete(hucreDegerleri["61"], numpy.where(hucreDegerleri["61"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["62"] = numpy.delete(hucreDegerleri["62"], numpy.where(hucreDegerleri["62"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["63"] = numpy.delete(hucreDegerleri["63"], numpy.where(hucreDegerleri["63"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["70"] = numpy.delete(hucreDegerleri["70"], numpy.where(hucreDegerleri["70"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["71"] = numpy.delete(hucreDegerleri["71"], numpy.where(hucreDegerleri["71"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["72"] = numpy.delete(hucreDegerleri["72"], numpy.where(hucreDegerleri["72"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["79"] = numpy.delete(hucreDegerleri["79"], numpy.where(hucreDegerleri["79"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["80"] = numpy.delete(hucreDegerleri["80"], numpy.where(hucreDegerleri["80"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["81"] = numpy.delete(hucreDegerleri["81"], numpy.where(hucreDegerleri["81"] == m))
                    except:
                        pass
    for sayac,x in enumerate(dikeyAlabilecegiDegerler[0]):
        for m in range(1,10):
            if sayac == 0:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["1"] = numpy.delete(hucreDegerleri["1"], numpy.where(hucreDegerleri["1"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["4"] = numpy.delete(hucreDegerleri["4"], numpy.where(hucreDegerleri["4"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["7"] = numpy.delete(hucreDegerleri["7"], numpy.where(hucreDegerleri["7"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["28"] = numpy.delete(hucreDegerleri["28"], numpy.where(hucreDegerleri["28"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["31"] = numpy.delete(hucreDegerleri["31"], numpy.where(hucreDegerleri["31"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["34"] = numpy.delete(hucreDegerleri["34"], numpy.where(hucreDegerleri["34"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["55"] = numpy.delete(hucreDegerleri["55"], numpy.where(hucreDegerleri["55"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["58"] = numpy.delete(hucreDegerleri["58"], numpy.where(hucreDegerleri["58"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["61"] = numpy.delete(hucreDegerleri["61"], numpy.where(hucreDegerleri["61"] == m))
                    except:
                        pass

            if sayac == 1:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["2"] = numpy.delete(hucreDegerleri["2"], numpy.where(hucreDegerleri["2"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["5"] = numpy.delete(hucreDegerleri["5"], numpy.where(hucreDegerleri["5"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["8"] = numpy.delete(hucreDegerleri["8"], numpy.where(hucreDegerleri["8"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["29"] = numpy.delete(hucreDegerleri["29"], numpy.where(hucreDegerleri["29"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["32"] = numpy.delete(hucreDegerleri["32"], numpy.where(hucreDegerleri["32"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["35"] = numpy.delete(hucreDegerleri["35"], numpy.where(hucreDegerleri["35"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["56"] = numpy.delete(hucreDegerleri["56"], numpy.where(hucreDegerleri["56"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["59"] = numpy.delete(hucreDegerleri["59"], numpy.where(hucreDegerleri["59"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["62"] = numpy.delete(hucreDegerleri["62"], numpy.where(hucreDegerleri["62"] == m))
                    except:
                        pass

            if sayac == 2:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["3"] = numpy.delete(hucreDegerleri["3"], numpy.where(hucreDegerleri["3"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["6"] = numpy.delete(hucreDegerleri["6"], numpy.where(hucreDegerleri["6"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["9"] = numpy.delete(hucreDegerleri["9"], numpy.where(hucreDegerleri["9"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["30"] = numpy.delete(hucreDegerleri["30"], numpy.where(hucreDegerleri["30"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["33"] = numpy.delete(hucreDegerleri["33"], numpy.where(hucreDegerleri["33"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["36"] = numpy.delete(hucreDegerleri["36"], numpy.where(hucreDegerleri["36"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["57"] = numpy.delete(hucreDegerleri["57"], numpy.where(hucreDegerleri["57"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["60"] = numpy.delete(hucreDegerleri["60"], numpy.where(hucreDegerleri["60"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["63"] = numpy.delete(hucreDegerleri["63"], numpy.where(hucreDegerleri["63"] == m))
                    except:
                        pass

            if sayac == 3:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["10"] = numpy.delete(hucreDegerleri["10"], numpy.where(hucreDegerleri["10"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["13"] = numpy.delete(hucreDegerleri["13"], numpy.where(hucreDegerleri["13"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["16"] = numpy.delete(hucreDegerleri["16"], numpy.where(hucreDegerleri["16"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["37"] = numpy.delete(hucreDegerleri["37"], numpy.where(hucreDegerleri["37"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["40"] = numpy.delete(hucreDegerleri["40"], numpy.where(hucreDegerleri["40"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["43"] = numpy.delete(hucreDegerleri["43"], numpy.where(hucreDegerleri["43"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["64"] = numpy.delete(hucreDegerleri["64"], numpy.where(hucreDegerleri["64"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["67"] = numpy.delete(hucreDegerleri["67"], numpy.where(hucreDegerleri["67"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["70"] = numpy.delete(hucreDegerleri["70"], numpy.where(hucreDegerleri["70"] == m))
                    except:
                        pass

            if sayac == 4:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["11"] = numpy.delete(hucreDegerleri["11"], numpy.where(hucreDegerleri["11"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["14"] = numpy.delete(hucreDegerleri["14"], numpy.where(hucreDegerleri["14"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["17"] = numpy.delete(hucreDegerleri["17"], numpy.where(hucreDegerleri["17"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["38"] = numpy.delete(hucreDegerleri["38"], numpy.where(hucreDegerleri["38"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["41"] = numpy.delete(hucreDegerleri["41"], numpy.where(hucreDegerleri["41"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["44"] = numpy.delete(hucreDegerleri["44"], numpy.where(hucreDegerleri["44"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["65"] = numpy.delete(hucreDegerleri["65"], numpy.where(hucreDegerleri["65"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["68"] = numpy.delete(hucreDegerleri["68"], numpy.where(hucreDegerleri["68"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["71"] = numpy.delete(hucreDegerleri["71"], numpy.where(hucreDegerleri["71"] == m))
                    except:
                        pass

            if sayac == 5:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["12"] = numpy.delete(hucreDegerleri["12"], numpy.where(hucreDegerleri["12"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["15"] = numpy.delete(hucreDegerleri["15"], numpy.where(hucreDegerleri["15"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["18"] = numpy.delete(hucreDegerleri["18"], numpy.where(hucreDegerleri["18"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["39"] = numpy.delete(hucreDegerleri["39"], numpy.where(hucreDegerleri["39"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["42"] = numpy.delete(hucreDegerleri["42"], numpy.where(hucreDegerleri["42"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["45"] = numpy.delete(hucreDegerleri["45"], numpy.where(hucreDegerleri["45"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["66"] = numpy.delete(hucreDegerleri["66"], numpy.where(hucreDegerleri["66"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["69"] = numpy.delete(hucreDegerleri["69"], numpy.where(hucreDegerleri["69"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["72"] = numpy.delete(hucreDegerleri["72"], numpy.where(hucreDegerleri["72"] == m))
                    except:
                        pass

            if sayac == 6:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["19"] = numpy.delete(hucreDegerleri["19"], numpy.where(hucreDegerleri["19"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["22"] = numpy.delete(hucreDegerleri["22"], numpy.where(hucreDegerleri["22"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["25"] = numpy.delete(hucreDegerleri["25"], numpy.where(hucreDegerleri["25"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["46"] = numpy.delete(hucreDegerleri["46"], numpy.where(hucreDegerleri["46"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["49"] = numpy.delete(hucreDegerleri["49"], numpy.where(hucreDegerleri["49"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["52"] = numpy.delete(hucreDegerleri["52"], numpy.where(hucreDegerleri["52"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["73"] = numpy.delete(hucreDegerleri["73"], numpy.where(hucreDegerleri["73"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["76"] = numpy.delete(hucreDegerleri["76"], numpy.where(hucreDegerleri["76"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["79"] = numpy.delete(hucreDegerleri["79"], numpy.where(hucreDegerleri["79"] == m))
                    except:
                        pass

            if sayac == 7:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["20"] = numpy.delete(hucreDegerleri["20"], numpy.where(hucreDegerleri["20"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["23"] = numpy.delete(hucreDegerleri["23"], numpy.where(hucreDegerleri["23"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["26"] = numpy.delete(hucreDegerleri["26"], numpy.where(hucreDegerleri["26"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["47"] = numpy.delete(hucreDegerleri["47"], numpy.where(hucreDegerleri["47"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["50"] = numpy.delete(hucreDegerleri["50"], numpy.where(hucreDegerleri["50"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["53"] = numpy.delete(hucreDegerleri["53"], numpy.where(hucreDegerleri["53"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["74"] = numpy.delete(hucreDegerleri["74"], numpy.where(hucreDegerleri["74"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["77"] = numpy.delete(hucreDegerleri["77"], numpy.where(hucreDegerleri["77"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["80"] = numpy.delete(hucreDegerleri["80"], numpy.where(hucreDegerleri["80"] == m))
                    except:
                        pass

            if sayac == 8:
                if len(numpy.where(x == m)[0]) == 0:
                    try:
                        hucreDegerleri["21"] = numpy.delete(hucreDegerleri["21"], numpy.where(hucreDegerleri["21"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["24"] = numpy.delete(hucreDegerleri["24"], numpy.where(hucreDegerleri["24"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["27"] = numpy.delete(hucreDegerleri["27"], numpy.where(hucreDegerleri["27"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["48"] = numpy.delete(hucreDegerleri["48"], numpy.where(hucreDegerleri["48"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["51"] = numpy.delete(hucreDegerleri["51"], numpy.where(hucreDegerleri["51"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["54"] = numpy.delete(hucreDegerleri["54"], numpy.where(hucreDegerleri["54"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["75"] = numpy.delete(hucreDegerleri["75"], numpy.where(hucreDegerleri["75"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["78"] = numpy.delete(hucreDegerleri["78"], numpy.where(hucreDegerleri["78"] == m))
                    except:
                        pass
                    try:
                        hucreDegerleri["81"] = numpy.delete(hucreDegerleri["81"], numpy.where(hucreDegerleri["81"] == m))
                    except:
                        pass

while True:
    for i in sudoku:
        for sayac,x in enumerate(i):
            for nsayac,n in enumerate(x):
                if n==0:
                    if sayac <3:
                        yatayDeger = ceil((nsayac + 1) / 3) - 1
                    elif sayac <6:
                        yatayDeger = ceil((nsayac + 1) / 3) + 2
                    elif sayac <9:
                        yatayDeger = ceil((nsayac + 1) / 3) + 5

                    if sayac == 0 or sayac == 3 or sayac == 6:
                        if nsayac == 0 or nsayac == 3 or nsayac == 6:
                            dikeyDeger = 0
                        elif nsayac == 1 or nsayac == 4 or nsayac == 7:
                            dikeyDeger = 1
                        elif nsayac == 2 or nsayac == 5 or nsayac == 8:
                            dikeyDeger = 2

                    elif sayac == 1 or sayac == 4 or sayac == 7:
                        if nsayac == 0 or nsayac == 3 or nsayac == 6:
                            dikeyDeger = 3
                        elif nsayac == 1 or nsayac == 4 or nsayac == 7:
                            dikeyDeger = 4
                        elif nsayac == 2 or nsayac == 5 or nsayac == 8:
                            dikeyDeger = 5

                    elif sayac == 2 or sayac == 5 or sayac == 8:
                        if nsayac == 0 or nsayac == 3 or nsayac == 6:
                            dikeyDeger = 6
                        elif nsayac == 1 or nsayac == 4 or nsayac == 7:
                            dikeyDeger = 7
                        elif nsayac == 2 or nsayac == 5 or nsayac == 8:
                            dikeyDeger = 8

                    rakam=numpy.intersect1d(numpy.intersect1d(yatayAlabilecegiDegerler[0][yatayDeger], dikeyAlabilecegiDegerler[0][dikeyDeger]),kareninAlabilecegiDegerler[0][sayac])
                    try:
                        rakam=numpy.delete(rakam,numpy.where(rakam==0))
                    except:
                        pass
                    if len(rakam)==1:
                        sudoku[0][sayac][nsayac]=rakam
                        yatayAlabilecegiDegerler[0][yatayDeger]=numpy.append(numpy.delete(yatayAlabilecegiDegerler[0][yatayDeger], numpy.where(yatayAlabilecegiDegerler[0][yatayDeger] == rakam)),0)
                        dikeyAlabilecegiDegerler[0][dikeyDeger]=numpy.append(numpy.delete(dikeyAlabilecegiDegerler[0][dikeyDeger], numpy.where(dikeyAlabilecegiDegerler[0][dikeyDeger] == rakam)),0)
                        kareninAlabilecegiDegerler[0][sayac]=numpy.append(numpy.delete(kareninAlabilecegiDegerler[0][sayac], numpy.where(kareninAlabilecegiDegerler[0][sayac] == rakam)),0)
                    hucreDegeriHesapla()
                    #print(sudoku)


    for x in range(1,82):
        try:
            if x == 1 or x == 4 or x == 7 or x == 28 or x == 31 or x == 34 or x == 55 or x == 58 or x == 61:
                dikeyDeger=0
            elif x == 2 or x == 5 or x == 8 or x == 29 or x == 32 or x == 35 or x == 56 or x == 59 or x == 62:
                dikeyDeger=1
            elif x == 3 or x == 6 or x == 9 or x == 30 or x == 33 or x == 36 or x == 57 or x == 60 or x == 63:
                dikeyDeger=2
            elif x == 10 or x == 13 or x == 16 or x == 37 or x == 40 or x == 43 or x == 64 or x == 67 or x == 70:
                dikeyDeger=3
            elif x == 11 or x == 14 or x == 17 or x == 38 or x == 41 or x == 44 or x == 65 or x == 68 or x == 71:
                dikeyDeger=4
            elif x == 12 or x == 15 or x == 18 or x == 39 or x == 42 or x == 45 or x == 66 or x == 69 or x == 72:
                dikeyDeger=5
            elif x == 19 or x == 22 or x == 25 or x == 46 or x == 49 or x == 52 or x == 73 or x == 76 or x == 79:
                dikeyDeger=6
            elif x == 20 or x == 23 or x == 26 or x == 47 or x == 50 or x == 53 or x == 74 or x == 77 or x == 80:
                dikeyDeger=7
            elif x == 21 or x == 24 or x == 27 or x == 48 or x == 51 or x == 54 or x == 75 or x == 78 or x == 81:
                dikeyDeger=8

            if x == 1 or x == 2 or x == 3 or x == 10 or x == 11 or x == 12 or x == 19 or x == 20 or x == 21:
                yatayDeger=0
            elif x == 4 or x == 5 or x == 6 or x == 13 or x == 14 or x == 15 or x == 22 or x == 23 or x == 24:
                yatayDeger=1
            elif x == 7 or x == 8 or x == 9 or x == 16 or x == 17 or x == 18 or x == 25 or x == 26 or x == 27:
                yatayDeger=2
            elif x == 28 or x == 29 or x == 30 or x == 37 or x == 38 or x == 39 or x == 46 or x == 47 or x == 40:
                yatayDeger=3
            elif x == 31 or x == 32 or x == 33 or x == 40 or x == 41 or x == 42 or x == 49 or x == 50 or x == 51:
                yatayDeger=4
            elif x == 34 or x == 35 or x == 38 or x == 43 or x == 44 or x == 45 or x == 52 or x == 53 or x == 54:
                yatayDeger=5
            elif x == 55 or x == 56 or x == 57 or x == 64 or x == 65 or x == 66 or x == 73 or x == 74 or x == 75:
                yatayDeger=6
            elif x == 58 or x == 59 or x == 60 or x == 67 or x == 68 or x == 69 or x == 76 or x == 77 or x == 78:
                yatayDeger=7
            elif x == 61 or x == 62 or x == 63 or x == 70 or x == 71 or x == 72 or x == 79 or x == 80 or x == 81:
                yatayDeger=8
            if len(hucreDegerleri[f"{x}"])==1:
                sudoku[0][int(str(x / 9.00000009).split(".")[0])][int(list(str(x / 9.00000009).split(".")[1])[0]) - 1] = hucreDegerleri[f"{x}"][0]
                yatayAlabilecegiDegerler[0][yatayDeger] = numpy.append(numpy.delete(yatayAlabilecegiDegerler[0][yatayDeger],numpy.where(yatayAlabilecegiDegerler[0][yatayDeger] == hucreDegerleri[f"{x}"][0])),0)
                dikeyAlabilecegiDegerler[0][dikeyDeger] = numpy.append(numpy.delete(dikeyAlabilecegiDegerler[0][dikeyDeger],numpy.where(dikeyAlabilecegiDegerler[0][dikeyDeger] == hucreDegerleri[f"{x}"][0])), 0)
                kareninAlabilecegiDegerler[0][int(str(x / 9.00000009).split(".")[0])] = numpy.append(numpy.delete(kareninAlabilecegiDegerler[0][int(str(x / 9.00000009).split(".")[0])],numpy.where(kareninAlabilecegiDegerler[0][int(str(x / 9.00000009).split(".")[0])] == hucreDegerleri[f"{x}"][0])), 0)
                hucreDegeriHesapla()

            elif len(hucreDegerleri[f"{x}"])==0:
                del hucreDegerleri[f"{x}"]
            hucreninIcindekiDegerSayisi=len(hucreDegerleri[f"{x}"])
            hucreninIcindekiYatayDegerKontrol=[]
            hucreninIcindekiDikeyDegerKontrol = []
            if x == 1:
                hucreninIcindekiYatayDegerler=[2,3,10,11,12,19,20,21]
                hucreninIcindekiDikeyDegerler=[4,7,28,34,33,55,58,61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 2:
                hucreninIcindekiYatayDegerler = [1, 3, 10, 11, 12, 19, 20, 21]
                hucreninIcindekiDikeyDegerler = [5, 8, 29, 32, 35, 56, 59, 62]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 3:
                hucreninIcindekiYatayDegerler = [1, 2, 10, 11, 12, 19, 20, 21]
                hucreninIcindekiDikeyDegerler = [6, 9, 30, 33, 36, 57, 60, 63]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 4:
                hucreninIcindekiYatayDegerler = [5, 6, 13, 14, 15, 22, 23, 24]
                hucreninIcindekiDikeyDegerler = [1, 7, 28, 31, 34, 55, 58, 61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 5:
                hucreninIcindekiYatayDegerler = [4, 6, 13, 14, 15, 22, 23, 24]
                hucreninIcindekiDikeyDegerler = [2, 8, 29, 32, 35, 56, 59, 62]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 6:
                hucreninIcindekiYatayDegerler = [4, 5, 13, 14, 15, 22, 23, 24]
                hucreninIcindekiDikeyDegerler = [3, 9, 30, 33, 36, 57, 60, 63]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 7:
                hucreninIcindekiYatayDegerler = [8, 9, 16, 17, 18, 25, 26, 27]
                hucreninIcindekiDikeyDegerler = [1, 4, 28, 31, 34, 55, 58, 61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 8:
                hucreninIcindekiYatayDegerler = [7, 9, 16, 17, 18, 25, 26, 27]
                hucreninIcindekiDikeyDegerler = [2, 5, 29, 32, 35, 56, 59, 62]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 9:
                hucreninIcindekiYatayDegerler = [7, 8, 16, 17, 18, 25, 26, 27]
                hucreninIcindekiDikeyDegerler = [3, 6, 30, 33, 36, 57, 60, 63]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 10:
                hucreninIcindekiYatayDegerler = [1, 2, 3, 11, 12, 19, 20, 21]
                hucreninIcindekiDikeyDegerler = [13, 16, 37, 40, 43, 64, 67, 70]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 11:
                hucreninIcindekiYatayDegerler = [1, 2, 3, 10, 12, 19, 20, 21]
                hucreninIcindekiDikeyDegerler = [14,17,38,41,44,65,68,71]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 12:
                hucreninIcindekiYatayDegerler = [1, 2, 3, 10, 11, 19, 20, 21]
                hucreninIcindekiDikeyDegerler = [15, 18, 39, 42, 45, 66, 69, 72]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 13:
                hucreninIcindekiYatayDegerler = [4, 5, 6, 14, 15, 22, 23, 24]
                hucreninIcindekiDikeyDegerler = [10, 16, 37, 40, 43, 64, 67, 70]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 14:
                hucreninIcindekiYatayDegerler = [4, 5, 6, 13, 15, 22, 23, 24]
                hucreninIcindekiDikeyDegerler = [11, 17, 38, 41, 44, 65, 68, 71]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 15:
                hucreninIcindekiYatayDegerler = [4,5,6,13,14,22, 23, 24]
                hucreninIcindekiDikeyDegerler = [12,18,39,42,45,66,69,72]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 16:
                hucreninIcindekiYatayDegerler = [7,8,9,17, 18, 25, 26, 27]
                hucreninIcindekiDikeyDegerler = [10,13,37,40,43,64,67,70]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 17:
                hucreninIcindekiYatayDegerler = [7,8,9,16,18, 25, 26, 27]
                hucreninIcindekiDikeyDegerler = [11,14,38,41,44,65,68,71]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 18:
                hucreninIcindekiYatayDegerler = [7,8,9,16,17,18,25, 26, 27]
                hucreninIcindekiDikeyDegerler = [12,15,39,42,45,66,69,72]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 19:
                hucreninIcindekiYatayDegerler = [1,2,3,10,11,12,20, 21]
                hucreninIcindekiDikeyDegerler = [22,25,46,49,52,73,76,79]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 20:
                hucreninIcindekiYatayDegerler = [1,2,3,10,11,12,19,21]
                hucreninIcindekiDikeyDegerler = [23,26,47,50,53,74,77,80]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 21:
                hucreninIcindekiYatayDegerler = [1,2,3,10,11,12,19,20]
                hucreninIcindekiDikeyDegerler = [24,27,48,51,54,75,78,81]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 22:
                hucreninIcindekiYatayDegerler = [4,5,6,13,14, 15, 23, 24]
                hucreninIcindekiDikeyDegerler = [19,25,46,49,52,73,76,79]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 23:
                hucreninIcindekiYatayDegerler = [4,5,6,13,14,15,22,24]
                hucreninIcindekiDikeyDegerler = [20,26,47,50,53,74,77,80]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 24:
                hucreninIcindekiYatayDegerler = [4,5,6,13,14,15,22,23]
                hucreninIcindekiDikeyDegerler = [21,27,48,51,54,75,78,81]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 25:
                hucreninIcindekiYatayDegerler = [7,8,9,16,17,18,26, 27]
                hucreninIcindekiDikeyDegerler = [19,22,46,49,52,73,76,79]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 26:
                hucreninIcindekiYatayDegerler = [7,8,9,16,17,18,25,27]
                hucreninIcindekiDikeyDegerler = [20,23,47,50,53,74,77,80]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 27:
                hucreninIcindekiYatayDegerler = [7,8,9,16,17,18,25,26]
                hucreninIcindekiDikeyDegerler = [21,24,48,51,54,75,78,81]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 28:
                hucreninIcindekiYatayDegerler=[29,30,37,38,39,46,47,48]
                hucreninIcindekiDikeyDegerler=[1,4,7,31,34,55,58,61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 29:
                hucreninIcindekiYatayDegerler = [28,30,37,38,39,46,47,48]
                hucreninIcindekiDikeyDegerler = [2,5,8,32, 35, 56, 59, 62]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 30:
                hucreninIcindekiYatayDegerler = [28,29,37,38,39,46,47,48]
                hucreninIcindekiDikeyDegerler = [3,6,9,33, 36, 57, 60, 63]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 31:
                hucreninIcindekiYatayDegerler = [32,33,40,41,42,49,50,51]
                hucreninIcindekiDikeyDegerler = [1,4,7,28,34, 55, 58, 61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 32:
                hucreninIcindekiYatayDegerler = [31,33,40,41,42,49,50,51]
                hucreninIcindekiDikeyDegerler = [2,5,8,29,35, 56, 59, 62]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 33:
                hucreninIcindekiYatayDegerler = [31,32,40,41,42,49,50,51]
                hucreninIcindekiDikeyDegerler = [3,6,9,30,36, 57, 60, 63]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 34:
                hucreninIcindekiYatayDegerler = [35,36,43,44,45,52,53,54]
                hucreninIcindekiDikeyDegerler = [1,4,7,28,31,55, 58, 61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 35:
                hucreninIcindekiYatayDegerler = [34,36,43,44,45,52,53,54]
                hucreninIcindekiDikeyDegerler = [2,5,8,29,32,56, 59, 62]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 36:
                hucreninIcindekiYatayDegerler = [34,35,43,44,45,52,53,54]
                hucreninIcindekiDikeyDegerler = [3,6,9,30,33,57, 60, 63]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 37:
                hucreninIcindekiYatayDegerler = [28,29,30,38,39,46,47,48]
                hucreninIcindekiDikeyDegerler = [10,13,16,40,43,64,67,70]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 38:
                hucreninIcindekiYatayDegerler = [28,29,30,37,39,46,47,48]
                hucreninIcindekiDikeyDegerler = [11,14,17,41,44,65,68,71]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 39:
                hucreninIcindekiYatayDegerler = [28,29,30,37,38,46,47,48]
                hucreninIcindekiDikeyDegerler = [12,15,18,42,45,66,69,72]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 40:
                hucreninIcindekiYatayDegerler = [31,32,33,41,42,49,50,51]
                hucreninIcindekiDikeyDegerler = [10,13,16,37,43,64,67,70]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 41:
                hucreninIcindekiYatayDegerler = [31,32,33,40,42,49,50,51]
                hucreninIcindekiDikeyDegerler = [11,14,17,38,44,65,68,71]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 42:
                hucreninIcindekiYatayDegerler = [31,32,33,40,41,49,50,51]
                hucreninIcindekiDikeyDegerler = [12,15,18,39,45,66,69,72]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 43:
                hucreninIcindekiYatayDegerler = [34,35,36,44,45,52,53,54]
                hucreninIcindekiDikeyDegerler = [10,13,16,37,40,64,67,70]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 44:
                hucreninIcindekiYatayDegerler = [34,35,36,43,45,52,53,54]
                hucreninIcindekiDikeyDegerler = [11,14,17,38,41,65,68,71]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 45:
                hucreninIcindekiYatayDegerler = [34,35,36,43,44,52,53,54]
                hucreninIcindekiDikeyDegerler = [12,15,18,39,42,66,69,72]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 46:
                hucreninIcindekiYatayDegerler = [28,29,30,37,38,39,47,48]
                hucreninIcindekiDikeyDegerler = [19,22,25,49,52,73,76,79]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 47:
                hucreninIcindekiYatayDegerler = [28,29,30,37,38,39,46,48]
                hucreninIcindekiDikeyDegerler = [20,23,26,50,53,74,77,80]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 48:
                hucreninIcindekiYatayDegerler = [28,29,30,37,38,39,46,47]
                hucreninIcindekiDikeyDegerler = [21,24,27,51,54,75,78,81]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 49:
                hucreninIcindekiYatayDegerler = [31,32,33,40,41,42,50, 51]
                hucreninIcindekiDikeyDegerler = [19,22,25,46,52,73,76,79]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 50:
                hucreninIcindekiYatayDegerler = [31,32,33,40,41,42,49,51]
                hucreninIcindekiDikeyDegerler = [20,23,26,47,53,74,77,80]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 51:
                hucreninIcindekiYatayDegerler = [31,32,33,40,41,42,49,50]
                hucreninIcindekiDikeyDegerler = [21,24,27,48,54,75,78,81]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 52:
                hucreninIcindekiYatayDegerler = [34,35,36,43,44,45,53, 54]
                hucreninIcindekiDikeyDegerler = [19,22,25,46,49,73,76,79]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 53:
                hucreninIcindekiYatayDegerler = [34,35,36,43,44,45,52,54]
                hucreninIcindekiDikeyDegerler = [20,23,26,47,50,74,77,80]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 54:
                hucreninIcindekiYatayDegerler = [34,35,36,43,44,45,52,53]
                hucreninIcindekiDikeyDegerler = [21,24,27,48,51,75,78,81]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 55:
                hucreninIcindekiYatayDegerler=[56,57,64,65,66,73,74,75]
                hucreninIcindekiDikeyDegerler=[1,4,7,28,31,34,58,61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 56:
                hucreninIcindekiYatayDegerler = [55,57,64,65,66,73,74,75]
                hucreninIcindekiDikeyDegerler = [2,5,8,29,32,35,59, 62]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 57:
                hucreninIcindekiYatayDegerler = [55,56,64,65,66,73,74,75]
                hucreninIcindekiDikeyDegerler = [3,6,9,30,33, 36, 60, 63]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 58:
                hucreninIcindekiYatayDegerler = [59,60,67,68,69,76,77,78]
                hucreninIcindekiDikeyDegerler = [1,4,7,28,31,34,55,61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 59:
                hucreninIcindekiYatayDegerler = [58,60,67,68,69,76,77,78]
                hucreninIcindekiDikeyDegerler = [2,5,8,29,32,35,56,62]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 60:
                hucreninIcindekiYatayDegerler = [58,59,67,68,69,76,77,78]
                hucreninIcindekiDikeyDegerler = [3,6,9,30,33,36,57,63]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 61:
                hucreninIcindekiYatayDegerler = [62,63,70,71,72,79,80,81]
                hucreninIcindekiDikeyDegerler = [1,4,7,28,31,34,55,58,61]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 62:
                hucreninIcindekiYatayDegerler = [61,63,70,71,72,79,80,81]
                hucreninIcindekiDikeyDegerler = [2,5,8,29,32,35,56,59]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 63:
                hucreninIcindekiYatayDegerler = [61,62,70,71,72,79,80,81]
                hucreninIcindekiDikeyDegerler = [3,6,9,30,33,36,57,60]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 64:
                hucreninIcindekiYatayDegerler = [55,56,57,65,66,73,74,75]
                hucreninIcindekiDikeyDegerler = [10,13,16,37,40,43,67,70]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 65:
                hucreninIcindekiYatayDegerler = [55,56,57,64,66,73,74,75]
                hucreninIcindekiDikeyDegerler = [11,14,17,38,41,44,68,71]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 66:
                hucreninIcindekiYatayDegerler = [55,56,57,64,65,73,74,75]
                hucreninIcindekiDikeyDegerler = [12,15,18,39,42,45,69,72]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 67:
                hucreninIcindekiYatayDegerler = [58,59,60,68,69,76,77,78]
                hucreninIcindekiDikeyDegerler = [10,13,16,37,40,43,64,70]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 68:
                hucreninIcindekiYatayDegerler = [58,59,60,67,69,76,77,78]
                hucreninIcindekiDikeyDegerler = [11,14,17,38,41,44,65,71]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 69:
                hucreninIcindekiYatayDegerler = [58,59,60,67,68,76,77,78]
                hucreninIcindekiDikeyDegerler = [12,15,18,39,42,45,66,72]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 70:
                hucreninIcindekiYatayDegerler = [61,62,63,71,72,79,80,81]
                hucreninIcindekiDikeyDegerler = [10,13,16,37,40,43,64,67]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 71:
                hucreninIcindekiYatayDegerler = [61,62,63,70,72,79,80,81]
                hucreninIcindekiDikeyDegerler = [11,14,17,38,41,44,65,68]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 72:
                hucreninIcindekiYatayDegerler = [61,62,63,70,71,79,80,81]
                hucreninIcindekiDikeyDegerler = [12,15,18,39,42,45,66,69]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 73:
                hucreninIcindekiYatayDegerler = [55,56,57,64,65,66,74,75]
                hucreninIcindekiDikeyDegerler = [19,22,25,46,49,52,76,79]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 74:
                hucreninIcindekiYatayDegerler = [55,56,57,64,65,66,73,75]
                hucreninIcindekiDikeyDegerler = [20,23,26,47,50,53,77,80]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 75:
                hucreninIcindekiYatayDegerler = [55,56,57,64,65,66,73,74]
                hucreninIcindekiDikeyDegerler = [21,24,27,48,51,54,78,81]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 76:
                hucreninIcindekiYatayDegerler = [58,59,60,67,68,69,77,78]
                hucreninIcindekiDikeyDegerler = [19,22,25,46,49,52,73,79]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 77:
                hucreninIcindekiYatayDegerler = [58,59,60,67,68,69,76,78]
                hucreninIcindekiDikeyDegerler = [20,23,26,47,50,53,74,80]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 78:
                hucreninIcindekiYatayDegerler = [58,59,60,67,68,69,76,77]
                hucreninIcindekiDikeyDegerler = [21,24,27,48,51,54,75,81]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 79:
                hucreninIcindekiYatayDegerler = [61,62,63,70,71,72,80,81]
                hucreninIcindekiDikeyDegerler = [19,22,25,46,49,52,73,76]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 80:
                hucreninIcindekiYatayDegerler = [61,62,63,70,71,72,79,81]
                hucreninIcindekiDikeyDegerler = [20,23,26,47,50,53,74,77]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            elif x == 81:
                hucreninIcindekiYatayDegerler = [61,62,63,70,71,72,79,80]
                hucreninIcindekiDikeyDegerler = [21,24,27,48,51,54,75,78]
                for s in hucreninIcindekiYatayDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiYatayDegerKontrol.append(i)
                                hucreninIcindekiYatayDegerler.remove(s)
                    except:
                        pass
                for s in hucreninIcindekiDikeyDegerler:
                    try:
                        if numpy.array_equal(hucreDegerleri[f"{x}"], hucreDegerleri[f"{s}"]) == True:
                            for i in hucreDegerleri[f"{x}"]:
                                hucreninIcindekiDikeyDegerKontrol.append(i)
                                hucreninIcindekiDikeyDegerler.remove(s)
                    except:
                        pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiYatayDegerKontrol):
                    for a in hucreninIcindekiYatayDegerler:
                        for b in hucreninIcindekiYatayDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
                if hucreninIcindekiDegerSayisi == len(hucreninIcindekiDikeyDegerKontrol):
                    for a in hucreninIcindekiDikeyDegerler:
                        for b in hucreninIcindekiDikeyDegerKontrol:
                            try:
                                hucreDegerleri[f"{a}"] = numpy.delete(hucreDegerleri[f"{a}"], numpy.where(hucreDegerleri[f"{a}"] == b))
                            except:
                                pass
            if len(hucreDegerleri[f"{x}"])==1:
                sudoku[0][int(str(x / 9.00000009).split(".")[0])][int(list(str(x / 9.00000009).split(".")[1])[0]) - 1] = hucreDegerleri[f"{x}"][0]
                yatayAlabilecegiDegerler[0][yatayDeger] = numpy.append(numpy.delete(yatayAlabilecegiDegerler[0][yatayDeger],numpy.where(yatayAlabilecegiDegerler[0][yatayDeger] == hucreDegerleri[f"{x}"][0])),0)
                dikeyAlabilecegiDegerler[0][dikeyDeger] = numpy.append(numpy.delete(dikeyAlabilecegiDegerler[0][dikeyDeger],numpy.where(dikeyAlabilecegiDegerler[0][dikeyDeger] == hucreDegerleri[f"{x}"][0])), 0)
                kareninAlabilecegiDegerler[0][int(str(x / 9.00000009).split(".")[0])] = numpy.append(numpy.delete(kareninAlabilecegiDegerler[0][int(str(x / 9.00000009).split(".")[0])],numpy.where(kareninAlabilecegiDegerler[0][int(str(x / 9.00000009).split(".")[0])] == hucreDegerleri[f"{x}"][0])), 0)
                hucreDegeriHesapla()
            elif len(hucreDegerleri[f"{x}"])==0:
                del hucreDegerleri[f"{x}"]
        except:
            pass
    if len(numpy.where(sudoku==0)[2])==0:
        print(sudoku)
        break

