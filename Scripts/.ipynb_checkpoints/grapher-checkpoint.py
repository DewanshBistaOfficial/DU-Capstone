import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_line_plot(df, text):
    x = df.index.astype(int)
    plt.figure(figsize=(10, 6))
    for i in df.columns:
        plt.plot(x, df[i], marker='o', label=i)
    plt.title(text + " Over Time")
    plt.xlabel("Year")
    plt.ylabel(text)
    plt.legend()
    plt.grid(True)
    plt.show()

def get_heat_plot(df, text):
    plt.figure(figsize=(6, 4))
    sns.heatmap(df, cmap='coolwarm', linewidths=0.5)
    plt.title(text)
    plt.show()

def graph_all(df, text):
    get_line_plot(df, text)
    get_heat_plot(df, text)