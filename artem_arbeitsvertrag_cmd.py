import avlib as la
import os

mitarbeiterdaten = la.vertragsdaten

la.get_vertrags_input_from_cmd(mitarbeiterdaten)
la.write_dict_to_configfile(inputdict=mitarbeiterdaten, outputfile="texdata/lat.tex")
ls.generate_avpdf(configfile="texdata/lat.tex", templatefile="latexdata/main.tex", outputdir=".", jobname=mitarbeiterdaten['nachname']+"_"+datetime(.......)):
