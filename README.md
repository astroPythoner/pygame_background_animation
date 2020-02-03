# pygame background animation
A background with moving points and lines made with pygame

# Notwendige Bibliotheken
- pygame

***

![](https://raw.githubusercontent.com/pygame_background_animation/Shmup/master/screenshot1.png)

# Verwendung

### 1. Erstellen eines neuen Backgroundobjekts:
```
my_background = Background(width,height,knoten_farbe,hintergrund_farbe,linienfarbe=None,anz_knoten=None,knoten_radius=5,max_speed=10,connection_distance=70,connection_line_width=1)
```
##### Attribute des Konstruktors:
- width,height (Größe des Bildschirms) (Ganzzahlen)
- knoten_farbe (Farbe der Punkte) (Pygame.Color Objekt mitgeben)
- hintergrund_farbe (Farbe des Hintergrunds) (Pygame.Color Objekt mitgeben)
- linienfarbe (Farbe der Linien, wenn nicht gesetzt gleich wie Knotenfrabe) (Pygame.Color Objekt mitgeben)
- anz_knoten (Anzahl der Punkte, wenn nicht gesetzt berechnet aus width und height) (Ganzzahl nicht 0)
- knoten_radius (Größe der Punkte, Standart 5) (Ganzzahl)
- max_speed (Maximalgeschindigkeit der Punkte, Standart 10) (Ganz- oder Kommazahl)
- connection_distance (Abstand bis zu der Linien zwischen Punkten gezeichnet werden) (Ganzzahl)
- connection_line_width (Dicke der Linien) (Ganzzahl)

### 2. Verwenden des Backgroundobjekts:
```
my_background.update()
image = my_background.draw()
```

##### Erklärung der update und draw Funktion:
- Die update Funktion bewegt alle Punkte um zum zeichnen bereit zu werden
- Die draw Funktion gibt eine pygame Surface zurück mit Größe (width,height), in der Linien und Punkte eingezeichnet sind

### Bearbeiten des Backgroundobjekts:
```
my_background.set_size(width,height)                # Verändert width und height (Ganzzahlen)
my_background.set_knoten_size(radius)               # Verändert Größe der Punkte (Ganzzahl)
my_background.set_line_size(width)                  # Verändert Breite der Linien (Ganzzahl)
my_background.set_anz_knoten(zahl)                  # Verändert Anzahl der Punkte (löscht oder erstellt neue) (Ganzzahl nicht 0)
my_background.get_num_knoten()                      # Gibt zurück wie viele Knoten momentan zu sehen sind
my_background.set_knoten_color(color)               # Farbe der Punkte setzten (pagame.Color Objekt)
my_background.set_background_color(color)           # Hintergrundfarbe setzten (pagame.Color Objekt)
my_background.set_linien_color(color)               # Farbe der Linien setzten (pagame.Color Objekt)
my_background.set_connection_distance(distance)     # Verändert Abstand bis zu der Linien zwischen Punkten gezeichnet werden (Ganzzahl)
```
