Ćwiczenia do POM
Istalacja samego PIP to -> $ sudo apt install python3-pip
instalacja virtualenvwrapper ->  $sudo pip3 install virtualenvwrapper
tworzysz folder $mkdir ~/Envs
no i dodajesz linijki w .bashrc na końcu najlepiej:
	WORKON_HOME=~/Envs
	VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
	. /usr/local/bin/virtualenvwrapper.sh
Instrukcja dostępna na: https://dev.to/jsgurugit/how-to-setup-python-virtual-environment-for-python3-on-ubuntu-19-10-dkp
$ mkvirtualenv myproject -> no i wiadomo, to juz tworzysz sobie srodowisko
po za tym workon i deactivate

$pip install -r requirements.txt -> instalacja requirements z pliku

