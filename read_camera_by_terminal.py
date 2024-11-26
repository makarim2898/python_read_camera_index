import subprocess
import cv2

# Periksa perangkat video dan simpan di daftar_kamera
try:
    hasil = subprocess.check_output("ls /dev/video*", shell=True, text=True)
    daftar_kamera = hasil.strip().split("\n")  # Pisahkan output per baris
    print("Daftar Kamera yang Terdeteksi:", daftar_kamera)
except subprocess.CalledProcessError:
    daftar_kamera = []
    print("Tidak ada perangkat kamera yang terdeteksi.")

# Jika ada kamera, gunakan indeks kamera pertama
if daftar_kamera:
    # Ambil indeks kamera (contoh: '/dev/video0' -> 0)
    index_kamera = int(daftar_kamera[0].replace("/dev/video", ""))
    print(f"Mencoba membuka kamera pada indeks {index_kamera}...")

    # Gunakan OpenCV untuk membuka kamera
    cap = cv2.VideoCapture(index_kamera)
    if cap.isOpened():
        print("Kamera berhasil dibuka.")
        # Tampilkan frame dari kamera
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Gagal membaca frame.")
                break
            cv2.imshow("Kamera", frame)

            # Tekan 'q' untuk keluar
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Gagal membuka kamera.")
else:
    print("Tidak ada kamera untuk digunakan.")
