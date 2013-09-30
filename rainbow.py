import RealEngine.clumaDe, random

bildschirmBreite = 1280
bildschirmHoehe = 800

## die kollision mit der wand noch richtig machen
## variablen bei draw mit hoehe und breite richtig anpassen

engine = RealEngine.clumaDe
engine.initialisieren(bildschirmBreite, bildschirmHoehe, True, (0,0,0))

class astronaut:
    def __init__(self, color = (255, 255, 255), position = [100,100], bewegungX = 1, bewegungY = 1, geschwindigkeit = 5, radius = 15, hoehe = 25, breite = 40):
        self.pos = position
        self.bewegungX = bewegungX
        self.bewegungY = bewegungY
        self.geschwindigkeit = geschwindigkeit
        self.color = color
        self.radius = radius
        self.hoehe = hoehe
        self.breite = breite
        
    def move(self):
        if self.pos[0] < 30: #links mit armen
            self.bewegungX = 1
        
        if self.pos[0] > bildschirmBreite-35: # rechts mit armen
            self.bewegungX = -1
            
        if self.pos[1] < self.hoehe: # oben mit kopf
            self.bewegungY = 1
            
        if self.pos[1] > bildschirmHoehe-40-17: # unten mit beinen von 17 - body hoehe von 40
            self.bewegungY = -1
        
        self.pos[0] += self.bewegungX * self.geschwindigkeit
        self.pos[1] += self.bewegungY * self.geschwindigkeit
        
    def draw(self):
        #Koerper
        engine.zeichneRechteck(self.pos[0], self.pos[1], self.hoehe, self.breite, self.color)
        #Kopf
        engine.zeichneKreis((self.pos[0]+13, self.pos[1]-8), self.radius, self.color)
        #Augen
        engine.zeichneKreis((self.pos[0]+8, self.pos[1]-8), self.radius-12, (255, 0, 0))
        engine.zeichneKreis((self.pos[0]+18, self.pos[1]-8), self.radius-12, (0, 0, 255))
        #Mund
        engine.zeichneLinie((self.pos[0]+5, self.pos[1]), (self.pos[0]+15, self.pos[1]), (255,0,0))
        #Arme
        engine.zeichneRechteck(self.pos[0]-20, self.pos[1]+8, self.breite-20, self.hoehe-20, self.color)
        engine.zeichneRechteck(self.pos[0]+25, self.pos[1]+8, self.breite-20, self.hoehe-20, self.color)
        #Beine
        engine.zeichneRechteck(self.pos[0]+3, self.pos[1]+40, self.breite-32, self.hoehe-5, self.color)
        engine.zeichneRechteck(self.pos[0]+14, self.pos[1]+40, self.breite-32, self.hoehe-5, self.color)

class unicorn:
    def __init__(self, color = (255, 255, 255), position = [100,100], bewegungX = 1, bewegungY = 1, geschwindigkeit = 5):
        self.pos = position
        self.bewegungX = bewegungX
        self.bewegungY = bewegungY
        self.geschwindigkeit = geschwindigkeit
        self.color = color
        
    def move(self):
        if self.pos[0] < 30: #links mit armen
            self.bewegungX = 1
        
        if self.pos[0] > bildschirmBreite-35: # rechts mit armen
            self.bewegungX = -1
            
        if self.pos[1] < self.hoehe: # oben mit kopf
            self.bewegungY = 1
            
        if self.pos[1] > bildschirmHoehe-40-17: # unten mit beinen von 17 - body hoehe von 40
            self.bewegungY = -1
        
        self.pos[0] += self.bewegungX * self.geschwindigkeit
        self.pos[1] += self.bewegungY * self.geschwindigkeit
        
    def draw(self):
        #Koerper
        engine.zeichneRechteck(self.pos[0], self.pos[1], 20, 100, self.color)
        #Kopf
        engine.zeichneKreis((self.pos[0]+13, self.pos[1]-8), self.radius, self.color)
        #Augen
        engine.zeichneKreis((self.pos[0]+8, self.pos[1]-8), self.radius-12, (255, 0, 0))
        engine.zeichneKreis((self.pos[0]+18, self.pos[1]-8), self.radius-12, (0, 0, 255))
        #Mund
        engine.zeichneLinie((self.pos[0]+5, self.pos[1]), (self.pos[0]+15, self.pos[1]), (255,0,0))
        #Arme
        engine.zeichneRechteck(self.pos[0]-20, self.pos[1]+8, self.breite-20, self.hoehe-20, self.color)
        engine.zeichneRechteck(self.pos[0]+25, self.pos[1]+8, self.breite-20, self.hoehe-20, self.color)
        #Beine
        engine.zeichneRechteck(self.pos[0]+3, self.pos[1]+40, self.breite-32, self.hoehe-5, self.color)
        engine.zeichneRechteck(self.pos[0]+14, self.pos[1]+40, self.breite-32, self.hoehe-5, self.color)


        
astronauten = []
for i in range(0,99):
    astronauten.append(astronaut(geschwindigkeit = random.randrange(3,18), bewegungX = random.randrange(-1, 1, 2), bewegungY = random.randrange(-1, 1, 2), position = [random.randrange(123,bildschirmBreite),random.randrange(123,bildschirmHoehe)]))

mittelpunktX = bildschirmBreite / 2
mittelpunktY = bildschirmHoehe / 2

while True:
    # Regenbogen wird gemalt
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 550, (255, 0, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 538, (255, 35, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 525, (255, 70, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 513, (255, 105, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 500, (255, 140, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 488, (255, 167, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 475, (255, 195, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 463, (255, 220, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 450, (255, 255, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 438, (195, 255, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 425, (127, 255, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 413, (65, 255, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 400, (0, 255, 0))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 388, (0, 195, 65))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 375, (0, 127, 127))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 363, (0, 65, 195))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 350, (0, 0, 255))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 338, (65, 0, 255))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 325, (127, 0, 255))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 313, (195, 0, 255))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 300, (255, 0, 255))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 289, (195, 0, 195))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 275, (127, 0, 127))
    engine.zeichneKreis((mittelpunktX, mittelpunktY), 263, (0, 0, 0))

    engine.zeichneKreis((bildschirmBreite, 0), 42, (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1210, 30), (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1225, 50), (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1250, 70), (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1275, 90), (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1300, 110), (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1325, 130), (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1350, 150), (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1375, 170), (255, 255, 0))
    engine.zeichneLinie((bildschirmBreite, 0), (1400, 190), (255, 255, 0))

    for astro in astronauten:
        astro.move()
        astro.draw()
    
    engine.zeichne()
           
engine.zerstoeren()
