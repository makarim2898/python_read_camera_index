import subprocess

def read_camera_idx(index_camera_yang_dimau=0):
    try:
        hasil_check_index = subprocess.check_output("ls /dev/video*", text=True, shell=True)
        array_index = hasil_check_index.strip().split("\n")
        return array_index[index_camera_yang_dimau]
    except subprocess.CalledProcessError:
        print("Tidak ada perangkat kamera yang terdeteksi.")
        return None

data = read_camera_idx()
print(data)