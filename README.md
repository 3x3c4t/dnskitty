# DNSKITTY 
**dnskitty** is a simple Windows-only Python tool that lets you quickly change your system DNS servers using `netsh`.

It provides a terminal interface with a cat-themed ASCII design, a list of DNS providers, and basic input handling.

---

## features

* windows only (uses `netsh`)
* admin permission detection
* multiple dns providers built-in
* easy selection menu
* automatic dns apply to all network interfaces
* clean console interface with colors
* invalid input handling with retry loop
* ascii cat theme

---

## requirements

* windows 10 / 11
* python 3.8+
* run as administrator (required)

---

## how to use

1. open a terminal as administrator
2. run the script:

```bash
python main.py
```

3. choose a dns provider from the list
4. the script automatically applies dns settings to all active interfaces

---

## how it works

dnskitty uses windows built-in `netsh interface ip` commands to:

* detect network interfaces
* set primary dns server
* add secondary dns server

example commands used internally:

```bash
netsh interface ip set dns name="interface" static 8.8.8.8
netsh interface ip add dns name="interface" 8.8.4.4 index=2
```

---

## dns providers included

* google
* cloudflare
* quad9
* opendns
* adguard
* cleanbrowsing
* comodo
* verisign
* alternate dns
* controld
* level3
* yandex
* dnswatch
* safe dns
* neustar
* freedns
* uncensored dns
* puntcat

---


## warnings

* you must run as administrator or it will not work
* changing dns affects all internet traffic on the system
* use trusted dns providers only

---

## file structure

```
main.py      # main script
README.md    # this file
```

---

## notes

this tool is made for learning, testing dns providers, and quick switching on windows systems.

 /\_/\\
 ( o.o )
  > ^ <
