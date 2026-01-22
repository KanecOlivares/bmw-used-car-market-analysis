import sys
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def is_debug_mode():
    return debug == 1

def activate_debug():
    global debug
    if (len(sys.argv)) > 1:
        debug = sys.argv[1]
    else:
        debug = 1 # default to debug mode currently


def init_data():
    global data
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "bmw.csv"
    if (is_debug_mode):
        print(f'Current Working Dir: {BASE_DIR}')
        print(f'Data Path: {data_path}')

    data = pd.read_csv(data_path)

def init():
    activate_debug()
    init_data()
    sns.set_theme()

def inital_data_exploration():
    if (is_debug_mode()):
        print(f'Data shape: {data.shape()}')

def main():
    init()
    inital_data_exploration()

main()