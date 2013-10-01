import RealEngine

class unicorn:
    def __init__(self, color = (255, 255, 255), position = [100,100], bewegungX = 1, bewegungY = 1, geschwindigkeit = 5, groesse = 1):
        self.pos = position
        self.bewegungX = bewegungX
        self.bewegungY = bewegungY
        self.geschwindigkeit = geschwindigkeit
        self.color = color
        self.groesse = groesse
        
    def move(self):
        bildschirmBreite = RealEngine.clumaDe.bekommeBildschirmGroesse()[0]
        bildschirmHoehe = RealEngine.clumaDe.bekommeBildschirmGroesse()[1]
        if self.pos[0] < 20 * self.groesse: #links mit schweif
            self.bewegungX = 1
        
        if self.pos[0] > bildschirmBreite-300 * self.groesse: # rechts mit horn
            self.bewegungX = -1
            
        if self.pos[1] < 150 * self.groesse: # oben mit horn
            self.bewegungY = 1
            
        if self.pos[1] > bildschirmHoehe - 145 * self.groesse: # unten mit beinen
            self.bewegungY = -1
        
        self.pos[0] += self.bewegungX * self.geschwindigkeit
        self.pos[1] += self.bewegungY * self.geschwindigkeit
        
    def draw(self):
        x = self.pos[0]
        y = self.pos[1]
        #Koerper
        
        RealEngine.clumaDe.zeichneRechteck(x, y, int(250 * self.groesse), int(75 * self.groesse), (255,255,255))

        #Beine und Hufen
        RealEngine.clumaDe.zeichneRechteck(x, y + int(75 * self.groesse), int(20 * self.groesse), int(60 * self.groesse), (255,255,255))
        RealEngine.clumaDe.zeichneRechteck(x, y + int(75 * self.groesse) + int(60 * self.groesse), int(20 * self.groesse), int(10 * self.groesse), (0,0,0))

        RealEngine.clumaDe.zeichneRechteck(x+int(230 * self.groesse), y + int(75 * self.groesse), 20 * self.groesse, 60 * self.groesse, (255,255,255))
        RealEngine.clumaDe.zeichneRechteck(x+int(230 * self.groesse), y + int(75 * self.groesse + 60 * self.groesse), int(20 * self.groesse), int(10 * self.groesse), (0,0,0))

        #Hals
        RealEngine.clumaDe.zeichneRechteck(x+int(250 * self.groesse) - int(30 * self.groesse), y, 30 * self.groesse, -50 * self.groesse, (255,255,255))

        #Horn
        RealEngine.clumaDe.zeichneDreieck((x+250 * self.groesse-25 * self.groesse, y-75 * self.groesse), (x+250 * self.groesse, y-75 * self.groesse), (x+300 * self.groesse, y-150 * self.groesse), (233,233,233))

        #Kopf
        RealEngine.clumaDe.zeichneKreis((int(x+250 * self.groesse) - int(15 * self.groesse), y - int(50 * self.groesse)), int(30 * self.groesse), (255,255,255))

        #Auge
        RealEngine.clumaDe.zeichneKreis((int(x+250 * self.groesse), y - int(60 * self.groesse)), int(5 * self.groesse), (0,0,0))

        #Schweif
        RealEngine.clumaDe.zeichneDreieck((x, y), (x-20 * self.groesse, y+90 * self.groesse), (x, y+40 * self.groesse), (0,0,0))
