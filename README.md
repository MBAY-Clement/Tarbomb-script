# Tarbomb-script

Script Python permettant d'extraire tous les fichiers d'un tarbomb contenant des fichiers .zip.bz2.bz / .zip / .zip.bz2

Voici la démarche : 

On a un fichier racine qui contient : 

un fichier .zip.bz2.gz qui lui meme contient .zip.bz2 et qui lui même contient un .zip

Ca fait donc : 

.zip.bz2.gz -> .zip.bz2 -> .zip -> .zip.bz2.gz -> .zip.bz2 -> .zip -> .zip.bz2.gz -> ....

Le script va alors extraire dans un premier temps le .zip.bz2.gz puis le .zip.bz2 et le .zip. 
Le .zip contient un .zip.bz2.gz qui lui même contient un .zip.bz2 (etc etc). 

Le script sait alors que la racine de la tarbombe est le fichier .zip.bz2.gz à la fin et va finir par tous extraire. 
