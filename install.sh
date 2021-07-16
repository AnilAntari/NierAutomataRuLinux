#!/usr/bin/env bash

[ -x "$(command -v bsdtar)" ] && TAR="bsdtar" || TAR="tar"

echo '
--------------------------
|                        |
|                        |
| Nier Automata Ru Linux |
|                        |
|                        |
--------------------------
'

VER="1.1"

LINK="https://github.com/AnilAntari/NierAutomataRuLinux/releases/download/$VER/generic.tar.gz"
GAMEPATH="$HOME/.local/share/Steam/steamapps/common/NieRAutomata"

[ -d "$GAMEPATH" ] && {
	echo "Игра была найдена в ${GAMEPATH}"
} || {
	read -rp "Игра не была найдена в $GAMEPATH, укажите путь к игре: " GAMEPATH
	[ -d "$GAMEPATH" ] || { echo "Игра не была найдена в $GAMEPATH, выход " ; exit 1 ; }
}

echo "Загрузка"
wget "$LINK"

$TAR -xzvf generic.tar.gz && cp -r generic/data/* "$GAMEPATH/data"

rm -r generic && rm generic.tar.gz

echo "Готово"
