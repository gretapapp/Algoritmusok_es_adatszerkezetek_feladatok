# Megoldás

## 1. Mátrixszorzás (matrix_mult függvény)
- Ezzel a függvénnyel két, adott méretű mátrixot (A és B) szorzunk össze, a függvény az eredményt $10^9$-dal modulozva adja vissza.
- Egy nullákkal feltöltött eredménymátrixot inicializálunk.
- Három for-in ciklussal végezzük a mátrixszorzást, és az eredményt $10^9$-dal modulozva vesszük.

## 2. Mátrix hatványozás (matrix_pow függvény)
- Kiszámoljuk a mátrix hatványát négyzetre emeléses hatványozással. 
- Az eredményt egységmátrixként inicializáljuk. 
- Iteratívan szorozzuk a bázismátrixot és négyzetre emeljük, miközben a hatványt felére csökkentjük, míg a hatvány nulla nem lesz.

## 3. $a_n$ kiszámítása (compute_an függvény)
- Ezzel a függvénnyel a sorozat $n$-edik elemét számoljuk ki a transzformációs mátrix és a kezdeti értékek felhasználásával. 
- Ha $n$ az első $k$ elem között van, akkor közvetlenül visszaadjuk a kezdeti sorozat $b$ megfelelő értékét. 
- Inicializáljuk a mátrixot $T$ a $c$ együtthatók alapján. 
- Kiszámítjuk a $T$ mátrixot $n-k$ hatványra emelve a matrix_pow függvénnyel. 
- Kiszámítjuk az $n$-edik elemet az eredménymátrix első sorának és a kezdeti értékek $b$ szorzatával, és az eredményt itt is $10^9$-dal modulozva veszük.

## 4. Bemenet/Kimenet kezelése
- Beolvassuk a tesztesetek számát. 
- Minden tesztesethez beolvasva a $k$, $b$, $c$ és $n$ értékeket. 
- Kiszámítjuk az $n$-edik elemet minden tesztesethez, és eltároljuk az eredményeket. 
- Végül kiíratjuk az összes teszteset eredményét.