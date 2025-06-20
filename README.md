🎯 Jogo da Forca (Python)
Um simples e divertido jogo da Forca feito em Python, jogado diretamente no terminal. O programa escolhe uma palavra aleatória de um arquivo de texto e o jogador tem um número limitado de tentativas para acertá-la, letra por letra.

📦 Funcionalidades
Escolha aleatória da palavra com a biblioteca random

Verificação de letras já tentadas

Contagem regressiva de tentativas

Exibição das letras corretas e ocultação das que ainda faltam

Mensagens de vitória e derrota

🧠 Como funciona?
O programa lê um arquivo chamado palavras.txt com uma lista de palavras (uma por linha).

Usa a função random.randint() para escolher uma palavra aleatória.

O jogador tenta adivinhar a palavra, digitando uma letra por vez.

O jogo termina quando:

Todas as letras forem descobertas ✅

Ou todas as tentativas forem usadas ❌

📁 Arquivos
Jogo_da_forca.py — Arquivo principal com a lógica do jogo.

palavras.txt — Arquivo de texto contendo as palavras que podem ser sorteadas.

Exemplo do conteúdo de PALAVRAS:

CACHOEIRA
SOMBRINHA
ABACAXI
TELEFONE
BORBOLETA
▶️ Como rodar
Certifique-se de ter Python instalado.

Clone o repositório:

git clone https://github.com/Igor-Brumana/Jogo-da-Forca.git
Entre na pasta:

Jogo da forca

Rode o jogo:
Jogo_da_forca.py

🧩 Bibliotecas utilizadas
random: Utilizada para escolher a palavra aleatória da lista.

📌 Requisitos
Python 3.x

📃 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
