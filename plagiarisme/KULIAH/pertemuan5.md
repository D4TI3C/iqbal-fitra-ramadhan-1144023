KECERDASAN BUATAN

"NATURAL LANGUAGE PROCESS"

1. Latar Belakang

Pengembangan aplikasi NLP sangat menantang karena komputer secara tradisional mengharuskan manusia untuk "berbicara" kepada mereka dalam bahasa pemrograman yang tepat, tidak ambigu dan sangat terstruktur atau, mungkin melalui sejumlah perintah suara yang jelas-jelas. Pidato manusia, bagaimanapun, tidak selalu tepat - seringkali ambigu dan struktur linguistik dapat bergantung pada banyak variabel kompleks, termasuk bahasa gaul, dialek daerah dan konteks social, Pendekatan saat ini terhadap NLP didasarkan pada pembelajaran mesin, sejenis kecerdasan buatan yang meneliti dan menggunakan pola dalam data untuk memperbaiki pemahaman program sendiri. Sebagian besar penelitian yang dilakukan pada pemrosesan bahasa alami berkisar pada pencarian, terutama pencarian perusahaan.

2. Pembahasan

Natural Language Processing (NLP) mengacu pada metode AI untuk berkomunikasi dengan sistem cerdas dengan menggunakan bahasa alami seperti bahasa Inggris. Pengolahan Bahasa Alami diperlukan bila Anda menginginkan sistem cerdas seperti robot untuk melakukansesuai instruksi Anda, bila Anda ingin mendengar keputusan dari sistem pakar klinis berbasis dialog, dll. Bidang NLP melibatkan pembuatan komputer untuk melakukan tugas yang bermanfaat dengan bahasa alami yang digunakan manusia. Input dan output dari sistem NLP bisa berupa •	Pidato •	Teks tertulis Tugas NLP yang umum dalam program perangkat lunak saat ini meliputi: •	Segmentasi kalimat, pemberian tag dan parsing part-of-speech. •	Analisis mendalam •	Dinamakan ekstraksi entitas. •	Co-referensi resolusi. Keuntungan dari pemrosesan bahasa alami dapat dilihat saat mempertimbangkan dua pernyataan berikut: "Asuransi komputasi awan harus menjadi bagian dari setiap perjanjian tingkat layanan" dan "SLA yang baik memastikan tidur malam lebih mudah - bahkan di awan." Jika Anda menggunakan pemrosesan bahasa nasional untuk pencarian, program ini akan mengenali bahwa komputasi awan adalah entitas, bahwa awan adalah bentuk singkat dari komputasi awan dan bahwa SLA adalah akronim industri untuk perjanjian tingkat layanan.

a)	Komponen NLP Ada dua

Pemahaman Bahasa Alami (NLU) Pengertian melibatkan tugas-tugas berikut - Pemetaan input yang diberikan dalam bahasa alami menjadi representasi yang berguna. Menganalisis berbagai aspek bahasa.
Natural Language Generation (NLG) Ini adalah proses menghasilkan ungkapan dan kalimat bermakna dalam bentuk bahasa alami dari beberapa representasi internal. Ini melibatkan - Perencanaan teks - Ini termasuk mengambil konten yang relevan dari basis pengetahuan. Perencanaan kalimat - Termasuk memilih kata-kata yang dibutuhkan, membentuk ungkapan bermakna, mengatur nada kalimat. Text Realization - Ini adalah pemetaan rencana kalimat ke dalam struktur kalimat
NLU lebih sulit dari NLG
b)	Kesulitan dalam NLU

NL memiliki bentuk dan struktur yang sangat kaya.
Ini sangat ambigu. Ada berbagai tingkat ambiguitas
Ketidakjelasan leksikal - Pada tingkat yang sangat primitif seperti word-level. Misalnya, memperlakukan kata "papan" sebagai kata benda atau kata kerja? Tingkat Sintaks ambiguitas
Kalimat dapat diuraikan dengan berbagai cara. Misalnya, "Dia mengangkat kumbang dengan topi merah."
Apakah dia menggunakan topi untuk mengangkat kumbang atau dia mengangkat kumbang yang memiliki tutup merah? Referential ambiguity
Mengacu pada sesuatu yang menggunakan kata ganti. Misalnya, Rima pergi ke Gauri. Dia berkata, "Saya lelah."
Tepat siapa yang lelah? Satu masukan bisa berarti makna yang berbeda. Banyak masukan bisa berarti hal yang sama.

c)	Terminologi NLP o	Fonologi - Ini adalah studi pengorganisasian yang terdengar sistematis o	Morfologi - Ini adalah studi tentang konstruksi kata-kata dari unit-unit bermakna primitif. o	Morpheme - Ini adalah satuan makna primitif dalam bahasa. o	Sintaks - Ini mengacu pada penyusunan kata-kata untuk membuat sebuah kalimat. Ini juga melibatkan penentuan peran struktural kata-kata dalam kalimat dan frasa. o	Semantik - Hal ini berkaitan dengan arti kata-kata dan bagaimana menggabungkan kata-kata menjadi frase dan kalimat yang berarti. o	Pragmatik - Ini berhubungan dengan menggunakan dan memahami kalimat dalam situasi yang berbeda dan bagaimana penafsiran kalimat tersebut akan terpengaruh. o	Wacana - Ini berkaitan dengan bagaimana kalimat sebelumnya bisa mempengaruhi penafsiran kalimat berikutnya. o	Pengetahuan Dunia - Ini mencakup pengetahuan umum tentang dunia.

d)	Langkah di NLP

- Lexical Analysis - Ini melibatkan identifikasi dan analisis struktur kata-kata. Leksikon bahasa berarti kumpulan kata dan ungkapan dalam bahasa. Analisis leksikal membagi keseluruhan potongan txt menjadi paragraf, kalimat, dan kata-kata.

- Syntax Analysis (Parsing) - Ini melibatkan analisis kata-kata dalam kalimat untuk tata bahasa dan mengatur kata-kata dengan cara yang menunjukkan hubungan di antara kata-kata. Kalimat seperti "The School goes to boy" ditolak oleh penganalisis sintaksis Inggris.

- Semantics Analysis - Ini menarik arti sebenarnya atau makna kamus dari teks. Teks itu diperiksa untuk keberanian. Hal ini dilakukan dengan memetakan struktur dan objek sintaksis dalam domain tugas. Analis semantik mengabaikan kalimat seperti "es krim panas".

- Disclosure Integration - Arti dari setiap kalimat tergantung pada arti kalimat sebelum itu. Selain itu, juga membawa makna langsung kalimatnya.

- Pragmatics Analysis - Selama ini, apa yang dikatakan diinterpretasikan kembali pada apa yang sebenarnya dimaksudkannya. Ini melibatkan aspek bahasa yang membutuhkan pengetahuan dunia nyata.

e)	SpeechRecognition

merupakan library python untuk melakukan pengenalan suara, dengan dukungan beberapa mesin dan API, online dan offline.

install terlebih dahulu pyaudio yang digunakan untuk menginput micropone.

**pip install pyaudio**
Selanjutnya install PocketSphinx untuk menggunakan Sphinx recognizer.

**pip install wheel**
Lalu install Google API Client Library for Python untuk menggunakan Google Cloud Speech API.

**pip install google-api-python-client**
Terakhir install SpeechRecognition.

**pip install SpeechRecognition**

Kesimpulan

pengolahan bahasa alami mengacu pada metode kecerdasan buatan digunakan untuk berkomunikasi dengan komputer menggunakan bahasa keseharian dan terdapat beberapa bidang yang berhubungan dengan pengolahan bahasa alami

Saran

Dengan membaca dari referensi yang lain akan menambahkan materi yang belum lengkap dan lebih baik dilakukannya praktek.

NAMA : IQBAL FITRA RAMADHAN 
NPM : 1144023 
KELAS : D4 TEKNIK INFORMATIKA 3C 
POLITEKNIK POS INDONESIA