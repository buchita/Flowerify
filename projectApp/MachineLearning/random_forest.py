#####################################################################################################
# description: Random Forest classifier - obtain the accuracy
#####################################################################################################


from pathlib import Path
import numpy as np
from sklearn import preprocessing, utils, model_selection, ensemble, metrics
# from sklearn.preprocessing import StandardScaler
# from sklearn.utils import Bunch
# from sklearn.model_selection import train_test_split
from skimage import io, transform
# from skimage.io import imread
# from skimage.transform import resize
# from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
# from sklearn import metrics
from keras.preprocessing import image
import pickle
import cv2



# this function is taken from this reference to load images from local directory and return as a bunch
# https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
def load_image_files(dataset_target, dataset_numpy, dimension=(96, 96, 3)):

    flat_data = []

    for image in dataset_numpy:

        img_resized = transform.resize(image, dimension, anti_aliasing=True, mode='reflect')



        flat_data.append(img_resized.flatten())



    flat_data = np.array(flat_data)
    target = np.array(dataset_target)


    return utils.Bunch(data=flat_data,
                 target=target)


def classifier(predict_imag_path, dataset_target, dataset_numpy):



    label = ['Barbeton Daisy', 'Blanket Flower', 'Buttercup',
                'Carnation', 'Common Dandelion', 'Corn Poppy',
                'Lotus', 'Marigold', 'Rose', 'Sunflower']


    image_dataset = load_image_files(dataset_target, dataset_numpy)



    # split data into 70% training, 30% testing
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        image_dataset.data, image_dataset.target, test_size=0.3, random_state=109)

    scaler = preprocessing.StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    # Instantiate model with 1000 decision trees

    rf = ensemble.RandomForestClassifier(n_estimators=100, random_state=0)

    # Train the model on training data
    rf.fit(X_train, y_train)


    # # save the model to disk
    # filename = 'finalized_model.sav'
    # pickle.dump(rf, open(filename, 'wb'))



    # # load the model from disk
    # loaded_model = pickle.load(open(filename, 'rb'))
    # result = loaded_model.score(X_test, Y_test)
    # print(result)



    y_pred = rf.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print('Accuracy of Random Forest classifier on test set: {:.2f}'.format(rf.score(X_test, y_test)))

    percent = rf.score(X_test, y_test)
    percent = percent*100

    root = "djangoProject"
    path = root + predict_imag_path
    flat_data1 = []
    dimension = 96, 96
    img = io.imread(path)
    img_resized = transform.resize(img, dimension, anti_aliasing=True, mode='reflect')
    flat_data1.append(img_resized.flatten())

    result = rf.predict(flat_data1)
    print(result)
    index = int(result)-1
    name = label[index]



    return result, percent, name


# root = "/djangoProject"
# path = root + "/images/daisy/g1.jpg"
# # path = r"C:\Users\buchi\OneDrive - Technological University Dublin\DT211c4\Dissertation\Dataset\sunflower\square-1460724927-orange-sunflower.jpg"
# classifier(path)
