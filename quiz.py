import RealEngine.clumaDe, random

bildschirmBreite = 1440
bildschirmHoehe = 900

engine = RealEngine.clumaDe
engine.initialisieren(bildschirmBreite, bildschirmHoehe, True, (0,0,0))

class Kreis:
    def __init__(self, color = (0, 0, 0), position = [100,100], bewegungX = 1, bewegungY = 1, geschwindigkeit = 5, radius = 1, vergroesserung = 3, maxVergroesserung = 300):
        self.pos = position
        self.bewegungX = bewegungX
        self.bewegungY = bewegungY
        self.geschwindigkeit = geschwindigkeit
        self.radius = radius
        self.vergroesserung = vergroesserung
        self.color = color
        self.maxVergroesserung = maxVergroesserung

    def move(self):
        if self.radius > self.maxVergroesserung:
            self.radius = 5
 #       elif self.radius < 1:
 #           self.radius = 1
 #           self.vergroesserung *= -1
        
        if self.pos[0] < 0+self.radius:
            self.bewegungX = 1
            self.radius += self.vergroesserung
        if self.pos[0] > bildschirmBreite-self.radius:
            self.bewegungX = -1
            self.radius += self.vergroesserung
        if self.pos[1] < 0+self.radius:
            self.bewegungY = 1
            self.radius += self.vergroesserung
        if self.pos[1] > bildschirmHoehe-self.radius:
            self.bewegungY = -1
            self.radius += self.vergroesserung
        
        
        self.pos[0] += self.bewegungX * self.geschwindigkeit
        self.pos[1] += self.bewegungY * self.geschwindigkeit


    def draw(self):
        engine.zeichneKreis((self.pos[0], self.pos[1]), self.radius, self.color)


kreise = []

for i in range(0,500):
    kreise.append(Kreis(maxVergroesserung = random.randrange(200,500), geschwindigkeit = random.randrange(3,18), bewegungX = random.randrange(-1, 1, 2), bewegungY = random.randrange(-1, 1, 2), radius = random.randrange(1,100), position = [random.randrange(123,bildschirmBreite),random.randrange(123,bildschirmHoehe)], color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), vergroesserung = random.randrange(1,23)))
      
while True:
    for kreis in kreise:
        kreis.move()
        kreis.draw()
            
    engine.zeichneWoerter(position = (350, 400), woerter = "Music 4 ever!!!", schriftGroesse = 137, schriftFarbe = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))
            
    engine.zeichne()
            
engine.zerstoeren()

