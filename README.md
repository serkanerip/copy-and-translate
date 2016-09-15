## What does this application do ? 
This application is doing fast translation with keyboard shortcuts.
## Which os do you support ? 
Just only linux, windows and mac os is coming soon.
## How does it work ?
This app gets current copied text from the system clipboard and then translates the text via yandex-api and shows translation like a notification.Immediately after translation, clipboard (original text) value is changed with translated text so you can do control + V to paste it. By using this application you do not need to open new web pages and copy paste around.

## Requirements
  * Linux
  * Git
  * Python 3
  * Xsel or Xclip clipboard package

## Getting started

### Before Build
If you don't have requirements prepared, install it.

```
sudo apt-get install xsel or sudo apt-get install xclip
sudo apt-get install git
sudo apt-get install python3
```
### Github Config

```
git config --global user.name "username"
git config --global user.email example@email.com
```

### Installing Application

```
git clone git@github.com:serkanerip/copy-and-translate.git
sudo mv copy-and-translate /usr/share/

```

### Adding Keyboard Shortcut

```
Go system settings and open keyboard shortcuts
Add a custom shortcut
Set the command of shortcut :
 * python3 '/usr/share/copy-and-translate/copy-translate.py'
And set your keyboard shortcut
```

![alt-tag](http://oi68.tinypic.com/2hh2n37.png)

### Some Examples

![alt tag](http://oi67.tinypic.com/23vjdw5.jpg)

![alt-tag](http://oi68.tinypic.com/20541g5.png)

![alt-tag](http://oi67.tinypic.com/24eosvr.jpg)



