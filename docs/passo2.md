# Passo 2 - Primeiro Plugin

Este documento é parte do [tutorial de desenvolvimento de plugins gimp](../README.md).

Como em todo tutorial de programação, o primeiro plugin que criaremos é um
simples "Olá Mundo".

Este plugin mostra a mensagem "Olá Mundo" na barra de progresso do gimp,
preenche a barra até 100% e finaliza.

O objetivo deste exemplo é ilustrar a estrutura de um plugin GIMP escrito em
Python.

Veja o código fonte do exemplo em [hello.py](../hello/hello.py)

Para testar o plugin, copie ou crie um link simbólico para o arquivo 
hello.py no diretório ".gimp2.8/plug-ins" abaixo do seu diretório home
e abra o GIMP.

O plugin vai aparece no menu em Filtros/Python-Fu/Tutorial/Olá Mundo

Vamos analisar este código aos poucos:

A primeira linha do código inicia com:

```python
#!/usr/bin/env python2
```

Indicando ao sistema operacional para executar com o interpretador padrão do
sistema para a linguagem Python versão 2.

na linha seguinte, há a indicação da codificação de caracteres:

```python
# -*- coding: utf-8 -*-
```

Utilize *sempre* utf-8 como codificação de caracters para plugins do GIMP. As
funções do GIMP que utilizam texto como parâmetro assumem que o texto está
sempre codificado em UTF-8.

Em seguida, temos um trecho de comentário indicando que o código dos plugins
deste tutorial são licenciados em GPL v3 (ver [Licença](../LICENSE.txt)).

O próximo bloco importa os módulos de integração do seu script com o gimp:

```python
import gimpfu
import gimp
```

Estes dois módulos são os principais para integração com o gimp: 

* *gimpfu* contém constantes, registro do plugin e objetos de acesso ao banco 
  de dados de funções do gimp, ou seja, é a interface para que seu plugin possa
  chamar as funcionalidades do gimp.
* *gimp* contém funções para comunicação com a interface com o usuário do gimp,
  e funções que manipulam o estado global do sistema.
  
Em seguida, é importado o módulo `time` padrão do python, que para uso da função
`sleep`.

```python
import time
```

O próximo passo, é definir a função principal (ponto de entrada) do plugin.
Esta função é a que vai ser chamada quando a opção de menu que executa o plugin
for selecionada pelo usuário.

```python
def hello():
    """Mostra a mensagem Olá Mundo! na barra de progresso"""
    gimp.progress_init("Olá Mundo")
    for i in range(100):
        gimp.progress_update(i/100.)
        time.sleep(.25)
```

Esta função utiliza recursos de interface com o usuário do gimp (módulo gimp)
para manipular a barra de progresso, inciando com o texto "Olá Mundo" e
alterando o progresso na barra em 1% a cada 0,25s.

Uma vez definida a função principal, é preciso registrar o plugin no banco de
dados de funções e procedimentos do GIMP, para que o GIMP saiba que o plugin
existe, saiba quais os parâmetros para invocar o plugin e em que posição do menu
principal será colocada a chamada para ele.

Isto é feito pela chamada à função `gimpfu.register`:

```python
gimpfu.register(
    "hello-tutorial", # name
    "Olá Mundo na barra de progresso", # blurb
    "Mostra o texto 'Olá Mundo' na barra de progresso", # help
    "Alexandre Machado", # author
    "Alexandre Machado", # copyright
    "2017", # date
    "<Toolbox>/_Tutorial/_Olá Mundo", # menupath
    "", # imagetypes
    [], # params
    [], # results
    hello, # function
    )
```

O primeiro parâmetro do registro é o nome do plugin (o nome que vai ser visível
para outros plugins via `gimpfu.query()`). No nosso caso, este nome é
`hello-tutorial`.

O segundo parâmetro, que o gimp chama de *blurb*, é um texto curto indicando o
que o plugin faz. Este texto normalmente é composto de uma frase curta (3 ou 4
palavras).

O próximo parâmetro é a mensagem de help do plugin, que irá ajudar outros
desenvolvedores que quiserem utilizar seu plugin como componente para outros
plugins a entender como utilizá-lo.

Em seguida, aparecem os parâmetros de autor e proprietário dos diretitos de
cópia (Copyright) do plugin, seguido pela data (ano) em que o plugin foi
desenvolvido.

O próximo parâmetro é a posição no menu onde a chamada do plugin será
instalada. Este parâmetro tem um prefixo que indica como o plugin será chamado:

* `<Image>`: Plugins inseridos com este prefixo operam sobre uma imagem inteira, 
  e precisam receber como parâmetro esta imagem.
* `<Layers>`: Plugins inseridos com este prefixo irão operar sobre camadas, e
  precisam receber os parâmetros de um plugin de camadas.
* `<Channels>`: Plugins que operam sobre canais, precisando receber os
  parâmetros adequados.
* `<Vectors>`: Plugins que operam sobre vetores, precisando receber os
  parâmetros adequados.
* `<Colormap>`: Plugins que operam sobre mapas de cores, recebendo uma imagem
  como parâmetro.
* `<Brushes>`: Plugins que operam sobre pincéis. 
* `<Dynamics>`: Plugins que operam sobre dinâmicas de pintura
* `<Gradients>`: Plugins que operam sobre gradientes
* `<Palettes>`: Plugins que operam sobre paletas de cores
* `<Patterns>`: Plugins que operam sobre padrões
* `<ToolPresets>`: Plugins que operam sobre configurações pré-definidas de ferramentas
* `<Fonts>`: Plugins que operam sobre fontes
* `<Buffers>`: Plugins que operam sobre buffers
* `<Toolbox>`: Plugins que acrescentam funcionalidades/ferramentas ao Gimp.

Destes, os plugins mais usados são do prefixo `<Toolbox>`, `<Image>` e
`<Layers>`.

Logo após o prefixo está o caminho no menu onde o plugin vai aparecer. Você pode
inserir em um local já existente do menu, como por exemplo sob o menu Arquivo,
indicando um caminho como `File/Seu Item de Menu`, ou diretamente no menu
principal, indicando um caminho de menu não existente no gimp.

Os menus já existentes no GIMP são:

* *File* : Arquivo
* *Edit* : Editar
* *Select* : Selecionar
* *View*: Visualizar
* *Image*: Imagem
* *Layer*: Camada
* *Colors*: Cores
* *Tools*: Ferramentas
* *Filters*: Filtros
* *Xtns*: Extensões (parte final do menu de Filtros)

Para facilitar o acesso, os plugins deste tutorial ficarão logo no menu
principal, abaixo da opção `Tutorial.`


*OBS:* O caracter sublinhado (`_`) antes de uma letra no caminho do menu indica
que a letra a seguir é o atalho para este menu.




Finalmente, após registrar o plugin, é necessário executar a função principal do
módulo gimpfu para iniciar a comunicação com o gimp:

```python
gimpfu.main()
```
