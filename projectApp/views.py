import os
from django.shortcuts import render
from projectApp.models import Flower, TrainModel
from django.core.files.storage import FileSystemStorage
from projectApp.MachineLearning import image_quality_assessment, random_forest, dataset_filter
from djangoProject import settings
import base64



def home(request):
    # fetch the content from db
    obj1 = Flower.objects.get(id=1)
    # convert from blob to bytes to string
    image_data1 = base64.b64encode(obj1.image).decode()

    data1 = {
        'flowerName': obj1.name,
        'image': image_data1
    }

    obj2 = Flower.objects.get(id=2)
    image_data2 = base64.b64encode(obj2.image).decode()

    data2 = {
        'flowerName': obj2.name,
        'image': image_data2
    }

    obj3 = Flower.objects.get(id=3)
    image_data3 = base64.b64encode(obj3.image).decode()

    data3 = {
        'flowerName': obj3.name,
        'image': image_data3
    }

    obj4 = Flower.objects.get(id=4)
    image_data4 = base64.b64encode(obj4.image).decode()

    data4 = {
        'flowerName': obj4.name,
        'image': image_data4
    }

    obj5 = Flower.objects.get(id=5)
    image_data5 = base64.b64encode(obj5.image).decode()

    data5 = {
        'flowerName': obj5.name,
        'image': image_data5
    }

    obj6 = Flower.objects.get(id=6)
    image_data6 = base64.b64encode(obj6.image).decode()

    data6 = {
        'flowerName': obj6.name,
        'image': image_data6
    }


    obj7 = Flower.objects.get(id=7)
    image_data7 = base64.b64encode(obj7.image).decode()

    data7 = {
        'flowerName': obj7.name,
        'image': image_data7
    }


    obj8 = Flower.objects.get(id=8)
    image_data8 = base64.b64encode(obj8.image).decode()

    data8 = {
        'flowerName': obj8.name,
        'image': image_data8
    }



    obj9 = Flower.objects.get(id=9)
    image_data9 = base64.b64encode(obj9.image).decode()

    data9 = {
        'flowerName': obj9.name,
        'image': image_data9
    }

    obj10 = Flower.objects.get(id=10)
    image_data10 = base64.b64encode(obj10.image).decode()

    data10 = {
        'flowerName': obj10.name,
        'image': image_data10
    }

    # populating the unqiue key to use in the html
    data_array = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]
    data_dict = {}
    index = 1
    for x in data_array:
        key = "key" + '_' + str(index)
        data_dict[key] = x
        index = index + 1

    return render(request, 'home.html',
                  data_dict)


# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
def upload_file(request):
    # this is the path to save the image to /media/images directory
    image_root = os.path.join(settings.MEDIA_ROOT, 'images/')

    # this is for accessing the image after saved
    image_url = os.path.join(settings.MEDIA_URL, 'images/')
    context = {}
    extension = ".jpg"

    # when submitted
    # https://github.com/sibtc/django-upload-example/blob/master/mysite/core/views.py
    if request.method == 'POST':
        # if file is selected
        if len(request.FILES) != 0:
            # fetch the file from upload
            uploaded_file = request.FILES['document']

            # check if the file ends with jpg
            if str(uploaded_file).endswith(extension):

                # declare the file system with location to /images
                fs = FileSystemStorage(location=image_root, base_url=image_url)
                # save image to the folder
                name = fs.save(uploaded_file.name, uploaded_file)
                # get url
                url = fs.url(name)
                # check the quality of the image
                image_result = image_quality_assessment.image_quality(url)
                print(image_result)
                if image_result > 70:
                    print("too blurry")
                    context = {'blurry': 'Upload a clearer image'}
                else:
                    # filter the RGB value
                    tag_name = dataset_filter.filer(url)

                    base64_im_ar = []
                    dataset_target = []
                    dataset_numpy = []

                    # if list of matched RGB is empty
                    if not tag_name:
                        print("not statement, empty")
                        for i in TrainModel.objects.all():
                            image_data = ""
                            # convert blob to string
                            image_data = base64.b64encode(i.image_dataset).decode()
                            base64_im_ar.append(image_data)

                            # convert from base 64 to numpy
                            numpy_arr_image = image_quality_assessment.stringToRGB(image_data)
                            # get label tag
                            dataset_target.append(i.id)
                            dataset_numpy.append(numpy_arr_image)
                    # if there is some matching from RGB
                    else:
                        for i in TrainModel.objects.all():
                            for j in tag_name:
                                if i.id == j:

                                    print(i.image_id)
                                    image_data = ""
                                    image_data = base64.b64encode(i.image_dataset).decode()
                                    base64_im_ar.append(image_data)

                                    # convert from base 64 to numpy
                                    numpy_arr_image = image_quality_assessment.stringToRGB(image_data)
                                    dataset_target.append(i.id)
                                    dataset_numpy.append(numpy_arr_image)
                    # classification process
                    predict, percent, name = random_forest.classifier(url, dataset_target, dataset_numpy)

                    # description, planting, care_information, disease, tips, meaning = ''


                    for i in Flower.objects.all().filter(name=name):
                        description = i.description
                        planting = i.planting
                        meaning = i.meaning
                        care_information = i.care_information
                        disease = i.disease
                        tips = i.tips

                    context = {'url': url, 'result': image_result, 'predict_result': predict, 'percent': percent,
                               'name': name,
                               'description': description, 'planting': planting,
                               'care_information': care_information, 'disease': disease,
                               'tips': tips, 'meaning': meaning}
                    # context = { 'url': url, 'result': result, 'predict': predict, 'percent': percent}
            else:
                error_text = "Only jpg extension is accepted"
                context = {'error_text': error_text}
        # if file is not selected
        else:
            print("no file selecteddddd+++++++++++++++++++++++++++")
            no_file = "No image is selected. Please select an image"
            context = {'no_file': no_file}

    return render(request, 'uploader.html', context)


# keyword filter
def filter(request):
    filtered = {}
    if request.method == "GET":
        try:
            # get keyword from search bar
            keyword = request.GET.get('searchkeyword')
            keyword = keyword.lower()
            # filter flower
            for i in Flower.objects.all().filter(name=keyword):
                image_data = base64.b64encode(i.image).decode()

                filtered = {
                    'description': i.description,
                    'name': i.name,
                    'image': image_data,
                    'planting': i.planting,
                    'meaning': i.meaning,
                    'care_information': i.care_information,
                    'disease': i.disease,
                    'tips': i.tips
                }

        except Flower.DoesNotExist:
            filtered = { 'error':  "this doesnt exist"}

    return render(request, 'display.html', filtered)



# this is the beginning of the reading flower from the database
def DaisyInformation(request):
    # return HttpResponse(index_home)
    # https: // stackoverflow.com / questions / 56138525 / how - to - show - a - blob - image - on - html - page - in -django
    obj = Flower.objects.get(id=1)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)


def BlanketFlower(request):
    # return HttpResponse(index_home)
    # https: // stackoverflow.com / questions / 56138525 / how - to - show - a - blob - image - on - html - page - in -django
    obj = Flower.objects.get(id=2)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)


def Buttercup(request):
    obj = Flower.objects.get(id=3)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)



def Carnation(request):
    obj = Flower.objects.get(id=4)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)


def Dandelion(request):
    obj = Flower.objects.get(id=5)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)


def CornPoppy(request):
    obj = Flower.objects.get(id=6)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)


def Lotus(request):
    obj = Flower.objects.get(id=7)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)


def Marigold(request):
    obj = Flower.objects.get(id=8)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)


def Sunflower(request):
    obj = Flower.objects.get(id=9)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    # flowers = Flower.objects.all()
    return render(request, 'flower_info_display.html', data)


def Rose(request):
    obj = Flower.objects.get(id=10)

    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data,
        'planting': obj.planting,
        'meaning': obj.meaning,
        'care_information': obj.care_information,
        'disease': obj.disease,
        'tips': obj.tips
    }
    return render(request, 'flower_info_display.html', data)
