
import time
import pandas as pd
import bisect
import numpy as np 
import time
import pandas as pd
import bisect
import os


def timeCaculator(startTime):
    endTime = time.time()
    elapsedTime = endTime - startTime
    formattedElapsedTime = f'{elapsedTime:.6f}'
    return formattedElapsedTime

def csv(binary,senquential,bisect,name):
    df = pd.read_csv(f'{name}.csv')
    df.loc[len(df)] = [binary,senquential,bisect]
    df.to_csv(f'{name}.csv', index=False)


def binarySearch(lst, num):

    startTimeBinarySearch = time.time()


    start = 0 
    end = len(lst) - 1

    while start <= end:
        midle = (start + end) // 2

        if lst[midle] == num:
            elapsedTimeBinarySearch = timeCaculator(startTimeBinarySearch)
            return midle, elapsedTimeBinarySearch
        
        elif lst[midle] < num:
            start = midle + 1
            
        else:
            end = midle - 1

    elapsedTimeBinarySearch = timeCaculator(startTimeBinarySearch)

    return -1,elapsedTimeBinarySearch

def sequentialSerach(lst,num):
    startTimeSequentialSearch = time.time()

    for x in lst:
        if x == num: 
            elapsedTimeSequential = timeCaculator(startTimeSequentialSearch)
            return x, elapsedTimeSequential
        
    elapsedTimeSequential = timeCaculator(startTimeSequentialSearch)
    return -1, elapsedTimeSequential

def bisectSearch(lst,num):
    startTimeBisect = time.time()

    index = bisect.bisect(lst,num)

    if index < len(lst) and lst[index] == num:
        return index ,timeCaculator(startTimeBisect)
    
    elapsedTimeBisect = timeCaculator(startTimeBisect)
    return -1, elapsedTimeBisect


def numpySearch(lst,num):
    startNumpy = time.time()
    index = np.searchsorted(lst,num)
    if index == num:
        elapsedNumpy = timeCaculator(startNumpy)
        return index, elapsedNumpy
    
    elapsedNumpy = timeCaculator(startNumpy)
    return -1, elapsedNumpy


def resultsFromBisect(lst,num):
    resultBisect, timeTraveleedFromBisect = bisectSearch(lst,num)

    if resultBisect != -1:
        print(f'o elemento foi encontrado no indice{resultBisect}')
    else:
        print('O elemento não foi encontrado na lista.')

    
    print(f'tempo percorrido foi de {timeTraveleedFromBisect} segungos')  
    print()
    return timeTraveleedFromBisect


def resultsFromBinary(lst,num):
    resultBinary, timeTraveledFromBinarySearch = binarySearch(lst, num)

    if resultBinary != -1:
        print(f'O elemento foi encontrado no índice {resultBinary}.')
    else:
        print('O elemento não foi encontrado na lista.')


    print(f'tempo percorrido foi de {timeTraveledFromBinarySearch} segungos')
    print()
    return timeTraveledFromBinarySearch


def resultsFromSequential(lst,num):
    resultSequential, timeTraveledFromSequentialSearch = sequentialSerach(lst,num)

    if resultSequential != -1:
        print(f'O elemento  foi encontrado no indice {resultSequential}')
    else:
        print('O elemento não foi encontrado na lista.')

    print(f'tempo percorrido foi de {timeTraveledFromSequentialSearch} segungos')
    print()
    return timeTraveledFromSequentialSearch

def resultFromNumpy(lst,num):
    resultNumpy, timeTraveledFromNUmpy = numpySearch(lst,num)

    if resultNumpy != -1:
        print(f'O elemento  foi encontrado no indice {resultNumpy}')
    else:
        print('O elemento não foi encontrado na lista.')

    print(f'tempo percorrido foi de {timeTraveledFromNUmpy} segungos')
    print()
    return timeTraveledFromNUmpy


lstRange = 500000
num = 450312

lst = list(range(lstRange))

for x in range(200):
    time.sleep(1)
    csv(resultsFromBinary(lst,num),resultsFromSequential(lst,num),resultsFromBisect(lst,num),lstRange)

    


