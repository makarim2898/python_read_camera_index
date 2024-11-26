read_camera_by_terminal: digunakan untuk membaca index video yang terpasang pada sistem linux, dan menggunakan index kamera yang dipilih untuk live;
ubahlah index_kamera = int(daftar_kamera[0].replace("/dev/video", "")) agar sesuai dengan index kamera yang di ingin kan;
code ini ditulis untuk menanggulangi problem index kamera pindah saat live open cv