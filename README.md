# UERJ Sistemas Distribuidos

Trabalho Final da matéria Sistemas Distribuídos da Universidade Estadual do Rio de Janeiro.

Aplicação feita para filtrar domínios de sites específicos, utilizando a biblioteca Sucuri.

## Requerimentos
- Python 2.x
- Linux

## Como funciona
- Clonar o projeto
``` git clone ```

- Na pasta raiz do projeto abra o console e execute
```python2 main.py numero_workers nome_arquivo```

- Irá aparecer na tela os tempos de execução

## Teste
- Para rodar um arquivo de testes testando de 1 a 8 workers e com os arquivos que estão na pasta data executar
```./test.sh > output.txt```

- Será gerado um log no arquivo output.txt

## No arquivo analise_dados.ods
Encontram-se os dados analisados durante a execução do trabalho

## O arquivo website_generator
Gera um arquivo com n quantidades de linhhas de com urls randômicas, sendo válidas ou não, para isso basta executar

```python2 website_generator.py 100```