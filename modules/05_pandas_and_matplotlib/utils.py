import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename) -> pd.DataFrame:
    df = pd.read_csv(filename)
    return df


def plot_data(dataframe, xcol, ycol, output_filename):

    plt.scatter(dataframe[xcol], dataframe[ycol])
    plt.xlabel(xcol)
    plt.ylabel(ycol)
    plt.title('Scatter Plot')
    plt.axis("on")
    plt.savefig(output_filename) 
    #plt.close()  # Close the plot to free up resources

    print(f"Plot saved as {output_filename}")

