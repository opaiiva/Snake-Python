# Configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption('SNAKE PYTHON')
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cor RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Parametros da cobra
tamanho_do_quadrado = 20
velocidade_jogo = 15

def gerar_comida():
    comida_x = (random.randrange(0,largura - tamanho_do_quadrado) / float(tamanho_do_quadrado)) * float(tamanho_do_quadrado)
    comida_y = (random.randrange(0, altura - tamanho_do_quadrado) / float(tamanho_do_quadrado)) * float(tamanho_do_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelho,[comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco,[pixel[0], pixel[1], tamanho, tamanho])
    
def desenhar_potuacao(pontuacao):
    fonte = pygame.font.SysFont('Helvetica', 35)
    texto = fonte.render(f'Pontos: {pontuacao}', True, verde)
    tela.blit(texto, [1, 1]) 
    
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_do_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = - tamanho_do_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_do_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = - tamanho_do_quadrado
        velocidade_y = 0
        
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False 
    
    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_cobra = 1 
    pixels = []
    
    comida_x, comida_y = gerar_comida()
    
     
    while not fim_jogo:
        tela.fill(preto)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT():
                fim_jogo = False
                
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
                
        
        # Desenhar comida
        desenhar_comida(tamanho_do_quadrado, comida_x, comida_y)
        
        # Atualizar a posicao da cobra 
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
                     
        x += velocidade_x
        y += velocidade_y
        
        # Desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
            
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
                
        desenhar_cobra(tamanho_do_quadrado, pixels)
        
        # Desenhar pontos
        desenhar_potuacao(tamanho_cobra - 1)
        
        #atualizacao da tela
        pygame.display.update()
        
        #Criar nova comida
        if x == comida_x and comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        
        relogio.tick(velocidade_jogo)
        
