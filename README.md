# Text-Driven Scene-Decoupled WS-VAD

**[ACM Multimedia 2024] TDSD: Text-Driven Scene-Decoupled Weakly Supervised Video Anomaly Detection**

Shengyang Sun, Jiashen Hua, Junyi Feng, Dongxu Wei, Baisheng Lai, Xiaojin Gong

<a href='https://openreview.net/pdf?id=TAVtkpjS9P'><img src='https://img.shields.io/badge/Paper-PDF-red'></a>

**This repository is still under maintenance, and the code will be uploaded progressively.**

## Framework
<p align="center">
    <img src=framework.jpg width="800" height="300"/>
</p>
An overview of the proposed framework. It includes the text-driven scene-decouple module (TDSDM), fine-grained visual augmentation (FVA), and the global encoder. The snowflake icon in the figure indicates that we have frozen this module in the training.

To the best of our knowledge, this is **the first work** to address scene-dependent video anomaly detection under a weakly supervised setting.

## News
- [2024.09] ⭐️ We release a partitioning method for the NWPU dataset, which enables its application in the training of scene-dependent weakly supervised video anomaly detection.

## Performance on Public Datasets
| Method | Dataset | Type | Performance (%) |
| ----------| :------:|:----:| :----:|
| TDSD (Ours)| UCF_SHT | Scene-dependent |85.94 (AUC) |
| TDSD (Ours)| NWPU | Scene-dependent | 80.22 (AUC) |
| TDSD (Ours)| XD-Violence | Scene-agnostic | 84.69 (AP) |
| TDSD (Ours)| TAD | Scene-agnostic | 93.90 (AUC) |


## Requirements  

    python==3.8.18
    torch==2.2.1  
    cuda==12.1

## Split the NWPU Dataset 

  You can use the **data/make_list_NWPU.py** to generate the training list **NWPU_train.list** and the testing list **NWPU_test.list**.

  In **make_list_NWPU.py**, **feats_dir** stores the extracted features, and the storage structure is consistent with the NWPU dataset structure.

  ```
  │CLIP_features
  │  
  ├─Test
  │      D001_01.npy
  │      D001_02.npy
  │      D001_03.npy
  │      ...
  └─Train
         D001_01.npy
         D001_02.npy
         D001_03.npy
         ...
  ```


## Citation
If you find our paper useful, hope you can star our repo and cite our paper as follows:
```
@inproceedings{sun2024tdsd,
  title={TDSD: Text-Driven Scene-Decoupled Weakly Supervised Video Anomaly Detection},
  author={Sun, Shengyang and Hua, Jiashen and Feng, Junyi and Wei, Dongxu and Lai, Baisheng and Gong, Xiaojin},
  booktitle={ACM Multimedia 2024},
  year={2024}
}
```
## License
This project is released under the MIT License.

