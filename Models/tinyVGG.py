from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D,MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense, Dropout
from keras import backend as k

class tinyVGG:
    @staticmethod
    def build(height, width, depth, classes):
        model = Sequential()
        input_shape = (height, width, depth)
        channel_dim = -1
        if (k.image_data_format() == 'channels_first'):
            input_shape = (depth, height, width)
            channel_dim = 1
            
        model.add(Conv2D(32,(3,3),padding='same'),input_shape=input_shape)
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(MaxPooling2D(pool_size = (3,3)))
        model.add(Dropout(0.25))
        
        model.add(Conv2D(64,(3,3),padding='same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(Conv2D(64,(3,3),padding='same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=channel_dim))
        
        model.add(MaxPooling2D(pool_size = (2,2)))
        model.add(Dropout(0.25))
        
        model.add(Conv2D(128,(3,3),padding='same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=channel_dim))
        model.add(Conv2D(128,(3,3),padding='same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=channel_dim))
        
        model.add(MaxPooling2D(pool_size = (2,2)))
        model.add(Dropout(0.25))
        
        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Activation('relu'))
        
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        
        model.add(Dense(3))
        model.add(Activation('softmax'))
        
        return model           
        
