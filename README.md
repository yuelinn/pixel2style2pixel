
This repo is a fork from the original [pSp repo](https://github.com/eladrich/pixel2style2pixel.git).
We modified the code for the purpose of training a style inversion model for [our repo](https://github.com/PRBonn/StyleGenForLabels).
The main difference is that the encoder of the model is trained using images generated with sampled latent variables **w**. 
So, the train set are images generated from the StyleGAN2 (as opposed to real images).
