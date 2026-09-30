import string

def buat_tabel_substitusi(kunci_kata):
    # Buang duplikat dan ubah ke huruf kapital
    kunci_bersih = ""
    for char in kunci_kata.upper():
        if char.isalpha() and char not in kunci_bersih:
            kunci_bersih += char
            
    # Tambahkan sisa huruf alfabet yang belum ada
    alphabet = string.ascii_uppercase
    sisa_huruf = "".join([c for c in alphabet if c not in kunci_bersih])
    
    cipher_alphabet = kunci_bersih + sisa_huruf
    return alphabet, cipher_alphabet

def mono_encrypt(plaintext, kunci_kata):
    std, cip = buat_tabel_substitusi(kunci_kata)
    trans_table = str.maketrans(std + std.lower(), cip + cip.lower())
    return plaintext.translate(trans_table)

def mono_decrypt(cipherteks, kunci_kata):
    std, cip = buat_tabel_substitusi(kunci_kata)
    trans_table = str.maketrans(cip + cip.lower(), std + std.lower())
    return cipherteks.translate(trans_table)

# Program Utama
if __name__ == "__main__":
    print("=== PROGRAM MONOALPHABETIC SUBSTITUTION ===")
    pesan = input("Ketikkan pesan: ")
    kunci = input("Masukkan kalimat kunci (contoh: 'kriptografi'): ")
    
    encrypted = mono_encrypt(pesan, kunci)
    print(f"Cipherteks: {encrypted}")
    
    decrypted = mono_decrypt(encrypted, kunci)
    print(f"Plainteks: {decrypted}")