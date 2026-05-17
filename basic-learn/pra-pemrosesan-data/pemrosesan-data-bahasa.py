# Contoh dasar tokenisasi teks
sentences = ["I love my cat"]

# Membuat tokenizer dengan maksimal 100 kata unik
tokenizer = Tokenizer(num_words=100)

# Mempelajari kata-kata dari dataset
tokenizer.fit_on_texts(sentences)

# Mengubah kalimat menjadi urutan angka
sequences = tokenizer.texts_to_sequences(sentences)

# Menampilkan hasil mapping kata dan sequence
print(tokenizer.word_index)
print(sequences)


# ======================================================
# Contoh penggunaan OOV (Out Of Vocabulary) dan Padding
# ======================================================

# Dataset awal untuk melatih tokenizer
sentences = [
    "I love my cat",
    "Do you think my cat is cute?"
]

# Tokenizer dengan token khusus untuk kata yang tidak dikenal
tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")

# Mempelajari kata dari dataset
tokenizer.fit_on_texts(sentences)

# Dataset baru untuk diuji
sentences = [
    "I love my cat",
    "Do you think my cat is cute?",
    "Additional cat for you"
]

# Mengubah setiap kalimat menjadi sequence angka
sequences = tokenizer.texts_to_sequences(sentences)

# Menyamakan panjang sequence dengan padding
padded = pad_sequences(
    sequences,
    padding="post",      # Tambahkan padding di akhir
    truncating="post",   # Potong sequence di akhir jika terlalu panjang
    maxlen=10            # Panjang maksimum sequence
)

# Menampilkan hasil tokenizer, sequence, dan padding
print("Tokenizer: ", tokenizer.word_index)
print("Sequences: ", sequences)
print("Padded: ", padded)