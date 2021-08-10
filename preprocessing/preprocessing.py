"""
Prepocessing functions used in transforming data into parameter-varying field and storing.

"""
import sys
import numpy as np
from PredGAN.args import Args

__author__  = "Mustapha Jolaade"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mustapha Jolaade"
__email__ = "mustapha.jolaade20@imperial.ac.uk"
__status__ = "Development"


def curl(u,v):
  """ 
  Function to calculate the curl of a 2-dimensional vector field.
  Parameters:
  -----------
    u : 2d array of size n*m
      vector component in the x direction.

    v : 2d array of size n*m
      vector component in the y direction
  Output:
  -------
    curl : 2d array of size n*m
      curl of vector field [i.e. (dv/dx)i - (du/dy)j]
  """
  curl = np.gradient(v)[0] - np.gradient(u)[1]
  return curl


def get_vortex(raw_data, n_samples):
  
    """ 
    Function to transform raw velocity data to vorticity.
    Parameters:
    -----------
        raw_data : np array of size n_sample*timestep*nx*nx*u,v
          raw velocity data in both x (u) and y(v) direction.

        n_samples : int
         number of samples to be processed.

    """
    
    nx = Args.gridx
    ny = Args.gridy
    timestep = Args.timestep

    assert len(raw_data.shape)>=4  # n_sample X timesteps X nx X ny X u,v
    assert raw_data.shape[-1] >=2, "Missing u,v data." 
    assert raw_data.shape[-2] == ny, "Data mismatch. Please check size of grid." 
    assert raw_data.shape[-3] == nx, "Data mismatch. Please check size of grid." 
    
    vorticity = np.zeros((n_samples, timestep, nx, ny))

    # case: n_sample_times_timesteps X nx X ny X u,v
    if len(raw_data.shape) == 4: 
        n_samples = int(n_samples/timestep)
        raw_data = raw_data.reshape(n_samples, timestep, nx, ny, raw_data.shape[-1])

    for i in range(len(raw_data)):
        for j in range(len(raw_data[0])):
            vorticity[i][j] = curl(raw_data[i][j][:, :, 0], raw_data[i][j][:, :, 1])
    
    return vorticity


def main(raw_data, n_samples, save=True, save_dir='/data/calc_vortex.npy'):
    
    # compute vorticity 
    vorticity = get_vortex(raw_data, n_samples)

    if save:
        np.save(save_dir, vorticity) 

if __name__ == "__main__":
    main(sys.argv)
