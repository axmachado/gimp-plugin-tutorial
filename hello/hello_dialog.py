#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Mesmo que você utilize ISO8859-1 como codificação de caracters padrão
# no seu sistema, é recomendável que você utilize UTF-8 nos plugins do GIMP,
# já que muitas das funções que irão manipular texto no GIMP assumem que a
# entrada (parâmetros) está codificada em UTF-8
#
#
# Copyright(c) 2017 - Alexandre Machado <axmachado@gmail.com>
#
#   This is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see
#   <http://www.gnu.org/licenses/>.
#
#

import gimpfu
import gimp
import time

import pygtk
import gtk

def hello():
    """Mostra a mensagem Olá Mundo em um quadro de mensagem modal"""
    gimp.progress_init("Olá Mundo")
    dlg = gtk.MessageDialog (type=gtk.MESSAGE_INFO,
                             buttons=gtk.BUTTONS_CLOSE)
    dlg.set_markup("Olá Mundo!")    
    dlg.run()
    dlg.destroy()
    while gtk.events_pending():
        gtk.main_iteration()
        
    for i in range(100):
        gimp.progress_update(i/100.)
        time.sleep(.05)
    gimpfu.pdb.gimp_progress_end()
            

gimpfu.register(
    "hello-dlg-tutorial", # name
    "Olá Mundo em MessageBox", # blurb
    "Mostra o texto 'Olá Mundo' em um MessageBox", # help
    "Alexandre Machado", # author
    "Alexandre Machado", # copyright
    "2017", # date
    "<Toolbox>/_Tutorial/_Olá Mundo Message",
    "", # imagetypes
    [], # params
    [], # results
    hello, # function
    )
                

gimpfu.main()

    
