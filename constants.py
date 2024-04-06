from tensorflow.keras.utils import load_img,img_to_array
from tensorflow.keras.models import load_model
from keras.optimizers import SGD

s = """Apple Pie: ~2.5 calories per gram
Baby Back Ribs: ~3.5 calories per gram
Baklava: ~5 calories per gram
Beef Carpaccio: ~2 calories per gram
Beef Tartare: ~2.5 calories per gram
Beet Salad: ~0.5 calories per gram
Beignets: ~3.5 calories per gram
Bibimbap: ~1.5 calories per gram
Bread Pudding: ~2.5 calories per gram
Breakfast Burrito: ~2 calories per gram
Bruschetta: ~1 calorie per gram
Caesar Salad: ~0.5 calories per gram
Cannoli: ~3.5 calories per gram
Caprese Salad: ~1 calorie per gram
Carrot Cake: ~3.5 calories per gram
Ceviche: ~0.5 calories per gram
Cheese Plate: ~3.5 calories per gram
Cheesecake: ~3.5 calories per gram
Chicken Curry: ~1.5 calories per gram
Chicken Quesadilla: ~2.5 calories per gram
Chicken Wings: ~3 calories per gram
Chocolate Cake: ~4 calories per gram
Chocolate Mousse: ~3 calories per gram
Churros: ~4 calories per gram
Clam Chowder: ~1.5 calories per gram
Club Sandwich: ~2.5 calories per gram
Crab Cakes: ~2 calories per gram
Creme Brulee: ~3.5 calories per gram
Croque Madame: ~3 calories per gram
Cupcakes: ~3.5 calories per gram
Deviled Eggs: ~1 calorie per gram
Donuts: ~4 calories per gram
Dumplings: ~2.5 calories per gram
Edamame: ~1 calorie per gram
Eggs Benedict: ~2.5 calories per gram
Escargots: ~1 calorie per gram
Falafel: ~2 calories per gram
Filet Mignon: ~2.5 calories per gram
Fish and Chips: ~2.5 calories per gram
Foie Gras: ~4.5 calories per gram
French Fries: ~3.5 calories per gram
French Onion Soup: ~1 calorie per gram
French Toast: ~2 calories per gram
Fried Calamari: ~2.5 calories per gram
Fried Rice: ~1.5 calories per gram
Frozen Yogurt: ~1 calorie per gram
Garlic Bread: ~4 calories per gram
Gnocchi: ~1.5 calories per gram
Greek Salad: ~0.5 calories per gram
Grilled Cheese Sandwich: ~3 calories per gram
Grilled Salmon: ~2 calories per gram
Guacamole: ~2 calories per gram
Gyoza: ~2 calories per gram
Hamburger: ~3.5 calories per gram
Hot and Sour Soup: ~0.5 calories per gram
Hot Dog: ~3.5 calories per gram
Huevos Rancheros: ~2 calories per gram
Hummus: ~1.5 calories per gram
Ice Cream: ~2 calories per gram
Lasagna: ~1.5 calories per gram
Lobster Bisque: ~1 calorie per gram
Lobster Roll Sandwich: ~2.5 calories per gram
Macaroni and Cheese: ~3 calories per gram
Macarons: ~4 calories per gram
Miso Soup: ~0.5 calories per gram
Mussels: ~0.5 calories per gram
Nachos: ~2.5 calories per gram
Omelette: ~1.5 calories per gram
Onion Rings: ~2.5 calories per gram
Oysters: ~0.5 calories per gram
Pad Thai: ~2 calories per gram
Paella: ~1.5 calories per gram
Pancakes: ~2 calories per gram
Panna Cotta: ~3.5 calories per gram
Peking Duck: ~4 calories per gram
Pho: ~1 calorie per gram
Pizza: ~2.5 calories per gram
Pork Chop: ~2.5 calories per gram
Poutine: ~2.5 calories per gram
Prime Rib: ~2.5 calories per gram
Pulled Pork Sandwich: ~2.5 calories per gram
Ramen: ~1 calorie per gram
Ravioli: ~1.5 calories per gram
Red Velvet Cake: ~4 calories per gram
Risotto: ~1.5 calories per gram
Samosa: ~2 calories per gram
Sashimi: ~1 calorie per gram
Scallops: ~1 calorie per gram
Seaweed Salad: ~0.5 calories per gram
Shrimp and Grits: ~2 calories per gram
Spaghetti Bolognese: ~1.5 calories per gram
Spaghetti Carbonara: ~2 calories per gram
Spring Rolls: ~1.5 calories per gram
Steak: ~2.5 calories per gram
Strawberry Shortcake: ~3.5 calories per gram
Sushi: ~1 calorie per gram
Tacos: ~2 calories per gram
Takoyaki: ~2.5 calories per gram
Tiramisu: ~3 calories per gram
Tuna Tartare: ~1.5 calories per gram
Waffles: ~2 calories per gram
"""
calories = s.splitlines()
s = "These values are approximations and can vary based on factors such as ingredients and cooking methods."
values = [
    {"Apple pie": 7.674},
    {"Baby back ribs": 61.785},
    {"Baklava": 45.3},
    {"Beef carpaccio": 0},
    {"Beef tartare": 100},
    {"Beet salad": 50.3215},
    {"Beignets": 38.172},
    {"Bibimbap": 100},
    {"Bread pudding": 33.1005},
    {"Breakfast burrito": 42.4635},
    {"Bruschetta": 100},
    {"Caesar salad": 38.9},
    {"Cannoli": 15.969},
    {"Caprese salad": 44.419},
    {"Carrot cake": 0},
    {"Ceviche": 100},
    {"Cheesecake": 4.984},
    {"Cheese plate": 0},
    {"Chicken curry": 100},
    {"Chicken quesadilla": 44.8},
    {"Chicken wings": 44.92},
    {"Chocolate cake": 0},
    {"Chocolate mousse": 15.428},
    {"Churros": 42.2},
    {"Clam chowder": 45.9795},
    {"Club sandwich": 100},
    {"Crab cakes": 43.058},
    {"Creme brulee": 100},
    {"Croque madame": 21.875},
    {"Cup cakes": 8.639},
    {"Deviled eggs": 27.29},
    {"Donuts": 1.177},
    {"Dumplings": 54.4595},
    {"Edamame": 69.5485},
    {"Eggs benedict": 100},
    {"Escargots": 100},
    {"Falafel": 18.536},
    {"Filet mignon": 49.44},
    {"Fish and chips": 60.0},
    {"Foie gras": 6.813},
    {"French fries": 39.2535},
    {"French onion soup": 100},
    {"French toast": 44.0465},
    {"Fried calamari": 100},
    {"Fried rice": 39.316},
    {"Frozen yogurt": 34.66},
    {"Garlic bread": 20.834},
    {"Gnocchi": 48.176},
    {"Greek salad": 54.049},
    {"Grilled cheese sandwich": 36.04},
    {"Grilled salmon": 71.9135},
    {"Guacamole": 49.271},
    {"Gyoza": 100},
    {"Hamburger": 39.7435},
    {"Hot and sour soup": 100},
    {"Hot dog": 54.41},
    {"Huevos rancheros": 100},
    {"Hummus": 22.408},
    {"Ice cream": 29.724},
    {"Lasagna": 54.1585},
    {"Lobster bisque": 100},
    {"Lobster roll sandwich": 100},
    {"Macaroni and cheese": 48.5985},
    {"Macarons": 100},
    {"Miso soup": 60.172},
    {"Mussels": 100},
    {"Nachos": 100},
    {"Omelette": 58.44},
    {"Onion rings": 29.84},
    {"Oysters": 100},
    {"Pad thai": 43.65},
    {"Paella": 22.2175},
    {"Pancakes": 32.935},
    {"Panna cotta": 30.1},
    {"Peking duck": 100},
    {"Pho": 100},
    {"Pizza": 38.0215},
    {"Pork chop": 100},
    {"Poutine": 20.585},
    {"Prime rib": 93.75},
    {"Pulled pork sandwich": 72.2545},
    {"Ramen": 37.2375},
    {"Ravioli": 39.765},
    {"Red velvet cake": 100},
    {"Risotto": 25.0425},
    {"Samosa": 100},
    {"Sashimi": 100},
    {"Scallops": 71.6055},
    {"Seaweed salad": 60.175},
    {"Shrimp and grits": 53.4535},
    {"Spaghetti bolognese": 51.414},
    {"Spaghetti carbonara": 76.4},
    {"Spring rolls": 100},
    {"Steak": 0},
    {"Strawberry shortcake": 22.187},
    {"Sushi": 100},
    {"Tacos": 0},
    {"Takoyaki": 50},
    {"Tiramisu": 85.463},
    {"Tuna tartare": 100},
    {"Waffles": 19.292}
]

model = load_model('models/model_food_101.h5', compile=False)
opt = SGD(lr=.1, momentum=.9)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
