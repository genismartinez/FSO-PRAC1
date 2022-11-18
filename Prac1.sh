#! /bin/bash
fil=0
cols=0
portSize=0

minFil=10
maxFil=120

minCol=8
maxCol=36
midaPaleta=0
minPort=8

minPort=8
temp=fil
posFilaPal=0
posColPal=0

posFilaPil=0
posColPil=0
velFil=0
velCol=0


Nflag=''
Fflag=''
Cflag=''
Pflag=''
OFlag=''
OneFlag=''
MFlag=''

found='false'
extraPilotes='false'
function readFile
{
	echo "READ FILE"
	#falta arreglar, sólo lee si hay 2 líneas en el archivo
	echo "Entra en 'readFile'"
	while IFS=' ' read -r fil cols portSize
	do
		echo "fils= $fil"
		echo "cols= $cols"
		echo "portSize= $portSize"
		exit
	done < $file
}

function writeFile
{
	echo "WRITE FILE"
	echo "$fil $cols $portSize" > $file
	echo "$posFilaPal $posColPal $midaPaleta" >> $file
	echo "$posFilaPil $posColPil $velFil $velCol" >>$file
	

}
function introducirRestantes 
{
	echo "INTRODUCIR VALORES RESTANTES"
	if [ -z $fil ] || [ -z $cols ] || [ -z $portSize ] ; then
		read -p "Introduce de nuevo las filas (10,120): " fil
		read -p "Introduce de nuevo las columnas (10,36): " cols
		let maxS=fil-1
		read -p "Introduce de nuevo el tamaño de la portería (8, $maxS): " portSize
	fi

	if [ -z $posFilaPal ] || [ -z $posColPal ] || [ -z $midaPaleta ] ; then
		read -p "Introduce de nuevo posFilaPal (1,118): " posFilaPal
		read -p "Introduce de nuevo posColPal (2,35): " posColPal
		let maxS=fil-1
		read -p "Introduce de nuevo midaPaleta (3,$maxS): " midaPaleta
	fi

	if [ -z $posFilaPil ] || [ -z $posColPil ] || [ -z $velCol ] || [ -z $velCol ]; then
		read -p "Introduce de nuevo posFilaPil (2,118): " posFilaPil
		read -p "Introduce de nuevo posColPil (2,35): " posColPil
		read -p "Introduce de nuevo velFil (-1.0-1.0): " velFil
		read -p "Introduce de nuevo velCol (-1.0-1.0): " velCol
	fi
}
function printVariables
{
	
	echo ""
	echo "VALORES DE LAS VARIABLES:"
	echo "fils: $fil"
	echo "cols: $cols"
	echo "portSize: $portSize"
	echo "posFilaPal: $posFilaPal"
	echo "posColPal: $posColPal"
	echo "midaPaleta: $midaPaleta"
	echo "posFilaPil: $posFilaPil"
	echo "posColPil: $posColPil"
	echo "velFil: $velFil"
	echo "velCol: $velCol"
}
function comprobarValores
{
	echo "COMPROBAR VALORES"
	if [ -z $file ] ; then
		read -p "Introdueix el nom del fitxer: " file
	fi
	if [ $fil -lt $minFil ] || [ $fil -gt $maxFil ] ; then
		read -p "Files incorrectes, torna a provar (10-120): " fil
	fi

	if [ $cols -lt $minCol ] || [ $cols -gt $maxCol ] ; then
		read -p "Columnes incorrectes, torna a provar (10-36): " cols
	fi
	let maxPort=fil-1
	if [ $portSize -lt $minPort ] || [ $portSize -gt $maxPort ] ; then
		read -p "Porteria incorrecta, torna a provar (8-numFiles-1): " portSize
	fi
	if [ $posFilaPal -lt 2 ] || [ $posFilaPal -gt 118 ] ; then
		read -p "posFilaPal incorrecta, torna a provar (2-118): " posFilaPal
	fi
	if [ $posColPal -lt 2 ] || [ $posColPal -gt 35 ] ; then
		read -p "posColPal incorrecta, torna a provar (2-35): " posColPal
	fi
	if [ $midaPaleta -lt 3 ] || [ $midaPaleta -gt $maxPort ] ; then
		read -p "Mida paleta incorrecta, torna a provar (3-numFil-1): " midaPaleta
	fi
	if [ $posFilaPil -lt 2 ] || [ $posFilaPil -gt 118 ] ; then
		read -p "posFilaPil incorrecta, torna a provar (2-118): " posFilaPil
	fi
	if [ $posColPil -lt 2 ] || [ $posColPil -gt 35 ] ; then
		read -p "posColPil incorrecta, torna a provar (2-35): " posColPil
	fi
	
	if (( $(echo "${velFil} > 1.0 || ${velFil} < -1.0" | bc -l ) )) ; then
		read -p "velFil incorrecta,  torna a provar (-1, 1): " velFil
	fi
	if (( $(echo "${velCol} > 1.0 || ${velCol} < -1.0" | bc -l ) )) ; then
		read -p "velCol incorrecta, torna a provar (-1, 1): " velCol
	fi
}

function comprobarfichero
{
	echo "COMPROBAR FICHERO"

	carlos='carlos'
	#file='/home/milax/Documents/GitHub/FSOPrac1/params.txt'
	#file='/home/milax/FSOPrac1/params.txt'

	if [ -f $file ] && [ -e $file ]
	then
		num=0
		while read line; do
		if [ $num -eq 0 ]
		then
			fil=`echo $line | cut -d' ' -f1`
			echo "$fil"
			cols=`echo $line | cut -d' ' -f2`
			echo "$cols"
			portSize=`echo $line | cut -d' ' -f3`
			echo "$portSize"
		elif [ $num -eq 1 ]
		then
			posFilaPal=`echo $line | cut -d' ' -f1`
			echo "$posFilaPal"
			posColPal=`echo $line | cut -d' ' -f2`
			echo "$posColPal"
			midaPaleta=`echo $line | cut -d' ' -f3`
			echo "$midaPaleta"

		elif [ $num -eq 2 ] 
        then
            posFilaPil=`echo $line | cut -d' ' -f1`
            echo "$posFilaPil"
            posColPil=`echo $line | cut -d' ' -f2`
            echo "$posColPil"
            velFil=`echo $line | cut -d' ' -f3`
            echo "$velFil"
            velCol=`echo $line | cut -d' ' -f4`
            echo "$velCol"


		elif [ $num -eq 3 ] && [ ! -z "$line" ]
		then
			extraPilotes='true'
			posFilaPil=`echo $line | cut -d' ' -f1`
            echo "$posFilaPil"
			
            posColPil=`echo $line | cut -d' ' -f2`
            echo "$posColPil"
            velFil=`echo $line | cut -d' ' -f3`
            echo "$velFil"
            velCol=`echo $line | cut -d' ' -f4`
            echo "$velCol"
		fi
    	let num=num+1

		
		found='true'
		done < $file
		let maxPort=$fil-1
		
	else
		echo "No existe el archivo $file, procedemos a crearlo"
		touch $file	#si no existe el fichero lo creamos

	fi
}


function readFromKeyboard
{
	echo "READ FROM KEYBOARD"
	if [ -z $Nflag ] ; then

		read -p "Introduce el nombre del archivo que quieres usar: " file
	fi
	
#FILAS
	if [ -z $Fflag ] ; then
		read -p "Introduce el numero de filas: " fil
	fi
		let maxPort=fil-1
		#rows output
		truncate -s-1 file
		#echo -n "$fil " > $file
#COLUMNAS
	if [ -z $Cflag ] ; then
		read -p "Introduce el numero de columnas: " cols
	fi
		#columns output//lo guardamos en el fichero $file
		truncate -s-1 file
		#echo -n "$cols " >> $file

#PORTERIA
	if [ -z $Pflag ] ; then
		read -p "Introduce la medida de la porteria: " portSize
	fi
		#output porteria// lo guardamos en el fichero $file
		truncate -s-1 file
		
		#echo -n "$portSize" >> $file
		comprobarValores
}
	
	
echo "BIENVENIDO/A AL PROGRAMA"
#primero de todo comprobamos que el fichero deseado existe
#si el fichero existe debemos comprobar que todos los parametros estan en regla
	#readFile
#en caso contrario pediremos los parametros que faltan porteclado al usuario
	#readFromKeyboard


while getopts 'n:f:c:p:m:0:1:' opcio; do
	case "${opcio}" in
		n) echo "Option n has been chosen" ;Nflag='true';file="${OPTARG}";;
		f) echo "Option f has been chosen";Fflag='true';fil=${OPTARG};;
		c) echo "Option c has been chosen";Cflag='true';cols=${OPTARG};;
		p) echo "Option p has been chosen";portSize=${OPTARG};Pflag='true';;
		m) echo "Option m has been chosen";midaPaleta=${OPTARG};MFlag='true';;
		0)IFS=',';read -a strarr <<< "${OPTARG}";posFilaPal=${strarr[0]};posColPal=${strarr[1]};OFlag='true';;
		1) echo ${OPTARG};IFS=',';read -a split <<< "${OPTARG}";posFilaPil=${split[0]};
			posColPil=${split[1]};velFil=${split[2]};velCol=${split[3]};OneFlag='true';;
		#*) error "Unexpected option ${opcio}" ;;
	esac
done

shift $(($OPTIND - 1))
echo "***********************************************"
printf "encara ens falta tractar els següents elements: %s\n$* \n"
echo "***********************************************";echo""
comprobarfichero
comprobarValores
printVariables
introducirRestantes
writeFile
IFS=',';read -a separar <<< "$1";
if [ ${#distro[@]} -eq 3 ] ; then
	echo "${separar[0]} ${separar[1]} ${separar[2]} ${separar[3]}" >$file
fi

#readFromKeyboard




