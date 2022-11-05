
## Persimpangan
                 J2  J1
               | ^      |
               | |    | |
               |      v |
               |        |
       --------+     T1 +--------
    J3   -->  T2             --> J8
    J4  <--             T4  <--  J7
       --------+ T3     +--------
               |        |
               | ^      |
               | |    | |
               |      v |
                 J5  J6

## Pseudocode
```
# Keterangan:
0 = merah
1 = kuning
2 = hijau

Tn= lampu lalin, n = [1,4]
Jm = ruas jalan, m = [1,8]

if T1 == 2:
  T2, T3, T4 == 0
  J3, J5, J7 berhenti

if T2 == 2:
  T1, T3, T4 == 0
  J1, J5, J7 berhenti

if T3 == 2:
  T1, T2, T4 == 0
  J1, J3, J7 berhenti

if T4 == 2:
  T1, T2, T3 == 0
  J1, J3, J5 berhenti

  
```

## Psedocode Pola
```
if Tn+1 == 2:
  Jm+1 jalan
  Jm, Jm, Jm berhenti
```
