import quizFL

def initialisieren(breite, hoehe, vollbild, hintergrundfarbe = (0,0,0)):
     quizFL.init(breite, hoehe, vollbild, hintergrundfarbe)

def zerstoeren():
     quizFL.destruct()

def zeichneRechteck(x, y, breite, hoehe, farbe):
     quizFL.drawRect(x, y, breite, hoehe, farbe)

def zeichneKreis(mittelpunkt, radius, farbe):
     quizFL.drawCircle(mittelpunkt, radius, farbe)
     
def zeichneEllipse(x, y, breite, hoehe, farbe):
    quizFL.drawEllipse(x, y, breite, hoehe, farbe)

def zeichneWoerter(position, woerter, schriftGroesse = 23, schriftFarbe = (255,255,255)):
     quizFL.drawWords(position, woerter, schriftGroesse, schriftFarbe)

def zeichneLinie(punkt1, punkt2, farbe):
     quizFL.drawLine(punkt1, punkt2, farbe)

def zeichneDreieck(punkt1, punkt2, punkt3, farbe):
     quizFL.drawTriangle(punkt1, punkt2, punkt3, farbe)
     
def bekommeBildschirmGroesse():
    """Gibt die Bildschirmgroesse zurueck"""
    return quizFL.getScreenSize()

def zeichne():
     quizFL.draw()
