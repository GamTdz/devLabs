# devLabs
## Lab1
1. Створив репозиторій на github. На локальному ПК змінив *README.md*, та закомітив його до репозиторію.
```console
gamt@DESKTOP-DNK8VI1:/mnt/f/devLabs$ echo "# devLabs" >> lab1/README.md
gamt@DESKTOP-DNK8VI1:/mnt/f/devLabs$ git init
Initialized empty Git repository in /mnt/f/devLabs/.git/
gamt@DESKTOP-DNK8VI1:/mnt/f/devLabs$ git add lab1/README.md
gamt@DESKTOP-DNK8VI1:/mnt/f/devLabs$ git commit -m "Lab 1: first commit"
[master (root-commit) a3f5819] Lab 1: first commit
 1 file changed, 1 insertion(+)
 create mode 100644 lab1/README.md
gamt@DESKTOP-DNK8VI1:/mnt/f/devLabs$ git remote add origin https://github.com/GamTdz/devLabs.git
gamt@DESKTOP-DNK8VI1:/mnt/f/devLabs$ git push -u origin master
```
2. Переглянув під яким хешем був створений попередній коміт.
```console
gamt@DESKTOP-DNK8VI1:/mnt/f/devLabs$ git log
commit a3f58198163566a57d318eae1b4228e79b42982d (HEAD -> master, origin/master)
Author: Yakovlev Dmitry <gamtdz@gmail.com>
Date:   Sun Nov 10 19:06:55 2019 +0200

    Lab 1: first commit
```
3. За допомогою команди `git checkout -b second_bransch` створив нову гілку і переключився на неї.
4. Створив та виконав pull request на злиття (merge).
5. Зробив зміни в веб версії, та ввів команду `git pull`, щоб побачити зміни на ПК.
![image](https://github.com/GamTdz/devLabs/blob/master/lab1/github.gif "image")
