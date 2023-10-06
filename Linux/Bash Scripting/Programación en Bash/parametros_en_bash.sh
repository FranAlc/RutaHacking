#! /bin/bash
# Se pide ingresar un valor y al ingresarlo lo muestra por consola.
echo "Introduce tu nombre:"
read nombre
echo "Tu nombre es: $nombre"


# --------------Condicionales--------------
echo "Introduce tu edad:"
read age

# 1ra forma
if [ $age -eq 20 ]
then # Que es lo que quiero ejecutar si se cumple esta condicion
    echo "Tu edad es igual a 20" 
else # caso contrario
    echo "Tu edad no es igual a 20"    
fi

# -eq igual
# -ge mayor o igual
# -le menor o igual

# 2da forma
if (($age >= 18)) # Se utiliza doble paréntesis
then 
    echo "Eres mayor de edad" # opcion 1
else
    echo "Eres menor de edad" # opcion 2
fi        

# 3ra forma
if (($age >= 18))
then 
    echo "Eres un adulto" # opción 1
elif (($age >= 14))
then
    echo "Eres un adolescente" # opción 2
else
    echo "Eres un niño" # opción 3
fi

# --------------Operador Lógico--------------

# 18 < age < 40
# if ((18 < age ||/&& age < 40))
# AND / OR