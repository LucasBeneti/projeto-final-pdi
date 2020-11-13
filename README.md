# Projeto final de PDI

## Corretor de gabarito de provas

Fase de testes puros, pra ver se encontro um jeito de criar uma máscara identificando a imagem e compará-la com a máscara do gabarito

No branch development:

- passo um thresh adaptativo gaussiano com mais alguns detalhes (th2)
- crio uma imagem em branco que é onde desenharei os contornos pertinentes mais pra frente
- no primeiro for só ocorre desenho todos os contornor encontrados em uma das imagens em branco afim de comparar com a segunda
- no segundo for eu busco encontrar contorno fechado com a `isContourConvex()` e se esse contorno tem uma área maior que X
- mantendo a contagem desses contornos eu acabo por plotar eles numa segunda imagem em branco

### Resultado no momento:

    (08/11) - Não é muito bom porque buscando esses contornos mesmo verificando se são fechados e e maiores que uma área estipulada, não está pegando todas as alternativas marcadas

    (09/11) - A file teste2.py parece mais promissora, apenas é aplicado um thresh meio arbitrário (mas provavelmente consigo encontrar o melhor valor pelo histograma), nessa mesma limiarização, é obtida imagem invertida e assim as opções marcadas ficam bem mais evidentes. Uma ideia pra pegar cada opção de cada linha é, cortar a imagem em 50 linhas com 6 colunas cada e a partir do index 1 (porque 0 será o número da questão), ver o número de pixels não nulos e pegar o maior valor dentre as cinco opções, e aquela que tiver uma discrepância maior, será eleita a resposta correta (se for o caso do gabarito) e a opção de quem respondeu (caso da prova) e assim
    fazer alguma lógica pra guardar e computar esses dados. Pra anular uma questão tbm é tranquilo, ou não tem uma diferença muito grande entre as alternativas ou tem mais de uma que será considerada anulada pois não é possível marcar duas alternativas

    (10/11) - NOTA MENTAL: `cv2.imshow(<NOME DA JANELA COMO STRING>, matrizDaImagem)`, os splits estão funcionando
        Parte 2: Terminei as funções mais críticas pra conseguir um array com as alternativas marcadas a partir de uma imagem. Próximo passo é usar essa função pra comparar duas imagens diferentes (gabarito x teste) e ver quantas questão estão iguais

    (11/11) - Mudei o threshold pra otsu pois parece melhor, falta um pouco mais de testes pra fechar com ele. Na pasta de `images` tem a `gabarito_1.jpg` e `prova_1.jpeg`, essas duas estão completamente preenchidas e foram tiradas com uma puta sombra, boas pra teste. (Breve teste com OTSU, deu bosta nessas duas imagens melhores)

### Melhorias

    [FEITO] Se o gabarito for mais quadrado, proporções mais certinhas, capaz de obtermos uma melhor precisão na hora de separar os pedaços das imagens. - Deu certo, melhorou bastante na separação dos imagens.

    Fazer um melhor display da correção, talvez algo parecido com uma tabela pra ficar mais claro pro usuário.

### Interface CLI

    Interface está implementada, bem básica.
    * Entradas (respectivamente):
        - path para a pasta contendo as files de gabarito
        - path da file do gabarito
        - tipo do gabarito (1, 2, 3...)

    O tipo de prova deve estar explicito no nome da file da imagem do gabarito, como gabarito_1.jpeg, gabarito_2.jpeg, gabarito_3.jpeg
