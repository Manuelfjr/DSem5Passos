# Passo a passo para usar o text to speech

## Passo 1:
Vamos criar um env (enviroment, ou ambiente para trabalharmos e não "cansar" sua máquina), vamos baixar o virtualenv da seguinte forma :
```
pip install virtualenv
```

## Passo 2:
Vamos criar o ambiente virtual da seguinte forma (escolha um nome):
```
virtualenv <NOME DO AMBIENTE> 

Ex: 
	virtualenv ambientepy
```

## Passo 3:
Vamos ativar esse ambiente :

* **LINUX**
```
source <NOME DO AMBIENTE>/bin/activate

Ex: 
	source ambientepy/bin/activate
```

* **MANJARO**
```
<NOME DO AMBIENTE>\Scripts\activate.bat

Ex:
	ambientepy\Scripts\activate.bat
```

## Passo 4:
Dado que estamos com o ambiente ativado, vamos instalar os nossos requirements desse projeto. O arquivo requirements.txt é muito comum em um projeto que precisa rodar em outros tipos de sistema operacionais, nele contem todas os modulo necessarios para rodar o código. Vamos instala-lo:
```
pip install -r requirements.txt
```
* **Obs.:** Para criarmos um requirements do nosso projeto, basta rodarmos :
```
pip freeze > <NOME>.txt

Ex:
	pip freeze > requirements.txt
```

## Passo 5
Para desativarmos o ambiente, e voltarmos ao padrão, rode o seguinte:
```
deactivate
```

© [manuelfjr.github.io](https://manuelfjr.github.io/)
