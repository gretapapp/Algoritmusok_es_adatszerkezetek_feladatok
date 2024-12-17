# Magyarázat:

### UnionFind osztály:
Ez az osztály megvalósítja az Union-Find adatstruktúrát útkompresszióval és méret szerinti egyesítéssel.

- ### find metódus:
Ez a metódus megtalálja annak a komponensnek az útját, amelyhez egy város tartozik, útkompresszióval a jövőbeli lekérdezések felgyorsítása érdekében.

- ### union metódus:
Ez a metódus egyesíti két város komponenseit, és frissíti a komponensek számát és a legnagyobb komponens méretét.

### Bemenet/Kimenet:
Beolvassa a bemenetet, inicializálja az Union-Find struktúrát, feldolgozza az egyes új utakat, és minden nap után kiírja a szükséges információkat.