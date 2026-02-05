import sys
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

IMAGE_PATH = "images/"
SEED = 1234
DEBUG = 0

def is_debug_mode():
    global DEBUG
    return DEBUG == 1

def activate_debug():
    global DEBUG
    if (len(sys.argv)) > 2:
        DEBUG = int(sys.argv[2])

def activate_seed():
    global SEED, DEBUG
    if (len(sys.argv)) > 1:
        SEED = sys.argv[1]
    else:
        SEED = 1 # default to DEBUG mode currently


def init_data():
    global data
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "bmw.csv"
    if is_debug_mode():
        print(f'Current Working Dir: {BASE_DIR}')
        print(f'Data Path: {data_path}')

    data = pd.read_csv(data_path)

def init():
    activate_debug()
    activate_seed()
    init_data()
    sns.set_theme()

def inital_data_exploration():
    if is_debug_mode():
        print(f'Data shape: {data.shape}\n') # (10781, 9)
        print(f'Top 5 observations \n{data.head()}\n')
        print(f'Last 5 observations \n{data.tail()}\n')
        print(f'Data Types:\n{data.info()}\n') # intreseting finding 
        print(f'Unique values:\n{data.nunique()}\n')
            # A few intresting feature I should check out: Model, fueltype
        print(f'Missing Values:\n{data.isnull().sum()}\n') # no missing values
        print(f'Percentage of Missing Values:\n{(data.isnull().sum()/(len(data)))*100}\n')
    # sns.heatmap(data)

def feature_inspection():
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

def plot_avg_price_by_model(data, output_path="model_avg_price.png"):
    avg_prices = (
          data.groupby("model", as_index=False)["price"]
          .mean()
          .sort_values("price", ascending=False)
      )
    plt.figure(figsize=(10, 6)), \
        sns.barplot(data=avg_prices, x="model", y="price")
    
    plt.xlabel("Model")
    plt.ylabel("Average Price")
    plt.title("Average Price by BMW Model")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def main():
    global data
    init()
    inital_data_exploration()
    if is_debug_mode():
        feature_inspection()
    plot_avg_price_by_model(data, IMAGE_PATH)

main()