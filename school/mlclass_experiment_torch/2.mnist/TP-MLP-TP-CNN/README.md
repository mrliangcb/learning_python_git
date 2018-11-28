## USAGES

### convertInkmlToImg.py
	Usage: convertInkmlToImg.py  (path to file or folder) dim padding
		+ (file|folder)        - required str
		+ dim                  - optional int (def = 28)
		+ padding              - optional int (def =  0)

### usefullTools.Py

Use func `load_dataset` to load CRHOME data and create database from image (png) folders if the .npz data file don't exist.


## TODO

changer GT files to keep key to filenames

Choisir un randseed arbitraire en début de fichier pour la reproductibilité

Cross Validation et choix du meilleur réseau avec différents méta-paramètres