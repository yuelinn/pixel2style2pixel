from torch.utils.data import Dataset
from PIL import Image
from utils import data_utils
import torchvision.transforms as transforms


class InferenceDataset(Dataset):

	def __init__(self, root, opts, transform=None):
		self.paths = sorted(data_utils.make_dataset(root))
		self.transform = transform
		self.opts = opts

	def __len__(self):
		return len(self.paths)

	def __getitem__(self, index):
		from_path = self.paths[index]
		from_im = Image.open(from_path)
		from_im = from_im.convert('RGB') # if self.opts.label_nc == 0 else from_im.convert('L')
		from_im = transforms.ToTensor()(from_im)
		normalize_transform = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])

		if self.transform:
			from_im = self.transform(from_im)
			from_im = normalize_transform(from_im)
		return from_im
