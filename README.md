# Biblioteca Comunitária Vila Esperança

Código da Atividade A9 de Engenharia de Software I. O roteiro da atividade explica o que fazer com ele, e o guia técnico detalha cada passo da preparação, o uso do VS Code e as soluções para os problemas mais comuns.

## Conteúdo

- `biblioteca.py`: as regras de empréstimo usadas pelo balcão de atendimento.
- `testes/test_bateria1.py`: a bateria 1 de testes.
- `testes/test_bateria2.py`: a bateria 2 de testes.
- `conferir_ambiente.py`: confere se o computador está pronto para a atividade.

## Preparação

No Windows, troquem `python3` por `py` em todos os comandos.

1. No botão **Code** desta página, copiem o endereço do repositório. No terminal, baixem o repositório e entrem na pasta criada:

   ```
   git clone <endereço copiado> a9-biblioteca
   cd a9-biblioteca
   ```

   Sem o Git, escolham **Download ZIP** no mesmo botão, descompactem o arquivo e abram o terminal dentro da pasta descompactada.

2. Instalem o pytest e o Pylint:

   ```
   python3 -m pip install --user -r requirements.txt
   ```

   Se o pip recusar a instalação com a mensagem `externally-managed-environment`, usem um ambiente virtual:

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt
   ```

   No Windows, o segundo comando é `.venv\Scripts\activate`. Cada terminal novo precisa ativar o ambiente outra vez.

3. Confiram a preparação:

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

- `git status` mostra se algum arquivo foi alterado.
- `git restore .` desfaz as alterações e devolve os arquivos ao estado em que foram baixados.
- `git pull` baixa uma correção que o professor tenha publicado depois do download.

Não alterem o código nem os testes.
