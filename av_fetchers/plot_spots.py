import pandas as pd
import matplotlib.pyplot as plt

def plot_spots(spots):
	spots = pd.Series(spots).astype(float)
	spots.index = pd.to_datetime(spots.index)
	plt.figure()
	plt.plot(spots,color='black')
	plt.xticks(rotation=45)
	plt.show()
