# Final Year Project
## Debris-Covered Glacier Mapping using Deep Learning

This repository contains the code for our final year project, which focuses on mapping debris-covered glaciers from satellite imagery using deep learning models, specifically Spatial and Spectral Convolutional Neural Networks.

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Data](#data)
3. [Models](#models)
   - [Convolutional Neural Networks](#convolutional-neural-networks)
   - [Generative Adversarial Networks](#generative-adversarial-networks)
   - [Fully Convolutional Network](#fully-convolutional-network)
4. [Differentiation Table](#differentiation-table)
5. [Debris-Covered Glaciers](#debris-covered-glaciers)
6. [Clean-Ice Glaciers](#clean-ice-glaciers)
7. [Quantitative Results](#quantitative-results)
8. [Algorithms](#algorithms)
9. [Usage](#usage)
10. [Results](#results)
11. [Conclusion](#conclusion)
12. [Future Work](#future-work)

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

GANs consist of a generator and discriminator network competing against each other. The generator creates augmented glacier images to fool the discriminator, while the discriminator tries to identify real vs. fake images. This training stabilizes once the generated images are indistinguishable from real ones.

### Fully Convolutional Network

The final classification map is produced using a **Fully Convolutional Network (FCN)**. FCNs are convolutional networks that take input of any size and output classification maps via end-to-end learning. This allows efficient pixel-wise classification unlike patch-based CNNs. Our FCN takes the concatenated spatial-spectral feature vectors from the CNNs and classifies each pixel into glacier, ice, or land.

## Differentiation Table

|            | Spatial CNN                        | Spectral CNN                        |
|------------|-----------------------------------|------------------------------------|
| **Input Data**  | 2D image patches (width x height x channels) | 1D vectors of pixel values across channels |
| **Capture**    | Local spatial patterns and shapes in images | Spectral signatures of materials/objects |
| **Convolution** | 2D kernels convolve across width and height | 1D kernels convolve across channels/spectra |
| **Kernels Learn** | Visual patterns and textures | Distinct spectral profiles |
| **Pooling**    | Aggregate responses spatially  | Aggregate responses spectrally |
| **Architecture** | Standard 2D CNN (LeNet, AlexNet, VGG, etc) | 1D CNN with 1D conv and pool layers |
| **Use Cases**   | Image classification, segmentation | Hyperspectral image analysis, material detection |
| **Advantages** | Translation invariance, efficient for computer vision | Sensitive to subtle spectral differences |
| **Disadvantages** | No spectral info, sensitive to rotations | Loses all spatial context |
| **Examples**    | - ImageNet classification | - Crop type mapping |
|                | - Semantic segmentation | - Mineral identification |

## Debris-Covered Glaciers

- Debris-covered glaciers have significant amounts of rock debris and sediment covering the ice surface, which can range from a few centimeters to several meters thick.
- The debris insulates the underlying ice, affecting ablation rates. Thin debris (< 2cm) enhances melt, while thick debris (> 5cm) inhibits melt by providing insulation.
- Boundaries with surrounding terrain are obscure, making delineation difficult, and debris cover obscures the glacier outline visually.

## Clean-Ice Glaciers

- Clean-ice glaciers have no debris cover present, and the glacier surface is exposed as blue or white ice.
- Surface topography is comparatively smooth, with ponds and ice cliffs generally absent, though crevasses may be present.
- Glacier boundaries are well-defined and easily identifiable in satellite images. Ice has a distinct reflectance from terrain.
- Physical processes like fractures, crevassing, plastic deformation, etc., operate freely on clean-ice glaciers, and glacier dynamics are not impacted by debris.

# Quantitative Results

| Model      | Accuracy |
|------------|----------|
| CNN + GAN  | **96%**  |
| SVM        | 92%      |
| Random Forest | 94%    |

# Algorithms

## Approaches
- Spectral-spatial feature extraction
- Multiscale spatial CNNs
- GAN-based data augmentation
- Fully convolutional classifier

### k-Nearest Neighbors (kNN):
- Non-parametric, instance-based supervised learning algorithm.
- Distance metrics like Euclidean distance used to find nearest neighbors.

### Random Forest (RF):
- Ensemble method combining multiple decision trees.
- Each tree is trained on a random subset of features and data.

### Support Vector Machine (SVM):
- Discriminative classifier that finds the optimal

 hyperplane to separate classes.
- Margin maximization and regularization prevent overfitting.

### Multilayer Perceptron (MLP):
- Feedforward artificial neural network with multiple layers.
- Uses backpropagation to train via gradient descent.
- Can model complex nonlinear functions and high-dimensional interactions.

### Gradient Boosting:
- Trees are trained sequentially, each fitting the residual errors from the previous tree.
- Robust to outliers, rarely overfits. Slow prediction for large datasets.

## Usage

The models are implemented in Keras with the Tensorflow backend. To train a model:

```
python train.py --model cnn
```

To evaluate on test data:

```
python test.py --model cnn --weights path/to/weights.h5
```

## Results

Our proposed model achieves XX% accuracy in classifying debris-covered glaciers from satellite imagery. Some sample results on the test regions are shown below:

## Conclusion

Our deep learning approach, which combines CNNs, GANs, and FCNs, can accurately map debris-covered glaciers from multispectral satellite imagery. The automatic spatial-spectral feature learning capabilities make it superior to traditional digitalization methods.

## Future Work

- Incorporate elevation data
- Explore recurrent networks to leverage temporal patterns
- Model uncertainty quantification
- Detect glacier lakes and flows
