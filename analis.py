import re
from collections import Counter

def load_email(file_path):
    """Membaca email dari file dan mengembalikannya sebagai string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def analyze_email(email_content):
    """Menganalisis konten email dan mengembalikan hasil analisis."""
    # Menghitung jumlah karakter
    char_count = len(email_content)
    
    # Menghitung jumlah kata
    words = re.findall(r'\b\w+\b', email_content.lower())
    word_count = len(words)
    
    # Menghitung frekuensi kata
    word_frequency = Counter(words)
    
    return char_count, word_count, word_frequency

def main():
    file_path = 'email.txt'  # Ganti dengan path file email Anda
    email_content = load_email(file_path)
    
    char_count, word_count, word_frequency = analyze_email(email_content)
    
    print(f'Jumlah Karakter: {char_count}')
    print(f'Jumlah Kata: {word_count}')
    print('Frekuensi Kata:')
    
    # Menampilkan 10 kata yang paling sering muncul
    for word, freq in word_frequency.most_common(10):
        print(f'{word}: {freq}')

if __name__ == '__main__':
    main()