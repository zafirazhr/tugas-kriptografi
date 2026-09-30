import math

def columnar_encrypt(plaintext, key):
    # Hilangkan spasi sesuai aturan umum transposisi kolom sederhana
    plaintext = plaintext.replace(" ", "")
    col = len(key)
    row = math.ceil(len(plaintext) / col)
    
    # Padding dengan huruf 'X' jika kurang
    plaintext = plaintext.ljust(row * col, 'X')
    
    # Buat matriks grid
    matrix = [plaintext[i:i + col] for i in range(0, len(plaintext), col)]
    
    # Urutkan kolom berdasarkan abjad dari key
    sorted_key_idx = sorted(range(len(key)), key=lambda k: key[k])
    
    cipherteks = ""
    for idx in sorted_key_idx:
        for r in range(row):
            cipherteks += matrix[r][idx]
            
    return cipherteks

def columnar_decrypt(cipherteks, key):
    col = len(key)
    row = len(cipherteks) // col
    sorted_key_idx = sorted(range(len(key)), key=lambda k: key[k])
    
    # Siapkan matriks kosong
    matrix = [[''] * col for _ in range(row)]
    
    # Isi matriks secara vertikal berdasarkan urutan kunci
    curr_idx = 0
    for idx in sorted_key_idx:
        for r in range(row):
            matrix[r][idx] = cipherteks[curr_idx]
            curr_idx += 1
            
    # Baca matriks secara horizontal
    plaintext = "".join(["".join(row) for row in matrix])
    return plaintext

# Program Utama
if __name__ == "__main__":
    print("=== PROGRAM COLUMNAR TRANSPOSITION ===")
    pesan = input("Ketikkan pesan: ")
    kunci = input("Masukkan kata kunci (contoh: 'TOMBAK'): ")
    
    encrypted = columnar_encrypt(pesan, kunci)
    print(f"Cipherteks: {encrypted}")
    
    decrypted = columnar_decrypt(encrypted, kunci)
    print(f"Plainteks (tanpa spasi): {decrypted}")