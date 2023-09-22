# Final Year Project 
## Debris-Covered Glacier Mapping using Deep Learning

This repository contains code for our final year project on mapping debris-covered glaciers from satellite imagery using deep learning models, Spatial and Spectral Convolutional Neural Network.

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Data](#data)
4. [Models](#models)
   - [Convolutional Neural Networks](#convolutional-neural-networks)
   - [Generative Adversarial Networks](#generative-adversarial-networks)  
   - [Fully Convolutional Network](#fully-convolutional-network)
5. [Differetiation Table](#Differetiation-Table)
6. [Debris-Covered Glaciers] (#Debris-Covered-Glaciers)
7. [Clean-Ice Glaciers](#Clean-Ice-Glaciers)
8. [Algorithms](#Algorithms)
7. [Usage](#usage)
8. [Results](#results)
9. [Conclusion](#conclusion)

## Problem Statement

Mapping debris-covered glaciers using traditional digitalization methods is challenging due to the surface similarity between the glacier and surrounding land. This project aims to accurately map debris-covered glaciers, ice, and land from multispectral satellite images using deep learning. 

## Data

The data used consists of Sentinel-2 satellite images covering the Shisper glacier region in Pakistan. It contains 10 spectral bands at 10m resolution acquired at different time periods from 2018-2019.

## Models

The following deep learning models are used:

### Convolutional Neural Networks

We use **Convolutional Neural Networks (CNNs)** to automatically extract spatial and spectral features from the satellite images. CNNs are ideal for imagery data as they can capture localized features via convolution filters and pool the features hierarchically to build robust representations.

Our model uses two CNN streams - a 1D CNN to extract spectral features from pixel vectors, and a multiscale 2D CNN to extract spatial features using varying kernel sizes. This allows combining both spectral and complementary spatial information efficiently.

### Generative Adversarial Networks

Since debris-covered glacier pixels are underrepresented compared to land/ice pixels, we use a **Generative Adversarial Network (GAN)** to augment the minority glacier class and balance the training data. 

GANs consist of a generator and discriminator network competing against each other. The generator creates augmented glacier images to fool the discriminator, while the discriminator tries to identify real vs fake images. This training stabilizes once the generated images are indistinguishable from real ones.

### Fully Convolutional Network

The final classification map is produced using a **Fully Convolutional Network (FCN)**. FCNs are convolutional networks that take input of any size and output classification maps via end-to-end learning. This allows efficient pixel-wise classification unlike patch-based CNNs.

Our FCN takes the concatenated spatial-spectral feature vectors from the CNNs and classifies each pixel into glacier, ice or land.

# Differetiation Table

| | Spatial CNN | Spectral CNN |
|-|-------------|--------------|
| **Input Data** | 2D image patches (width x height x channels) | 1D vectors of pixel values across channels  |
| **Capture** | Local spatial patterns and shapes in images | Spectral signatures of materials/objects |
| **Convolution** | 2D kernels convolve across width and height | 1D kernels convolve across channels/spectra |  
| **Kernels Learn** | Visual patterns and textures | Distinct spectral profiles |
| **Pooling** | Aggregate responses spatially | Aggregate responses spectrally |
| **Architecture** | Standard 2D CNN (LeNet, AlexNet, VGG, etc) | 1D CNN with 1D conv and pool layers|
| **Use Cases** | Image classification, segmentation | Hyperspectral image analysis, material detection |
| **Advantages** | Translation invariance, efficient for computer vision | Sensitive to subtle spectral differences |
| **Disadvantages** | No spectral info, sensitive to rotations | Loses all spatial context |
| **Examples** | - ImageNet classification<br>- Semantic segmentation | - Crop type mapping<br>- Mineral identification |

- Distinguishing debris vs glacier in close vicinity
- Focusing only on glacier/debris classes without surroundings
- Imbalance between glacier vs land/ice training samples
- Classifies glacier, ice and land jointly
- Fuses spatial and spectral features automatically
- Uses multiscale spatial features for robustness 
- Employs GANs to generate minority class data
- Analyzes various artifacts like sample size, time complexity etc.

# Debris-Covered Glaciers

- Have significant amounts of rock debris and sediment covering the ice surface. This debris layer can range from a few centimeters to several meters thick.

- Debris insulates the underlying ice and affects ablation rates. Thin debris (< 2cm) enhances melt, while thick debris (> 5cm) inhibits melt by providing insulation.

- Boundaries with surrounding terrain are obscure making delineation difficult. Debris cover obscures the glacier outline visually.

# Clean-Ice Glaciers

- No debris cover present. Glacier surface is exposed blue or white ice.

- Surface topography is comparatively smooth. Ponds and ice cliffs are generally absent. Crevasses may be present.

- Glacier boundaries are well defined and easily identifiable in satellite images. Ice has distinct reflectance from terrain. 

- Physical processes like fractures, crevassing, plastic deformation, etc. operate freely. Glacier dynamics not impacted by debris.

# Algorithms

### k-Nearest Neighbors (kNN):
- Non-parametric, instance-based supervised learning algorithm. 
- Distance metrics like Euclidean distance used to find nearest neighbors.
 
### Random Forest (RF):
- Ensemble method combining multiple decision trees.
- Each tree is trained on a random subset of features and data. 

### Support Vector Machine (SVM): 
- Discriminative classifier that finds optimal hyperplane to separate classes. 
- Margin maximization and regularization prevent overfitting.

### Multilayer Perceptron (MLP):
- Feedforward artificial neural network with multiple layers. 
- Uses backpropagation to train via gradient descent.
- Can model complex nonlinear functions and high-dimensional interactions.

### Gradient Boosting:
- Trees are trained sequentially, each fitting the residual errors from previous tree. 
- Robust to outliers, rarely overfits. Slow prediction for large datasets.

## Usage

The models are implemented in Keras with Tensorflow backend. To train a model:

```
python train.py --model cnn
```

To evaluate on test data:

```
python test.py --model cnn --weights path/to/weights.h5 
```

## Results

Our proposed model achieves XX% accuracy in classifying debris-covered glaciers from the satellite imagery. Some sample results on the test regions are shown below:

![Results]()

## Conclusion

Our deep learning approach combining CNNs, GANs and FCNs can accurately map debris-covered glaciers from multispectral satellite imagery. The automatic spatial-spectral feature learning capabilities make it better than traditional digitalization.
