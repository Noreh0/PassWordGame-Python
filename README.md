# Password Game em Python

Um jogo de quebra-cabeça simples, mas desafiador, onde você deve criar uma senha que satisfaça uma lista crescente de regras malucas. Este projeto é inspirado no popular "The Password Game" e é implementado inteiramente em Python, rodando diretamente no seu terminal.

## Como Jogar

Este jogo não requer nenhuma biblioteca externa, apenas o Python 3.

1.  **Clone o repositório** (ou apenas baixe o arquivo `passwordgame.py`):
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Navegue até o diretório** do projeto:
    ```bash
    cd seu-repositorio
    ```

3.  **Execute o script** com Python:
    ```bash
    python3 passwordgame.py
    ```

4.  **Siga as instruções!** O jogo começará com a primeira regra. Sua tarefa é digitar uma senha que atenda a **todas** as regras exibidas. A cada rodada bem-sucedida, uma nova regra é adicionada, aumentando o desafio.

## Exemplo de Sessão

Veja como o jogo funciona no terminal:

```bash
$ python3 passwordgame.py

🔒 BEM-VINDO AO PASSWORD GAME! 🔒

Crie uma senha que atenda a todas as regras que aparecem.
As regras vão ficando mais difíceis conforme você avança!


📋 REGRAS ATIVAS (Total: 1):
   ➡️ Regra 1: Sua senha deve ter pelo menos 5 caracteres

🎯 Você precisa passar em TODAS as regras acima para continuar!

 Digite sua senha: test

📊 Resultado da verificação:
   ❌ Regra 1: Sua senha deve ter pelo menos 5 caracteres

❌ Você ainda precisa corrigir algumas regras antes de continuar.


📋 REGRAS ATIVAS (Total: 1):
   ➡️ Regra 1: Sua senha deve ter pelo menos 5 caracteres

🎯 Você precisa passar em TODAS as regras acima para continuar!

 Digite sua senha: teste123

📊 Resultado da verificação:
   ✅ Regra 1: Sua senha deve ter pelo menos 5 caracteres

✅ SUCESSO! Nova regra desbloqueada: Sua senha deve incluir um número

... e assim por diante ...
