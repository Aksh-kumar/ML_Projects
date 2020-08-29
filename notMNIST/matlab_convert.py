#!/usr/bin/python2.6
# Turns directory of notMNIST glyphs into Matlab dataset.
#
# Usage: matlab_convert.py dataset_dir target.mat
#
# dataset_dir --> A --> img1.png
#                   --> img2.png
#             --> B --> img1.png
#                   --> img2.png
#      ...
#             --> J --> img1.png
#                   --> img2.png
#
# Show some images with their labels
#   load('target.mat')
#   for i=1:5
#     figure('Name',num2str(labels(i))),imshow(images(:,:,i)/255)
#   end


from scipy.io import savemat
import numpy, Image, glob, sys, os

def generate_dataset(folder,target):
  print folder
  max_count = 0
  for (root, dirs, files) in os.walk(folder):
    for f in files:
      if f.endswith('.png'):
          max_count+=1

  print 'Found %s files'%(max_count,)
  data = numpy.zeros((28,28,max_count))
  labels = numpy.zeros((max_count,))
  count = 0
  for (root, dirs, files) in os.walk(folder):
    for f in files:
      if f.endswith('.png'):
        try:
          img = Image.open(os.path.join(root,f));
          data[:,:,count]=numpy.asarray(img)
          surround_folder = os.path.split(root)[-1]
          assert len(surround_folder)==1
          labels[count]=ord(surround_folder)-ord('A')
          count+=1
        except:
          pass

  print 'Saving to '+target
  savemat(target,{'images':data[:,:,:count],'labels':labels[:count]})

def main(argv):
  generate_dataset(argv[1],argv[2])

if __name__=='__main__':
  main(sys.argv)
