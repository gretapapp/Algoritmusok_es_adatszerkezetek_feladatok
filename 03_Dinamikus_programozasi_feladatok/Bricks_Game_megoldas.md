# Magyarázat

## Függvény
A `bricksGame(arr)` függvény egy `arr` tömböt vesz át, mely a téglákat és azok értékeit tartalmazza.

## Alapesetek
- Ha nincs tégla $n == 0$, az eredmény 0.
- Ha egy tégla van $n == 1$, az eredmény a tégla értéke.
- Ha két tégla van $n == 2$, az eredmény a két tégla értékének összege.
- Ha három tégla van $n == 3$, az eredmény mindhárom tégla értékének összege.

## Dinamikus programozás inicializálása
- A `max_scores` egy tömb, ahol a `max_scores[i]` az i-edik téglától a végéig elérhető maximális pontszámot jelenti. 
- Inicializáljuk a `max_scores` utolsó három elemét az utolsó három tégla értékei alapján.

## Maximális pontszám kiszámítása
- a ciklus a negyedik utolsó téglától (n-4) az első tégláig (0) iterál, visszafelé haladva.
- Minden téglára `n-4`-től 0-ig kiszámítjuk a maximális pontszámot, amit 1, 2 vagy 3 tégla elvételével érhetünk el, figyelembe véve barátunk optimális lépéseit. A `min` függvényt hasznájuk a pontszámunk minimalizálására (figyelembe véve az barátunk lépéseit).
- 1 tégla elvétele: arr[i]
Hozzáadjuk a minimális pontszámot, amit barátunk kényszeríthet ránk a maradék téglákból (i+2, i+3, i+4).
- 2 tégla elvétele: arr[i] + arr[i+1]
Hozzáadjuk a minimális pontszámot, amit barátunk kényszeríthet ránk a maradék téglákból (i+3, i+4, i+5).
- 3 tégla elvétele: arr[i] + arr[i+1] + arr[i+2]
Hozzáadjuk a minimális pontszámot, amit barátunk kényszeríthet ránk a maradék téglákból (i+4, i+5, i+6).

## Eredmény
Az egyes tesztesetek eredménye a `max_scores[0]`-ban van tárolva.

## Bemenet és kimenet
- Először a tesztesetek számát tolvassuk be.
- Minden tesztesethez beolvassuk a téglák számát és a téglák értékeit tartalmazó listát.
- Kiíratjuk az egyes tesztesetek eredményét, a maximális pontszámot.