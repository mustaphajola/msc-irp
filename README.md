# msc-irp 
(M.sc. Individul Research Project)

## Prediction and Data Assimilation Using Generative Models for 2D Turbulent Fluid Modelling


## About The Project

This project was completed as part of fulfillment of Msc in Applied Computational Science and Engineering (ACSE) requirement at the Department of Earth Science and Engineering, Imperial College London. 

### Dataset 
The dataset in this project comprises of 12,000 trajectories of 2-d vortices representing parameter varying flow in a box. The domain is a 256-by-256 grid cells with a time domain of 100s and 0.01s time discretisation. Snapshots of the data are captured every 2s resulting in 50 snapshots per trajectory. A sample trajectory is shown below. The parameters used in generating the dataset are as follows:
 - _Re_ = 5000
 - Constant viscosity
 - Boundary condition: no slip walls

**Trajectory**

https://user-images.githubusercontent.com/72414090/130993274-ce1b333a-beeb-4fea-9566-ff80f39e2161.mp4

**Time snapshots of the sample trajectory**

![vort_snapshot](https://user-images.githubusercontent.com/72414090/130993558-d922b8ea-35d8-4ee6-bc83-5d83d0ef24e6.jpg)

### Generative Models

#### Methodology

#### WGAN- GP 

**Architecture and Hyperparameter** 

![GAN_pt2](https://user-images.githubusercontent.com/72414090/132218680-8e8ec2dd-3df2-4389-b85d-f2f65b247f98.jpg)

**Prediction Methodology using WGAN-GP**


#### AAE

**Architecture and Hyperparameter** 

Prediction Methodology using AAE
![AAE_workflow](https://user-images.githubusercontent.com/72414090/132031730-e830362a-32d7-4bf9-81cc-6775df1480e2.png)

![image](https://user-images.githubusercontent.com/72414090/132230246-3d87b69c-b199-4987-ac9d-8637e028d031.png)



## Prerequisites
More info can be found in the environment.yml file.

## Results 

**Sample generation using WGAN-GP**

![image](https://user-images.githubusercontent.com/72414090/132235646-1bddc7d1-72a0-4483-aab2-2b3a115036f0.png)


**AAE Reconstruction Performance**

![image](https://user-images.githubusercontent.com/72414090/132217325-b7a6ce5f-1f81-4916-87c1-6ff8e51e8013.png)

### Prediction
Forward prediction was performed using the above algorithm. The input to each generative model is the series of snapshots from time **t=0 to t=30**. Time levels **t=35 to t=45** are multiple time predictions from both models. We see from the results that the AAE has low mismatch and a better performance compared to the WGAN-GP.

**Original snapshots of trajectory**

![image](https://user-images.githubusercontent.com/72414090/132218250-c71de12a-6b16-48c1-95d6-82221faabb44.png)

The bottom row images show the magnitude of the vortices projected unto a 1D linear domain. The vertical axis is the magnitude of the vortices while the horizontal axis represents teh spatial dimension.

**WGAN-GP Prediction Results**

![image](https://user-images.githubusercontent.com/72414090/132217432-098617de-d6ac-4781-8c79-31a879cc08b5.png)

**AAE Prediction Results**

![image](https://user-images.githubusercontent.com/72414090/132217443-fc2254a2-f242-46c6-a583-ec4e228c9329.png)


## License
Distributed under the MIT license. See `License` for more information.

## Contact
- Mustapha Jolaade jolaademustapha@yahoo.com

## Acknowledgements

- Prof. Christopher Pain
- Dr. Claire Healy 
- Vinicius, Santos Silva (Ph.D. student).
- Royal School of Mines

I would also like to acknowledge the contributions of Nenko Nenov, Lily Hua and Danhui Shao through discussions and resource-sharing. 

Mustapha Jolaade
08/26/2021
