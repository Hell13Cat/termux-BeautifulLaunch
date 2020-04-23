










# termux-BeautifulLaunch
Красивый запуск при старте Termux

* [Как установить?](#Install)
* [Требования](#Requirements)
* [Скачать](https://github.com/Hell13Cat/termux-BeautifulLaunch/releases)

![Скриншот](https://i.imgur.com/6EMU7do.png)

## <a name="Requirements"></a> Требования

* Python 3.7 и выше

## <a name="Install"></a> Как установить?

* Установить Python 3

    pkg install python

* Скачать файлы "termux-br.sh", "termux-br.py", "termux-br.cfg" и поместить в одну папку

* Выполнить две команды

    echo "cd [ПОЛНЫЙ ПУТЬ ДО ПАПКИ С ФАЙЛАМИ]" >> "/data/data/com.termux/files/usr/etc/bash.bashrc"

    echo "bash termux-br.sh" >> "/data/data/com.termux/files/usr/etc/bash.bashrc"

* Отредактировать файл "termux-br.cfg" заменив

[FLASH] на "yes" если у вас есть флешка

[ROOT FLASH]  на полный путь к корневой папке флешки если она есть

[ROOT PHONE] на полный путь к корневой папке телефона