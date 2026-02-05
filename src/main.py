import sys
import inspect
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import graph_creation as graphs

IMAGE_PATH = "images/"
SEED = 1234
DEBUG = 0

def is_debug_mode():
    """Return whether debug mode is enabled."""
    global DEBUG
    return DEBUG == 1

def activate_debug():
    """Set the DEBUG flag from command-line arguments when provided."""
    global DEBUG
    if (len(sys.argv)) > 2:
        DEBUG = int(sys.argv[2])

def activate_seed():
    """Set the random SEED from command-line arguments or fall back to default value shown on top."""
    global SEED, DEBUG
    if (len(sys.argv)) > 1:
        SEED = sys.argv[1]


def init_data(data):
    """Load the BMW dataset into the global data variable."""
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "bmw.csv"
    if is_debug_mode():
        print(f'Current Working Dir: {BASE_DIR}')
        print(f'Data Path: {data_path}')

    return pd.read_csv(data_path)


def init():
    """Initialize runtime settings, load data, and configure plot styling."""
    activate_debug()
    activate_seed()
    data = init_data()
    sns.set_theme()
    return data

def inital_data_exploration(data):
    """Print basic dataset diagnostics when debug mode is enabled."""
    if is_debug_mode():
        print(f'Data shape: {data.shape}\n') # (10781, 9)
        print(f'Top 5 observations \n{data.head()}\n')
        print(f'Last 5 observations \n{data.tail()}\n')
        print(f'Data Types:\n{data.info()}\n') # intreseting finding 
        print(f'Unique values:\n{data.nunique()}\n')
            # A few intresting feature I should check out: Model, fueltype
        print(f'Missing Values:\n{data.isnull().sum()}\n') # no missing values
        print(f'Percentage of Missing Values:\n{(data.isnull().sum()/(len(data)))*100}\n')
    

def feature_inspection():
    """Summarize model counts and render a bar chart of frequencies."""
    if is_debug_mode():
        print(data['model'].value_counts().sort_index())
    model_data = data["model"].to_frame() #
    print(type(model_data))


    if is_debug_mode():
        print(model_data.nunique()) # 24
        print(model_data.value_counts().sort_index(ascending=True)) 

    counts = model_data.value_counts().sort_index()
    counts = counts.reset_index()
    print(counts.info())
    counts.columns = ['model', 'count']
    sns.set_color_codes("pastel")
    ax = sns.barplot(data=counts, x='count', y='model')
    plt.savefig("model_plot.png", dpi=300, bbox_inches="tight")
    plt.show()

def plot_all_plots(input_data, image_dir_path, excluded: list):
    all_functions = inspect.getmembers(graphs, inspect.isfunction)
    
    for func_name, plot_graph in all_functions:
        if  func_name in excluded:
            continue
        else:
            plot_graph(input_data, image_dir_path)




def main():
    """Run the full analysis workflow and produce plots."""
    global data
    init()
    inital_data_exploration()
    if is_debug_mode():
        feature_inspection()
        plot_all_plots()
    

main()
