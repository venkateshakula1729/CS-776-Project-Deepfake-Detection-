# CS-776-Project-Deepfake-Detection-



## Overview
This repository contains state-of-the-art deep learning models for detecting deepfake images, featuring:
1. **Adversarial Training Models** - Robust models trained with adversarial examples
2. **CNN+Transformer Hybrid Models** - Combining convolutional and/or transformer architectures for improved detection 

We have mainly worked with 2 datasets -  CIFAKE & Deepfake and real images
## Project Structure
```bash

assets/
    ├── Baseline model.png
    ├── Baseline models without defense.png
    ├── Model comparison .png
    └── Readme
Attacks/
    ├── FGSM.py
    ├── one_pixel_attack.py
    └── PGD.py
Models/
    ├── adversarial-training/
        ├── Best model/
            └── CIFAKE/
                ├── adversarial-training_CIFAKE_best.ipynb
                ├── efficientnet_cifake_baseline.ipynb
                ├── efficientnet-cifake-adv.ipynb
                ├── mobilenet_cifake_adv .ipynb
                └── Resnet_cifake_adv.ipynb
        ├── cifake_adv-training.ipynb
        ├── cifake_adversarial-FGSM_training_V2.ipynb
        ├── cifake_adversarial-training_FGSM.ipynb
        ├── cifake-on-resnet.ipynb
        ├── efficientnet_cifake_baseline.ipynb
        ├── efficientnet-cifake-adv.ipynb
        ├── mobilenet_cifake_adv .ipynb
        ├── Resnet_cifake_adv.ipynb
        ├── vgg19_baseline_cifake.ipynb
        └── vgg19_DFRI_baseline (1).ipynb
    ├── CNN+Vision Transformers/
        ├── final_models/
            ├── CNN+Tranformers_ cifake_adv.ipynb
            ├── CNN+transformers_cifake_baseline.ipynb
            ├── CNN+Transformers_DFRI_baseline.ipynb
            ├── DeiT_cifake_baseline.ipynb
            ├── DeiT_DFRI_Adv.ipynb
            ├── DeiT_on_CIFAKE.ipynb
            └── README.md
        ├── cifake best hybrid.ipynb
        ├── cifake-adv-hybrid-v1.ipynb
        ├── CNN+Transformers_cifake_adv.ipynb
        ├── CNN+transformers_cifake_baseline.ipynb
        ├── DeiT_on_CIFAKE.ipynb
        ├── DeiT-cifake-baseline.ipynb
        ├── hybrid_cifake_adv_v2.ipynb
        └── Readme.md
    └── readme.md
plots/
    ├── deepfake plots .ipynb
    └── Readme.md
.gitignore
DeepFake-1.pptx
Endterm Presentation.pptx
inference .ipynb
LICENSE.txt
Project Report.pdf
README.md
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
2. Open the required model and download the libraries metioned in the imports section

3. Download the dataset and set the paths appropriately in the notebook
    [https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images) for CIFAKE
   
   [https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images/data](https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images/data) for DFRI
    
5. Run all the cells sequentially

### 2. CNN + transformers
**Location:** `Models/CNN+Vision Transformers/`

Key Notebooks:
- `CNN+Tranformers_cifake_adv.ipynb` - hybrid adversarial model 
- `DeiT_cifake_adv.ipynb` - Best performing adversarial model
- `DeiT_cifake_baseline.ipynb` - Best performing non defense model

#### How to Run:
1. Navigate to the directory:
```bash
cd Models/CNN+Vision Transformers/
```
2. Open the required model and download the libraries metioned in the imports section

3. Download the dataset and set the paths appropriately in the notebook
    [https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images) for CIFAKE
   
    [https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images/data](https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images/data) for DFRI
   
5. Run all the cells sequentially


