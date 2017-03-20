graph = {
             'derwati': ['bojongsoang'],
             'ciwastra': ['margahayu'],
			 'kordon': ['margaasih'],
             'bubat': ['bkr'],
             'kircon': ['sekejati'],
             'gatsu': ['gumuruh'],
             'naripan': ['asia-afrika'],
			 'tamim': ['jendral-sudirman'],
        }

def rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[]):
        rute = rute + [lokasi_awal]
        if lokasi_awal == lokasi_tujuan:
            return rute
            if not graph.has_key(lokasi_awal):
                    return None
        rutependek = None
        for node in graph[lokasi_awal]:
            if node not in rute:
                rutebaru = rutepalingpendek(graph, node, lokasi_tujuan, rute)
                if rutebaru:
                    if not rutependek or len(rutebaru) < len(rutependek):
                        rutependek = rutebaru
        return rutependek
print("Rute Jalan Raya derwati sampai tamim")
print("(derwati-ciwastra-kordon-bubat-kircon-gatsu-naripan-tamim)")
print("Iqbal Fitra Ramadhan-1144023")
print("\n")
lokasi_awal = raw_input("Masukan Lokasi Awal : ")
lokasi_tujuan = raw_input("Masukan Lokasi Tujuan : ")
hasilnya = rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[])
print "Rute Terpendek", hasilnya ,".",