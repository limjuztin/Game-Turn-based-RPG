# Changelog

## [v0.2.0] - 2026-11-26

Pembaruan prototipe sistem karakter dan pertarungan.

### Ditambahkan
- Kelas abstrak `combatant` sebagai dasar bersama untuk `character` dan `boss`.
- Penerimaan damage yang memperhitungkan defense dan pengecekan apakah combatant masih hidup.
- Fitur heal dan tampilan status pada `character`.
- Basic attack dan skill fireball pada `boss`.
- Pemulihan 15 mana setelah basic attack, dibatasi agar mana tidak melebihi maksimum menggunakan `min()`.

### Catatan
- Fitur heal saat ini hanya tersedia untuk `character`, bukan `boss`.
- Proyek masih berupa prototipe dan battle engine belum disertakan.
