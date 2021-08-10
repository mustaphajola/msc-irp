#!/usr/bin/env py3ml

class Args:


    def make_parser():
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(title='Commands')

        # train

        train_parser = subparsers.add_parser('train', help='Train model')
        train_parser.set_defaults(func=train)

        train_parser.add_argument('--dataset', default='vortex300')
        train_parser.add_argument('--model', default='wgan')
        train_parser.add_argument('-e', '--epochs', type=int, default=50000)
        train_parser.add_argument('-l', '--logdir', default='logs/vortex300')
        train_parser.add_argument('--glr', type=float, default=1e-4)
        train_parser.add_argument('--dlr', type=float, default=1e-4)
        train_parser.add_argument('--ncritic', type=int, default=5)
        train_parser.add_argument('-b', '--BATCH_size', type=int, default=125)

        return parser

    kernel_initializer = 'glorot_uniform'

    dropout = 0.3

    latent_space = 1000

    # alpha used by leaky relu 
    alpha_D = 0.2
    alpha_G = 0.2

    BATCH_SIZE = 125

    beta_1 = 0.5
    beta_2 = 0.99

    sample_size = 15000
    timestep = 50
    grid = 256

    ntimes = 7
    step = 5


