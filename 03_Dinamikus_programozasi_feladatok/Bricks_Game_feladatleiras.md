# Játék leírása

Te és a barátod úgy döntötök, hogy egy játékot játszotok egy `N` téglából álló halommal. Ebben a játékban felváltva eltávolíthattok 1, 2 vagy 3 téglát a tetejéről, és az eltávolított téglákra vésett számok hozzáadódnak a pontszámodhoz. Úgy kell játszanod, hogy a lehető legmagasabb pontszámot érd el. <br>
Adott, hogy a barátod is optimálisan fog játszani, és te teszed meg az első lépést.

Például a téglák számozása $arr=[1,2,3,4,5]$. <br>
Eltávolíthatsz $[1]=1$, $[1,2]=3$ vagy $[1,2,3]=6$ téglát. A barátod a te lépéseid után $1$ és $3$ elemek közül választhat $[2,3,4]=9$-ből, így neked marad $5$ (összpontszám $=6$). <br> 
$[3,4,5=12]$ vagy $[4,5=9]$. Ebben az esetben soha nem lesz optimális a barátod számára, hogy kevesebb elemet vegyen el, mint amennyi elérhető. <br>
A maximális lehetséges pontszámod $6$, amely kétféleképpen érhető el: $1$ első lépés és $5$ a második, vagy $[1,2,3]$ az első lépésben.

## Függvény leírása

Egészítsd ki a `bricksGame` függvényt. <br>
Egy egész számot kell visszaadnia, ami a maximális lehetséges pontszámodat jelenti.

A `bricksGame` függvénynek a következő paramétere(i) vannak:

- `arr`: egy egész számokat tartalmazó tömb

## Bemenet

Az első sor egy $t$ egész számot tartalmaz, a tesztesetek számát.

A következő $t$ páros sorok a következő formátumban vannak:
- Az első sor egy $n$ egész számot tartalmaz, a téglák számát $arr$ -ban.
- A következő sor $n$ szóközzel elválasztott egész számot tartalmaz, `arr[i]`.

## Korlátozások

- $1 \leq t \leq 10$
- $1 \leq n \leq 10^5$
- $0 \leq arr[i] \leq 10^9$

## Kimenet

Minden tesztesethez írass ki egy sort, amely a maximális pontszámodat tartalmazza.

## Minta bemenet
2 <br>
5 <br>
999 1 1 1 0 <br>
5 <br>
0 1 1 1 999

## Minta kimenet
1001 <br> 
999

## Magyarázat

Az első tesztesetben `999, 1, 1` téglát fogsz választani. Ha bármilyen más módon játszol, nem éred el az `1001` pontot.
A második esetben a legjobb lehetőség az első tégla (0 ponttal) felvétele. Ezután a barátod választja a következő három téglát, és neked marad az utolsó tégla.