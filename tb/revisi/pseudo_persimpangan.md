
### Persimpangan
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

# Pseudocode
```
# Keterangan:
0 = merah
1 = kuning
2 = hijau

Tn= lampu lalin, n = [1,4]
Jm = ruas jalan, m = [1,8]

if T1 == 2:
  J1 jalan
  J2, J3, J4 berhenti

if T2 == 2:
  J2 jalan
  J1, J3, J4 berhenti
  
if T3 == 2:
  J3 jalan
  J1, J2, J4 berhenti

if T4 == 2:
  J4 jalan
  J1, J2, J3 berhenti
```

# Psedocode Pola
```
if Tn+1 == 2:
  Jm+1 jalan
  Jm, Jm, Jm berhenti
```
