#####################################################################################################
# description: Random Forest classifier - obtain the accuracy
#####################################################################################################


import numpy as np
from sklearn import preprocessing, utils, model_selection, ensemble, metrics
from skimage import io, transform


WIDTH = 200
HEIGHT = 200

# this function is taken from this reference to load images from local directory and return as a bunch
# https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
def load_image_files(dataset_target, dataset_numpy, dimension=(WIDTH, HEIGHT, 3)):

    flat_data = []

    for image in dataset_numpy:
        # resize the image and add it back to the array
        img_resized = transform.resize(image, dimension, anti_aliasing=True, mode='reflect')
        flat_data.append(img_resized.flatten())

    flat_data = np.array(flat_data)
    target = np.array(dataset_target)

    # make a dict like with numpyarray of image and target
    return utils.Bunch(data=flat_data,
                 target=target)


# classification process
def classifier(predict_imag_path, dataset_target, dataset_numpy):
    label = ['Barbeton Daisy', 'Blanket Flower', 'Buttercup',
                'Carnation', 'Common Dandelion', 'Corn Poppy',
                'Lotus', 'Marigold', 'Rose', 'Sunflower']

    # make the dataset
    image_dataset = load_image_files(dataset_target, dataset_numpy)



    # split data into 70% training, 30% testing
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        image_dataset.data, image_dataset.target, test_size=0.3, random_state=109)

    # make into scaler so the ensure that all values fit in the same range
    scaler = preprocessing.StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    # Instantiate model with 100 decision trees
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

    # make a prediction
    y_pred = rf.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    # print('Accuracy of Random Forest classifier on test set: {:.2f}'.format(rf.score(X_test, y_test)))

    # get the accuracy of the classifier
    percent = rf.score(X_test, y_test)
    percent = percent*100

    # get the path of the uploaded image
    root = "djangoProject"
    path = root + predict_imag_path
    flat_data1 = []
    dimension = WIDTH, HEIGHT

    # open image
    img = io.imread(path)
    # resize
    img_resized = transform.resize(img, dimension, anti_aliasing=True, mode='reflect')
    flat_data1.append(img_resized.flatten())

    # predict
    result = rf.predict(flat_data1)
    print(result)
    # since array starts with 0 but the label starts with 1
    index = int(result)-1
    name = label[index]

    return result, percent, name
