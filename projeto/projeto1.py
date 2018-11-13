import pygame
import random
import time






PECA_S = [['.....', '.....', '..OO.', '.OO..', '.....'], ['.....', '..O..', '..OO.', '...O.', '.....']]

PECA_Z = [['.....', '.....', '.OO..', '..OO.', '.....'], ['.....', '..O..', '.OO..', '.O...', '.....']]

PECA_I = [['..O..', '..O..', '..O..', '..O..', '.....'], ['.....', '.....', 'OOOO.', '.....', '.....']]

PECA_O = [['.....', '.....', '.OO..', '.OO..', '.....']]

PECA_J = [['.....', '.O...', '.OOO.', '.....', '.....'], ['.....', '..OO.', '..O..', '..O..', '.....'], ['.....', '.....', '.OOO.', '...O.', '.....'], ['.....', '..O..', '..O..', '.OO..', '.....']]

PECA_L = [['.....', '...O.',  '.OOO.', '.....', '.....'], ['.....', '..O..', '..O..', '..OO.', '.....'], ['.....', '.....', '.OOO.', '.O...', '.....'], ['.....', '.OO..', '..O..', '..O..', '.....']]

PECAS = {'S': PECA_S,
         'Z': PECA_Z,
         'I': PECA_I,
         'O': PECA_O,
         'J': PECA_J,
         'L': PECA_L}




# localização decida de peca
x = 360
y = 5

ALTURA_JANELA = 720
LARGURA_JANELA = 1080
tela = pygame.display.set_mode([LARGURA_JANELA, ALTURA_JANELA])
pygame.display.set_caption('TETRIS')
EM_BRANCO = -1
relogio = pygame.time.Clock()
tem_peca = pygame.time.Clock()
TAMANHO_BLOCO = 50


for i in PECAS:
    for j in range(len(PECAS[i])):
        dados_formato = []
        for x in range(5):
            coluna = []
            for y in range(5):
                if PECAS[i][j][y][x] == '.':
                    coluna.append(EM_BRANCO)
                else:
                    coluna.append(1)
            dados_formato.append(coluna)
        PECAS[i][j] = dados_formato

# cores

cor_branca = (255, 255, 255)
cor_azulado = (11, 139, 244)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)
cor_amarela = (255, 255, 0)
cor_preta = (0, 0, 0)
cor_peca = [cor_azulado, cor_vermelha, cor_verde, cor_amarela]

cor_borda = cor_amarela
cor_bg = cor_preta
# pecas
# areas do jogo
area_jogo_pecas = pygame.Surface((800, 710))
area_jogo_pecas.fill(cor_branca)
area_jogo_placar = pygame.Surface((265, 710))
area_jogo_placar.fill(cor_azulado)

# limites area do jogo

limite_esquerdo = pygame.Rect(0, 5, 5, 710)
limite_direito = pygame.Rect(805, 5, 5, 710)
limite_inferior = pygame.Rect(0, 715, 810, 5)
limite_superior = pygame.Rect(0, 0, 810, 5)



def nova_peca():
    forma = random.choice(list(PECAS.keys()))
    nova_peca = {'forma': forma,
                 'rotacao': random.randint(0, len(PECAS[forma])-1),
                 'x': int(LARGURA_JANELA /2 )-2,
                 'y': -2,
                 'cor': random.randint(0, len(cor_peca)-1) }
    return nova_peca

peca_atual = nova_peca()
proxima_peca = nova_peca()

def atingiu_fundo(peca):
    altp, larp = peca.width, peca.height

    peca_fixa = pygame.Rect(peca.x, peca.y, altp, larp)


    return pygame.draw.rect(tela, cor_verde, peca_fixa




def desenha_peca(piece, customCoords=(None, None)):
    shapeToDraw = PECAS[piece['forma']][piece['rotacao']]
    if customCoords == (None, None):

        pixelx, pixely = converter_pixels(piece['x'], piece['y'])
    else:
        pixelx, pixely = customCoords

        # draw each of the blocks that make up the piece
    for x in range(5):
        for y in range(5):
            if shapeToDraw[x][y] != EM_BRANCO:
                pygame.draw.rect(tala, cor_peca[piece['cor']], (
                    pixelx + (x * TAMANHO_BLOCO) + 1, pixely + (y * TAMANHO_BLOCO) + 1, TAMANHO_BLOCO - 1,
                    TAMANHO_BLOCO - 1))



def run():
    global peca_atual, proxima_peca
    pygame.init()


    # tamanho


    # limite_esquerdo = pygame.Surface((5, 710))
    # limite_direito = pygame.Surface((5, 710))
    # limite_inferior = pygame.Surface((810, 5))
    # limite_superior = pygame.Surface((810, 5))


    sair = False
    while sair == False:

        if peca_atual == None:
            peca_atual = proxima_peca
            proxima_peca = nova_peca()
            #ultimo_tempo_queda = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.KEYDOWN and not peca.colliderect(limite_inferior):
                if event.key == pygame.K_LEFT and not peca.colliderect(limite_esquerdo):
                    peca.move_ip(-30, 0)
                if event.key == pygame.K_RIGHT and not peca.colliderect(limite_direito):
                    peca.move_ip(30, 0)
                if event.key == pygame.K_UP:
                    peca = pygame.Rect(peca.x, peca.y, peca.height, peca.width)


        relogio.tick(29)
        tela.blit(area_jogo_pecas, [5, 5])
        tela.blit(area_jogo_placar, [810, 5])

        pygame.draw.rect(tela, cor_amarela, limite_direito)
        pygame.draw.rect(tela, cor_amarela, limite_esquerdo)
        pygame.draw.rect(tela, cor_amarela, limite_superior)
        pygame.draw.rect(tela, cor_amarela, limite_inferior)


        pygame.draw.rect(tela, cor_vermelha, peca_atual)

        y = 5




        if not peca.colliderect(limite_inferior):
            tem_peca.tick(15)
            peca = peca.move(0, y)
            y += 5

        if peca.colliderect(limite_inferior):
            atingiu_fundo(peca_atual)
            peca_atual = None




        pygame.display.update()



    pygame.quit()



run()