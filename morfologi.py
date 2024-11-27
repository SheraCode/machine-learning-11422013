import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar dalam mode grayscale
image = cv2.imread('IMG_0092.JPG', cv2.IMREAD_GRAYSCALE)  # Membaca gambar dalam grayscale

# Membuat kernel untuk operasi morfologi (5x5 ukuran kernel)
kernel = np.ones((5, 5), np.uint8)  # Kernel berbentuk matriks 5x5 berisi angka 1

# Dilasi (Melebarkan area putih)
# Operasi dilasi menambah ukuran objek putih pada gambar
dilated = cv2.dilate(image, kernel, iterations=2)  # Dilasi dilakukan 2 kali

# Erosi (Mengurangi area putih)
# Operasi erosi mengurangi objek putih pada gambar
eroded = cv2.erode(image, kernel, iterations=2)  # Erosi dilakukan 2 kali

# Opening (Erosi kemudian Dilasi)
# Opening menghilangkan noise kecil dengan erosi diikuti dilasi
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing (Dilasi kemudian Erosi)
# Closing digunakan untuk menutup celah atau lubang dalam objek dengan dilasi diikuti erosi
closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Menampilkan hasil dalam bentuk subplot
titles = ['Original Image', 'Dilated', 'Eroded', 'Opened', 'Closed']  # Daftar judul untuk gambar
images = [image, dilated, eroded, opened, closed]  # Gambar-gambar yang akan ditampilkan

plt.figure(figsize=(15, 8))  # Menyiapkan ukuran gambar untuk tampil lebih besar
for i in range(len(images)):  # Loop untuk menampilkan gambar-gambar
    plt.subplot(2, 3, i + 1)  # Menampilkan gambar dalam format 2 baris, 3 kolom
    plt.imshow(images[i], cmap='gray')  # Menampilkan gambar dengan colormap grayscale
    plt.title(titles[i])  # Memberi judul untuk setiap gambar
    plt.axis('off')  # Menyembunyikan sumbu untuk tampilan yang lebih bersih

plt.tight_layout()  # Mengatur layout agar gambar tidak saling tumpang tindih
plt.show()  # Menampilkan gambar
