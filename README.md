# ChatBot Assistente de Vendas em Python com ChatterBot

Este é um projeto de exemplo de um ChatBot em Python com a personalização de um assistente de vendas. O ChatBot é treinado para responder a perguntas relacionadas a vendas de cursos.

## Visão Geral

Este projeto utiliza a biblioteca ChatterBot para criar um ChatBot personalizado que age como um assistente de vendas de cursos. O ChatBot é treinado com interações relacionadas a perguntas comuns de clientes interessados em um curso.

## Estrutura de Pastas

A estrutura de pastas do projeto é organizada da seguinte forma:

  ```bash
  chatbot-assistente-de-vendas/
  |-- main.py
  |-- requirements.txt
  ```

- `main.py`: Este é o arquivo principal do projeto, onde o ChatBot é criado, treinado e a interação com o usuário ocorre.

- `requirements.txt`: Este arquivo lista as dependências do Python necessárias para o projeto. Use o pip para instalar essas dependências.

## Pré-requisitos

Antes de começar, você deve ter as seguintes dependências instaladas:

- Python 3.8

Certifique-se de ter essas dependências instaladas no seu ambiente de desenvolvimento.

## Configuração

1. Clone o repositório:

  ```bash
  git clone https://github.com/alan-vieira/chatbot-assistente-de-vendas.git
  cd chatbot-assistente-de-vendas
  ```

2. Instale as dependências usando o pip:

  ```bash
  pip install -r requirements.txt
  ```

## Modificação no arquivo `compat.py` da biblioteca SQLAlchemy

Ao utilizar a biblioteca SQLAlchemy em conjunto com o sistema operacional Windows ou Jython, foi identificado um possível problema relacionado à função `time.clock` na linha 264 do arquivo `compat.py`.

### Problema Identificado

No código original:

  ```python
  if win32 or jython:
      time_func = time.clock
  else:
      time_func = time.time
  ```

A função time.clock é utilizada, porém, em algumas situações específicas, essa abordagem pode levar a problemas.

### Solução Aplicada

A seguinte modificação foi realizada para evitar possíveis complicações:

  ```python
  if win32 or jython:
    #time_func = time.clock
    pass
  else:
    time_func = time.time
  ```

Essa alteração evita o uso da função `time.clock` e opta por manter o código compatível em ambientes Windows e Jython.

Nota: Modificar diretamente o código de bibliotecas pode ter implicações. Recomenda-se monitorar as atualizações da biblioteca e verificar se o problema foi abordado nas versões mais recentes.

## Como Usar

Para executar o ChatBot, você pode usar o seguinte comando:

  ```bash
   python main.py
   ```
O ChatBot iniciará e estará pronto para interagir com você como um assistente de vendas.

## Funcionalidades do ChatBot

O ChatBot é personalizado para responder a perguntas comuns relacionadas a vendas de cursos. Algumas perguntas que você pode experimentar fazer incluem:

- "Me fale mais sobre o curso de Análise de Dados."
- "Qual é o preço do curso?"
- "O curso oferece certificado de conclusão?"

Sinta-se à vontade para adicionar suas próprias interações ao arquivo `main.py` e treinar o ChatBot com mais informações.

## Documentação

### ChatBot

`ChatBot(nome, logic_adapters, storage_adapter, database_uri)`

Cria uma instância do ChatBot.

- `nome`: Nome do ChatBot.
- `logic_adapters`: Lista de adaptadores lógicos a serem utilizados.
- `storage_adapter`: Adaptador de armazenamento a ser utilizado.
- `database_uri`: URI do banco de dados para armazenar interações do ChatBot.

### Treinamento

O treinamento do ChatBot é realizado usando o método `train` do adaptador de treinamento, seja `ListTrainer` ou `ChatterBotCorpusTrainer`.

`ListTrainer(bot)`

Treinador para treinar o ChatBot com uma lista personalizada de interações.

- `bot`: Instância do ChatBot a ser treinada.

Exemplo:

  ```bash
  conversa = ListTrainer(bot)
  conversa.train([
    'Qual é o preço do curso?',
    'O preço do curso é de R$ 720,00. No entanto, oferecemos descontos para grupos de 10 ou mais.'
  ])
  ```
`ChatterBotCorpusTrainer(bot)`
Treinador para treinar o ChatBot com corpus de linguagem pré-definido.

- `bot`: Instância do ChatBot a ser treinada.

Exemplo:

  ```bash
  conversa = ChatterBotCorpusTrainer(bot)
  conversa.train('chatterbot.corpus.portuguese')
  ```


## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE]() para detalhes.

## Autor

| [<img src="https://avatars.githubusercontent.com/alan-vieira" width=115><br><sub>Alan Vieira</sub>](https://github.com/alan-vieira) |
| :---: |

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Agradecimentos

Agradecemos pelo uso e interesse neste projeto! Esperamos que seja útil para seus propósitos.
