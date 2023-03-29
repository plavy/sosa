# Pokretanje aplikacije

1. Izgraditi maven paket. U IntelliJ Idea moguće je otvoriti padajući izbornik na datoteci `pom.xml` te odabrati Maven > Reload project.
2. Postaviti konfiguraciju za pokretanje. Postaviti `hr.fer.lab1.Lab1Application` za glavnu klasu te JDK 18 ili više.
3. Izgraditi projekt iz Idea IDE-a.
4. Zavrtiti projekt iz Idea IDE-a.

# Postavljanje Keycloaka

Keycloak je open-source SSO alat za upravljanje identitetom.

Može se preuzeti ovdje: https://www.keycloak.org/downloads

## Pokretanje

```bash
keycloak-21.0.1/bin/kc.sh start-dev
```

## Postavljanje

Prvo je potrebno postaviti lozinku za administratora instance.

Cilj je kreirati vlastite korisnike koji će pristupiti našoj aplikaciji.

Prvo ćemo kreirati novi realm.
To je prostor koji sadrži logički povezane resurse.
Potrebno je klinuti na trenutni realm `master` te kreirati novi.
Nazvat ćemo ga `springboot`.

Zatim ćemo kreirati novi klijent. Njega ćemo nazvati `lab1`.
On predstavlja našu aplikaciju.
Dovoljno je ostaviti zadane postavke i postaviti samo `valid redirect URI`.
To je URI na koji nas Keycloak smije vratiti nakon logina.
Postavit ćemo ga na adrese aplikacije: `http://localhost:8000/*`.

Zatim ćemo kreirati realm role. To su role vidljive na cijelom realmu, ukljućujući sve klijente.
Neka se role zovu `admin` i `user`.

Konačno, kreirat ćemo 2 korisnika.
Svakom korisniku treba dati ime, a nakon toga postaviti lozinku (pod `Credentials`).
Zbog lakoće, postavit ćemo ne-privremenu lozinku.
Neka se korisnici zovu `user1` i `admin1`, a lozinke neka budu iste kao i korisnikovo ime.

Korisnicima trebamo pridružiti role. Pod `Role mapping` dodat ćemo rolu `admin` za `admin1` te rolu `user` za `user1`.

Keycloak je sada postavljen.
Izvještaj o aplikaciji i demontracija nalaze se [ovdje](IZVJESTAJ.md).