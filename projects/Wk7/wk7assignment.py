import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('school_students.csv')
print(df.head())  # Displays the first few rows of the DataFrame
print(df.info())# Displays the number of rows and columns
print(df.describe())  # Shows mean, std, min, max, and quartiles for numerical columns
print(df.shape)
print(df.groupby('Stream').mean(numeric_only=True))  # Mean scores by stream
print(df.groupby('Stream')['Average'].mean())  # Mean of 'Average' column by stream


#Line Plot
def line_plot():
    plt.figure()
    stream_means = df.groupby('Stream')['Average'].mean()
    plt.plot(stream_means.index, stream_means.values)
    plt.xlabel('Stream')
    plt.ylabel('Average Score')
    plt.title('Average Score by Stream')
    plt.savefig('line_plot.png')  # Saves the plot as a PNG file
    plt.close()

#Bar Graph
def bar_graph():
    plt.figure()
    grouped_means = df.groupby('Stream')['Average'].mean()
    grouped_means.plot(kind='bar', color='skyblue')
    plt.xlabel('Strams')
    plt.ylabel('Average Score')
    plt.title('Average Scores by Streams')
    plt.savefig('bar_graph.png')
    plt.close()

#Histogram
def histogram():
    plt.figure()
    df['Average'].plot(kind='hist', bins=10, color='lightgreen', edgecolor='black')
    plt.xlabel('Average Scores')
    plt.title('Distribution of Scores')
    plt.savefig('histogram.png')
    plt.close()

#Scatter Plot
def scatter_plot():
    plt.figure()
    stream_means = df.groupby('Stream')['Average'].mean()
    plt.scatter(stream_means.index, stream_means.values)
    plt.xlabel('Stream')
    plt.ylabel('Average Score')
    plt.title('Average Score by Stream')
    plt.savefig('scatter_plot.png')
    plt.close()

line_plot()
bar_graph()
histogram()
scatter_plot()
print("Plots saved as PNG files. Thank you for using the data visualization tool!")