import numpy
from math import ceil

sudoku=numpy.array\
(
    [
        [
            [0, 2, 4, 0, 0, 7, 8, 3, 0],
            [8, 0, 7, 0, 9, 0, 5, 0, 0],
            [0, 5, 0, 2, 0, 0, 0, 0, 0],

            [0, 4, 6, 3, 0, 0, 0, 1, 8],
            [0, 5, 0, 0, 0, 0, 0, 7, 0],
            [8, 9, 0, 0, 0, 7, 3, 6, 0],

            [0, 0, 0, 0, 0, 2, 0, 6, 0],
            [0, 0, 1, 0, 6, 0, 2, 0, 3],
            [0, 8, 2, 1, 0, 0, 5, 7, 0]




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

    if len(numpy.where(sudoku==0)[2])==0:
        print(sudoku)
        break