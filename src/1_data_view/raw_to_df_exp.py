import pandas as pd
from util.global_constant import RAW_DATA_PATH

file = open(RAW_DATA_PATH + "totalExposureLog.out")

line = file.readline()

print(line.split())


