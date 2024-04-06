from tensorflow.keras.utils import load_img,img_to_array
from PIL import Image

from constants import values,calories,s,model
from recommendation import diet_reccomend

def food_recognition_function(image_file):
    ## preprocessing
    img = Image.open(image_file)
    img = img.resize((224,224))
    img = img_to_array(img)
    img = img/255
    img = img.reshape(1, 224,224,3)

    ## prediction
    p1 = (model.predict(img)).argmax()
    print("Class ",p1,": ",values[p1],sep='')
    print(calories[p1],'\nNote:',s)
    # return {'samosa',100}
    return values[p1]
    

def diet_planning_function(weight, target_calories):
    return diet_reccomend(weight,target_calories)
