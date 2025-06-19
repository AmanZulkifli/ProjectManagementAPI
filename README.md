## 🗂️ Project Management API (Django)

Ini adalah backend REST API untuk aplikasi manajemen proyek, dibangun menggunakan Django dan Django REST Framework.

### 🚀 Fitur Utama

* Autentikasi JWT (register, login, logout)
* Manajemen proyek (buat, lihat, edit, hapus)
* Manajemen tugas dalam proyek (dengan status seperti Trello)
* Sistem relasi user–proyek–tugas

## 🛠️ Cara Menjalankan (Local)

### 1. Clone repository

```bash
git clone https://github.com/AmanZulkifli/ProjectManagementAPI.git
cd ProjectManagementAPI
```

### 2. Buat dan aktifkan virtual environment

```bash
python -m venv env
source env/bin/activate     # Mac/Linux
env\\Scripts\\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan migrasi database

```bash
python manage.py migrate
```

---

### 5. Jalankan server lokal

```bash
python manage.py runserver
```

Akses API di: [http://localhost:8000](http://localhost:8000)

## 🔐 Autentikasi

API menggunakan JWT (JSON Web Token). Endpoint yang tersedia:

* `POST /api/auth/register/` – Registrasi user
* `POST /api/auth/login/` – Login dan dapatkan token
* `POST /api/auth/logout/` – Logout (blacklist token)
* `GET  /api/auth/user/` – Ambil data user yang sedang login

Gunakan token akses (access_token) pada header:

```
Authorization: Bearer <access_token>
```

## 📦 Endpoint Proyek

| Method | Endpoint             | Deskripsi                      |
| ------ | -------------------- | ------------------------------ |
| GET    | `/api/projects/`     | Daftar semua proyek milik user |
| POST   | `/api/projects/`     | Tambah proyek baru             |
| GET    | `/api/projects/:id/` | Detail proyek tertentu         |
| PATCH  | `/api/projects/:id/` | Edit proyek                    |
| DELETE | `/api/projects/:id/` | Hapus proyek                   |

---

## ✅ Endpoint Tugas

| Method | Endpoint                            | Deskripsi                 |
| ------ | ----------------------------------- | ------------------------- |
| GET    | `/api/projects/:id/tasks/`          | Daftar tugas dalam proyek |
| POST   | `/api/projects/:id/tasks/`          | Tambah tugas ke proyek    |
| PATCH  | `/api/projects/:id/tasks/:task_id/` | Edit tugas                |
| DELETE | `/api/projects/:id/tasks/:task_id/` | Hapus tugas               |


## 🧪 Tools yang Digunakan

* Django
* Django REST Framework
* SimpleJWT
* PostgreSQL
* CORS Headers

---

## 🧍‍♂️ Developer

> 🚧 Versi backend ini dibuat sebagai bagian dari sistem manajemen proyek berbasis web yang akan terhubung dengan frontend React.
> Link frontendnya akan saya lampirkan di deskripsi

