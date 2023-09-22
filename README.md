# Final Year Project 
## Debris-Covered Glacier Mapping using Deep Learning

This repository contains code for our final year project on mapping debris-covered glaciers from satellite imagery using deep learning models, Spatial and Spectral Convolutional Neural Network.

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
