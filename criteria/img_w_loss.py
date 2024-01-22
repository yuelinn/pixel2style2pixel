import torch
from torch import nn
import torch.nn.functional as F


class ImgWLoss(nn.Module):

	def __init__(self):
		super(ImgWLoss, self).__init__()

	def forward(self, latent, des_latent):
		return F.mse_loss(latent, des_latent, reduction = "mean")
