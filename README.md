# Lorong Waktu — 42 Perkemahan

Booth Sejarah Penebusan, AETOS Community Gathering V · Universitas Kristen Maranatha, Bandung · 31 Oktober 2026.

Satu permainan web untuk tiap tempat perkemahan di Bilangan 33, ditambah Yerikho sebagai penutup.
Tidak ada proses build: semuanya HTML + ES module biasa.

## Menjalankan

**Dari web (GitHub Pages).** Buka `index.html` lewat alamat `https://…`. Kamera dan mikrofon jalan
karena https, dan Chrome akan meminta izin sekali untuk alamat itu.

**Dari komputer sendiri (untuk hari acara, tanpa internet).** Jalankan `jalankan.bat`, lalu buka
`http://localhost:8765` di Chrome. Cara ini yang dipakai di booth supaya tidak bergantung pada jaringan.

Kamera dan mikrofon **tidak** jalan kalau berkasnya dibuka langsung sebagai `file:///…`, atau lewat
alamat IP LAN tanpa https.

## Tombol

`SPASI` mulai / lanjut · `R` ulangi narasi · `S` pengaturan · `D` kerangka tubuh · `M` mode mouse ·
`F` layar penuh · `ESC` kembali ke daftar.

## Isi folder

| Folder | Isi |
|---|---|
| `engine/` | Inti: shell, kamera (MediaPipe), mikrofon, narasi, gambar, aturan teks hasil |
| `engine/vendor/mediapipe/` | MediaPipe Tasks Vision 0.10.14 + model pose (±24 MB, sengaja disimpan sendiri supaya bisa offline) |
| `kemah/` | Satu modul + satu halaman untuk tiap perkemahan |
| `narasi/` | Draf narasi (`.md`) dan subtitle (`.vtt`) |
| `audio/` | Rekaman narasi (`NN-nama.mp3`). Kalau belum ada, permainan langsung mulai |
| `tests/` | Unit test: `node --test "tests/*.test.mjs"` |
| `untuk-guru.html` | Ringkasan untuk guru: konsep, aturan, status 43 perkemahan |
| `tambah-kemah.py` | Membuat halaman perkemahan baru dan mendaftarkannya ke menu |

## Menambah permainan baru

1. Tulis `kemah/NN-nama.js` mengikuti pola modul yang sudah ada.
2. `python tambah-kemah.py NN NN-nama "Nama Perkemahan"`.
3. Taruh rekaman di `audio/NN-nama.mp3` kalau sudah ada.

## Aturan yang tidak boleh dilanggar

Pelajaran tidak pernah ditulis di layar. Layar hasil hanya boleh memuat akibat di dalam cerita,
angka yang dihasilkan pemain, dan kutipan yang diucapkan tokoh Alkitab. `engine/rules.js` memeriksanya
dan memunculkan peringatan merah kalau ada teks yang melanggar.

## Catatan GitHub Pages

- `.nojekyll` harus ikut terunggah, supaya semua berkas disajikan apa adanya.
- Pemuatan pertama mengunduh ±15 MB (wasm + model). Sesudah itu browser menyimpannya.
