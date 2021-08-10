#!/usr/bin/env py3ml
import os
import sys
import numpy as np
import random
from models import models
from args import Args

# ------------------------------------------------------------

def train(args):
  import models
  # np.random.seed(1234)

  if args.dataset == 'mnist':
    n_dim, n_out, n_channels = 28, 10, 1
    X_train, y_train, X_val, y_val, _, _ = data.load_mnist()
  elif args.dataset == 'random':
    n_dim, n_out, n_channels = 2, 2, 1
    X_train, y_train = data.load_noise(n=1000, d=n_dim)
    X_val, y_val = X_train, y_train
  else:
    raise ValueError('Invalid dataset name: %s' % args.dataset)

  # set up optimization params
  opt_params = { 'lr' : args.lr, 'c' : args.c, 'n_critic' : args.n_critic }

  # create model
  if args.model == 'dcgan':
    model = models.DCGAN(n_dim=n_dim, n_chan=n_channels, opt_params=opt_params)
  elif args.model == 'wgan':
    model = models.WGAN(n_dim=n_dim, n_chan=n_channels, opt_params=opt_params) 
  elif args.model == 'ugan':
    model = models.UGAN(n_dim=n_dim, n_chan=n_channels, opt_params=opt_params)
  elif args.model == 'aae':
    model = models.AAE(n_dim=n_dim, n_chan=n_channels, opt_params=opt_params)
  else:
    raise ValueError('Invalid model')

# --------------------------------------------------------------------------------------
def main():
    parser = Args.make_parser()
    args = parser.parse_args()
    args.func(args)
    
if __name__=='__main__':
    main(sys.argv)