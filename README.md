## API FLIGHTRADAR24

Dibuat dengan python3 menggunakan package [pyflightdata](https://github.com/supercoderz/pyflightdata)

Doskumentasi : [pyflightdata](https://pyflightdata.readthedocs.io/en/latest/pyflightdata.html)

### Cara install

1. Install Python 3.6 atau yang lebih tinggi
2. Buka terminal (CMD / PowerShell) clone 
    ```
    git clone https://github.com/Miftahuddin-cod/flightradar24-Api.git
    ```
3. Masuk ke project 
    ```
    cd flightradar24-Api
    ```
4. Jalankan sintaks berikut untuk membuat vietual environment dan menginstall package yang diperlukan

    ```
    py -3 -m venv .venv
    .venv\scripts\activate
    pip install -r requirements.txt
    ```

5. Jalankan api

    ```
    flask run
    ```
6. Gunakan url yang muncul di terminal

### End-point

#### Details

```
http://127.0.0.1:5000/<iata>/details/<page>
```
- iata diisi dengan kode bandara
- page diisi dengan angka mulai dari 1

Contoh Makassar (UPG / WAAA) :
```
http://127.0.0.1:5000/WAAA/details/1
```
Untuk lainnya seperti arrivals, departures, weather, onground, dll, cek di file app.py

Note : arrivals dan departures untuk yang akun free / tidak login cuma bisa sampai page 3

Mungkin ada yang mau kontribusi tambah kodenya dipersilahkan.
