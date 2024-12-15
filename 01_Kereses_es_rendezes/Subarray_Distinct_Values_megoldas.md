# Megoldás
(Sliding Window)
### **Bemenet:**
Az első bemeneti sor két egész számot tartalmaz: $n$ és $k$. <br>
A következő sor n egész számot tartalmaz: $ x_1, x_2, \dots, x_n$: a tömb elemei.
### **Inicializálás:** 
Inicializáljuk a bal pointert 0-ra, a számlálót 0-ra, a freq ditionary-t az előfordulások számolására, és a distinct_count-ot a különböző elemek számának nyomon követésére.

### **Iteráció:**
Végig iterálunk a tömbön a jobb pointerrel, frissítve az aktuális elem gyakoriságát és a különböző elemek számát.
### **Mozgatás:**
Ha a különböző elemek száma meghaladja a k-t, mozgassuk a bal pointer a méret csökkentése érdekében, amíg a különböző elemek száma legfeljebb k lesz.
### **Részhalmazok számlálása:** 
A jobb pointer minden pozíciójánál adjuk hozzá az adott pozíción végződő érvényes részhalmazok számát az összesített számlálóhoz.
### **Kimenet:** 
Kiíratjuk a legfeljebb k különböző értéket tartalmazó részhalmazok összesített számát.
