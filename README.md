# test_python

##### https://docs.pytest.org/en/latest/getting-started.html
Usar pytest para ejecutar desde la terminal y ejecutar todos los de test con el patron 'test_\*.py' o '\*\_test.py'

Instalarlo, en entornor virtual no se usa sudo
```
$ sudo pip install -U pytest
```

Dependiendo de que versiones de python se tenga instaladas y a que version de python este apuntando pip, el pytest usara la version de python a la cual pip este apuntando
Primero verificar a donde esta apuntando pip
```
$ pip --version
```

Si el pip este apuntando a python3 y los test se quieran usar con python2
instalar pip con python2 o veriricar las versiones de pip instaladas

Obtener la ruta donde se encuentra instalado pip
```
$ which -a pip
```

Luego verificar las versiones de los pip instalados
```
$ ls -l /usr/local/bin/ | grep pip
```

Si se encuentra un pip2 verificar su versiones y se comprueba que apunta a python2
```
$ pip2 --version
```

Luego instalar pytest para python2
Instalarlo, en entornor virtual no se usa sudo
```
$ sudo pip2 install -U pytest
```




Ejecutar pytest, ubicarse en la raiz donde estan los archivos tests de python
```
$ pytest
```




##### http://stackoverflow.com/questions/40718770/pytest-running-with-another-version-of-python
Si ya se encuentra pytest instalado apuntando a python2 y se quiere usar pytest para python3
Primero comprobar si se tiene instalado pytest para python3
```
$ pip freeze | grep pytest
$ pip3 freeze | grep pytest
```

Si no se encuentra instalarlo
Usar pytest apuntando a python2 para tests en python3
```
$ python3 -m pytest
```
