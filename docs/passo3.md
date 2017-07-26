# Passo 3 - Descobrindo funções do GIMP

Este documento é parte do [tutorial de desenvolvimento de plugins gimp](../README.md).

Agora que já temos um exemplo da estrutura de um plugin, está na hora de
descobrir o que o GIMP é capaz de fazer via programação.

O GIMP organiza toda a sua funcionalidade acessível para scripts e plugins
através de um banco de dados de procedimentos. Este banco de dados é
representado pelo objeto `pdb` do módulo `gimpfu`.

A maneira mais simples de acessar informações deste banco de dados é através do
console python presente no GIMP (Menu *Filtros/Python-Fu/Console* no GIMP em
pt_BR).

O console aparece como a figura a seguir:

![Python Console](img/console.png)

## Console Python no GIMP

O console python executa a instrução `from gimpfu import *` na inicialização,
fazendo com que os objetos definidos no módulo `gimpfu` estejam acessíveis no
namespace padrão. Desta forma, você pode acessar diretamente os objetos `gimp` e
`pdb` no console.

O Console executa o mesmo interpretador Python que o GIMP irá executar
normalmente. Desta forma, qualquer instrução que você pode colocar em um plugin
pode ser executada diretamente no console.

Por exemplo, ao executar no console:

~~~python
>>> gimp.progess_init("Olá Mundo")
~~~

A barra de progresso é mostrada com a mensagem "Olá Mundo".

Com isto, podemos utilizar o console para fazer pesquisas no banco de dados de
procedimentos.

# O banco de dados PDB

A chamada à função `gimpfu.register` no exemplo do [Passo 1](passo1.md) faz o
registro (inclusão) do seu plugin no banco de dados PDB, o banco de dados de
procedimentos do GIMP.

Qualquer plugin e muitas funcionalidades internas do GIMP estão registradas
neste banco de dados, e podem ser acessadas a partir dele.

A maneira mais simples de fazer buscas neste banco de dados é utilizar o método
`query` do objeto `pdb` via console:

~~~python
>>> pdb.query('load')
['file-xjt-load', 'file-png-load', 'file-faxg3-load', 'file-openraster-load-thumb', 'file-bz2-load', 'file-ico-load-thumb', 'file-pcx-load', 'file-tiff-load', 'file-cel-load', 'file-sunras-load', 'gimp-register-magic-load-handler', 'file-jpeg-load-thumb', 'file-gbr-load', 'file-svg-load', 'file-sgi-load', 'gimp-xcf-load', 'file-fits-load', 'gimp-register-load-handler', 'gimp-get-module-load-inhibit', 'file-xwd-load', 'file-pat-load', 'file-wmf-load-thumb', 'gimp-file-load-layer', 'file-xpm-load', 'file-psd-load', 'file-pdf-load', 'file-psd-load-thumb', 'file-jp2-load', 'file-ico-load', 'gimp-selection-load', 'file-psp-load', 'file-dicom-load', 'file-pnm-load', 'file-svg-load-thumb', 'gimp-file-load-layers', 'gimp-file-load', 'file-gz-load', 'file-tga-load', 'file-jpeg-load', 'file-wmf-load', 'file-xmc-load-thumb', 'file-openraster-load', 'file-gif-load-thumb', 'gimp-register-thumbnail-loader', 'file-pdf-load-thumb', 'file-eps-load', 'file-ps-load', 'file-raw-load', 'file-gih-load', 'file-xmc-load', 'file-desktop-link-load', 'file-pix-load', 'file-fli-load', 'file-ps-load-thumb', 'file-uri-load', 'file-bmp-load', 'file-ps-load-setargs', 'file-xbm-load', 'file-gif-load', 'gimp-file-load-thumbnail']
~~~
