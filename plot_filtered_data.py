#! /usr/bin/env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def plot(species_name):
    """
    This function filters a dataframe for a certain species, runs a linear  regression analysis, and prints out the plot in a png format
    """

    #read in the dataframe
    dataframe = pd.read_csv("iris.csv")

    #filters for a specific species
    df = dataframe[dataframe.species == species_name]

    if df.empty:
        print(f"No data found for species: {species_name}")
        return None

    #assign values to x and y axes
    x = df.petal_length_cm
    y = df.sepal_length_cm

    #do linear regression analysis
    regression = stats.linregress(x, y)

    #make a slope
    slope = regression.slope

    #estimate the intercept
    intercept = regression.intercept

    #make a scatter plot for the analyzed data
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.title(f'{species_name} species')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig(f"{species_name}.png")
    return species_name



if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the species name for which to get the plot")
    species_name = str(sys.argv[1])
    if not species_name:
        sys.exit(sys.argv[0] + ": Expecting a species name")

    plot(species_name)

