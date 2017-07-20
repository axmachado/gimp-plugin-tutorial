# Tutorial Gimp - Preparando o Ambiente.

Este documento é parte do [tutorial de desenvolvimento de plugins gimp](../README.md).

Este tutorial assume o desenvolvimento do plugin em ambiente GNU/Linux. Se você
utiliza outro sistema operacional, é possível adaptar, e contribuições para
adequação deste tutorial para outros sistemas são bem vindas.

## Instalação do GIMP

O tutorial presume o GIMP versão 2.8 ou superior instalado. A instalação padrão
do gerenciador de pacotes do seu sistema geralmente é satisfatória.

A execução de plugins em python é feita através da extensão GIMP-Python,
presente por padrão na grande maioria das distribuições. Você pode verificar se
esta extensão está instalada e o interpretador usável no seu GIMP pela
existência do menu Filtros/Python-Fu.

## Instalação do interpretador Python

O tutorial e os exemplos utilizarão Python2.7, que é o que vem instalado como
padrão na maioria das distribuições linux.

## Ambiente de desenvolvimento

Este tutorial não assume nenhuma preferência pelo ambiente de
desenvolvimento. Utilize o seu editor de textos favorito, preferencialmente
algum que possa pelo menos destacar a sintaxe da linguagem Python para facilitar
a detecção de erros de digitação.

## Instalação dos seus plugins

Ao ser carregado, o GIMP executa tudo o que encontrar em
~/.gimp2.8/plug-ins. Você pode copiar os seus plugins para este diretório ou
criar links simbólicos para o seu diretório de desenvolvimento.

É importante que o seu script possa ser executado em linha de comando pelo
GIMP. Desta forma, seus plugins precisam ter o bit de permissão de execução
configurado (`chmod a+x seu-plugin.py`), e que começe com a diretiva 
([shebang](https://pt.wikipedia.org/wiki/Shebang) para
indicar que deve ser executado pelo interpretador python.

Usualmente, isto significa que a primeira linha do script é: 

`#!/usr/bin/env python` 

indicando que o script deve ser execuado pelo interpretador python padrão do
sistema operacinal.

No meu caso particular, como costumo trabalhar em alguns ambientes várias
versões do Python instaladas, prefiro especificar qual versão do python a
utilizar para este script em particular:

`#!/usr/bin/env python2.7`

