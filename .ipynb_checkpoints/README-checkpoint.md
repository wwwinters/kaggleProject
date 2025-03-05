# Convolutional Neural Network (CNN) Binary Brain Tumor Classification

<h4>This repository contains the research, scripts and jupyter notebooks used for my Brian Tumor Classification study</h4>

### Dataset Description
The dataset used in this development effort is a combination of the following two data repositories and contains a total of 5,100 images.
- [Brain Tumor Dataset by Viradiya](https://www.kaggle.com/datasets/preetviradiya/brian-tumor-dataset)
- [Brain Tumor Classification (MRI) by Bhuvaji](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)</p>
Here is a breakdown of the images used for training and testing.  The datasets can be found on [Google Drive](https://drive.google.com/drive/folders/1o98tM0BlMP5Y4YcHaSkTKVWMAo7NpU0F?usp=drive_link)</p>

| Class    | Training | Testing | Total |
|----------|----------|---------|-------|
| Negative | 2,065    |   522   | 2,587 |
| Positive | 2,011    |   502   | 2,513 |
| Totals   | 4,076    | 1,024   | 5,100 |

The images were loaded into Pandas' DataFrames to allow for easier Exploratory Data Analysis (EDA) on them.  EDA indicated the *negative* and *positive* classes are roughly balanced with just a handful more of negative images.  Creation of the validation dataset was accomplished by splitting it from the training dataset.  A standard 20/80 percent split was used.</p>

### Model Architecture
A functional API architecture was used in the beginning of this project to define the model's structure.  However, this proved to be ineffective in this case and it was abandoned and the `model.Sequential()` method was used instead.  This method creates a simple but effective architecture. The architecture for the model used in this study consists of four convolution layers with pooling, a flattening layer, a fully connected layer with dropout, and the fully connected output layer using *softmax* as the activation function instead of *relu* as used in the previous layers.

### Callbacks
Two *callbacks* were deployed to help prevent the model from overfitting.  The `EarlyStopping()` callback will stop the model when validation loss stops decreasing and the `ReduceLROnPlateau()` will reduce the learning rate if the validation loss plateaus.  Numerous adjustments were made to the callbacks and the combination being used for training usually stops the training process at approximately 40 to 50 epochs.

### Compile and Model Training
The model was compiled using the Adam optimizer and categorical cross entropy as the loss function.  The learning rate of 0.001 was specified even though it is the default.  Experimentation was conducted to determine the optimal settings to use in the optimizer function.  In addition, the following metrics were specified:
- accuracy
- precision,
- AUC
Data was fitted to the model using the two callbacks discussed earlier.

### Overall Conclusion
The model preformed well on generalizing data from the test set.  F1 scored between 0.90 and 0.98.  For this measure we are looking for a number that is as close to 1 as possible.  In addition, the model did very well predicting true positives and negatives.  With some additional hyperparameter tuning and saving the model's weights for future use, it may be possible to accurately predict which category (negative/positive) with a rate of up to 99%.