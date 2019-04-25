# coding:utf-8
import os, sys, time, yaml
import argparse
import SimpleITK as sitk
import numpy as np
from chainer.datasets import mnist

parser = argparse.ArgumentParser()
parser.add_argument('--base', '-B', default=os.path.dirname(os.path.abspath(__file__)),
                    help='base directory path of program files')
parser.add_argument('--outputDir', '-o', default='data/raw',
                    help='Directory to output the result(base path)')
parser.add_argument('--save_type', type=str, default='png',
                    help='Save type (mhd or png)')
args = parser.parse_args()

print('----- Load mnist -----')
train, test = mnist.get_mnist(withlabel = False, ndim = 2)

print('----- Save mnist -----')
result_dir = os.path.join(args.base, args.outputDir, args.save_type)
if not os.path.exists(result_dir):
    os.makedirs(result_dir)
with open('{}/config_{}.yml'.format(result_dir, time.strftime('%Y-%m-%d_%H-%M-%S')), 'w') as f:
    f.write(yaml.dump(vars(args), default_flow_style=False))

for i, img in enumerate(train):
    if i % 100 == 0:
        print('Num: {} / {}'.format(i, len(train)))

    if args.save_type =='png':
        img = np.asarray(np.clip(img*255.0, 0.0, 255.0), dtype=np.uint8)
    elif args.save_type == 'mhd':
        img = img
    else:
        raise NotImplementedError()

    sitkImg = sitk.GetImageFromArray(img)
    sitkImg.SetSpacing([1,1])
    sitk.WriteImage(sitkImg, '{}/{:05d}.{}'.format(result_dir, i, args.save_type))
