This repo contains our research code used in the [paper](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/chong2023ral.pdf) "Unsupervised Generation of Labeled Training Images for Crop-Weed Segmentation in New Fields and on Different Robotic Platforms". 
The code in this repo has been frozen at the time of submission of the paper and will not be extended, but feel free to email me if you have any issues.

This repo is a fork from the original [pSp repo](https://github.com/eladrich/pixel2style2pixel.git).
We modified the code for the purpose of training a style inversion model for [our repo](https://github.com/PRBonn/StyleGenForLabels).
The main difference is that the encoder of the model is trained using images generated with sampled latent variables **w**. 
So, the train set are images generated from the StyleGAN2 (as opposed to real images).
For instructions on how to use the code in this repo, refer to the README from [the parent repo](https://github.com/PRBonn/StyleGenForLabels).
