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

    Não é muito bom porque buscando esses contornos mesmo verificando se são fechados e e maiores que uma área estipulada, não está pegando todas as alternativas marcadas
