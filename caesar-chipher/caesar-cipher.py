def caesar_encrypt(plaintext, k):
    cipherteks = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            c = (ord(char) - start + k) % 26
            cipherteks += chr(c + start)
        else:
            cipherteks += char  # Karakter selain huruf dibiarkan tetap
    return cipherteks

def caesar_decrypt(cipherteks, k):
    plainteks = ""
    for char in cipherteks:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            c = (ord(char) - start - k) % 26
            plainteks += chr(c + start)
        else:
            plainteks += char
    return plainteks

# Program Utama
if __name__ == "__main__":
    print("=== PROGRAM CAESAR CIPHER ===")
    pesan = input("Ketikkan pesan: ")
    kunci = int(input("Masukkan jumlah pergeseran (k): "))
    
     hasil_enkripsi = caesar_encrypt(pesan, kunci)
    print(f"Cipherteks: {hasil_enkripsi}")
    
    hasil_dekripsi = caesar_decrypt(hasil_enkripsi, kunci)
    print(f"Plainteks: {hasil_dekripsi}")