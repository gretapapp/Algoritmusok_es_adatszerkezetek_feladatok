# Feladatleírás
**Forrás:** https://www.spoj.com/problems/SEQ/

A természetes számok $a_i$ sorozata a következőképpen van definiálva:

$a_i = b_i \quad (i \leq k)$
$a_i = c_1 a_{i-1} + c_2 a_{i-2} + \ldots + c_k a_{i-k} \quad (i > k)$

ahol $b_j$ és $c_j$ adott természetes számok $1 \leq j \leq k$. <br>
A feladatod, hogy kiszámold $a_n$-t adott $n$-re, és az eredményt $10^9$-dal modulozva add meg.

## Bemenet

Az első sorban a tesztesetek száma $C$ található (kb. 1000).

Minden teszteset négy sort tartalmaz:

- $k$ - az elemek száma a $c$ és $b$ sorozatokban $(1 ≤ k ≤ 10)$
- $b_1, \ldots, b_k$ - $k$ természetes szám, ahol $0 \leq b_j \leq 10^9$, szóközzel elválasztva
- $c_1, \ldots, c_k$ - $k$ természetes szám, ahol $0 \leq c_j \leq 10^9$, szóközzel elválasztva
- $n$ - természetes szám $(1 ≤ n ≤ 10^9)$

## Kimenet

Pontosan $C$ sor, minden tesztesethez egy: $a_n$ modulo $10^9$.

## Példa

### Bemenet:
3 <br>
3 <br>
5 8 2 <br>
32 54 6 <br>
2 <br>
3 <br>
1 2 3 <br>
4 5 6 <br>
6 <br>
3 <br>
24 354 6 <br>
56 57 465 <br>
98765432 <br>

### Kimenet:
8 <br>
714 <br>
257599514