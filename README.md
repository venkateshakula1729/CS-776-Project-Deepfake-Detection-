# CS-776-Project-Deepfake-Detection-



## Overview
This repository contains state-of-the-art deep learning models for detecting deepfake images, featuring:
1. **Adversarial Training Models** - Robust models trained with adversarial examples
2. **CNN+Transformer Hybrid Models** - Combining convolutional and/or transformer architectures for improved detection 

We have mainly worked with 2 datasets -  CIFAKE & Deepfake and real images
## Project Structure
```bash

Deep fake detection/
├── Attacks/
│ ├── FGSM.py
│ ├── one_pixel_attack.py
│ └── PGD.py
├── Models/
│ ├── adversarial-training/
│ │ ├── Best model/
│ │ │ └── CIFAKE/
│ │ │ ├── adversarial-training_CIFAKE_best.ipynb
│ │ │ ├── efficientnet_cifake_baseline.ipynb
│ │ │ ├── efficientnet-cifake-adv.ipynb
│ │ │ ├── mobilenet_cifake_adv.ipynb
│ │ │ └── Resnet_cifake_adv.ipynb
│ ├── CNN+Vision Transformers/
│ │ ├── final_models/
│ │ │ ├── CNN+Tranformers_cifake_adv.ipynb
│ │ │ ├── CNN+transformers_cifake_baseline.ipynb
│ │ │ ├── CNN+Transformers_DFRI_baseline.ipynb
│ │ │ ├── DeiT_cifake_baseline.ipynb
│ │ │ ├── DeiT_DFRI_Adv.ipynb
│ │ │ └── DeiT_on_CIFAKE.ipynb
├── plots/
│ └── deepfake plots.ipynb
├── .gitignore
└── README.md
```

### 1. Adversarial Training Models
**Location:** `Models/adversarial-training/Best model/CIFAKE/`

Key Notebooks:
- `adversarial-training_CIFAKE_best.ipynb` - Best performing adversarial model
- `efficientnet-cifake-adv.ipynb` - EfficientNet with adversarial training
- `Resnet_cifake_adv.ipynb` - ResNet with adversarial defenses

#### How to Run:
1. Navigate to the directory:
```bash
cd Models/adversarial-training/Best model/CIFAKE/
```

### 2. CNN + transformers
**Location:** `Models/adversarial-training/Best model/CIFAKE/`

Key Notebooks:
- `adversarial-training_CIFAKE_best.ipynb` - Best performing adversarial model
- `efficientnet-cifake-adv.ipynb` - EfficientNet with adversarial training
- `Resnet_cifake_adv.ipynb` - ResNet with adversarial defenses

#### How to Run:
1. Navigate to the directory:
```bash
cd Models/adversarial-training/Best model/CIFAKE/

