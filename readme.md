# Turn-Based RPG (OOP Rework)

Halo semuanya, kembali lagi bersama `limjuztin` di sini.

Kali ini saya sedang membangun sebuah projek kreatif berupa **Turn-Based RPG** di mana pemain dapat bertarung menggunakan *basic attack*, *skill*, dan *inventory* berhadapan dengan seorang *boss* yang kuat. Perlu diperhatikan bahwa program ini dikembangkan secara bertahap (*work in progress*) dan mungkin membutuhkan waktu untuk menyelesaikannya.

## Tujuan Pembangunan Projek
- Melatih pemrograman terutama pada penerapan prinsip **OOP** (*Object-Oriented Programming*).
- Melatih logika game serta memperhatikan alur proses data.
- Me-*rework* projek serupa dari masa lalu yang sebelumnya ditulis secara prosedural menjadi struktur OOP.
- Menjadi inspirasi bagi pembaca untuk membuat dan mengembangkan program sendiri.

## Rencana Mode Permainan
*(Tersedia bertahap selama pengembangan berlangsung)*
- **Solo vs Boss**
- **Solo vs Solo** (antarkelas karakter)
- **Party vs Boss**
- **Story Mode**

## Rencana Struktur File
*(Dapat bertambah atau berkurang seiring jalannya pengembangan)*
- `models.py` — definisi kelas entitas karakter, *boss*, *skill*, dan item.
- `engine_solo.py` — logika *battle engine* untuk mode *Solo vs Boss* dan *Solo vs Solo*.
- `engine_party.py` — logika *battle engine* untuk mode *Party vs Boss*.
- `story.py` — alur narasi dan tahapan *Story Mode*.

## Alur Permainan Secara Singkat
1. *Engine* menentukan giliran siapa yang maju berdasarkan stat *speed* dan urutan giliran.
2. Pemain dapat memilih aksi menyerang menggunakan *basic attack*, *skill*, atau menggunakan *inventory*.
3. Lawan akan melakukan serangan ke pihak pemain secara acak (*random*).
4. Pertarungan terus berlanjut hingga salah satu pihak kehabisan *HP* / nyawa.
5. Permainan selesai, dan pihak yang bertahan hingga akhir dinyatakan sebagai pemenang.

## Catatan Pengembangan
- **Peran AI:** AI digunakan sebagai penguji dan penasihat teknis selama proses, sementara konsep utama dan draf awal tetap dipegang oleh *programmer*.
- **Bahasa Kode:** Implementasi kode program menggunakan bahasa Inggris.
- **Status Kualitas:** Program ini belum 100% sempurna dan masih terus disempurnakan secara bertahap.

---

Terima kasih sudah mampir dan membaca. Silakan jika terdapat kritik maupun saran.