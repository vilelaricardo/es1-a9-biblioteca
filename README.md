# Biblioteca Comunitária Vila Esperança

Código da Atividade A9 de Engenharia de Software I. O roteiro da atividade descreve as tarefas, e o guia técnico detalha cada etapa da preparação, o uso do VS Code e as soluções para os problemas mais frequentes.

## Conteúdo

- `biblioteca.py`: regras de empréstimo utilizadas pelo balcão de atendimento.
- `testes/test_bateria1.py`: bateria 1 de testes.
- `testes/test_bateria2.py`: bateria 2 de testes.
- `conferir_ambiente.py`: verificação da preparação do computador para a atividade.

## Preparação

No Windows, substituam `python3` por `py` em todos os comandos.

1. Obtenham uma cópia do repositório e acessem a pasta criada:

   ```
   git clone https://github.com/vilelaricardo/es1-a9-biblioteca a9-biblioteca
   cd a9-biblioteca
   ```

   Na ausência do Git, escolham **Download ZIP** no botão **Code** desta página, extraiam o conteúdo do arquivo e abram o terminal na pasta resultante.

2. Instalem o pytest e o Pylint:

   ```
   python3 -m pip install --user -r requirements.txt
   ```

   Se o pip recusar a instalação com a mensagem `externally-managed-environment`, utilizem um ambiente virtual:

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt
   ```

   No Windows, o segundo comando é `.venv\Scripts\activate`. Sempre que um novo terminal for aberto, o ambiente deve ser ativado novamente.

3. Verifiquem a preparação do computador:

   ```
   python3 conferir_ambiente.py
   ```

## Comandos da atividade

```
python3 -m pytest testes/test_bateria1.py -v
python3 -m pytest testes/test_bateria2.py -v
python3 -m pylint biblioteca.py
```

## Comandos do Git

- `git status` indica se algum arquivo foi modificado.
- `git restore .` desfaz as modificações e restaura os arquivos ao estado original do repositório.
- `git pull` obtém eventuais correções publicadas pelo professor após a cópia inicial.

O código e os testes não devem ser alterados.
