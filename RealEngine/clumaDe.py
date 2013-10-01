import cluma

def initialisieren(breite, hoehe, vollbild, hintergrundfarbe = (0,0,0)):
     cluma.init(breite, hoehe, vollbild, hintergrundfarbe)

def zerstoeren():
     cluma.destruct()

def zeichneRechteck(x, y, breite, hoehe, farbe):
     cluma.drawRect(x, y, breite, hoehe, farbe)

def zeichneKreis(mittelpunkt, radius, farbe):
     cluma.drawCircle(mittelpunkt, radius, farbe)
     
def zeichneEllipse(x, y, breite, hoehe, farbe):
    cluma.drawEllipse(x, y, breite, hoehe, farbe)

def zeichneWoerter(position, woerter, schriftGroesse = 23, schriftFarbe = (255,255,255)):
     cluma.drawWords(position, woerter, schriftGroesse, schriftFarbe)

def zeichneLinie(punkt1, punkt2, farbe):
     cluma.drawLine(punkt1, punkt2, farbe)

def zeichneDreieck(punkt1, punkt2, punkt3, farbe):
     cluma.drawTriangle(punkt1, punkt2, punkt3, farbe)
     
def bekommeBildschirmGroesse():
    """Gibt die Bildschirmgroesse zurueck"""
    return cluma.getScreenSize()

def zeichne():
     cluma.draw()
