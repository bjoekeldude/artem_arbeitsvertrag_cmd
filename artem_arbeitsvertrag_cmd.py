import avlib as la
import os

mitarbeiterdaten = la.vertragsdaten

la.get_vertrags_input_from_cmd(mitarbeiterdaten)
la.write_dict_to_configfile(inputdict=mitarbeiterdaten, outputfile="texdata/lat.tex")
os.system("pdflatex texdata/main.tex")
