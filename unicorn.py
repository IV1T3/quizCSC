import RealEngine.clumaDe

bildschirmBreite = 1280
bildschirmHoehe = 800

engine = RealEngine.clumaDe

engine.initialisieren(bildschirmBreite, bildschirmHoehe, False, (255, 0, 255))

x = 200
y = 200

while True:

     #Koerper
     engine.zeichneRechteck(x, y, 250, 75, (255,255,255))

     #Beine und Hufen
     engine.zeichneRechteck(x, y + 75, 20, 60, (255,255,255))
     engine.zeichneRechteck(x, y + 75 + 60, 20, 10, (0,0,0))
     
     engine.zeichneRechteck(x+230, y + 75, 20, 60, (255,255,255))
     engine.zeichneRechteck(x+230, y + 75+60, 20, 10, (0,0,0))

     #Hals
     engine.zeichneRechteck(x+250-30, y, 30, -50, (255,255,255))

     #Horn
     engine.zeichneDreieck((x+250-25, y-75), (x+250, y-75), (x+300, y-150), (233,233,233))

     #Kopf
     engine.zeichneKreis((x+250-15, y - 50), 30, (255,255,255))

     #Auge
     engine.zeichneKreis((x+250, y - 60), 5, (0,0,0))
     
     #Schweif
     engine.zeichneDreieck((x, y), (x-20, y+90), (x, y+40), (0,0,0))
     
     engine.zeichne()

engine.zerstoere()
