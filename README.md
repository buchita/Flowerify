# djangoPythonAnywhere

Flowerify is a web application that classifies and provides the flower name from an input flower image. The application describes the flowers scientific name and botanical information which includes the maintenance and upkeep of the flower such as when and where to plant this flower, possible pests and diseases.  
 
As part of this project one of the aims is to optimise the classifier using different methods of image processing and image manipulation. The image processing GrabCut is used for image segmentation to segment the foreground and background from the input image.  
 
The RGB values are used to filter down the list of possible outcome flowers. 
Dominant RGB values are extracted from each image of the dataset which go through the GrabCut process. 
The input image RGB values are also extracted. These values are then used to identify the dominant colour of each flower type.  
The ColorThief python module is then used to retrieve the dominant RGB values of an image. The classifier Random Forest algorithm is used as the classification process.  
