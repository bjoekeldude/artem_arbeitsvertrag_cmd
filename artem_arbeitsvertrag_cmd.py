from os import closerange
from tkinter import *
import library_arbeitsvertrag as la
import os
import arbeitsvertrag_gui as ag

mitarbeiterdaten = la.vertragsdaten

la.get_vertrags_input_from_cmd(mitarbeiterdaten)
la.write_dict_to_configfile(inputdict=mitarbeiterdaten, outputfile="texdata/lat.tex")
#ag.write_dict_to_configfile_from_gui(inputdict=mitarbeiterdaten, outputfile="texdata/lat.tex")
os.system("pdflatex texdata/main.tex")