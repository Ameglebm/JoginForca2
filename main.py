import pygame
import random
import sys

pygame.init()

LARGURA, ALTURA = 800, 600
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Forca")

BRANCO = (67, 4, 71)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

FONTE = pygame.font.SysFont('comicsans', 40)
FONTE_LETRA = pygame.font.SysFont('comicsans', 30)
FONTE_TITULO = pygame.font.SysFont('comicsans', 60)


palavras = ["amar","azul","acordado","amargura","assistir","apetecer","ascender","arrojado","aprender","alcançar","atribuir","anarquia","amistoso","arretado","ajudante","atraente","apoteose","atrofiar","adiantar","arrancar","afrontar","abestado","bizarro","bem","buscar","basculho","bastardo","bom","brado","brasileiro","burro","bruma","base","brega","bravo","bonito","bojo","barganha","beldade","bondade","bola","bajulador","belo","brasil","bolo","burrice","bobo","bruços","bônus","biodiversidade","cultura","confiança","como","conserto","circunstância","caos","consequência","casual","cinismo","cético","conveniência","compaixão","consonância","cordial","compartilhar","complexo","céu","clichê","critério","coragem","consoante","carência","canalha","coerente","custódia","colapso","casa","caridade","conhecer","complexidade","conforme","descobrir","defasagem","desalento","diplomata","democrata","divertido","destituir","dezesseis","discordar","distraído","devolução","disfarçar","devastado","desonesto","dilapidar","desabafar","denunciar","desbocado","devaneios","despedida","desamparo","descrença","desgastar","debandada","desanimar","deliciosa","decrescer","dessagrar","desatacar","elo", "entusiasta", "estima", "emissão","extorquir","esboço", "extinguir","explicar", "errante","exalar","executar", "exclusão", "elegibilidade","erudito", "eficaz", "estúpido","expedido","exótico", "estereótipo","fragmentado", "fascinante","flanco","factual","fragrância","fito","férias", "fiel","funcionalidade", "feminino","fechar","fascínio","fatores","franqueza", "fofoca","fugir","fenda", "fustigado", "fascinar","fraternal", "flor", "fundamentar", "ficha","geocentrismo", "geringonça", "gesticular", "gene", "germânico", "gelo", "gerenciamento","gelatina","germinação", "geek","geleira", "gerencial" "gel","gelificante","geba", "gesticulação","gelar" "germinal","geomorfológico","geminação", "geotermômetro", "gertrudes", "geologicamente","georreferenciar", "geniculado","gerontológico", "gemar","genialmente","geminípara","gengibirra","honorário","hidrópico","herético", "hiato", "haja", "honorários", "honrar","higiene","heterodoxo","hígido","herança", "homeostase", "higienizar","horrível","heteronomia","humanização", "habitat","hífen", "homeopático","hospício", "hansa", "herdar", "hibridismo", "hotel","honroso","hereditariedade", "hilariante", "honorável", "hostilizado" "homizio", "hiância","imanente", "insípido", "indiferença", "intrínseca", "interesse", "instância","insano","intersecção", "intempestivo", "instável", "idiossincrático", "intolerância","inútil", "inevitável","impor", "imiscuir", "interdependência", "imperativo","intervir",  "incrédulo", "indissociável", "imaginação","imagem", "inescrupuloso", "ilusão" ,"injúria", "insolência", "ilustre","jazigo", "jactar", "jogo", "jovialidade", "justa", "justificação", "justaposto","jamanta", "judiação", "jesuíta", "jazida", "javé","jogador","jerivá" "jangada","janeiro", "jarro", "joana", "jabiraca", "jandaia", "Jogatina","julho", "junípero", "jubilamento", "joule", "jurígeno", "jararaca", "jaca","jarretar","juncar","judas", "jardar", "jejuar","jogado", "judicativo", "jongo", "japão", "karaokê","ketchup","kit","kitchenette","kickboxing","kung fu","kart","kartódromo","Kimono","lua", "lembrança", "literalmente", "lucidez", "lastro", "lástima", "laico", "lânguido","ladainha", "linguagem", "ludibriado", "lenda","louvor", "litigar", "leite", "legítimo","ladrão", "lassidão", "limitação", "liberal","lema", "libido" ,"light", "loucura","lindeiro","latino", "lacustre","lapela", "livrearbítrio", "libertino","légua", "levantamento", "lábia","linhagem", "litigância","logia","limpo","lutar", "lúbrico", "mesmo","menção","método","martírio","mostrar", "mercê", "melindre", "maroto","mediador","moderado","monogâmico", "memória","miliciano", "manutenção","manter","marrento", "moção","misticismo", "morar", "metafísica", "mutável","mameluco","modesta", "modo", "mentor", "manifesto", "medida", "mancomunado", "moralista","metonímia", "massivo", "mau-caráter", "murmúrio", "monastério", "morfologicamente" "mau","nascimento","nativo","natural","navegante","necessidade","neto","nível","nobre","nadadeira","narguilé","navalha","nave","navio","nebulizador","niple","obcecado", "otimizar","oneroso","outro", "opressão", "obtuso","orla", "oblação", "onerar","obstruir", "obstrução","opcional", "orvalho", "olá","obra","oásis","ordenado", "oferta", "online", "ocasionalmente","oficial", "ocupado" ,"ordeiro","obrigada", "ourives", "osso", "oportunismo", "opróbio", "obediente", "off", "objetar","outdoor", "originário","organizado","oscular", "olfato","operacional","paciência", "problema", "pejorativo", "preceito", "proposição", "paralelo", "primordial","pragmatismo", "pesar", "perseverar", "providência","pela", "prazer", "postergar","pudor", "pitoresco", "patente", "prosélito", "parecer", "preponderante", "ponderado","propiciar", "práxis","proeza","puder","pleito", "passiva", "preterido","preservar", "prosperidade", "pulha", "pátria", "proposta", "perfazer","patológico","quadro", "qualidade", "quase", "quatro", "quebrado", "queda", "queijo", "queimar", "queixa", "quente", "querer", "quero", "questão", "química", "quilate", "quilômetro", "quimera", "quindim", "quiosque", "quociente", "quota", "quintal", "quinhão", "quarto", "quieto", "quiver", "quorum", "quente", "quinteto", "quorum", "quartzo", "quadrado", "quasar", "quebra", "quadro", "qualquer", "quartel", "queijo", "química", "química", "quimono", "quilombo", "quintal", "querido", "querido", "quilograma", "quarentena", "quinhão", "quadrúpede", "quarto","rabisco", "rabo", "raça", "rachado", "radar", "rádio", "rádix", "raia", "raio", "raiva","raiz", "rajada", "ralar", "ralo", "ramal", "rã", "ranger", "ranho", "ranzinza", "rapadura","rapariga", "rapaz", "rapel", "rápido", "rapina", "raposa", "raquete", "rasante", "rasgar", "raso","rastro", "ratificar", "rato", "razoável", "razão", "realeza", "realidade", "rebanho", "rebelde", "recado","receber", "recessão", "recibo", "recipiente", "recitar", "recobrar", "recolher", "recordar", "recurso", "redemoinho","sábio", "sabão", "sabedoria", "saber", "saborear", "sabor", "sacada", "saco","sacrifício", "sádico","sagacidade", "saga", "sagrado", "saída", "salada", "salário", "saldo", "salgado", "saliva", "salmão","salmo", "salpicado", "salsa", "saltador", "saltar", "salto", "samba", "sâmbico", "sanatório", "sangue","santa", "santo", "sapa", "sapo", "saque", "saracoteio", "sarjeta", "sarna", "sarna", "sátira","satisfação", "sazonal", "saudável", "saudade", "saudar", "saúde", "saudoso", "seara", "sebo", "seção","tabaco", "tábua", "taco", "tática", "taberneiro", "tabuleiro", "tábula", "tacão","táctil", "tagarela","tamanho", "tamanco", "tâmara", "tampo", "tampar", "tandem", "tanga", "tango", "tanque", "tanto","tarde", "tarefa", "tártaro", "tarugo", "tascar", "tatu", "tatuagem", "tatuar", "teatro", "tecido","tecla", "teclar", "tecnologia", "teimoso", "telhado", "telha", "telescópio", "telúrico", "tempo", "tenda","tênis", "tenor", "tentar", "tentação", "tênue", "teor", "teórico", "ter", "terra", "terraço","ubíquo", "ubíquo", "uberaba", "ubá", "ubi", "ubíqua", "ubíquas", "ubre", "úlcera", "ulisse","ultimato", "último", "umidade", "umidade", "único", "unidade", "uniforme", "unificar", "unilateral", "unir","universal", "universidade", "urbano", "urgente", "urna", "urubu", "urze", "usufruir", "usual", "usura","usurpador", "utilidade", "utilitário", "utilizar", "utopia", "utrículo", "uva", "vadio", "validação", "vapor","vasta", "veloz", "vênia", "veneno", "verídico", "vermelho", "verão", "vestido", "vexatório", "viabilidade","xadrez", "xale", "xangô", "xará", "xarope", "xeque", "xícara", "xiita", "xilogravura", "xodó","xoxo", "xote", "xuxa", "xícara", "xaxim", "xênon", "xerife", "xerox", "xexéu", "xará","xadrezista", "xamã", "xamânico", "xanadu", "xará", "xará", "xávega", "xavante", "xeque-mate", "xenofobia","xereca", "xerox", "xicara", "xilogravura", "xilofone", "xiririca", "xixi", "xodó", "xucro", "xuxu","xadrezista", "xamã", "xenofobia", "xerocópia", "xerox", "xará", "xerox", "xénon", "xenofobia", "xenon","zabumba", "zaga", "zagueiro", "zangado", "zangão", "zanzar", "zape", "zapear", "zebu", "zéfi","zelador", "zeloso", "zênite", "zênite", "zézinho","ziguezague", "zimbrar", "zincar", "zíper", "zíper","ziriguidum", "zircônia", "ziziphus", "zizófaga", "zoada", "zombar", "zoológico", "zoom", "zoonomia", "zoonomia","zoomorfismo", "zorra", "zulu", "zumbido", "zumbi", "zumbir", "zuílo", "zulu", "zumbi", "zunir","zunzum", "zunzunzum", "zuízo", "zúrico", "zuzum", "zíper", "zózimo", "zuísmo", "zuíz", "zóxis","zuízo", "zíper", "zoada", "zoa", "zoada", "zoada", "zoada", "zoada", "zoada", "zoada"]


def escolher_palavra():
    return random.choice(palavras)


def desenhar(palavra, letras_corretas, letras_erradas, estado_forca):
    janela.fill(BRANCO)
    
    
    texto_titulo = FONTE_TITULO.render("Jogo da Forca", 1, PRETO)
    titulo_x = LARGURA // 2 - texto_titulo.get_width() // 2
    janela.blit(texto_titulo, (titulo_x, 20))
    
    
    palavra_exibida = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
    texto_palavra = FONTE.render(palavra_exibida, 1, PRETO)
    palavra_x = LARGURA // 1.5 - texto_palavra.get_width() // 2
    janela.blit(texto_palavra, (palavra_x, ALTURA // 2))
    
    
    texto_letras_erradas = FONTE_LETRA.render("Letras Erradas: " + " ".join(letras_erradas), 1, VERMELHO)
    letras_erradas_x = 10
    janela.blit(texto_letras_erradas, (letras_erradas_x, ALTURA - 50))
    
    
    base_x = 0  
    if estado_forca >= 1:
        pygame.draw.line(janela, PRETO, (base_x + 50, 450), (base_x + 50, 150), 10)
    if estado_forca >= 2:
        pygame.draw.line(janela, PRETO, (base_x + 50, 150), (base_x + 200, 150), 10)
    if estado_forca >= 3:
        pygame.draw.line(janela, PRETO, (base_x + 200, 150), (base_x + 200, 200), 10)
    if estado_forca >= 4:
        pygame.draw.circle(janela, PRETO, (base_x + 200, 250), 50, 10)
    if estado_forca >= 5:
        pygame.draw.line(janela, PRETO, (base_x + 200, 300), (base_x + 200, 450), 10)
    if estado_forca >= 6:
        pygame.draw.line(janela, PRETO, (base_x + 200, 300), (base_x + 150, 350), 10)
        pygame.draw.line(janela, PRETO, (base_x + 200, 300), (base_x + 250, 350), 10)
        pygame.draw.line(janela, PRETO, (base_x + 200, 450), (base_x + 150, 500), 10)
        pygame.draw.line(janela, PRETO, (base_x + 200, 450), (base_x + 250, 500), 10)
    
    pygame.display.update()


def principal():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    estado_forca = 0
    
    
    FPS = 60
    relogio = pygame.time.Clock()
    executando = True
    while executando:
        relogio.tick(FPS)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key >= pygame.K_a and evento.key <= pygame.K_z:
                    letra = chr(evento.key).lower()  
                    if letra in palavra and letra not in letras_corretas:
                        letras_corretas.append(letra)
                    elif letra not in palavra and letra not in letras_erradas:
                        letras_erradas.append(letra)
                        estado_forca += 1
        
        desenhar(palavra, letras_corretas, letras_erradas, estado_forca)
        
        
        ganhou = all(letra in letras_corretas for letra in palavra)
        if ganhou:
            exibir_mensagem("Você Ganhou!", VERDE)
            pygame.time.delay(3000)
            break
        
        if estado_forca == 6:
            exibir_mensagem(f"Você Perdeu! era {palavra}", VERMELHO)
            pygame.time.delay(3000)
            break
    
    pygame.quit()


def exibir_mensagem(mensagem, cor):
    texto = FONTE.render(mensagem, 1, cor)
    janela.blit(texto, (LARGURA/2 - texto.get_width()/2, ALTURA/2))
    pygame.display.update()


if __name__ == "__main__":
    principal()
