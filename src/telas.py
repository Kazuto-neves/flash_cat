import pygame
import uteis as u
import os
import sprites as spr
import gameMain as g

tela = pygame.display.set_mode((u.LARGURA, u.ALTURA))
pygame.display.set_caption('Flash cat')

def menu_audio(x):
    if x == False:ss = pygame.image.load(os.path.join(spr.diretorio_imagens, 'Ssom.png')).convert_alpha()
    else:ss = pygame.image.load(os.path.join(spr.diretorio_imagens, 'Csom.png')).convert_alpha()
    tela.blit(ss, [4, 304,20,20])

def Power_ups(pts,S,Tm,Q,u,UP):
    tela.fill(bg(Tm))
    texto("UPGRADE",bc(Tm),100,u.LARGURA/4, u.ALTURA/14)
    texto("Pontuação:"+str(pts),bt(Tm),50,u.LARGURA/3, u.ALTURA/4)
    if UP == u:
        pygame.draw.rect(tela,bt(Tm), [140,140,150,50])
        if Q<=3:
            pygame.draw.rect(tela,u.Amarelo, [150,150,30,30])
            texto("++",fcb(Tm),60,200,141)
        else:texto("Level MAX",fcb(Tm),30,155,145)
        pygame.draw.rect(tela,bt(Tm), [350,140,150,50])
        pygame.draw.rect(tela,u.Amarelo, [360,150,30,30])
        texto(">>",fcb(Tm),60,410,141)
    else:
        texto("Voce precisa de mais "+str(UP-u),bc(Tm),40,u.LARGURA/3, u.ALTURA/2.8)
        pygame.draw.rect(tela,bt(Tm), [250,170,130,25])
        texto("Continue",fcb(Tm),30,275,175) 
    control(bc(Tm),fc(Tm))
    tema(bt(Tm),bc(Tm),Tm)
    menu_audio(S)
    pygame.display.update()


def Plot(s,Tm):
    inicio = True
    while inicio:
        tela.fill(bg(Tm))
        texto("Historia:",bc(Tm),40,u.LARGURA/3,10)
        texto("No planeta Yōmō no bōru",bt(Tm),25,u.LARGURA/3,40)
        texto("os seres viviam livremente",bt(Tm),25,u.LARGURA/3,70)
        texto("raças como cães, aves e seres aquáticos",bt(Tm),25,u.LARGURA/3,100)
        texto("viviam em plena amônia, mas um dia",bt(Tm),25,u.LARGURA/3,130)
        texto("os ratos do planeta Akushū",bt(Tm),25,u.LARGURA/3,160)
        texto("vieram para tomar o planeta",bt(Tm),25,u.LARGURA/3,190)
        texto("então foi selecionado o melhor Neko",bt(Tm),25,u.LARGURA/3,220)
        texto("do planeta para combater os ratos",bt(Tm),25,u.LARGURA/3,250)
        pygame.draw.rect(tela,bt(Tm), [250,290,130,25])
        texto("Continuar",fcb(Tm),30,275,295)
        pygame.draw.rect(tela,u.Vermelho, [510,0,130,25])
        texto("Sair(esc)",u.BRANCO,30,535,5)
        tema(bt(Tm),bc(Tm),Tm)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        inicio = False
                        main(s,Tm)
                    if event.key == pygame.K_l:
                        u.tema(Tm)
                        pygame.display.update()
                        
                    if event.key == pygame.K_ESCAPE:pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 250 and y > 290 and x < 380 and y < 315:
                        inicio = False
                        main(s,Tm)
                    if x > 10 and y > 10 and x < 60 and y < 60:
                        u.tema(Tm)
                        pygame.display.update()
                    if x > 510 and y > 0 and x < 640 and y < 25:pygame.quit()

def control(CT,C):
    texto("Controles:",CT,40,u.LARGURA/3,220)
    texto("Mover com WASD ou as Cetas",C,30,u.LARGURA/3,250)
    texto("Pausar use o P",C,30,u.LARGURA/3,270)
    texto("Mudar o tema L",C,30,u.LARGURA/3,290)
    texto("SOM com TAB",C,30,u.LARGURA/3,310)
    texto("Especial com Q",C,30,u.LARGURA/3,330)
    
def placar(pts,x,N,u,UP):
    texto("Pontuação:"+str(pts),u.Preto,25,440,10)
    texto("Wave",u.Preto,25,u.LARGURA/2,10)
    texto(" "+str(N),u.Vermelho,25,u.LARGURA/1.7,10)
    texto("Mega cheeses:",u.Preto,25,10,10)
    pygame.draw.rect(tela,u.Amarelo, [133,14,x,10])
    pygame.draw.rect(tela,u.Preto, [184, 14, 0, 10], 5)
    pygame.draw.rect(tela,u.Vermelho, [134, 14, 100, 10], 5)
    texto("Power UP:",u.Preto,25,10,30)
    texto(" "+str(u),u.Vermelho,25,94,30)
    if UP == u: texto("Precione U",u.Verde,25,134,30)

def go(pts,S,Tm):
    tela.fill(bg(Tm))
    texto("Game Over",bc(Tm),100,u.LARGURA/5, u.ALTURA/14)
    texto("Pontuação:"+str(pts),bt(Tm),50,u.LARGURA/3, u.ALTURA/4)
    pygame.draw.rect(tela,bt(Tm), [140,140,150,50])
    texto("Continuar",fcb(Tm),30,155,145)
    texto("(ESPAÇO)",fcb(Tm),30,155,165)
    pygame.draw.rect(tela,bt(Tm), [350,140,150,50])
    texto("Sair",fcb(Tm),30,400,145)
    texto("(Esc)",fcb(Tm),30,400,165)
    control(bc(Tm),fc(Tm))
    tema(bt(Tm),bc(Tm),Tm)
    menu_audio(S)
    pygame.display.update()

def pause(pts,S,Tm):
    tela.fill(bg(Tm))
    texto("Pause",bc(Tm),100,u.LARGURA/3, u.ALTURA/14)
    texto("Pontuação:"+str(pts),bt(Tm),50,u.LARGURA/3, u.ALTURA/4)
    pygame.draw.rect(tela,bt(Tm), [140,140,150,50])
    texto("Continuar",fcb(Tm),30,155,145)
    texto("(ESPAÇO)",fcb(Tm),30,155,165)
    pygame.draw.rect(tela,bt(Tm), [350,140,150,50])
    texto("Re-começar",fcb(Tm),30,380,145)
    texto("(F5)",fcb(Tm),30,400,165)
    control(bc(Tm),fc(Tm))
    tema(bt(Tm),bc(Tm),Tm)
    menu_audio(S)
    pygame.display.update()

def texto(msg, cor, t,x,y):
    fonte = pygame.font.SysFont(None, t)
    texto1 = fonte.render(msg, True, cor)
    tela.blit(texto1, [x, y])

def bg(bg):
    if bg == True:return (u.Preto)
    else:return (u.BRANCO)

def fc(fc):
    if fc == True:return (u.BRANCO)
    else:return (u.Preto)

def bc(bc):
    if bc == True:return (u.Amarelo)
    else:return (u.Vermelho)

def bt(bt):
    if bt == True:return (u.Verde)
    else:return (u.Preto)

def fcb(fcb):
    if fcb == True:return (u.Amarelo)
    else:return (u.BRANCO)

def img(tl):
    if tl == True:sl = pygame.image.load(os.path.join(spr.diretorio_imagens, 'sol.png')).convert_alpha()
    else:sl = pygame.image.load(os.path.join(spr.diretorio_imagens, 'lua.png')).convert_alpha()
    tela.blit(sl, [19, 19])

def tema(bt,bc,T):
        pygame.draw.rect(tela,bt, [12,12,44,44], border_radius=15)
        pygame.draw.rect(tela,bc, [10, 10, 50, 50], 5, border_radius=15)
        img(T)

def main (s,Tm):
    inicio = True
    while inicio:
        tela.fill(bg(Tm))
        texto("Flash Cat",bc(Tm),60,u.LARGURA/3, u.ALTURA/14)
        pygame.draw.rect(tela,bt(Tm), [250,70,130,25])
        texto("Medio(1)",fcb(Tm),30,275,75)
        pygame.draw.rect(tela,bt(Tm), [250,120,130,25])
        texto("Dificil(2)",fcb(Tm),30,275,125)
        pygame.draw.rect(tela,bt(Tm), [250,170,130,25])
        texto("Insano(3)",fcb(Tm),30,275,175)
        pygame.draw.rect(tela,u.Vermelho, [510,0,130,25])
        texto("Sair(esc)",u.BRANCO,30,535,5)
        tema(bt(Tm),bc(Tm),Tm)
        menu_audio(s)
        control(bc(Tm),fc(Tm))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        inicio = False
                        n=1
                        g.game_loop(n,s)
                    if event.key == pygame.K_2:
                        inicio = False
                        n=2
                        g.game_loop(n,s)
                    if event.key == pygame.K_3:
                        inicio = False
                        n=3
                        g.game_loop(n,s)
                    if event.key == pygame.K_TAB:
                        if s== True:s=False
                        else:s=True
                        pygame.display.update()
                    if event.key == pygame.K_l:
                        u.tema(Tm)
                        pygame.display.update()
                        
                    if event.key == pygame.K_ESCAPE:pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 250 and y > 70 and x < 380 and y < 95:
                        inicio = False
                        n=1
                        g.game_loop(n,s)
                    if x > 250 and y > 120 and x < 380 and y < 145:
                        inicio = False
                        n=2
                        g.game_loop(n,s)
                    if x > 250 and y > 170 and x < 380 and y < 195:
                        inicio = False
                        n=3
                        g.game_loop(n,s)
                    if x > 2 and y > 302 and x < 46 and y < 352:
                        if s== True:s=False
                        else:s=True
                        print("mudei")
                        pygame.display.update()
                    if x > 10 and y > 10 and x < 60 and y < 60:
                        u.tema(Tm)
                        pygame.display.update()
                    if x > 510 and y > 0 and x < 640 and y < 25:pygame.quit()