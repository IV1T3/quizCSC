import RealEngine

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
        bildschirmBreite = RealEngine.clumaDe.bekommeBildschirmGroesse()[0]
        bildschirmHoehe = RealEngine.clumaDe.bekommeBildschirmGroesse()[1]
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
        RealEngine.clumaDe.zeichneRechteck(self.pos[0], self.pos[1], self.hoehe, self.breite, self.color)
        #Kopf
        RealEngine.clumaDe.zeichneKreis((self.pos[0]+13, self.pos[1]-8), self.radius, self.color)
        #Augen
        RealEngine.clumaDe.zeichneKreis((self.pos[0]+8, self.pos[1]-8), self.radius-12, (255, 0, 0))
        RealEngine.clumaDe.zeichneKreis((self.pos[0]+18, self.pos[1]-8), self.radius-12, (0, 0, 255))
        #Mund
        RealEngine.clumaDe.zeichneLinie((self.pos[0]+5, self.pos[1]), (self.pos[0]+15, self.pos[1]), (255,0,0))
        #Arme
        RealEngine.clumaDe.zeichneRechteck(self.pos[0]-20, self.pos[1]+8, self.breite-20, self.hoehe-20, self.color)
        RealEngine.clumaDe.zeichneRechteck(self.pos[0]+25, self.pos[1]+8, self.breite-20, self.hoehe-20, self.color)
        #Beine
        RealEngine.clumaDe.zeichneRechteck(self.pos[0]+3, self.pos[1]+40, self.breite-32, self.hoehe-5, self.color)
        RealEngine.clumaDe.zeichneRechteck(self.pos[0]+14, self.pos[1]+40, self.breite-32, self.hoehe-5, self.color)
