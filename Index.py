from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

#register the Aoolication
app = ClarifaiApp(api_key='add_your_api_key')

#upload 10 images for 'dogs' concept
img1 = ClImage(file_obj=open('DogImages/dog1.jpg', 'rb'),concepts=['dogs'])
img2 = ClImage(file_obj=open('DogImages/dog2.jpg', 'rb'),concepts=['dogs'])
img3 = ClImage(file_obj=open('DogImages/dog3.jpg', 'rb'),concepts=['dogs'])
img4 = ClImage(file_obj=open('DogImages/dog4.jpg', 'rb'),concepts=['dogs'])
img5 = ClImage(file_obj=open('DogImages/dog5.jpg', 'rb'),concepts=['dogs'])
img6 = ClImage(file_obj=open('DogImages/dog6.jpg', 'rb'),concepts=['dogs'])
img7 = ClImage(file_obj=open('DogImages/dog7.jpg', 'rb'),concepts=['dogs'])
img8 = ClImage(file_obj=open('DogImages/dog8.jpg', 'rb'),concepts=['dogs'])
img9 = ClImage(file_obj=open('DogImages/dog9.jpg', 'rb'),concepts=['dogs'])
img10 = ClImage(file_obj=open('DogImages/dog10.jpg', 'rb'),concepts=['dogs'])

#upload 10 images for 'cats' concept
img11 = ClImage(file_obj=open('CatImages/cat1.jpg', 'rb'),concepts=['cats'])
img12 = ClImage(file_obj=open('CatImages/cat2.jpg', 'rb'),concepts=['cats'])
img13 = ClImage(file_obj=open('CatImages/cat3.jpg', 'rb'),concepts=['cats'])
img14 = ClImage(file_obj=open('CatImages/cat4.jpg', 'rb'),concepts=['cats'])
img15 = ClImage(file_obj=open('CatImages/cat5.jpg', 'rb'),concepts=['cats'])
img16 = ClImage(file_obj=open('CatImages/cat6.jpg', 'rb'),concepts=['cats'])
img17 = ClImage(file_obj=open('CatImages/cat7.jpg', 'rb'),concepts=['cats'])
img18 = ClImage(file_obj=open('CatImages/cat8.jpg', 'rb'),concepts=['cats'])
img19 = ClImage(file_obj=open('CatImages/cat9.jpg', 'rb'),concepts=['cats'])
img20 = ClImage(file_obj=open('CatImages/cat10.jpg', 'rb'),concepts=['cats'])

#add images to Application
app.inputs.bulk_create_images([img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14,
                               img15, img16, img17,img18, img19, img20])

#create the model
app.models.create('pets', concepts=['dogs','cats'])

#get the 'pets' model from application
model = app.models.get('pets')

#train the model
model.train()