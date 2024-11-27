import cv2
import matplotlib.pyplot as plt

# Membaca gambar asli
image = cv2.imread('IMG_0092.JPG')  # Gambar dibaca dalam format BGR (default OpenCV)

# Mengubah gambar menjadi grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Mengonversi gambar ke skala abu-abu (grayscale)

# Mengurangi noise menggunakan Gaussian Blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)  # Kernel 5x5 digunakan untuk meratakan gambar, mengurangi noise

# Deteksi tepi menggunakan metode Canny
# Threshold dapat disesuaikan berdasarkan intensitas objek pada gambar
low_threshold = 50  # Batas bawah untuk deteksi tepi
high_threshold = 150  # Batas atas untuk deteksi tepi
edges = cv2.Canny(blurred_image, threshold1=low_threshold, threshold2=high_threshold)  # Menemukan tepi

# Menampilkan hasil dalam tiga tahap: gambar asli, gambar yang diblur, dan hasil deteksi tepi
titles = ['Original Image', 'Blurred Image', 'Edges (Canny)']  # Judul untuk setiap gambar
images = [gray_image, blurred_image, edges]  # Daftar gambar yang akan ditampilkan

plt.figure(figsize=(15, 5))  # Menyiapkan ukuran figure untuk tampilan
for i in range(3):  # Loop untuk menampilkan ketiga gambar
    plt.subplot(1, 3, i + 1)  # Menempatkan gambar dalam subplot
    plt.imshow(images[i], cmap='gray')  # Menampilkan gambar dalam mode grayscale
    plt.title(titles[i])  # Menampilkan judul untuk gambar
    plt.axis('off')  # Menyembunyikan sumbu untuk tampilan lebih bersih

plt.tight_layout()  # Menata layout agar gambar tidak tumpang tindih
plt.show()  # Menampilkan gambar
