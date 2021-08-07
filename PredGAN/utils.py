"""
General utility functions used for auxiliary tasks.

"""

import matplotlib.pyplot as plt
import numpy as np

__author__  = "Mustapha Jolaade"
__credits__ = ["Vinicius Santos Silva"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mustapha Jolaade"
__email__ = "mustapha.jolaade20@imperial.ac.uk"
__status__ = "Development"


def plot_vortex(data, times, cols, rows=1, save_dir='vortex_plot.png'):

  """ 
  Plots the spatial-temporal distribution of vorticity.

  Args:
    data (ndarray): time-continuous series of vortex data to plot
    times (list):   specific time snapshot to plot
    cols (int):     columns of subplot
    rows (int):     rows of subplot
    save_dir (str): directory to save vortex images

  Returns:
  
  """

  fig, ax = plt.subplots(rows, cols, figsize=[20, 5*cols])
  for i, step in enumerate(times):
      im = ax.flatten()[i].imshow(data[step], cmap='RdBu')
      cbar = plt.colorbar(im, ax=ax.flatten()[i], shrink=0.25, pad=0.05, panchor=(0.0, 0.0))    
      ax.flatten()[i].set_title('t = {}'.format(step), y=1.05, 
                          fontsize=16, fontweight="bold")
  plt.show()

def movie_vortex(data, times, move_dir='vortex_movie.mov'):
  pass

def concat_timesteps(X_train, ntimes, step, timestep):
  """
  Time series concatenation - 
    function to concantenate data into continuos timesteps as traing datasets.

  Args:
    X_train (ndarray): training data set. 

    ntimes (int): number of time instances in each sample.

    step (int): gap between time instances. 

  Returns:
    X_train_concat (ndarray): concatenated array of time series. shape: (n_sample, ntimes, size_of_pod_coeffs)

  """

  assert (len(X_train.shape)==2) # ensure data is reduced and ordered.

  sample_size = int(X_train.shape[0]/timestep) # number of trajectories/samples in dataset

  # time window start and end for each concantenated sample 
  # (e.g. with step=2 and ntimes=7, 2nd sample starts from t2 and ends t14)
  window_start = [(sample*timestep)for sample in range(sample_size)] 
  window_end = [(sample*timestep) - (ntimes*step) for sample in range(1, sample_size + 1)]

  X_train_concat = []
  for start, end in zip(window_start, window_end):
    for i in range(start, end+step): 
      X_train_concat.append(X_train[i:i+ntimes*step:step])
  return np.array(X_train_concat)