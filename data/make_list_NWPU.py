import numpy as np
import os
import glob

gt = np.load('/ssd/ssy/NWPUCampusDataset/groundtruth/NWPU_Campus_gt.npz')
feats_dir = '/data/ssy/datasets/NWPU/CLIP_features'
save_dir = '/data/ssy/code/TDSD/data'
split_dir = '/data/ssy/code/TDSD/data/NWPU_split'

with open(os.path.join(save_dir, 'NWPU_train.list'), 'w+') as f:
    for key in open(os.path.join(split_dir, 'trainingSet_train.txt'), 'r').readlines():
        video_name = key.strip().split(' ')[0]
        video_feat_path = os.path.join(feats_dir, 'Train/' + video_name + '.npy')
        out = video_feat_path + ',0'+ '\n'
        f.write(out)

    for key in open(os.path.join(split_dir, 'trainingSet_test_label.txt'), 'r').readlines():
        video_name = key.strip().split(' ')[0]
        label = key.strip().split(' ')[1]
        video_feat_path = os.path.join(feats_dir, 'Test/' + video_name + '.npy')
        out = video_feat_path + ',' + label + '\n'
        f.write(out)

with open(os.path.join(save_dir, 'NWPU_test.list'), 'w+') as f:
    for key in open(os.path.join(split_dir, 'testingSet_train.txt'), 'r').readlines():
        video_name = key.strip().split(' ')[0]
        video_feat_path = os.path.join(feats_dir, 'Train/' + video_name + '.npy')
        out = video_feat_path + ',0' + '\n'
        f.write(out)

    for key in open(os.path.join(split_dir, 'testingSet_test.txt'), 'r').readlines():
        video_name = key.strip().split(' ')[0]
        video_feat_path = os.path.join(feats_dir, 'Test/' + video_name + '.npy')
        if np.sum(gt[video_name]) > 0:
            label = '1'
        else:
            label = '0'
        out = video_feat_path + ',' + label + '\n'
        f.write(out)