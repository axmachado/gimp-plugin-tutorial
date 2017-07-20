#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import gimpfu
import gimp
import time

def hello():
    """Mostra a mensagem Olá Mundo! na barra de progresso"""
    gimp.progress_init("Olá Mundo")
    for i in range(100):
        gimp.progress_update(i/100.)
        time.sleep(.25)
            

gimpfu.register(
    "hello_tutorial", # name
    "Olá Mundo na barra de progresso", # blurb
    "Mostra o texto 'Olá Mundo' na barra de progresso", # help
    "Alexandre Machado", # author
    "Alexandre Machado", # copyright
    "2017", # date
    "<Toolbox>/Xtns/Languages/Python-Fu/Tutorial/_Olá Mundo", # menupath
    "", # imagetypes
    [], # params
    [], # results
    hello, # function
    )
                

gimpfu.main()

    
