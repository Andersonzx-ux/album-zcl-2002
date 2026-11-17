# Zezé Di Camargo & Luciano — 2002 (player)

Player estático (HTML/CSS/JS, sem build) para GitHub Pages. Todos os dados ficam em `data/album.js`.

## Identidade (tudo medido na capa)
| Papel | Cor | De onde vem |
|---|---|---|
| black | `#020205` | cabelos e sombras |
| wine | `#522821` | vermelho-escuro nas sombras |
| brown | `#573D2C` | marrom da jaqueta/pele na sombra |
| crimson | `#A33C2F` | carmim da faixa superior e dos fios |
| red | `#D94F3A` | vermelho vivo da faixa inferior |
| copper | `#D99155` | fios de luz |
| gold | `#F0C485` | realces |
| cream | `#F7CC8E` | título da capa |

- **Progresso = fios da capa**: a faixa de fios de cobre da parte de baixo da capa (recorte real `assets/fios.jpg`) escurece onde a faixa ainda não tocou e acende por onde já passou, com uma linha-guia creme. Clique/arraste nela para buscar na faixa (a barra comum continua funcionando).
- Fonte dos títulos: Marcellus (humanista, parecida com a do título da capa); texto: Jost (ambas OFL, em `assets/fonts/`).
- Divisória feita de três fios de cobre/carmim.
- Tela bloqueada/central de mídia (Media Session) com capa, play/pause, faixa anterior/próxima e seek.

## Arquivos
`index.html`, `css/style.css`, `js/{app,player,ui}.js`, `data/album.js` (só ganhou o bloco `palette`), `assets/{cover.jpg, cover-256.jpg, cover-512.jpg, fios.jpg, fonts/}`, `tools/{medir_paleta.py, gerar_recortes.py}`.
`assets/zcl.png` e `assets/zclogo.png` não são mais usados.
Letras e tradução: continue colando em `lyrics` / `translation` de cada faixa em `data/album.js`.
