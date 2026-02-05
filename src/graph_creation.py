
import sys
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from debug_utils import is_debug_mode

def feature_inspection(data):
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

def plot_avg_price_by_model(data, output_path="model_avg_price.png"):
    """Plot and save average price by model from the provided dataset."""
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

def plot_mileage_distribution(data, output_path="mileage_distribution.png", bins=30):
    """Plot and save a histogram of car mileage distribution."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x="mileage", bins=bins, kde=False)

    plt.xlabel("Mileage")
    plt.ylabel("Count")
    plt.title("Distribution of Car Mileage")
    plt.tight_layout()

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
