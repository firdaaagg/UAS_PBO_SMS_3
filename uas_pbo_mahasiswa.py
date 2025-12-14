import tkinter as tk
from tkinter import messagebox, ttk
import csv

# =======================================
#                  MODEL
# =======================================

class Mahasiswa:
    def __init__(self, nim, nama, kls, prodi, tahun_masuk):
        self._nim = nim
        self._nama = nama
        self._kls = kls
        self._prodi = prodi
        self._tahun_masuk = tahun_masuk

    # Getter
    def get_nim(self): return self._nim
    def get_nama(self): return self._nama
    def get_kls(self): return self._kls
    def get_prodi(self): return self._prodi
    def get_tahun_masuk(self): return self._tahun_masuk

    # Setter
    def set_nama(self, val): self._nama = val
    def set_kls(self, val): self._kls = val
    def set_prodi(self, val): self._prodi = val
    def set_tahun_masuk(self, val): self._tahun_masuk = val

    def display_info(self):
        return (f"NIM: {self._nim}\n"
                f"Nama: {self._nama}\n"
                f"Kelas: {self._kls}\n"
                f"Program Studi: {self._prodi}\n"
                f"Tahun Masuk: {self._tahun_masuk}\n")


class MahasiswaReguler(Mahasiswa):
    def display_info(self):
        return "[REGULER]\n" + super().display_info()


class MahasiswaTransfer(Mahasiswa):
    def __init__(self, nim, nama, kls, prodi, tahun_masuk, asal_kampus):
        super().__init__(nim, nama, kls, prodi, tahun_masuk)
        self._asal_kampus = asal_kampus

    def get_asal_kampus(self): return self._asal_kampus
    def set_asal_kampus(self, val): self._asal_kampus = val

    def display_info(self):
        return (f"[TRANSFER]\n"
                f"{super().display_info()}"
                f"Asal Kampus: {self._asal_kampus}\n")


# =======================================
#          DATABASE / CONTROLLER
# =======================================

class Database:
    def __init__(self):
        self._data = []

    def add(self, mhs):
        self._data.append(mhs)

    def update(self, index, new_mhs):
        self._data[index] = new_mhs

    def delete(self, index):
        del self._data[index]

    def all(self):
        return self._data

    # ✨ PENCARIAN LENGKAP (NIM / NAMA / PRODI / KELAS / TAHUN MASUK)
    def search(self, keyword):
        q = keyword.lower()
        return [
            m for m in self._data
            if q in m.get_nim().lower()
            or q in m.get_nama().lower()
            or q in m.get_prodi().lower()
            or q in m.get_kls().lower()
            or q in str(m.get_tahun_masuk())
        ]


# =======================================
#                   VIEW (GUI)
# =======================================

class App:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Data Mahasiswa - UAS PBO (Final)")
        self.root.geometry("1050x550")
        self.root.resizable(False, False)

        self.setup_fonts()
        self.build_gui()
        self.seed_demo()
        self.refresh_list()

    def setup_fonts(self):
        self.font_title = ("Segoe UI", 12, "bold")
        self.font_normal = ("Segoe UI", 10)

    def build_gui(self):
        top = tk.Frame(self.root, bg="#f2f2f2")
        top.pack(fill="x")

        tk.Label(top, text="Data Mahasiswa", bg="#f2f2f2", font=self.font_title) \
            .pack(side="left", padx=10, pady=10)

        tk.Label(top, text="Cari (NIM / Nama / Prodi / Kelas / Tahun Masuk):", bg="#f2f2f2") \
            .pack(side="left", padx=5)

        self.entry_cari = tk.Entry(top, width=40)
        self.entry_cari.pack(side="left", padx=5)

        tk.Button(top, text="Cari", width=12, command=self.cari) \
            .pack(side="left", padx=5)

        tk.Button(top, text="Tampilkan Semua", width=15, command=self.refresh_list) \
            .pack(side="left", padx=5)

        body = tk.Frame(self.root)
        body.pack(fill="both", expand=True, padx=10)

        # LISTBOX
        left_frame = tk.Frame(body)
        left_frame.pack(side="left", fill="y")

        tk.Label(left_frame, text="Daftar Mahasiswa", font=self.font_title) \
            .pack(pady=5)

        self.listbox = tk.Listbox(left_frame, width=40, height=20, font=self.font_normal)
        self.listbox.pack(side="left", fill="y")
        self.listbox.bind("<<ListboxSelect>>", self.show_detail)

        scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # DETAIL BOX
        right_frame = tk.Frame(body)
        right_frame.pack(side="left", fill="both", expand=True, padx=10)

        tk.Label(right_frame, text="Detail Mahasiswa", font=self.font_title) \
            .pack(pady=5)

        self.text_detail = tk.Text(right_frame, height=15, font=self.font_normal)
        self.text_detail.pack(fill="both", expand=True)

        # BUTTONS
        btn_frame = tk.Frame(right_frame)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Tambah Reguler", width=15, command=self.tambah_reguler).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Tambah Transfer", width=15, command=self.tambah_transfer).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Edit Terpilih", width=15, command=self.edit_data).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Hapus Terpilih", width=15, command=self.hapus_data).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Export CSV", width=15, command=self.export_csv).grid(row=0, column=4, padx=5)

        # STATUS BAR
        self.status = tk.Label(self.root, text="Jumlah Mahasiswa: 0", anchor="w")
        self.status.pack(fill="x")

    # ===========================================
    #           SEED DATA DEMO
    # ===========================================

    def seed_demo(self):
        data = [
            MahasiswaReguler("24100101", "Andi Pratama", "2024B", "Sistem Informasi", 2024),
            MahasiswaTransfer("24100102", "Erika Putri", "2024C", "Manajemen Informatika", 2024, "WIJAYA KUSUMA"),
            MahasiswaReguler("23100201", "Bunga Lestari", "2023B", "Manajemen Informatika", 2023),
            MahasiswaTransfer("23100202", "Farel Nugroho", "2023C", "Teknik Komputer", 2023, "UPN"),
            MahasiswaReguler("22100301", "Cici Ramadhani", "2022A", "Teknik Komputer", 2022),
            MahasiswaReguler("22100302", "Gina Marlina", "2022C", "Sistem Informasi", 2022),
            MahasiswaTransfer("21100401", "Dimas Setiawan", "2021B", "Sistem Informasi", 2021, "UINSA"),
            MahasiswaTransfer("21100402", "Hendra Wijaya", "2021C", "Manajemen Informatika", 2021, "UT"),
        ]

        for d in data:
            self.db.add(d)

    # ===========================================
    #             REFRESH / DISPLAY
    # ===========================================

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for i, m in enumerate(self.db.all(), start=1):
            self.listbox.insert(tk.END, f"[{i:02}] {m.get_nim()}   {m.get_nama()}")
        self.status.config(text=f"Jumlah Mahasiswa: {len(self.db.all())}")

    def show_detail(self, evt):
        index = self.get_selected_index()
        if index is None:
            return

        m = self.db.all()[index]
        self.text_detail.delete("1.0", tk.END)
        self.text_detail.insert(tk.END, m.display_info())

    def get_selected_index(self):
        try:
            return self.listbox.curselection()[0]
        except:
            return None

    # ===========================================
    #                  CARI
    # ===========================================

    def cari(self):
        keyword = self.entry_cari.get().strip()
        hasil = self.db.search(keyword)

        self.listbox.delete(0, tk.END)

        for i, m in enumerate(hasil, start=1):
            self.listbox.insert(tk.END, f"[{i:02}] {m.get_nim()}   {m.get_nama()}")

    # ===========================================
    #           TAMBAH / EDIT / HAPUS
    # ===========================================

    def tambah_reguler(self):
        self.popup_form("reguler")

    def tambah_transfer(self):
        self.popup_form("transfer")

    def edit_data(self):
        index = self.get_selected_index()
        if index is None:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu.")
            return

        m = self.db.all()[index]
        jenis = "transfer" if isinstance(m, MahasiswaTransfer) else "reguler"
        self.popup_form(jenis, index, m)

    def hapus_data(self):
        index = self.get_selected_index()
        if index is None:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih!")
            return

        if messagebox.askyesno("Konfirmasi", "Hapus data terpilih?"):
            self.db.delete(index)
            self.refresh_list()
            self.text_detail.delete("1.0", tk.END)

    # ===========================================
    #          POP UP FORM TAMBAH/EDIT
    # ===========================================

    def popup_form(self, jenis, index=None, mhs=None):
        win = tk.Toplevel(self.root)
        win.title("Form Mahasiswa")
        win.geometry("400x400")

        labels = ["NIM", "Nama", "Kelas", "Program Studi", "Tahun Masuk"]
        entries = {}

        for i, lbl in enumerate(labels):
            tk.Label(win, text=lbl).pack()
            ent = tk.Entry(win, width=30)
            ent.pack()
            entries[lbl] = ent

        # Field tambahan jika Transfer
        entry_asal = None

        if jenis == "reguler":
            tk.Label(win, text="Asal Sekolah (SMA)").pack()
            entry_asal = tk.Entry(win, width=30)
            entry_asal.pack()

        elif jenis == "transfer":
                tk.Label(win, text="Asal Kampus").pack()
                entry_asal = tk.Entry(win, width=30)
                entry_asal.pack()

        # Kalau EDIT → isi data lama
        if mhs:
            entries["NIM"].insert(0, mhs.get_nim())
            entries["Nama"].insert(0, mhs.get_nama())
            entries["Kelas"].insert(0, mhs.get_kls())
            entries["Program Studi"].insert(0, mhs.get_prodi())
            entries["Tahun Masuk"].insert(0, mhs.get_tahun_masuk())

            if jenis == "transfer":
                entry_asal.insert(0, mhs.get_asal_kampus())

        def simpan():
            nim = entries["NIM"].get().strip()
            nama = entries["Nama"].get().strip()
            kls = entries["Kelas"].get().strip()
            prodi = entries["Program Studi"].get().strip()
            tahun = entries["Tahun Masuk"].get().strip()

            if jenis == "reguler":
                new = MahasiswaReguler(nim, nama, kls, prodi, int(tahun))
            else:
                asal = entry_asal.get().strip()
                new = MahasiswaTransfer(nim, nama, kls, prodi, int(tahun), asal)

            if mhs is None:
                self.db.add(new)
            else:
                self.db.update(index, new)

            self.refresh_list()
            win.destroy()

        tk.Button(win, text="Simpan", width=15, command=simpan).pack(pady=10)

    # ===========================================
    #               EXPORT CSV
    # ===========================================

    def export_csv(self):
        with open("data_mahasiswa.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["NIM", "Nama", "Kelas", "Prodi", "Tahun Masuk", "Jenis", "Asal Kampus"])

            for m in self.db.all():
                jenis = "Transfer" if isinstance(m, MahasiswaTransfer) else "Reguler"
                asal = m.get_asal_kampus() if jenis == "Transfer" else "-"
                w.writerow([m.get_nim(), m.get_nama(), m.get_kls(),
                            m.get_prodi(), m.get_tahun_masuk(), jenis, asal])

        messagebox.showinfo("Berhasil", "Data berhasil diexport ke CSV!")


# =======================================
#                MAIN
# =======================================

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
