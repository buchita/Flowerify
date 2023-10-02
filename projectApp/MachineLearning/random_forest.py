#####################################################################################################
# description: Random Forest classifier - obtain the accuracy
#####################################################################################################

import numpy as np
from sklearn import preprocessing, utils, model_selection, ensemble, metrics
from skimage import io, transform
import cv2


WIDTH = 200
HEIGHT = 200


# this function is taken from this reference to load images from local directory and return as a bunch
# https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
def load_image_files(dataset_target, dataset_numpy, dimension=(WIDTH, HEIGHT, 3)):

    flat_data1 = []

    for image in dataset_numpy:
        img_resized = transform.resize(image, dimension, anti_aliasing=True, mode='reflect')

        flat_data1.append(img_resized.flatten())

    flat_data1 = np.array(flat_data1)
    target1 = np.array(dataset_target)

    return utils.Bunch(data=flat_data1, target=target1)


def classifier(predict_imag_path, dataset_target, dataset_numpy):

    label = ["Barbeton Daisy", "Blanket Flower", "Buttercup", "Carnation", "Common Dandelion",
             "Corn Poppy", "Lotus", "Marigold", "Rose", "Sunflower"]

    image_dataset = load_image_files(dataset_target, dataset_numpy)

    # split data into 70% training, 30% testing
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        image_dataset.data, image_dataset.target, test_size=0.3, random_state=109)

    # ensures that all values fit in the same range
    scaler = preprocessing.StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    # Instantiate model
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
    print(percent)

    begin = cv2.os.getcwd()
    image_root = begin.replace("\\", "/")

    path = image_root + predict_imag_path

    flat_data1 = []
    dimension = WIDTH, HEIGHT
    img = io.imread(path)
    img_resized = transform.resize(img, dimension, anti_aliasing=True, mode='reflect')
    flat_data1.append(img_resized.flatten())

    result = rf.predict(flat_data1)
    print(result)

    result = list(result)
    index = (int(result[0]))
    index = index-1
    name = label[index]

    return result, percent, name