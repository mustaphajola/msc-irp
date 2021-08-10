"""
Classess, attributes and methods used for data loading, manipulation, transformation and storage.

"""
import numpy as np
import joblib 
from sklearn.decomposition import pca
from sklearn.preprocessing import StandardScaler, MinMaxScaler

__author__  = "Mustapha Jolaade"
__credits__ = ["Vinicius Santos Silva"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mustapha Jolaade"
__email__ = "mustapha.jolaade20@imperial.ac.uk"
__status__ = "Development"


class Data():

    def __init__(self, data=None, pca=None, scaler=None):
        # not complete
        # self.data = data
        # self.pca
        # self.scaler
        # self.sample_size
        # self.transform_flag
        # self.inverted_flag
        pass
    

    def load(self, load_dir_dict):
        
        assert(len(load_dir_dict) < 4)
        
        data_dir = load_dir_dict{'data'}
        pca_dir = load_dir_dict{'pca'}
        
        self.data = np.load(data_dir, mmap_mode='r+')
        self.pca = joblib.load(pca_dir)


    def reduce_transform (self):
        """
        Function to transform and scale data following order reduction using POD.
        """
        
        self.scaler = MinMaxScaler()
        _ = self.pca.fit_transform(self.data)
        self.reduced = self.scaler.fit_transform(_)
        return self.reduced

    def invert(self, x_transform):
        """
        Function to inverse scaling on order reduction from PCA.
        """

        _ = self.scaler.inverse_transform(x_transform)
        self.reverse = self.pca.inverse_transform(_)
        return self.reverse

    def save_transformed(self, save_dir_dict={}):
        """ 
        Function to save transformed data.
        """ 

        np.save(save_dir_dict{'pca'}, self.pca)
        np.save(save_dir_dict{'data'}, self.reduced)


