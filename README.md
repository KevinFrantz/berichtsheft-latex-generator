# Berichtsheft LATEX Generator #
Dieses Repository stellt ein tool zur Verfügung, welches Git-Logs eines bestimmten Nutzers in LATEX-Berichtsheft-Dokumente umwandelt.

## Installation ##
Vor der Verwendung dieser Software ist es notwendig die setup.sh auszuführen.

Dies geschieht in der Konsole mit:

```
sudo ./setup.sh
```

Die setup.sh ist allerdings lediglich für Ubuntu optimiert.

## Bedienung ##

### Parameterübergabe via Konsole ###
```
python3 cli.py git-repositorypfad git-nutzername vorname nachname
```

### CLI Interface ###
```
python3 cli.py
```

## Lizenz ##
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Dieses Werk von [Kevin Frantz](http://kevin-frantz.de/) ist lizenziert unter einer <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz</a>.
