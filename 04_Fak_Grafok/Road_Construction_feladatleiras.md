# Feladatleírás

Forrás: https://cses.fi/problemset/task/1676/

Van $n$ város, és kezdetben nincs köztük út. Azonban minden nap egy új út épül, és összesen $m$ út lesz.
Egy komponens olyan városok csoportja, ahol bármely két város között van út használva az útvonalakat. Minden eltelt nap után a feladatod az, hogy meghatározd a komponensek számát és a legnagyobb komponens méretét.

## Bemenet
Az első bemeneti sor két egész számot tartalmaz $n$ és $m$ : a városok és utak számát. <br> 
A városok számozása $1,2,\dots,n$.
Ezután $m$ sor következik, amelyek az új utakat írják le. Minden sor két egész számot tartalmaz, $a$ és $b$ : egy új út épül $a$ és $b$ városok között.
Feltételezheted, hogy minden út két különböző város között épül.

## Kimenet
Írass ki $m$ sort: a szükséges információkat minden nap után.

## Feltételek

- $1 \le n \le 10^5$ <br>
- $1 \le m \le 2 \cdot 10^5$ <br>
- $1 \le a,b \le n$

## Példa
### Bemenet:
5 3 <br>
1 2 <br>
1 3 <br>
4 5 <br>

### Kimenet:
4 2 <br>
3 3 <br>
2 3 <br>