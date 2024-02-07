
list_user = [{'nama': 'sumeet', 'email': 'v@g.com', 'password': 'sumeet', 'saldo': 347200, 'riwayat': [{'buytime': '00:41 26-12-2022', 'hall': 'PVR\nStudio 1', 'movie': 'Black Adam', 'date and time': '13:30 26-12-2022', 'Ticket': 'E3', 'Total': 'Rp450,00'}, {'buytime': '00:47 26-12-2022', 'hall': 'PVR\nStudio 4', 'movie': 'ONE PIECE FILM: RED', 'date and time': '13:30 26-12-2022', 'Ticket': 'A7', 'Total': 'Rp500,00'}, {'buytime': '00:54 26-12-2022', 'hall': 'PVR\nStudio 3', 'movie': 'DOCTOR G', 'date and time': '13:30 27-12-2022', 'Ticket': 'A1', 'Total': 'Rp500,00'}, {'buytime': '01:09 26-12-2022', 'hall': 'PVR\nStudio 1', 'movie': 'Black Adam', 'date and time': '13:30 26-12-2022', 'Ticket': 'E7', 'Total': 'Rp450,00'}, {'buytime': '01:15 26-12-2022', 'hall': 'KORUM MALL\nStudio 1', 'movie': 'Black Adam', 'date and time': '16:00 27-12-2022', 'Ticket': 'A1', 'Total': 'Rp450,00'}, {'buytime': '01:21 26-12-2022', 'hall': 'INOX\nStudio 1', 'movie': 'Black Adam', 'date and time': '13:30 27-12-2022', 'Ticket': 'A1', 'Total': 'Rp450,00'}]}]
location =  ['PVR', 'INOX', 'KORUM MALL']

time_str = ['13:30', '16:00', '18:30', '21:00']
time_int = [
            {'hour': 13, 'minute': 30},
            {'hour': 16, 'minute': 00},
            {'hour': 18, 'minute': 30},
            {'hour': 21, 'minute': 00},
        ]


list_validasi = {
    50000: {
            'gopay': '4',
            'ovo': '4',
            'bca': '4',
            'mandiri': '4',
            'bni': '4',
            'bri': '4',
        },
    100000: {
        'gopay': '4',
        'ovo': '4',
        'bca': '4',
        'mandiri': '4',
        'bni': '4',
        'bri': '4',
    },
    150000: {
        'gopay': '4',
        'ovo': '4',
        'bca': '4',
        'mandiri': '4',
        'bni': '4',
        'bri': '4',
    },
    200000: {
       'gopay': '4',
        'ovo': '4',
        'bca': '4',
        'mandiri': '4',
        'bni': '4',
        'bri': '4',
    }
}

# Data Upcoming Movie
movie_upcoming = [
    {
        'img_on': 'images/blackpanther_on.png',
        'img_off': 'images/blackpanther_off.png',
        'title': 'Black Panther: Wakanda Forever',
        'age': 'SU',
        'genre': 'Action, Adventure, Drama',
        'duration': '- Minutes',
        'plot': 'Rakyat Wakanda kali ini akan berjuang untuk melindungi negerinya dari campur tangan kekuatan dunia setelah kematian sang Raja T\'Challa.',
        'producer': 'Kevin Feige, Nate Moore',
        'director': 'Ryan Coogler',
        'writer': 'Ryan Coogler, Joe Robert Cole',
        'cast': 'Letitia Wright, Lupita Nyong\'o, Tenoch Huerta, Angela Bassett, Martin Freeman, Danai Gurira, Michaela Coel, Dominique Thorne, Winston Duke, Richard Schiff, Mabel Cadena',
    },
    {
        'img_on': 'images/bosslevel_on.png',
        'img_off': 'images/bosslevel_off.png',
        'title': 'BOSS LEVEL',
        'age': '17+',
        'genre': 'Action, Adventure, Comedy',
        'duration': '101 Minutes',
        'plot': 'Terperangkap dalam lingkaran waktu yang terus-menerus mengulangi hari pembunuhannya, seorang mantan agen pasukan khusus harus membuka misteri di balik kematiannya sebelum dunia hancur.',
        'producer': 'Joe Carnahan, Frank Grillo',
        'director': 'Joe Carnahan',
        'writer': 'Chris Borey, Eddie Borey, Joe Carnahan',
        'cast': 'Frank Grillo, Mel Gibson, Naomi Watts, Will Sasso, Annabelle Walls, Sheaun Mckinney, Selina Lo, Michelle Yeoh, Ken Jeong, Meadow Williams, Mathilde Ollivier, Armida Lopez',
    },
    {
        'img_on': 'images/sriasih_on.png',
        'img_off': 'images/sriasih_off.png',
        'title': 'SRI ASIH',
        'age': '-',
        'genre': 'Action, Sci-fi',
        'duration': '- Minutes',
        'plot': 'Alana tidak mengerti mengapa dia selalu dikuasai oleh kemarahan. Tapi dia selalu berusaha untuk melawannya. Dia lahir saat letusan gunung berapi yang memisahkan dia dan orang tuanya. Dia kemudian diadopsi oleh seorang wanita kaya yang berusaha membantunya menjalani kehidupan normal. Tapi saat dewasa, Alana menemukan kebenaran tentang asalnya. Dia bukan manusia biasa. Dia bisa menjadi kebaikan untuk kehidupan. Atau menjadi kehancuran bila ia tidak dapat mengendalikan amarahnya.',
        'producer': 'Bismarka Kurniawan, Wicky V. Olindo, Joko Anwar',
        'director': 'Upi',
        'writer': 'Upi, Joko Anwar',
        'cast': 'Pevita Pearce, Reza Rahadian, Christine Hakim, Jefri Nichol, Dimas Anggara, Surya Saputra, Jenny Zhang, Randy Pangalila',
    },
    {
        'img_on': 'images/tegar_on.png',
        'img_off': 'images/tegar_off.png',
        'title': 'TEGAR',
        'age': 'SU',
        'genre': 'Drama',
        'duration': '92 Minutes',
        'plot': 'Tegar (10), seorang anak berkebutuhan khusus yang menginginkan bisa seperti anak pada umumnya, berteman dan bersekolah. Di hari ulang tahunnya yang ke-10, Tegar mengutarakan impiannya kepada sang Kakek. Namun, keputusan Kakek untuk mewujudkan impian Tegar justru membuat Kakek dan Ibu berselisih. Akhirnya, Tegar memutuskan untuk pergi dari rumah demi mengejar mimpinya.',
        'producer': 'Chandra Sembiring, Surajuddin Datau',
        'director': 'Anggi Frisca',
        'writer': 'Alim Sudio, Anggi Frisca',
        'cast': 'Aldifi Tegarajasa, Deddy Mizwar, Sha Ine Febriyanti, Joanita Chatarina, M. Adhiyat, Prihartono Mirsaputra, Jamaluddin Latief',
    },
]

# Data Daftar Film
movie_now = [
    {
        'img_on': 'images/blackadam_on.png',
        'img_off': 'images/blackadam_off.png',
        'title': 'Black Adam',
        'age': 'R13',
        'genre': 'Action, Fantasy, Sci-Fi',
        'duration': '125 Minutes',
        'plot': 'Black adam.',
        'producer': 'Beau Flynn, Dany Garcia, Hiram Garcia',
        'director': 'Jaume Collet-serra',
        'writer': 'Adam Sztykiel, Rory Haines, Sohrab Noshirvani',
        'cast': 'Dwayne Johnson, Viola Davis, Sarah Shahi, Pierce Brosnan, Noah Centineo, Aldis Hodge, Angel Rosario Jr., Joseph Gatt, Mohammed Amer, Quintessa Swindell',
        'price': 450,
        'sold_seat': {'PVR_0': {'25-12-2022': {'21:00': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, True, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}, '26-12-2022': {'13:30': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, True, True, True, 0, True, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}, '27-12-2022': {'13:30': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [True, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}}, 'INOX_0': {'27-12-2022': {'13:30': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [True, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}}, 'KORUM MALL_0': {'26-12-2022': {'21:00': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, True, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}, '27-12-2022': {'16:00': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [True, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}}}
    },
    {
        'img_on': 'images/amsterdam_on.png',
        'img_off': 'images/amsterdam_off.png',
        'title': 'AMSTERDAM',
        'age': 'R13',
        'genre': 'Drama, History',
        'duration': '134 Minutes',
        'plot': 'Set in the 1930s, three best friends Burt Berendsen (Christian Bale), Valerie Voze (Margot Robbie) and Harold Woodman (John David Washington) are witnesses to a murder who eventually becomes a suspect. The three try to find a way out and change the course of American history.',
        'producer': 'Christian Bale, Matthew Budman, Anthony Katagas, Arnon Milchan, David O. Russell',
        'director': 'David O. Russell',
        'writer': 'David O. Russell',
        'cast': 'Christian Bale, Margot Robbie, John David Washington, Rami Malek, Mike Myers, Taylor Swift, Zoe Saldana, Robert De Niro, Anya Taylor-joy, Chris Rock, Michael Shannon.',
        'price': 400,
        'sold_seat': {'PVR_1': {'26-12-2022': {'13:30': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [True, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}}, 'INOX_1': {}, 'KORUM MALL_1': {}}        
    },
    {
        'img_on': 'images/doctorg_on.png',
        'img_off': 'images/doctorg_off.png',
        'title': 'DOCTOR G',
        'age': 'R17+',
        'genre': 'Comedy',
        'duration': '122 Minutes',
        'plot': 'A medical school comedy-drama, Doctor G is about the hilarious struggles of Dr. Uday Gupta, he had a desire to specialize in Orthopedics, but was stuck in the all-female Gynecology class.',
        'producer': 'Vineet Jain',
        'director': 'Anubhuti Kashyap',
        'writer': 'Saurabh Bharat',
        'cast': 'Ayushmann Khuranna, Rakul Preet Singh, Shefali Shah, Sheeba Chaddha, Abhinay Raj Singh, Paresh Pahuja, Jhumma Mitra, Azzy Bagria',
        'price': 500,
        'sold_seat': {'PVR_2': {'27-12-2022': {'13:30': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [True, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}}, 'INOX_2': {}, 'KORUM MALL_2': {}}
    },
    {
        'img_on': 'images/onepiece_on.png',
        'img_off': 'images/onepiece_off.png',
        'title': 'ONE PIECE FILM: RED',
        'age': 'R13',
        'genre': 'Animation, Adventure, Fantasy',
        'duration': '115 Minutes',
        'plot': 'Untuk pertama kalinya, Uta - penyanyi paling dicintai akan mengungkapkan dirinya kepada dunia di konser langsungnya. Suara yang ditunggu-tunggu oleh seluruh dunia akan segera bergema.',
        'producer': 'Eiichiro Oda',
        'director': 'Goro Taniguchi',
        'writer': 'Tsutomu Kuroiwa',
        'cast': 'Kazuya Nakai, Kaori Nazuka, Akemi Okamura, Kappei Yamaguchi, Mayumi Tanaka, Yuriko Yamaguchi, Hiroaki Hirata, Shuichi Ikeda',
        'price': 500,
        'sold_seat': {'PVR_3': {'26-12-2022': {'13:30': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, True, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}}, 'INOX_3': {}, 'KORUM MALL_3': {}},
    }
]
