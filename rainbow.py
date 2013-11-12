import QuizFL.quizFLG, random
import figures.unicorn, figures.astronaut

bildschirmBreite = 1440
bildschirmHoehe = 900

## die kollision mit der wand noch richtig machen
## variablen bei draw mit hoehe und breite richtig anpassen

engine = QuizFL.quizFLG
engine.initialisieren(bildschirmBreite, bildschirmHoehe, True, (0,0,0))

        
astronauten = []
unicorns = []
for i in range(0,99):
    astronauten.append(figures.astronaut.astronaut(color = (255,255,255), geschwindigkeit = random.randrange(3,18), bewegungX = random.randrange(-1, 1, 2), bewegungY = random.randrange(-1, 1, 2), position = [random.randrange(123,bildschirmBreite),random.randrange(123,bildschirmHoehe)]))
 #   unicorns.append(figures.unicorn.unicorn(groesse = random.randrange(1,8)/10.0, geschwindigkeit = random.randrange(3,18), position = [random.randrange(123,bildschirmBreite),random.randrange(123,bildschirmHoehe)]))


mittelpunktX = bildschirmBreite / 2
mittelpunktY = bildschirmHoehe

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

    #engine.zeichneKreis((bildschirmBreite, 0), 42, (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1210, 30), (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1225, 50), (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1250, 70), (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1275, 90), (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1300, 110), (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1325, 130), (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1350, 150), (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1375, 170), (255, 255, 0))
    #engine.zeichneLinie((bildschirmBreite, 0), (1400, 190), (255, 255, 0))

    for astro in astronauten:
        astro.move()
        astro.draw()
        
   # for unicorn in unicorns:
 #       unicorn.move()
 #       unicorn.draw()
    
    engine.zeichne()
           
engine.zerstoeren()
