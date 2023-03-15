import xml.etree.ElementTree as ET

class Samochod():
    def __init__(self,color,engine,type,brand):
        self.color = color
        self.engine = engine
        self.type = type
        self.brand = brand
        

List_car = []              
List_car.append(Samochod("red","4.2","suv","honda"))
List_car.append(Samochod("black","3.0","crossover","bmw"))
List_car.append(Samochod("yellow","1.6","suv","toyota"))
List_car.append(Samochod("grey","3.0","suv","jeep"))
List_car.append(Samochod("red","1.0","crossover","dacia"))
List_car.append(Samochod("yellow","1.2","hatchback","renault"))
List_car.append(Samochod("red","2.0","coupe","mercedes"))
List_car.append(Samochod("black","2.0","sedan","skoda"))
List_car.append(Samochod("white","2.0","wagon","vw"))
List_car.append(Samochod("blue","3.2","roadster","porsche"))
List_car.append(Samochod("black","3.0","sedan","bentley"))

root = ET.Element("cars")
for car in List_car:
    car1 = ET.SubElement(root, "car", brand=car.brand)
    ET.SubElement(car1 , "color").text = car.color
    ET.SubElement(car1 , "engine").text = car.engine
    ET.SubElement(car1 , "type").text = car.type    
tree = ET.ElementTree(root)
tree.write("samochody.xml")   
  
  
tree = ET.parse('samochody.xml') # zmiana pojemności silnika dla każdego z obiektów i dodanie atrybutu do silnika "modified"
root = tree.getroot()
for engine in root.iter('engine'): 
    new_engine = float(engine.text) +1
    engine.text = str(new_engine)
    engine.set('modified','yes')
tree.write('samochody.xml')

tree1 = ET.parse('samochody.xml') # utworzenie obiektów klasy i wypisanie w konsoli
root1 = tree1.getroot()
Cars_to_add=[] 
for i in root1:
    z = i.get("brand")
    Cars_to_add.append(Samochod(color=i[0].text,engine=i[1].text,type=i[2].text,brand=z)) 
    
for car in Cars_to_add:
    print(f"Car Brand: {car.brand}, Color: {car.color}, Engine: {car.engine}, Type: {car.type}")
       



