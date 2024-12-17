# Feladatleírás

**Forrás:** https://www.spoj.com/problems/HORRIBLE/

# HORRIBLE - Horrible Queries

A világ egyre gonoszabbá válik, és egyre nehezebb bekerülni a Gonoszok Ligájába. Mivel a legendás Bad Horse visszavonult, most helyesen kell megválaszolnod Dr. Horrible gonosz kérdéseit, aki PhD fokozattal rendelkezik a gonoszság terén (de nem a számítástechnikában). <br>
Egy **N** elemű tömböt kapsz, amely kezdetben csak 0 -kat tartalmaz. Ezután **C** parancsot kapsz. <br>
Ezek a következők:

***0 p q v**- hozzá kell adnod **v** értéket az összes számhoz a **p** és **q** tartományban (beleértve p és q), ahol **p** és **q** a tömb két indexe.

***1 p q** - egy sort kell kiírnod, amely egyetlen egész számot tartalmaz, ami a **p** és **q** közötti összes tömb elem összegét jelenti (beleértvep és q)

## Bemenet
Az első sorban megkapod **T** -t, a tesztesetek számát.

Minden teszteset **N** -nel ( **N** <= 100 000) és **C** -vel ( **C** <= 100 000) kezdődik. Ezután **C** parancsot kapsz a fent említett formátumban. 1 <= **p** , **q** <= **N** és 1 <= **v** <= $10^7$ .

## Kimenet
Írassuk ki a lekérdezések válaszait.

## Példa
### Bemenet:
1 <br> 8 6 <br> 0 2 4 26 <br> 0 4 8 80 <br> 0 4 5 20 <br> 1 8 8 <br> 0 5 7 14 <br> 1 4 8
### Kimenet:
80 <br> 508