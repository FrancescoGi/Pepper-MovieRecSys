# Pepper-MovieRecSys

Come eseguire il sistema:

1. Apri Choregraphe e connetti il robot ad esso.
2. Importa il progetto 'MovieRecSysLib' su Choregraphe 
3. Installa l'applicazione 'MovieRecSysLib' su pepper (Sul riquadro 'Robot Applications' clicca sul bottone 'package and install current project to the robot' per intallare)
4. Importa il progetto 'pepper_movierecsys' su Choregraphe 
3. Installa l'applicazione 'pepper_movierecsys' su pepper (Sul riquadro 'Robot Applications' clicca sul bottone 'package and install current project to the robot' per intallare)
4. Esegui 'pepper_movierecsys' premendo play o eseguendolo direttamente dalla lista delle applicazioni installate su pepper.

P.s. Controllare nel box 'Add Modules' che il path del 'folder name' (folderName = "/data/home/nao/.local/share/PackageManager/apps/movierecsyslib-0fb8f5/behavior_1/lib") sia uguale a quello dell'applicazione 'MovieRecSysLib' precedentemente installata.
Ovvero che l'application ID nel path, 'movierecsyslib-0fb8f5' in questo caso, sia uaguale all'application ID del progetto 'MovieRecSysLib' installato. Nel caso fosse diverso, aggioirnare l'application ID nel path del box 'Add Modules'.