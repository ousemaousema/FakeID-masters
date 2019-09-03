#!/usr/bin/env python2.7
#THNX TO ICODZ & MRAFX
# https://boostini.pw/
#

import random, string
import os

logo = """     
                                                                             
                                                               _______       
                       .           __.....__               .--.\  ___ `'.    
     _.._            .'|       .-''         '.             |__| ' |--.\  \   
   .' .._|         .'  |      /     .-''"'-.  `.           .--. | |    \  '  
   | '       __   <    |     /     /________\   \          |  | | |     |  ' 
 __| |__  .:--.'.  |   | ____|                  |          |  | | |     |  | 
|__   __|/ |   \ | |   | \ .'\    .-------------'          |  | | |     ' .' 
   | |   `" __ | | |   |/  .  \    '-.____...---.          |  | | |___.' /'  
   | |    .'.''| | |    /\  \  `.             .'           |__|/_______.'/   
   | |   / /   | |_|   |  \  \   `''-...... -'                 \_______|/    
   | |   \ \._,\ '/'    \  \  \                                              
   |_|    `--'  `"'------'  '---'                                            
                 
\033[1m\033[1;91m       }--{+}  Coded By Oussama {+}--{\033[1;m          """
menu = """
    {1}--Man ID Generator
    {2}--Woman ID Generator
    
    {99}--Exit
    
"""
fn = "Mohamed","Ahmed","Abdelkader","Abdelhak","Abderrahmane","Amine","Elyes","Khaled","Mourad","Ismail","Abdel","Kader","Salim","Brahim","Walid","Sofiane","Wissem","Menad","Aziz","Samir","Fateh","Mounir","Kacem","Salah","Aymen","Nadir","Nabil","Hamid","Farid","Hocine","Houcine","Yacine","Madjid","Yanis","Mehdi","Sofiane","Younes","Amir","Hamza","Badredine","Khalil","Ayoub","Djamel","Sami","Samy","Mustapha","lyes","Rabah","Abbas","Chakib","Hichem","Wassim","Fares","Rachid","Farouk","Najib","Anis","Karim","Amin","Chahid","Youcef","Youssef","Nazim","Faycal","Malik","Malek","Nassim","Kamel","Yassar","Akram","Zakaria","Islem"
ff = "Akila", "Amani", "Aya", "Bahiya", "Bilkis", "Beya", "Chainez", "Dina", "Eliza", "Souad", "Fatine", "Feryel", "Hayet", "Ibtissem", "Ihsane", "Imane", "Jelila", "Jinen", "Jihene", "kahina", "Laela", "Maissa", "Nawel", "Nihal", "Nour", "Rihab", "Rihem", "Sabah", "Safia", "Saliha", "Sourour", "Taslim", "Oumayma", "Wided", "Wissal", "Wissem", "Mellisa", "Lidya", "Soulef", "Dalila", "Werda", "Linda", "Liza", "Manel", "Kaouter", "Fatima", "Fatiha", "Fazila", "Fazia", "Fadila", "Salima", "Ania", "Baya", "Lilla", "Dana", "Feriel", "Hayda", "Kahina", "Lena", "Louna", "Masila", "Nelia", "Kenza", "Tinhinan", "Tamilla", "Mina", "Nina", "Siline", "Melinda", "Aylana", "Nourhane", "Sabrina", "Amina"
oc = "0540","0541","0542","0550","0551","0555","0666","0667","0677","0643","0771","0770","0772","0773","0774","0776","0777","0778"
mo = "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"
jr = "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"
yr = "1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000"
bi = "4172","4172"
ex = "2019","2020","2021","2022"
bb = "96", "97", "35", "24", "48", "31", "03", "98", "17", "99", "37", "95", "73", "89", "41", "22", "63", "88", "01", "02", "34", "33", "55", "36 "
ln = "MANSOURI", "HADDAD", "SAIDI", "SAADI", "ZITOUNI", "BOUZID", "BOUMAZA", "MEBARKI", "AMARA", "MERABET", "BENYAHIA", "YOUSFI", "RAHMANI", "SALHI", "TOUATI", "BOUZIDI", "HAMLAOUI", "BENAISSA", "SLIMANI", "ABDESSEMED", "YAHIAOUI", "ZAIDI", "KADRI", "MEZIANI", "DIB", "SOLTANI", "BENAMARA", "BEKKOUCHE", "GASMI", "MADI", "BENCHEIKH", "MESSAOUDI", "SAHRAOUI", "AYADI", "CHERIET", "BOURAS", "AISSAOUI", "ROUABAH", "LAOUAR", "FILALI", "BOURAOUI", "MECHERI", "HADJI", "DAOUDI", "MEBARKIA", "LABED", "BELABED", "ZOUAOUI", "BRAHIMI", "BOUDRAA", "MOUSSAOUI", "HAMZA", "TOUMI", "BOUZIANE", "TALBI", "LATRECHE", "ABED", "LAIB", "DEROUICHE", "IKHLEF", "BAHLOUL", "KARA", "SERIDI", "BENSALEM", "BOUGUERRA", "RAMOUL", "HAMANI", "LOUCIF", "BOUDIAF", "SOUILAH", "BOUMAIZA", "HANNACHI", "MEROUANI", "TALEB", "ABDELAZIZ", "BOUAZIZ", "KHALDI", "BELAID", "ZIANI", "GUERFI", "MAKHLOUFI", "MERROUCHE", "BOUAKAZ", "DJABALLAH", "GRINE", "BOURBIA", "BENDJAMA", "SOUAMES", "GHARBI", "SELLAMI", "BOUSSOUF", "NOUI", "HAMDI", "NASRI", "AGGOUN", "AMRANI", "MOKHTARI", "AZZOUZ", "SAMAI", "DRIDI", "AOUADI", "DIABI", "RAMDANE", "AZIZI", "AISSANI", "BOUHIDEL", "MIHOUBI", "AMIRECHE", "CHAOUI", "MESSIKH", "BOUALI", "MADANI", "OUALI", "DERRADJI", "ALIOUA", "MOSBAH", "BAALI", "CHERGUI", "MILI", "ABBAS", "SAIDANI", "CHAIB", "SAHLI", "DAOUD", "BOUAFIA", "MERDACI", "ACHOURI", "LAIFA", "BEKHOUCHE", "ZEROUAL", "BOUCHAREB", "KASSA", "KHALED", "RAIS", "DERBAL", "KAHOUL", "SEDRATI", "KHELLAF", "MESSAI", "ABADA", "DJEBBAR", "MALLEM", "SAIFI", "ATTIA", "DRID", "AYAD", "BOUTEFNOUCHET", "BERKANE", "LAKEHAL", "RAMDANI", "BENDJABALLAH", "SAOUDI", "CHABBI", "KEHAL", "NIBOUCHA", "RIGHI", "GHODBANE", "AMARI", "CHABOU", "MAIZA", "AYACHI", "AMIRA", "SAADANE", "BOUKHALFA", "MAALEM", "CHAKER", "BOUKERZAZA", "GHANEM", "TENIOU", "HAMMOUCHE", "KHALFALLAH", "MAKHLOUF", "MARREF", "BENAMIRA", "LABIOD", "LARABA", "DJAMA", "MOHAMEDBENALI", "MENASRIA", "BOUNOUR", "FOUGHALI", "KITOUNI", "ALLAOUA", "KRIM", "AIDEL", "CHERIFI", "AOUATI", "HACHEMI", "KETFI", "MOHAMMEDI", "BENABED", "KHODJA", "BOUCHERIT", "BOUNAB", "AOUISSI", "KACIMI", "BENFLIS", "MAHMOUDI", "BENDIB", "BOUSSAID", "LAYACHI", "MEKKI", "MOKRANI", "BENCHARIF", "FELLAHI", "RIDA", "DAIBOUNSAHEL", "OUDINA", "YOUNES", "MAHDJOUB", "BOUACHA", "GOUASMIA", "FELLAH", "BENABDERRAHMANE", "BENACHOUR", "LEBSIR", "BENABID", "MAOUCHE", "HEDNA", "SEDDIKI", "SAYAD", "DAFRI", "OUMEDDOUR", "BARKAT", "AKKOUCHE", "BAZA", "GUIDOUM", "BOUDJADJA", "ROULA", "ZEHAR", "BOUAITA", "CHEBLI", "REDJEM", "BENCHERIF", "BOUABDELLAH", "ATOUI", "BENDJEDID", "BOUKACHABIA", "FARFAR", "BAAZIZ", "DILMI", "FERDI", "DJEFFAL", "HADEF", "SAKER", "BENTRAD", "MEDDOUR", "BOUDECHICHA", "SEHILI", "BENABBES", "AHMEDCHAOUCH", "DJABRI", "SALEM", "SOUAHI", "ABID", "BENDJEDDOU", "HACINI", "NADJI", "REZZAG", "BELHADJMOSTEFA", "DERROUICHE", "KADI", "ABBAOUI", "ALLOUACHE", "BOUDOUKHA", "GUENIFI", "BIROUK", "BOUNAR", "CHEBEL", "SILINI", "AMMARI", "BELKACEM", "BEDDIAR", "HALAIMIA", "BELHADJ", "BENAMEUR", "BENAZZOUZ", "BOUHROUM", "BRIKI", "SNANI", "MEZHOUD", "HANI", "LEHTIHET", "MESSAOUDENE", "LOUAHEMM'SABAH", "ABDA", "ARIBI", "KHELIF", "ARAB", "ZAOUI", "BOUABDALLAH", "TOUAREF", "BENLATRECHE", "BENSLIMANE", "BOUDEMAGH", "BOUKERROU", "BOULAHBEL", "KERMICHE", "ABDELATIF", "BENTOUMI", "KRID", "ACHOUR", "BOUAOUDIA", "BOUNECHADA", "ZIANE", "GUESSOUM", "KOALAL", "MOUATS", "BELKHIRI", "SMAIL", "BECHIRI", "BENDJELLOUL", "BOUSSAHA", "HAMMOUDI", "NOURI", "OTMANI", "TAIBI", "ZEMOULI", "BENDAOUD", "BENHACINE", "KHELIFI", "TALHI", "KHEIDRI", "ATMANI", "BOURAI", "BRAHMI", "MANSOUR", "KHALFI", "LAMRI", "MESSALTI", "SAADNA", "SAYOUD", "CHEGHIB", "BENCHADI", "CHIOUKH", "MEGUELLATI", "BRAHMIA", "ABDELLI", "HAMZAOUI", "HARBI", "RACHEDI", "BENYEZZAR", "BOUCHAMA", "BOUGHACHICHE", "TIR", "KALLI", "METALLAOUI", "CHABANE", "LAMECHE", "LOUNIS", "RIMOUCHE", "YAHIACHERIF", "ZAIMEN", "MEKSEN", "NOUAR", "YOUNESBOUACIDA", "MADOUI", "OUCHENE", "TATAR", "HAMMADI", "NECIB", "REFES", "BACHTARZI", "BELALA", "BENMEBAREK", "BOUNAAS", "BOURSAS", "HABCHI", "REGHIOUA", "SEGHIRI", "BELLA", "BENALI", "BOUROUBA", "KOUSSA", "ZAZOUA", "SARROUB", "BENSAADA", "BAHLOULI", "BENSEHIL", "MEHENNI", "AMAMRA", "GRABSI", "REDJEL", "BERREDJEM", "BOUTARFA", "CHELBI", "KERKOUB", "MERAH", "ACHI", "ALLAM", "BELKADI", "BOUHOUCHE", "BOULFELFEL", "CHELGHOUM", "DJEHA", "GHIMOUZ", "HAMADA", "KHABABA", "SACI", "ZEGHAD", "TIGHIDET", "KERAGHEL", "KHARCHI", "KHELFI", "BALASKA", "BOUKERMA", "CHENIKI", "OUADDAH", "ZAOUALI", "AMIRI", "AYADAT", "BENDERRADJ", "ZAATOUT", "BELGACEM", "BAHRI", "BELHANI", "BELLILI", "BOULANOUAR", "LOUKIL", "AIMEUR", "BENABBAS", "BOUFENARA", "BOUOUDEN", "DEHIMI", "GUECHI", "KOUIDER", "REBAI", "ROUICHI", "ZAROUR", "ZEBIRI", "BENYOUNES", "KABOUCHE", "KELLIL", "ADIMI", "ADRAR", "IDIR", "CHERAGA", "BOUKRAA", "MESTAR", "BENYOUCEF", "BOUDEBZA", "DOB", "GUEDDAH", "SLIMANETICHTICH", "ABDAOUI", "BENTALEB", "DAAS", "KOUDA", "NEZZAR", "HAZOURLI", "TOUALBIA", "ALLOUCHE", "BELDI", "DJOUDI", "MERAD", "SAOULI", "BENBAKIR", "BENCHEIKHELHOCINE", "BENKARA", "BENMATTI", "BENNOUI", "BOUARROUDJ", "BOUDERSA", "BOUHALI", "BOULAHLIB", "BOUMEZBEUR", "CHEROUAT", "DEBBACHE", "DJAOU", "KEROUAZ", "MECHATI", "SOUALMIA", "TAOUTAOU", "ABDELLAOUI", "MEGHRICHE", "ZEGHLACHE", "HOCINI", "KACI", "TERKI", "ABDELLAH", "CHENITI", "DROUA", "MERICHE", "BOUMOUD", "BOUZEBRA", "MEKKIOU", "SOLTANE", "CHETTIBI", "ESSALHI", "TOUAHRI", "ZAMITI", "AKROUF", "BELFERKOUS", "MOUFFOK", "ALLEG", "SEHAILIA", "SLAMA", "ABIDI", "BENOUHIBA", "BOUACIDA", "BOUDJEMAA", "CHAOUCH", "DEKHIL", "FRIKH", "HADJAR", "HAMEL", "HANACHI", "LAKHAL", "MALKI", "MELIANI", "TEMIM", "ZAIM", "ABLA", "AMINEKHODJA", "AOUICHE", "AYACHE", "BENAHMED", "BENCHEIKHELFEGOUN", "BENTCHICOU", "BENTOBBAL", "BENZAID", "BOUANANE", "BOUCHEMAL", "CHEROUANA", "RAHMOUNI", "REDOUANE", "SAIGHI", "TOUIL", "ZELLAGUI", "BOURENANE", "FERRAH", "SAFERTABI", "FERDJALLAH", "KHOULALENE", "TIAB", "BELHIMEUR", "KEROUANI", "KRACHE", "NEGHIZ", "RADJAH", "TCHIER", "TITI", "ALIMESSIAD", "ALIDRA", "DAMECHE", "SID", "MESSADEK", "BELLOULA", "CHIKHI", "DJEFFALI", "HARIRECHE", "NOUIOUA", "BECHICHI", "BENKHELIFA", "BOUARICHA", "BOUCHAMI", "BOUKARI", "FELFLI", "FRIDJAT", "HAMDANE", "KETTACHE", "MEFTAH", "ZERARI", "BELHADEF", "BELILI", "BENDAHMANE", "BENHARKOU", "BENMALEK", "BENMOSTEFA", "BENSAAD", "BENADJAOUD", "BOUABELLOU", "BOUCENNA", "BOUDA", "BOUDJELLAL", "BOUDRA", "CHERIBET", "DJEBASSI", "HADJADJ", "HARKATI", "IDRI", "KECHKAR", "KHELASSI", "MAHDI", "MILES", "NEDJAR", "NIA", "SEBTI", "SEMRA", "SEMRI", "SERAOUI", "SIFI", "SOUALAH", "TEBBANI", "BENABDERRAHMANE", "BERKANI", "CHICOUCHE", "DJEBAILI", "ELAIHAR", "HATTAB", "ABBOU", "AMIROUCHE", "BENATTIA", "KHIMA", "ZAOUCHE", "CHIAH", "BRIHOUM", "GHEBGHOUB", "HAINE", "KESKES", "KHEBBACHE", "KHOUATRA", "LAISSAOUI", "NECHADI", "ROUIBAH", "SERRAR", "ZINE", "BEDDAI", "BELLARA", "BOUGHAZI", "CHEKKAT", "GAS", "LEMRABET", "LEULMI", "MATALLAH", "SIAFA", "ROUABHIA", "ZERGUINE", "BENKHALFALLAH", "DAMA", "LAMMARI", "LEFKIR", "MEGUEDEM", "TEBBI", "BERGHOUT", "BITAM", "HAOUES", "LOUCHENE", "BOUFARH", "BRAKNI", "DJOUAIFIA", "GHRIEB", "ABBACI", "BACHA", "BOUDOUR", "BOUKHARI", "CHEROUALI", "HAMADI", "LABIDI", "LASKRI", "MANSEUR", "SELMI", "TAHRAOUI", "ZANAT", "ZENATI", "ZENNADI", "ARZOUR", "BADAOUI", "BEHNAS", "BELAIB", "BELAIDI", "BELHOULA", "BENDADA", "BENDJABEUR", "BENHAFED", "BENHAMLA", "BENHAMOUDA", "BENMOUNAH", "BENSOUICI", "BENGHANEM", "BENZAOUI", "BOUCHAIR", "BOUHAFS", "BOUKIR", "BOULMERKA", "BOUSSEBOUA", "CHEBIRA", "CHIBANI", "DEBBAH", "DJEBLI", "DJEGHRI", "FERRAD", "GHAZI", "GUEDJALI", "HAMIMI", "IDIOU", "LADJABI", "LAHMAR", "MANAA", "MIMECHE", "MOUSSA", "OUACIF", "SAID", "SEGHIR", "ZATER", "ZEGHIB", "ZERMANE", "ZIOUANE", "CHEKHAB", "HIMEUR", "KOUACHI", "MAMERI", "TAAMALLAH", "TAGUIDA", "YAHI", "BABAAISSA", "BENDRIS", "BENHOCINE", "BERARMA", "BOUAMAMA", "BOUGUESSA", "BOUKEMOUCHE", "DJAFRI", "RHAMANI", "DALI", "GHARZOULI", "GHEDJATI", "GUEZATI", "HAMADOU", "HARFOUCHE", "BOURIDANE", "CHEMCHEM", "DJELLIT", "KHELOUFI", "MECHTER", "MEKIDECHE", "MEZAACHE", "NEKHOUL", "ROUIDI", "SELLAM", "SEMCHEDDINE", "SMARA", "SMATI", "TEBIBEL", "BOULFOUL", "BOUROUIS", "FADEL", "GUIRA", "HADJAMI", "HAMDOUCHE", "KHENCHOUL", "LESSAK", "NEFLA", "TEBBOUCHE", "CHIHEB", "GUERROUDJ", "HARIDI", "OUARTSI", "OULEDDIAF", "BELAYADI", "BENDERRADJI", "BOUBETRA", "DOUIBI", "GOUADER", "HANNICHE", "LAHOUASSA", "LOUNICI", "MOHAMADI", "OUSSALAH", "SEGUENI", "TIBOURTINE", "AOUFI", "BENAICHA", "BENBRAHIM", "BENTAYEB", "BOUMARAF", "CHAABNA", "CHERIF", "DJENANE", "BAYAZA", "BENARFA", "BENHADDA", "BOUALLEG", "CHIBI", "DAIRA", "DJELLAB", "DJOUINI", "HAFDALLAH", "KHEDIRI", "KOUIDRI", "MOUICI", "ROUAINIA", "ALLOUI", "AMIRAT", "ATTOUI", "BAHI", "BENOTMANE", "BOUBIR", "BOULEDROUA", "BOUMENDJEL", "DELLALOU", "DENDANI", "DJEBARI", "DJEDID", "KAHLI", "KOLLI", "LALLALI", "MAHIEDDINE", "MAZOUZI", "SAKRI", "SARI", "SEDIRA", "SOUICI", "AOUABDIA", "BELGUECHI", "BENARAB", "BENELMOUFFOK", "BENHAMADA", "BENMOHAMED", "BENRABAH", "BIOUD", "BOUFRAH", "BOUHROUR", "BOULKROUN", "CHELLI", "CHENNOUF", "DEHIMAT", "DENECHE", "FARAH", "FERGANI", "FERHAT", "HAMAMA", "HAMIDOUCHE", "KARAALI", "KEBAILI", "KHEBBAB", "KIMOUCHE", "LAKHDARA", "LOUADFEL", "MANA", "MENIAI", "MILLES", "MILOUDI", "RAHAL", "SELLAOUI", "SIMOUD", "TAFER", "ZERTAL", "ADNANE", "BAKHTI", "BAKIRI", "BELOUADAH", "BENABOUD", "ELBAHI", "HERIZI", "LADJROUD", "MAKRI", "SABRI", "AZRINE", "BENBAOUCHE", "BOUCHEBBAH", "CHOUDER", "DJOUADI", "IDIRI", "LALAOUI", "OUARET", "OUKACI", "DEKHILI", "DJILANI", "GUESSAS", "GUETTAF", "ALIANE", "BOUADJIMI", "DRAA", "FELTANE", "KECHACHA", "MANALLAH", "MESSAILI", "NAFA", "REGGAD", "REZIG", "SABER", "YAICI", "ZADI", "ZEDIOUI", "BENRAIS", "BOUCHOUL", "BOUGHLITA", "BOUHADJA", "BOUSNANE", "CHARIM", "HERMOUCHE", "LEBDIOUI", "MIHOUB", "MOHAMEDBOUTEBEN", "SAADALLAH", "ADJABI", "BENKIRAT", "BOUCHELAGHEM", "DAHEL", "BENZIOUCHE", "BOUAOUINA", "KHODRI", "LAYADI", "MEBAREK", "ZETCHI", "AHMANE", "BENSBAA", "GHARIB", "HOUAMEL", "HOUFANI", "KHELIFA", "KHOUNI", "MELAKHESSOU", "MENZER", "MESSAOUDANI", "SEMMACHE", "ZIDANI", "AYARI", "FADELEDDINE", "GHELIS", "GRAIRIA", "GUEHAIRIA", "HAOUAM", "LAHCENE", "ALLALI", "ALOUI", "AMRI", "AMROUCI", "BADJI", "BADR", "BELHOUCHET", "BOUKEF", "BOUKHATEM", "BOUREFIS", "DAHMANI", "DJABER", "DJEDDI", "DJEMILI", "FEDDAOUI", "GACEM", "GHERBI", "GOUASMI", "HABES", "KENOUNI", "KHEROUF", "KLAI", "LAFIFI", "MENACER", "MERADI", "NOUACER", "OUELAA", "REHAILIA", "SAYAH", "SELATNIA", "ABDELMOUMENE", "AFRIT", "BEGHIDJA", "BENCHAIB", "BENKAHOUL", "BENSEGUENI", "BERRAHAL", "BOUGHABA", "BOUKABACHE", "BOULAININE", "BOULKROUNE", "BOUTAGHANE", "CHAALAL", "CHARAOUI", "DJESSAS", "GUETTALA", "HANNACHE", "HASSANI", "KAHLOUCHE", "KAOUA", "KERMANI", "KHANFRI", "LAGGOUNE", "LAOUBI", "LEMMOU", "MALOUM", "MAMMERI", "MEHAZZEM", "MERZOUG", "MESBAH", "MIMOUNI", "NABTI", "NAILI", "NEMOUCHI", "OUILI", "RACHI", "TRAD", "BENZAIM", "BOUAOUICHE", "BOUDJABI", "BOUHADJAR", "CHADI", "GUERRAM", "KIRECHE", "MAZOUZ"
rh = "A+","A-","B+","B-","AB+","AB-","O+","O-"
cp = "Air Algerie", "Air Express Algeria", "Algerian Petroleum Institute", "Algerie Ferries", "Asmidal", "Cevital", "Djezzy", "Echourouk", "El Khabar", "El Massa", "El Moudjahid", "El Watan", "Entreprise nationale de Radiodiffusion sonore (ENRS)", "Hamoud Boualem", "Naftal", "National Company for Rail Transport (SNTF)", "Saidal", "SNVI", "Sonatrach", "Sonelgaz", "Star Aviation", "Tassili Airlines","SIDAR SARL", "PSG EURL", "CATERING CHEF EXPRESS SARL", "ASLAN CONSTRUCTION ET COMMERCE", "SAG ESSALEM SARL", "EL KENDI INDUSTRIES DU MEDICAM", "SHAPS SARL", "SAIDA EURL", "AL AMINE GARD SARL", "SGS CENTRE SARL", "SECUR SARL", "SSS ALGERIE SARL", "ELIT SPA", "SECURITE 2000 SARL", "UNIVERSAL TRANSIT SARL", "IDOINE EURL", "TRANSMEX SPA", "DYWIDAG INTERNATIONAL GMBH", "SOMABE", "TOYOTA ALGERIE SPA", "HYUNDAI MOTOR ALGERIE SPA", "BATIMETAL SPA", "SNC LAVALIN ALGERIE EURL", "Liste", "PEUGEOT ALGERIE SPA", "SARENS ALGERIE SARL", "MICHELIN ALGERIE SPA", "ARDIS SPA", "KIA MOTORS CORPORATION SARL", "EL KENDI INDUSTRIES DU MEDICAM", "TOYOTA ALGERIE SPA"
em = "@gmail.com", "@yahoo.fr", "@hotmail.fr", "@live.com", "@hotmail.com", "@yahoo.com", "@outlook.fr", "@outlook.com", "@live.fr", "@poste.dz"
ii = "109","119"
ig = "0001","0002","0003","0004","0005";"0006","0007","0008","0009","0011","0010"
pp = "11","12","13","14","15","16","17","18","19"
      
os.system("clear && clear")
print logo  
print menu 
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()  
def  select():
  try:
    choice = input("FDZ~# ")
    if choice == 1: 
      f = random.choice(fn)
      l = random.choice(ln)
      o = random.choice(oc)
      j = random.choice(jr)
      y = random.choice(yr)
      m = random.choice(mo)
      r = random.choice(rh)
      b = random.choice(bi)
      p = random.choice(bb)
      e = random.choice(ex)
      w = random.choice(cp)
      a = random.choice(em)
      k = random.choice(ii)
      h = random.choice(ig)
      q = random.choice(pp)

      d = "0123456789"
      n1 = 6
      n2 = 2
      n3 = 4
      n4 = 3
      n5 = 9
      n6 = 7
      s1 = "".join(random.sample(d,n1 ))
      s2 = "".join(random.sample(d,n3 ))
      s3 = "".join(random.sample(d,n3 )) 
      s4 = "".join(random.sample(d,n2 )) 
      s5 = "".join(random.sample(d,n4 ))
      s6 = "".join(random.sample(d,n5 ))
      s7 = "".join(random.sample(d,n6 ))
      
      os.system("clear")
      
      print " "
      print "{+} PERSONAL INFO {+}"
      print " "
      print "First Name : " + f
      print "Last Name : " + l
      print "Phone Number : " + o + s1
      print "Birthday : " + j + "/" + m + "/" + y
      print "RH : " + r 
      print " "
      print "{+} BANK INFO {+}"
      print " "
      print "Bank Name : CPA Bank"
      print "Visa Card : "+ b + " " + p + s4 + " " + s2 + " " + s3
      print "Expires : "+ m + "/" + e
      print "CVV : "+ s5
      print " "
      print "{+} PROFESSIONAL INFO {+}"
      print " "
      print "Company : "+ w
      print "Email : "+ f + l + y + a
      print "IDN Number : "+ k + s6 + s4 + h
      print "Passport Number : "+ q + s7
      print " "
      print " "
      quit()
    elif choice == 2:
      z = random.choice(ff)
      l = random.choice(ln)
      o = random.choice(oc)
      j = random.choice(jr)
      y = random.choice(yr)
      m = random.choice(mo)
      r = random.choice(rh)
      b = random.choice(bi)
      p = random.choice(bb)
      e = random.choice(ex)
      w = random.choice(cp)
      a = random.choice(em)
      k = random.choice(ii)
      h = random.choice(ig)
      q = random.choice(pp)
      z = random.choice(ff)

      d = "0123456789"
      n1 = 6
      n2 = 2
      n3 = 4
      n4 = 3
      n5 = 9
      n6 = 7
      s1 = "".join(random.sample(d,n1 ))
      s2 = "".join(random.sample(d,n3 ))
      s3 = "".join(random.sample(d,n3 )) 
      s4 = "".join(random.sample(d,n2 )) 
      s5 = "".join(random.sample(d,n4 ))
      s6 = "".join(random.sample(d,n5 ))
      s7 = "".join(random.sample(d,n6 ))
      
      os.system("clear")

      print " "
      print "{+} PERSONAL INFO {+}"
      print " "
      print "First Name : " + z
      print "Last Name : " + l
      print "Phone Number : " + o + s1
      print "Birthday : " + j + "/" + m + "/" + y
      print "RH : " + r 
      print " "
      print "{+} BANK INFO {+}"
      print " "
      print "Bank Name : CPA Bank"
      print "Visa Card : "+ b + " " + p + s4 + " " + s2 + " " + s3
      print "Expires : "+ m + "/" + e
      print "CVV : "+ s5
      print " "
      print "{+} PROFESSIONAL INFO {+}"
      print " "
      print "Company : "+ w
      print "Email : "+ z + l + y + a
      print "IDN Number : "+ k + s6 + s4 + h
      print "Passport Number : "+ q + s7
      print " "
      print " "
      quit()

    elif choice == 99:
      exit()
  except(KeyboardInterrupt):
    print ""
select()
