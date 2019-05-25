
class Gif:
    
    def __init__(self, cantImgs, nameImg, framesPorImg = 3): #Cantidad de Imagenes, Formato de Nombre, Frames a pasar por cada imagen.
        
        self.cont = 0
        self.frame = 0
        self.cantImgs = cantImgs
        self.nameImg = nameImg
        self.framesPorImg = framesPorImg
        self.imgs = [loadImage(nameImg.format(_)) for _ in range(cantImgs)]
    
    def show(self, xIni, yIni, xFin=False, yFin=False): # posicion Inicial en X, posicion Inicial en Y, posicion Final en X, posicion Final en Y.
        
        if self.cont % self.framesPorImg == 0:
            self.frame = (self.frame+1) % self.cantImgs
        
        if not xFin or not yFin:
            image(self.imgs[self.frame], xIni, yIni)
        else:
            image(self.imgs[self.frame], xIni, yIni, xFin, yFin)
        
        self.cont += 1

class Obj:
    def __init__(self, xplus, yplus):
        self.Activo = True
        self.radio = diametro/2
        self.Width  = 0
        self.Height = 0
        self.xplus = xplus
        self.yplus = yplus
        self.x = x + xplus
        self.y = y + yplus
        self.col = (random(255),random(255),random(255))
        self.Plus = False
    
    def __str__(self): return str(self.x) + ' ' + str(self.y)
    
    def crearRect(self, Width, Height, Show = True):
        if Show: rect(self.x, self.y, Width, Height)
        self.Width =  Width
        self.Height = Height
    
    #Si hay una colision precisa de un circulo y un rectangulo devuelve True.
    def isCollidingCR(self): # CR = Circle and Rectangle.
        circleDistanceX = abs(circX - self.x - self.Width/2)
        circleDistanceY = abs(circY - self.y - self.Height/2)
        if circleDistanceX >  (self.Width/2 + self.radio):  return False
        if circleDistanceY >  (self.Height/2 + self.radio): return False
        if circleDistanceX <= (self.Width/2):  return True
        if circleDistanceY <= (self.Height/2): return True
        cornerDistance_sq = pow(circleDistanceX - self.Width/2, 2) + pow(circleDistanceY - self.Height/2, 2)
        return (cornerDistance_sq <= pow(self.radio,2))
    
    def isCollidingCREnemy(self): # CR = Circle and Rectangle.
        circleDistanceX = abs(x+enemyX - self.x - self.Width/2)
        circleDistanceY = abs(y+enemyY - self.y - self.Height/2)
        if circleDistanceX >  (self.Width/2 + self.radio):  return False
        if circleDistanceY >  (self.Height/2 + self.radio): return False
        if circleDistanceX <= (self.Width/2):  return True
        if circleDistanceY <= (self.Height/2): return True
        cornerDistance_sq = pow(circleDistanceX - self.Width/2, 2) + pow(circleDistanceY - self.Height/2, 2)
        return (cornerDistance_sq <= pow(self.radio,2))
        
    def isPos(self, Pos):
        if self.x < circX and self.y > circY:
            if not Pos == 'Aba': return False
        elif self.x > circX and self.y < circY:
            if not Pos == 'Der': return False
        elif self.x+self.Width > circX and self.y+self.Height < circY:
            if not Pos == 'Arr': return False
        elif self.x+self.Width < circX and self.y+self.Height > circY:
            if not Pos == 'Izq': return False
        
        return True


class ObjM:
    def __init__(self, x, y):
        self.Activo = True
        self.radio = diametro/2
        self.Width  = 0
        self.Height = 0
        self.x = x
        self.y = y
        self.col = (random(255),random(255),random(255))
        self.Plus = False
    
    def __str__(self): return str(self.x) + ' ' + str(self.y)
    
    def crearRect(self, Width, Height, Show = True):
        if Show: rect(self.x, self.y, Width, Height)
        self.Width =  Width
        self.Height = Height
    
    #Si hay una colision precisa de un circulo y un rectangulo devuelve True.
    def isCollidingCR(self): # CR = Circle and Rectangle.
        circleDistanceX = abs(player1X - self.x - self.Width/2)
        circleDistanceY = abs(player1Y - self.y - self.Height/2)
        if circleDistanceX >  (self.Width/2 + self.radio):  return False
        if circleDistanceY >  (self.Height/2 + self.radio): return False
        if circleDistanceX <= (self.Width/2):  return True
        if circleDistanceY <= (self.Height/2): return True
        cornerDistance_sq = pow(circleDistanceX - self.Width/2, 2) + pow(circleDistanceY - self.Height/2, 2)
        return (cornerDistance_sq <= pow(self.radio,2))
    
    def isCollidingCR2(self): # CR = Circle and Rectangle.
        circleDistanceX = abs(player2X - self.x - self.Width/2)
        circleDistanceY = abs(player2Y - self.y - self.Height/2)
        if circleDistanceX >  (self.Width/2 + self.radio):  return False
        if circleDistanceY >  (self.Height/2 + self.radio): return False
        if circleDistanceX <= (self.Width/2):  return True
        if circleDistanceY <= (self.Height/2): return True
        cornerDistance_sq = pow(circleDistanceX - self.Width/2, 2) + pow(circleDistanceY - self.Height/2, 2)
        return (cornerDistance_sq <= pow(self.radio,2))
    
    def isPosPlayer1(self, Pos):
        if self.x < player1X and self.y > player1Y:
            if not Pos == 'Aba': return False
        elif self.x > player1X and self.y < player1Y:
            if not Pos == 'Der': return False
        elif self.x+self.Width > player1X and self.y+self.Height < player1Y:
            if not Pos == 'Arr': return False
        elif self.x+self.Width < player1X and self.y+self.Height > player1Y:
            if not Pos == 'Izq': return False
        
        return True
    
    def isPosPlayer2(self, Pos):
        if self.x < player2X and self.y > player2Y:
            if not Pos == 'Aba': return False
        elif self.x > player2X and self.y < player2Y:
            if not Pos == 'Der': return False
        elif self.x+self.Width > player2X and self.y+self.Height < player2Y:
            if not Pos == 'Arr': return False
        elif self.x+self.Width < player2X and self.y+self.Height > player2Y:
            if not Pos == 'Izq': return False
        
        return True

def creaEstante(cordX, cordY, limite, dir):
    
    Lista = []
    ancho = 0
    separ = 0
    
    for i in range(100):
        if dir == 'h':
            if cordX+separ+10 > limite-10: break
        if dir == 'v':
            if cordY+separ+10 > limite-10: break
        
        separ += ancho
        ancho = int(random(10,20))
        if dir == 'h': obj = Obj(cordX+separ+10, cordY+5)
        if dir == 'v': obj = Obj(cordX+5, cordY+separ+10)
        Lista.append((obj, ancho))
        
    return Lista

def rangos(val): return (-int(val/2), int(val/2))



#=================================================================================================
# Variables Globales: Minijuego #1: ==============================================================
#=================================================================================================
Mapa = [(600, 300), (600,600), (600,600), (600,600), (600,600)]
Nivel = 1
circX, circY = 0, 0
r1 = rangos(Mapa[Nivel-1][0])
r2 = rangos(Mapa[Nivel-1][1])

x, y = 900, 50
enemyX, enemyY = -500, -200

diametro = 40
puntaje = 0
puntajenemy = 0
Ancho = 50
Objetos = []
cantLibs = 8
randy = int(random(24))
PersonRandom = int(random(6))
victorias = 0

vel = 3
Plus = 0
PlusE = 0
reinicio = False
iniciar = False
cont = 0
miliseg = 0
seconds = 0

Libros1 = [Obj(0, 0) for _ in range(cantLibs)]
Libs = [(int(random(r1[0]-50, r1[1]+50)), int(random(r2[0], r2[1]))) for _ in range(cantLibs)]
randLibs = [int(random(30)) for _ in range(24)]
randLibs2 = [int(random(33)) for _ in range(100)]
estantes = [
            creaEstante(-Mapa[Nivel-1][0]+Ancho,  Mapa[Nivel-1][1],        Mapa[Nivel-1][0], 'h'),
            creaEstante(-Mapa[Nivel-1][0],       -Mapa[Nivel-1][1],        Mapa[Nivel-1][0], 'h'),
            creaEstante(-Mapa[Nivel-1][0],       -Mapa[Nivel-1][1]+Ancho,  Mapa[Nivel-1][1], 'v'),
            creaEstante( Mapa[Nivel-1][0],       -Mapa[Nivel-1][1],        Mapa[Nivel-1][1], 'v')
        ]
#=================================================================================================
#=================================================================================================
#=================================================================================================


ObjetosM = []
player1X, player1Y, player2X, player2Y = 100, 500, 900, 500
multiplayer = False

puntajeP1 = 0
puntajeP2 = 0
PlusP1 = 0
PlusP2 = 0
velP1 = 2
velP2 = 2
selectP1 = 0
selectP2 = 9
victoriasP1 = 0
victoriasP2 = 0

reinicioM = False
milisegM = 0
totalLibsM = 300
cantMonedasM = 30
secTemp = 0
cooldown = 30

randLibsM = [int(random(30)) for _ in range(totalLibsM)]
LibrosM = [ObjM(int(random(100, 950)), int(random(100, 400))) for _ in range(totalLibsM)]
randyM = [int(random(totalLibsM)) for _ in range(cantMonedasM)]


#=================================================================================================
#=================================================================================================
#=================================================================================================


def crearObjetosEstaticos():
    
    global Objetos
    Objetos = []
    
    estante1 = Obj(-Mapa[Nivel-1][0],       -Mapa[Nivel-1][1])
    estante2 = Obj(-Mapa[Nivel-1][0],       -Mapa[Nivel-1][1]+Ancho)
    estante3 = Obj( Mapa[Nivel-1][0],       -Mapa[Nivel-1][1])
    estante4 = Obj(-Mapa[Nivel-1][0]+Ancho,  Mapa[Nivel-1][1])
    
    Objetos.append(estante1)
    Objetos.append(estante2)
    Objetos.append(estante3)
    Objetos.append(estante4)
    
    fill(100, 50, 0)
    stroke(0)
    
    Objetos[0].crearRect(Mapa[Nivel-1][0]*2, Ancho)
    Objetos[1].crearRect(Ancho, Mapa[Nivel-1][1]*2)
    Objetos[2].crearRect(Ancho, Mapa[Nivel-1][1]*2)
    Objetos[3].crearRect(Mapa[Nivel-1][0]*2, Ancho)

    
def crearLibros():
    
    global Libros1, puntajenemy, inicio, estantes, enemyX, enemyY, Libs, puntaje, PlusE
    
    stroke(0)
    
    menorX, menorY = 9999, 9999
    Lista  = []
    Lista2 = []
    
    for i, obj in enumerate(Libros1):
        
        if randy == i: obj.Plus = True
        
        obj.x = x + Libs[i][0]
        obj.y = y + Libs[i][1]
        Lista.append(obj)
        if obj.Activo:
            if abs(x+enemyX - obj.x - obj.Width/2)  < menorX: menorX = obj.x
            if abs(y+enemyY - obj.y - obj.Height/2) < menorY: menorY = obj.y
            if obj.isCollidingCREnemy():
                obj.Activo = False
                if not obj.Plus: puntajenemy += 1
                else: puntaje += 1; PlusE += .5
    
    Libros1 = Lista
    
    if puntaje+puntajenemy != len(Libros1):
        if menorX <= x+enemyX: enemyX -= 1.5 + PlusE + (.1*puntaje)
        if menorX >  x+enemyX: enemyX += 1.5 + PlusE + (.1*puntaje)
        if menorY <= y+enemyY: enemyY -= 1.5 + PlusE + (.1*puntaje)
        if menorY >  y+enemyY: enemyY += 1.5 + PlusE + (.1*puntaje)
    
    for i, obj in enumerate(Libros1):
        if obj.Activo:
            if obj.Plus:
                Libros1[i].crearRect(32, 32, False)
                iCoin.show(obj.x, obj.y, 32, 32)
            else:
                fill(obj.col[0], obj.col[1], obj.col[2])
                Libros1[i].crearRect(20, 35, False)
                image(iLibs[randLibs[i]], obj.x, obj.y, 20, 35)
    
    #imageMode(CENTER)
    
    for j, est in enumerate(estantes):
        Lista = []
        for i, val in enumerate(est):
            obj = val[0]
            obj.x = x + obj.xplus
            obj.y = y + obj.yplus
            Lista.append((obj, val[1]))
        for i, obj in enumerate(Lista):
            ancho = obj[1] 
            obj = obj[0]
            fill(obj.col[0], obj.col[1], obj.col[2])
            #obj.crearRect(ancho, 40)
            if j == 0: image(iLibsEst[randLibs2[i]], obj.x, obj.y, ancho, 40)
            if j == 1:
                pushMatrix()
                rotate(radians(180))
                image(iLibsEst[randLibs2[i]], -obj.x-20, -obj.y-40, ancho, 40)
                popMatrix()
            elif j == 2:
                pushMatrix()
                rotate(radians(90))
                image(iLibsEst[randLibs2[i]], obj.y, -obj.x-40, ancho, 40)
                popMatrix()
            elif j == 3:
                pushMatrix()
                rotate(radians(270))
                image(iLibsEst[randLibs2[i]], -obj.y-20, obj.x, ancho, 40)
                popMatrix()
        Lista2.append(est)
        
    estantes = Lista2


def chkKeys():
    
    global x, y, vel, Objetos, Libros1, enemyX, enemyY, puntaje, reinicio, miliseg, Plus
    global iniciar, Nivel
    
    if (key == 'r'):
        #Permite que solo reinicie 1 vez cuando se presiona la tecla, sino, reinicia infinitamente.
        if (millis() - miliseg) > 20 and (millis() - miliseg) < 40: reinicio = True
    elif (key == ESC): exit()
    elif key == 'm':
        if (millis() - miliseg) > 20 and (millis() - miliseg) < 40:
            reinicio = True
            Nivel = 1
            iniciar = False
    
    if keyPressed:
        vel = 4 + Plus
        miliseg = millis()
    
    xD = False
    pos = False
    
    if _keys[0] or _keys[4]:
        for i, obj in enumerate(Objetos):
            if not obj.isCollidingCR() or not obj.isPos('Izq'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: x += (4+Plus)
            else: x += vel
    
    if _keys[1] or _keys[5]:
        for i, obj in enumerate(Objetos):
            if not obj.isCollidingCR() or not obj.isPos('Aba'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: y -= (4+Plus)
            else: y -= vel
    
    if _keys[2] or _keys[6]:
        for i, obj in enumerate(Objetos):
            if not obj.isCollidingCR() or not obj.isPos('Der'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: x -= (4+Plus)
            else: x -= vel
    
    if _keys[3] or _keys[7]:
        for i, obj in enumerate(Objetos):
            if not obj.isCollidingCR() or not obj.isPos('Arr'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: y += (4+Plus)
            else: y += vel
    
    for i, Lib in enumerate(Libros1):
        if Lib.Activo == True:
            if Lib.isCollidingCR():
                if Lib.Plus: Plus = .5
                pos = True
                puntaje += 1
                break
    if pos == True: Libros1[i].Activo = False;


def reiniciar():
    
    global x, y,  Libros1, Libs, enemyX, enemyY, cantLibs, estantes, Plus, PlusE
    global puntaje, puntajenemy, reinicio, cont, r1, r2, randLibs, randy
    
    if reinicio:
        randy = int(random(24))
        Plus = 0
        PlusE = 0
        cantLibs = 8 + (4*(Nivel-1))
        cont = 0
        puntajenemy = 0
        puntaje = 0
        enemyX, enemyY = -500, -200
        reinicio = False
        r1 = rangos(Mapa[Nivel-1][0])
        r2 = rangos(Mapa[Nivel-1][1])
        randLibs = [int(random(30)) for _ in range(24)]
        Libros1  = [Obj(0, 0) for _ in range(cantLibs)]
        Libs = [(int(random(r1[0], r1[1])), int(random(r2[0], r2[1]))) for _ in range(cantLibs)]
        x, y = 900, 50+(100*(Nivel-1))
        estantes = [
                    creaEstante(-Mapa[Nivel-1][0]+Ancho,  Mapa[Nivel-1][1],        Mapa[Nivel-1][0], 'h'),
                    creaEstante(-Mapa[Nivel-1][0],       -Mapa[Nivel-1][1],        Mapa[Nivel-1][0], 'h'),
                    creaEstante(-Mapa[Nivel-1][0],       -Mapa[Nivel-1][1]+Ancho,  Mapa[Nivel-1][1], 'v'),
                    creaEstante( Mapa[Nivel-1][0],       -Mapa[Nivel-1][1],        Mapa[Nivel-1][1], 'v')
                ]



#============================================================================================================
# Multijugador ==============================================================================================
#============================================================================================================


def chkKeysMultiplayer():
    
    global player1X, player1Y, player2X, player2Y
    global ObjetosM, LibrosM, puntajeP1, puntajeP2, reinicioM, milisegM, iniciar, Nivel
    global velP1, velP2, PlusP1, PlusP2
    
    if (key == 'r'):
        #Permite que solo reinicie 1 vez cuando se presiona la tecla, sino, reinicia infinitamente.
        if (millis() - milisegM) > 20 and (millis() - milisegM) < 40:
            reinicioM = True
    elif (key == ESC): exit()
    elif key == 'm':
        if (millis() - milisegM) > 20 and (millis() - milisegM) < 40:
            reinicioM = True
            Nivel = 1
            iniciar = False
    
    if keyPressed: milisegM = millis()
    
    xD = False
    velP1 = 2 + PlusP1
    velP2 = 2 + PlusP2
    
    #============================================================================
    #Player 1: ==================================================================
    #============================================================================
    if _keys[0]:
        for i, obj in enumerate(ObjetosM):
            if not obj.isCollidingCR() or not obj.isPosPlayer1('Izq'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: player1X -= (velP1 + 1)
            else: player1X -= velP1
    
    if _keys[1]:
        for i, obj in enumerate(ObjetosM):
            if not obj.isCollidingCR() or not obj.isPosPlayer1('Aba'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: player1Y += (velP1 + 1)
            else: player1Y += velP1
    
    if _keys[2]:
        for i, obj in enumerate(ObjetosM):
            if not obj.isCollidingCR() or not obj.isPosPlayer1('Der'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: player1X += (velP1 + 1)
            else: player1X += velP1
    
    if _keys[3]:
        for i, obj in enumerate(ObjetosM):
            if not obj.isCollidingCR() or not obj.isPosPlayer1('Arr'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: player1Y -= (velP1 + 1)
            else: player1Y -= velP1
    #============================================================================
    #Player 2: ==================================================================
    #============================================================================
    if _keys[4]:
        for i, obj in enumerate(ObjetosM):
            if not obj.isCollidingCR2() or not obj.isPosPlayer2('Izq'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: player2X -= (velP2 + 1)
            else: player2X -= velP2
    
    if _keys[5]:
        for i, obj in enumerate(ObjetosM):
            if not obj.isCollidingCR2() or not obj.isPosPlayer2('Aba'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: player2Y += (velP2 + 1)
            else: player2Y += velP2
    
    if _keys[6]:
        for i, obj in enumerate(ObjetosM):
            if not obj.isCollidingCR2() or not obj.isPosPlayer2('Der'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: player2X += (velP2 + 1)
            else: player2X += velP2
    
    if _keys[7]:
        for i, obj in enumerate(ObjetosM):
            if not obj.isCollidingCR2() or not obj.isPosPlayer2('Arr'): xD = True
            else: xD = False; break
        if xD:
            if _keys.count(True) == 1: player2Y -= (velP2 + 1)
            else: player2Y -= velP2
    #============================================================================
    #============================================================================
    #============================================================================
    
    cont = 0
    for i, Lib in enumerate(LibrosM):
        if Lib.Activo:
            
            cont += 1
            
            if Lib.isCollidingCR():
                if Lib.Plus: PlusP1 += .55
                if PlusP1 > 0.01: PlusP1 -= .05
                LibrosM[i].Activo = False
                puntajeP1 += 1
                break
            
            if Lib.isCollidingCR2():
                if Lib.Plus: PlusP2 += .55
                if PlusP2 > 0.01: PlusP2 -= .05
                LibrosM[i].Activo = False
                puntajeP2 += 1
                break
            
            if cont == 10: break


def reiniciarM():
    
    global player1X, player1Y, player2X, player2Y
    global reinicioM, ObjetosM, multiplayer, LibrosM, randyM, randLibsM
    global puntajeP1, puntajeP2, velP1, velP2, PlusP1, PlusP2, seconds
    
    if reinicioM:
        if not iniciar:
            victoriasP1 = 0
            victoriasP2 = 0
        ObjetosM = []
        reinicioM = False
        multiplayer = True
        player1X, player1Y = 100, 500
        player2X, player2Y = 900, 500
        puntajeP1 = 0
        puntajeP2 = 0
        PlusP1 = 0
        PlusP2 = 0
        velP1 = 2
        velP2 = 2
        seconds = millis()//1000
        randyM = [int(random(totalLibsM)) for _ in range(cantMonedasM)]
        randLibsM = [int(random(30)) for _ in range(totalLibsM)]
        LibrosM = [ObjM(int(random(50, 1000)), int(random(50, 550))) for _ in range(totalLibsM)]

def crearLibrosM():
    
    global LibrosM
    
    stroke(0)
    
    Lista = []
    cont  = 0
    
    for i, obj in enumerate(LibrosM):
        if i in randyM: obj.Plus = True
        Lista.append(obj)
    
    LibrosM = Lista
    
    for i, obj in enumerate(LibrosM):
        if obj.Activo:
            cont += 1
            if obj.Plus:
                LibrosM[i].crearRect(16, 16, False)
                iCoin.show(obj.x, obj.y, 16, 16)
            else:
                fill(obj.col[0], obj.col[1], obj.col[2])
                LibrosM[i].crearRect(15, 25, False)
                image(iLibs[randLibsM[i]], obj.x, obj.y, 15, 25)
            
            if cont == 10: break

#============================================================================================================
#============================================================================================================
#============================================================================================================



def mouseReleased():
    global iniciar, multiplayer
    if mouseX > width/2-100 and mouseX < width/2+100 and mouseY > height/2-200 and mouseY < height/2-150:
        iniciar = True
        multiplayer = False
    if mouseX > width/2-100 and mouseX < width/2+100 and mouseY > height/2-100 and mouseY < height/2-50:
        iniciar = True
        multiplayer = True

def mainMenu():
    
    fill(255)
    
    image(iBackground, 0, 0, 1050, 600)
    
    if mouseX > width/2-100 and mouseX < width/2+100 and mouseY > height/2-200 and mouseY < height/2-150:
        if mousePressed:
            image(iBotones[0], width/2-100, height/2-210, 200, 70)
        else:
            image(iBotones[2], width/2-100, height/2-200, 200, 50)
    else:
        image(iBotones[1], width/2-100, height/2-200, 200, 50)
        
    text('1 Jugador', width/2-25, height/2-170)
    
    
    if mouseX > width/2-100 and mouseX < width/2+100 and mouseY > height/2-100 and mouseY < height/2-50:
        if mousePressed:
            image(iBotones[0], width/2-100, height/2-110, 200, 70)
        else:
            image(iBotones[3], width/2-100, height/2-110, 200, 70)
    else:
        image(iBotones[4], width/2-100, height/2-100, 200, 50)
    
    text('2 Jugadores', width/2-27, height/2-70)
    
    image(iPlayers[selectP1], 200, 400, 100, 100)
    image(iPlayers[selectP2], 800, 400, 100, 100)
    
    text('Piedras Ganadas Por Terminar Partidas de 1 Jugador', 380, 50)
    
    for i in range(3): image(iPiedras[i+3], 475+(40*i), 65, 32, 32)
    
    for i in range(victorias):
        if i < 3: image(iPiedras[i], 475+(40*i), 65, 32, 32)
    
    for i in range(victoriasP1):
        if i < 20: image(iStar, 10+(20*i), 577, 15, 15)
    
    for i in range(victoriasP2):
        if i < 20: image(iStar, 1020-(20*i), 577, 15, 15)
    
    nombreP1 = ''
    nombreP2 = ''
    
    if selectP1 == 0: nombreP1 = '   Deadpool'
    if selectP2 == 0: nombreP2 = '   Deadpool'
    if selectP1 == 1: nombreP1 = 'Gato Galleta'
    if selectP2 == 1: nombreP2 = 'Gato Galleta'
    if selectP1 == 2: nombreP1 = 'Hamburguesa'
    if selectP2 == 2: nombreP2 = 'Hamburguesa'
    if selectP1 == 3: nombreP1 = '  Papas Fritas'
    if selectP2 == 3: nombreP2 = '  Papas Fritas'
    if selectP1 == 4: nombreP1 = '     Muffin'
    if selectP2 == 4: nombreP2 = '     Muffin'
    if selectP1 == 5: nombreP1 = '      Dona'
    if selectP2 == 5: nombreP2 = '      Dona'
    if selectP1 == 6: nombreP1 = '      Navi'
    if selectP2 == 6: nombreP2 = '      Navi'
    if selectP1 == 7: nombreP1 = '        Sol'
    if selectP2 == 7: nombreP2 = '        Sol'
    if selectP1 == 8: nombreP1 = ' Ying y Yang'
    if selectP2 == 8: nombreP2 = ' Ying y Yang'
    if selectP1 == 9: nombreP1 = 'Majoras Mask'
    if selectP2 == 9: nombreP2 = 'Majoras Mask'
    
    text('temporizador', width//2-30, 380)
    text(str(cooldown), width//2-5, 400)
    text('Cambia el tiempo por partida en multijugador', width//2-110, 440)
    text('con las Teclas Z o X', width//2-50, 452)
    text('Jugador 1', 220, 380)
    text('Jugador 2', 820, 380)
    text(nombreP1, 215, 520)
    text(nombreP2, 815, 520)
    text('Selecciona un Personaje con las Teclas A o S', 130, 540)
    text('Selecciona un Personaje con las Flechas Izq o Der', 720, 540)
    text('Wars   v1.1.0', width//2-30, height-20)
    
    


def keyPressed():
    
    global _keys, selectP1, selectP2, cooldown, victoriasP1, victoriasP2, victorias
    
    if (key == 'a') or (key == 'A'): _keys[0] = True
    if (key == 's') or (key == 'S'): _keys[1] = True
    if (key == 'd') or (key == 'D'): _keys[2] = True
    if (key == 'w') or (key == 'W'): _keys[3] = True
    if (key == CODED) and (keyCode == LEFT):  _keys[4] = True
    if (key == CODED) and (keyCode == DOWN):  _keys[5] = True
    if (key == CODED) and (keyCode == RIGHT): _keys[6] = True
    if (key == CODED) and (keyCode == UP):    _keys[7] = True
    if (key == 'z') or (key == 'Z'): _keys[8] = True
    if (key == 'x') or (key == 'X'): _keys[9] = True
    if (key == 'u') or (key == 'U'): _keys[10] = True
    if (key == 'i') or (key == 'I'): _keys[11] = True
    if (key == 'o') or (key == 'O'): _keys[12] = True
    if (key == 'p') or (key == 'P'): _keys[13] = True
    if (key == 't') or (key == 'T'): _keys[14] = True
    if (key == 'y') or (key == 'Y'): _keys[15] = True
    
    if not iniciar:
        if _keys[0]:
            if selectP1 > 0: selectP1 -= 1
        if _keys[2]:
            if selectP1 < 9: selectP1 += 1
        if _keys[4]:
            if selectP2 > 0: selectP2 -= 1
        if _keys[6]:
            if selectP2 < 9: selectP2 += 1
        if _keys[8]:
            if cooldown > 10: cooldown -= 1
        if _keys[9]:
            if cooldown < 120: cooldown += 1
        if _keys[10]: victoriasP1 += 1
        if _keys[11]: victoriasP2 += 1
        if _keys[12]: victoriasP1  = 0
        if _keys[13]: victoriasP2  = 0
        if _keys[14]:
            if victorias > 0: victorias -= 1
        if _keys[15]:
            if victorias < 3: victorias += 1

def keyReleased():
    
    global _keys
    if (key == 'a') or (key == 'A'): _keys[0] = False
    if (key == 's') or (key == 'S'): _keys[1] = False
    if (key == 'd') or (key == 'D'): _keys[2] = False
    if (key == 'w') or (key == 'W'): _keys[3] = False
    if (key == CODED) and (keyCode == LEFT):  _keys[4] = False
    if (key == CODED) and (keyCode == DOWN):  _keys[5] = False
    if (key == CODED) and (keyCode == RIGHT): _keys[6] = False
    if (key == CODED) and (keyCode == UP):    _keys[7] = False
    if (key == 'z') or (key == 'Z'): _keys[8] = False
    if (key == 'x') or (key == 'X'): _keys[9] = False
    if (key == 'u') or (key == 'U'): _keys[10] = False
    if (key == 'i') or (key == 'I'): _keys[11] = False
    if (key == 'o') or (key == 'O'): _keys[12] = False
    if (key == 'p') or (key == 'P'): _keys[13] = False
    if (key == 't') or (key == 'T'): _keys[14] = False
    if (key == 'y') or (key == 'Y'): _keys[15] = False

def setup():
    
    global iStar, iFloor, iCoin, iLibs, iLibsEst, iBotones, iBackground, iPlayers, iPiedras
    global x, y, circX, circY, Ancho, _keys
    
    _keys = [False for _ in range(16)]
    
    PathLibs = 'PixelArts/Libros/'
    PathObjs = 'PixelArts/Objetos/'
    PathBots = 'PixelArts/Botones/'
    PathTexs = 'PixelArts/Texturas/'
    PathFond = 'PixelArts/Background/'
    PathPers = 'PixelArts/Personajes/'
    
    iStar  = loadImage(PathObjs+'Star_01.png')
    iFloor = loadImage(PathTexs+'Floor_Ladder.png')
    iCoin  = Gif(7, PathObjs+'coin-frame-{}.png', 8)
    iPiedras = [loadImage(PathObjs+'Piedra Esmeralda.png'), loadImage(PathObjs+'Piedra Rubi.png'), loadImage(PathObjs+'Piedra Zafiro.png'),
                loadImage(PathObjs+'Piedra Esmeralda Bloqueada.png'), loadImage(PathObjs+'Piedra Rubi Bloqueada.png'), loadImage(PathObjs+'Piedra Zafiro Bloqueada.png')]
    iLibs  = [loadImage(PathLibs+'Book_0{}.png'.format(_)) for _ in range(10)]
    iLibs += [loadImage(PathLibs+'Book_{}.png'.format(_)) for _ in range(10,30)]
    iLibsEst  = [loadImage(PathLibs+'Book_above_0{}.png'.format(_)) for _ in range(10)]
    iLibsEst += [loadImage(PathLibs+'Book_above_{}.png'.format(_)) for _ in range(10,33)]
    iBotones = [loadImage(PathBots+'Boton2Negro.png'), loadImage(PathBots+'BotonPurpura.png'),
                loadImage(PathBots+'BotonAzul.png'),   loadImage(PathBots+'Boton2.png'),
                loadImage(PathBots+'BotonVerde.png')]
    iBackground = loadImage(PathFond+'Fondo.jpg')
    iPlayers = [loadImage(PathPers+'Deadpool.png'),     loadImage(PathPers+'Gato Galleta.png'),
                loadImage(PathPers+'Hamburguesa.png'),  loadImage(PathPers+'Papas Fritas.png'),
                loadImage(PathPers+'Muffin.png'),       loadImage(PathPers+'Dona.png'),
                loadImage(PathPers+'Navi.png'),         loadImage(PathPers+'Sol.png'),
                loadImage(PathPers+'Yin Yang.png'),    loadImage(PathPers+'Majoras Mask.png')]
    
    
    
    smooth(8)
    #frameRate(120)
    frameRate(60)
    size(1050, 600)
    circX, circY = width/2, height/2
    
    #ellipseMode(CENTER)
    #rectMode(CORNER)

def draw():
    
    global iniciar, cont, Nivel, reinicio, reinicioM, miliseg, seconds
    global victoriasP1, victoriasP2, secTemp, multiplayer, victorias
    #print(frameCount, millis())
    
    reinicio = False
    reinicioM = False
    
    background(6, 97, 120)
    
    if iniciar:
        
        if not multiplayer:
            v_ = 300
            for _1 in range(Mapa[Nivel-1][0]*2//v_):
                for _2 in range(Mapa[Nivel-1][1]*2//v_):
                    image(iFloor, x+((-Mapa[Nivel-1][0])+_1*v_), y+((-Mapa[Nivel-1][1])+_2*v_), v_, v_)
            
            crearObjetosEstaticos()
            crearLibros()
            
            fill(255); stroke(255)
            text('FPS: '+str(int(frameRate)), 30, 590) #'Coordenadas: x='+str(int(x))+' y='+str(int(y))+' '+
            
            #ellipse(circX, circY, diametro, diametro)
            #ellipse(x+enemyX, y+enemyY, diametro, diametro)
            
            if selectP1 == 9:
                image(iPlayers[selectP1], circX-(diametro//2+12), circY-(diametro//2+12), diametro+20, diametro+20)
                if PersonRandom == 7:
                    image(iPlayers[PersonRandom], x+enemyX-(diametro//2+12), y+enemyY-(diametro//2+12), diametro+20, diametro+20)
                else:
                    image(iPlayers[PersonRandom], x+enemyX-(diametro//2), y+enemyY-(diametro//2), diametro+2, diametro+2)
            else:
                if selectP1 == 7:
                    image(iPlayers[selectP1],  circX-(diametro//2+12), circY-(diametro//2+12), diametro+20, diametro+20)
                else:
                    image(iPlayers[selectP1], circX-(diametro//2), circY-(diametro//2), diametro+2, diametro+2)
                
                image(iPlayers[-1], x+enemyX-(diametro//2+12), y+enemyY-(diametro//2+12), diametro+20, diametro+20)
            
            chkKeys()
            
            text('Nivel', 5, 15)
            text('Velocidad de Jugador: '+str(int((vel+Plus)*10)), 5, 30)
            text('Velocidad de NPC:       '+str(int((1.5+PlusE+(.1*puntaje))*10)), 5, 45)
            text('Libros: '+str(puntaje+puntajenemy)+' de '+str(cantLibs), 400, 15)
            
            if puntaje == len(Libros1):
                if Nivel == 5:
                    if puntaje == len(Libros1):
                        fill(255)
                        
                        if   victorias == 0: text('Haz Ganado la Piedra Esmeralda', width/2-90, height/2-40); image(iPiedras[0], width/2-16, height/2-100, 32, 32)
                        elif victorias == 1: text('Haz Ganado la Piedra Rubi',      width/2-75, height/2-40); image(iPiedras[1], width/2-16, height/2-100, 32, 32)
                        elif victorias == 2: text('Haz Ganado la Piedra Zafiro',    width/2-80, height/2-40); image(iPiedras[2], width/2-16, height/2-100, 32, 32)
                        else:
                            text('Ya tienes todas las Piedras', width/2-75, height/2-40)
                            image(iPiedras[0], width/2-56, height/2-100, 32, 32)
                            image(iPiedras[1], width/2-16, height/2-100, 32, 32)
                            image(iPiedras[2], width/2+26, height/2-100, 32, 32)
                        cont += 1
                        if cont >= 400:
                            cont = 0
                            Nivel = 1
                            reinicio = True
                            iniciar = False
                            victorias += 1
                else:
                    fill(255); text('Siguiente Nivel !!!', width/2-50, height/2-40)
                    cont += 1
                    if cont >= 200:
                        reinicio = True
                        Nivel += 1
                        cont = 0
            elif puntajenemy > 0:
                fill(255); text('Vuelve a Intentar !!!', width/2-50, height/2-40)
                cont += 1
                if cont >= 200: reinicio = True
            
            if Nivel >= 1: image(iStar, 40,  2, 15, 15)
            if Nivel >= 2: image(iStar, 60,  2, 15, 15)
            if Nivel >= 3: image(iStar, 80,  2, 15, 15)
            if Nivel >= 4: image(iStar, 100, 2, 15, 15)
            if Nivel >= 5: image(iStar, 120, 2, 15, 15)
        else:
            
            global ObjetosM
            
            v_ = 150
            for _1 in range(1050//v_):
                for _2 in range(600//v_):
                    image(iFloor, _1*v_, _2*v_, v_, v_)
            
            ObjetosM = []
            estante1 = ObjM(0,    0)
            estante2 = ObjM(25,   575)
            estante3 = ObjM(0,    25)
            estante4 = ObjM(1025, 0)
            
            ObjetosM.append(estante1)
            ObjetosM.append(estante2)
            ObjetosM.append(estante3)
            ObjetosM.append(estante4)
            
            fill(100, 50, 0); stroke(0)
            ObjetosM[0].crearRect(1025, 25)
            ObjetosM[1].crearRect(1025, 25)
            ObjetosM[2].crearRect(25, 1025)
            ObjetosM[3].crearRect(25, 1025)
            
            fill(255); stroke(255)
            text('FPS: '+str(int(frameRate)), 30, 570)
            
            text('Jugador 1', player1X-24, player1Y+34)
            text('Jugador 2', player2X-24, player2Y+34)
            
            #ellipse(player1X, player1Y, 30, 30)
            #ellipse(player2X, player2Y, 30, 30)
            
            if selectP1 in [7, 9]:
                image(iPlayers[selectP1], player1X-27, player1Y-27, 50, 50)
            else:
                image(iPlayers[selectP1], player1X-16, player1Y-16, 32, 32)
        
            if selectP2 in [7, 9]:
                image(iPlayers[selectP2], player2X-27, player2Y-27, 50, 50)
            else:
                image(iPlayers[selectP2], player2X-16, player2Y-16, 32, 32)
            
            if 1+cooldown - (millis()//1000 - seconds) >= 0:
                chkKeysMultiplayer()
                text(str(1+cooldown - (millis()//1000 - seconds)), width//2-10, 18)
                secTemp = millis()//1000
            else:
                if puntajeP1 > puntajeP2:   text('Victoria Para Jugador 1', width//2-60, 18)
                elif puntajeP1 < puntajeP2: text('Victoria Para Jugador 2', width//2-60, 18)
                #else: text('Empate', width//2-25, 18)
                
                if 2 - (millis()//1000 - secTemp) >= 0: pass
                else:
                    if   puntajeP1 > puntajeP2: victoriasP1 += 1
                    elif puntajeP1 < puntajeP2: victoriasP2 += 1
                    else:  victoriasP1 += 1; victoriasP2 += 1
                    seconds = millis()//1000
                    reinicioM = True
            
            for i in range(victoriasP1):
                if i < 20: image(iStar, 110+(20*i), 577, 15, 15)
            
            text('Victorias: '+str(victoriasP1), 30, 590)
            text(str(puntajeP1), 170, 25)
            text('Jugador 1', 150, 12)
            text(str(puntajeP1), 170, 25)
            text('velocidad', 250, 12)
            text(str(int((velP1+PlusP1)*10)), 270, 25)
            
            for i in range(victoriasP2):
                if i < 20: image(iStar, 920-(20*i), 577, 15, 15)
            
            text('Victorias: '+str(victoriasP2), 950, 590)
            text('Jugador 2', 800, 12)
            text(str(puntajeP2), 820, 25)
            text('velocidad', 700, 12)
            text(str(int((velP1+PlusP2)*10)), 720, 25)
            
            text('Presiona M para volver al Menu Principal', 410, 570)
            crearLibrosM()
            
    else:
        
        if key == ENTER:
            iniciar = True
            multiplayer = True
        mainMenu()
        seconds = millis()//1000
        
    if not multiplayer: reiniciar()
    else: reiniciarM()
    
    #print(millis())
    
    
    
