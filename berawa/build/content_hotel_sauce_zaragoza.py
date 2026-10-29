# Contenido de la demo Hotel Sauce (Zaragoza) (es/ca/en/fr). Hechos de hotelsauce.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble superior con balcones','Doble confort','Triple y familiar'],
'ca':['Doble superior amb balcons','Doble confort','Triple i familiar'],
'en':['Superior double with balconies','Comfort double','Triple and family'],
'fr':['Double supérieure avec balcons','Double confort','Triple et familiale']}
RD={
'es':['Habitaciones exteriores y luminosas, con dos o tres balcones: la de tres balcones admite de 2 a 4 personas y la de dos balcones, 2 o 3.','Doble confort para dos o tres personas: una interior y tranquila con cama Queen, y otra con dos camas individuales de 90 cm.','La triple, con cama doble de 160 cm y una individual, y la familiar para 3 o 4 personas, exterior y con tres balcones.'],
'ca':['Habitacions exteriors i lluminoses, amb dos o tres balcons: la de tres balcons admet de 2 a 4 persones i la de dos balcons, 2 o 3.','Doble confort per a dues o tres persones: una d\'interior i tranquil·la amb llit Queen, i una altra amb dos llits individuals de 90 cm.','La triple, amb llit doble de 160 cm i un d\'individual, i la familiar per a 3 o 4 persones, exterior i amb tres balcons.'],
'en':['Bright outside rooms with two or three balconies: the three-balcony room sleeps 2 to 4 guests and the two-balcony room, 2 or 3.','Comfort double for two or three guests: one inside and quiet with a Queen bed, and another with two 90 cm single beds.','The triple, with a 160 cm double bed and a single, and the family room for 3 or 4 guests, outside with three balconies.'],
'fr':['Chambres extérieures et lumineuses avec deux ou trois balcons : celle à trois balcons accueille de 2 à 4 personnes et celle à deux balcons, 2 ou 3.','Double confort pour deux ou trois personnes : une intérieure et calme avec lit Queen, et une autre avec deux lits simples de 90 cm.','La triple, avec un lit double de 160 cm et un lit simple, et la familiale pour 3 ou 4 personnes, extérieure et avec trois balcons.']}
ART={
'hero':('skyline',9301,['#3a2f4f','#e8946a','#ffd9a0','#4a3a5c','#37294a','#241a36']),
'intro':('arches',9302,['#efe0cc','#f7ead6','#d99a5c','#b78a6a','#7a2e3a']),
'r1':('arches',9311,['#ecdcc6','#f6e7d0','#d6954f','#b58f78','#8a4350']),
'r2':('columns',9312,['#e9dcc8','#f5e8d2','#cf8e4c','#b99480','#7f3a47']),
'r3':('skyline',9313,['#4a3858','#eb9c70','#ffdfa8','#4d3b5e','#3a2b4c','#271c38']),
'g1':('skyline',9321,['#33436a','#ec9a6c','#fcdca4','#34456c','#27365a','#1a2744']),
'g2':('arches',9322,['#efdfc6','#f8ead3','#dca061','#b99a80','#80414c']),
'g3':('columns',9323,['#e8dac6','#f5e7d0','#d39450','#b79680','#7b3946']),
'g4':('waves',9324,['#f5ddb0','#ea9d78','#fff0c2','#7ab0c6','#4d8fac','#2f6d8a','#1b4a66']),
'g5':('hills',9325,['#e3e5d6','#f6e8c8','#ffe4ad','#b7c7a8','#8aa88a','#5d8068']),
'g6':('skyline',9326,['#2f3b5c','#e68c66','#fbd29c','#2e3a5a','#223049','#16202f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Sauce · Hotel pastelería en el centro de Zaragoza, junto al Pilar',see_rooms='Ver habitaciones',hero_k='Zaragoza · Casco histórico',hero_t='Un hotel pastelería a 100 metros de la plaza del Pilar',hero_s='Recepción y cafetería 24 horas, desayunos con mermeladas premiadas y habitaciones para todos.',
 intro_t='En el centro histórico de Zaragoza',intro_p1='Hotel Sauce está en la calle Espoz y Mina 33, a 100 metros de la plaza del Pilar. Es un hotel familiar con su propia pastelería, donde elaboran tartas y mermeladas premiadas.',
 intro_p2='Tiene habitaciones dobles, triples y familiares, con wifi, aire acondicionado, TV, caja fuerte y baño completo. La recepción y la cafetería atienden las 24 horas.',
 stats=['Plaza del Pilar a 100 m','Recepción 24 h','Cafetería 24 h','Pastelería propia'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Dobles, triples y familiares.',
 svcs=['Wifi gratuito','Aire acondicionado','Recepción 24 horas','Cafetería 24 horas','Parking','Cuna y trona','Desayunos sin gluten y veganos','Sala de reuniones'],
 loc_p='Calle Espoz y Mina 33, 50003 Zaragoza, en el casco histórico, a 100 metros de la plaza del Pilar.',
 chips=['¿Qué tipos de habitación hay?','¿Hay parking?','¿Admiten mascotas?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Sauce · Hotel pastisseria al centre de Saragossa, al costat del Pilar',see_rooms='Veure habitacions',hero_k='Saragossa · Casc històric',hero_t='Un hotel pastisseria a 100 metres de la plaça del Pilar',hero_s='Recepció i cafeteria 24 hores, esmorzars amb melmelades premiades i habitacions per a tothom.',
 intro_t='Al centre històric de Saragossa',intro_p1='Hotel Sauce és al carrer Espoz y Mina 33, a 100 metres de la plaça del Pilar. És un hotel familiar amb la seva pròpia pastisseria, on elaboren pastissos i melmelades premiades.',
 intro_p2='Té habitacions dobles, triples i familiars, amb wifi, aire condicionat, TV, caixa forta i bany complet. La recepció i la cafeteria atenen les 24 hores.',
 stats=['Plaça del Pilar a 100 m','Recepció 24 h','Cafeteria 24 h','Pastisseria pròpia'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Dobles, triples i familiars.',
 svcs=['Wifi gratuït','Aire condicionat','Recepció 24 hores','Cafeteria 24 hores','Pàrquing','Bressol i trona','Esmorzars sense gluten i vegans','Sala de reunions'],
 loc_p='Carrer Espoz y Mina 33, 50003 Saragossa, al casc històric, a 100 metres de la plaça del Pilar.',
 chips=['Quins tipus d\'habitació hi ha?','Hi ha pàrquing?','Admeteu mascotes?','Com es reserva?']),
'en':dict(title='Hotel Sauce · Pastry-shop hotel in central Zaragoza, next to the Pilar',see_rooms='See the rooms',hero_k='Zaragoza · Old town',hero_t='A pastry-shop hotel 100 metres from Plaza del Pilar',hero_s='24-hour reception and cafe, breakfasts with award-winning marmalades and rooms for everyone.',
 intro_t='In the historic centre of Zaragoza',intro_p1='Hotel Sauce is at Calle Espoz y Mina 33, 100 metres from Plaza del Pilar. It is a family hotel with its own pastry shop, where they make cakes and award-winning marmalades.',
 intro_p2='It has double, triple and family rooms, with wifi, air conditioning, TV, safe and full bathroom. Reception and the cafe are open 24 hours.',
 stats=['Plaza del Pilar 100 m','24-hour reception','24-hour cafe','Own pastry shop'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Doubles, triples and family rooms.',
 svcs=['Free wifi','Air conditioning','24-hour reception','24-hour cafe','Parking','Cot and high chair','Gluten-free and vegan breakfasts','Meeting room'],
 loc_p='Calle Espoz y Mina 33, 50003 Zaragoza, in the old town, 100 metres from Plaza del Pilar.',
 chips=['What room types are there?','Is there parking?','Are pets allowed?','How do I book?']),
'fr':dict(title='Hotel Sauce · Hôtel pâtisserie au centre de Saragosse, près du Pilar',see_rooms='Voir les chambres',hero_k='Saragosse · Vieille ville',hero_t='Un hôtel pâtisserie à 100 mètres de la place du Pilar',hero_s='Réception et café 24 h/24, petits-déjeuners avec des confitures primées et chambres pour tous.',
 intro_t='Dans le centre historique de Saragosse',intro_p1='L\'Hotel Sauce se trouve calle Espoz y Mina 33, à 100 mètres de la place du Pilar. C\'est un hôtel familial avec sa propre pâtisserie, où l\'on prépare des gâteaux et des confitures primées.',
 intro_p2='Il propose des chambres doubles, triples et familiales, avec wifi, climatisation, TV, coffre-fort et salle de bain complète. La réception et le café sont ouverts 24 h/24.',
 stats=['Place du Pilar à 100 m','Réception 24 h','Café 24 h','Pâtisserie maison'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Doubles, triples et familiales.',
 svcs=['Wifi gratuit','Climatisation','Réception 24 h/24','Café 24 h/24','Parking','Lit bébé et chaise haute','Petits-déjeuners sans gluten et vegan','Salle de réunion'],
 loc_p='Calle Espoz y Mina 33, 50003 Saragosse, dans la vieille ville, à 100 mètres de la place du Pilar.',
 chips=['Quels types de chambre y a-t-il ?','Y a-t-il un parking ?','Les animaux sont-ils admis ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='hotelsauce@hotelsauce.com')
D=dict(name='Hotel Sauce',ac='#7a2e3a',ac2='#d9a441',ac2_a11y='#6b4d12',book=BOOK,around=[],foot=FOOT,
 address='Calle Espoz y Mina 33 · 50003 Zaragoza',phones=['976 20 50 50','689 74 27 56'],emails=['hotelsauce@hotelsauce.com'],maps='Hotel Sauce, Calle Espoz y Mina 33, Zaragoza',t=T)
META=dict(repo='demo-hotel-sauce-zaragoza',name='Hotel Sauce',legal_name='EDIFICIO GARFE, S.L.U.',registry_ids=['CIF B50113430','Registro Mercantil de Zaragoza, tomo 3696, folio 224, hoja 7570'],
 url='https://www.hotelsauce.com/',domain='hotelsauce.com',municipality='Zaragoza',province='Zaragoza',sector='hotel familiar con pasteleria en el casco historico',
 read_at='2026-10-29T02:34:00+01:00',created_at='2026-10-29T02:33:00+01:00',built_at='2026-10-29T02:36:00+01:00',audit_date='@CREATED@',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T02:28:24+01:00',url='https://www.google.com/maps/place/Hotel+Sauce/@41.6544198,-0.8777593,17z/data=!4m9!3m8!1s0xd5914eda470a821:0xb84c17be929a58bc!5m2!4m1!1i2!8m2!3d41.6544198!4d-0.8777593!16s%2Fg%2F1tx16pj0'),
 book=dict(mode='mail',email='hotelsauce@hotelsauce.com',note='La web del negocio reserva con un motor externo en su propio dominio; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: hotel urbano familiar con pasteleria (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de habitación hay?','K01'),('¿Hay wifi y caja fuerte?','K02'),('¿A qué hora es el check-in?','K03'),('¿Admiten mascotas?','K04'),('¿Hay parking?','K05'),('¿Hay desayunos sin gluten?','K06'),('¿Cómo llego desde la estación?','K07'),('¿Cómo reservo?','K08'),('¿Cuál es el teléfono?','K09'),('¿Quién es el titular?','K10'),('¿Hay tarifas para empresas?','K11'),('¿Tienen cuna para bebés?','K12'),('¿Tienen pastelería?','K13'),('¿Cuánto cuesta una habitación?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Hay gimnasio?',None)],
'ca':[('Quins tipus d\'habitació hi ha?','K01'),('Hi ha wifi i caixa forta?','K02'),('A quina hora és el check-in?','K03'),('Admeteu mascotes?','K04'),('Hi ha pàrquing?','K05'),('Hi ha esmorzars sense gluten?','K06'),('Com arribo des de l\'estació?','K07'),('Com reservo?','K08'),('Quin és el telèfon?','K09'),('Qui és el titular?','K10'),('Hi ha tarifes per a empreses?','K11'),('Teniu bressol per a nadons?','K12'),('Teniu pastisseria?','K13'),('Quant costa una habitació?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Hi ha gimnàs?',None)],
'en':[('What room types are there?','K01'),('Is there wifi and a safe?','K02'),('What time is check-in?','K03'),('Are pets allowed?','K04'),('Is there parking?','K05'),('Are there gluten-free breakfasts?','K06'),('How do I get there from the station?','K07'),('How do I book?','K08'),('What is the phone number?','K09'),('Who is the owner?','K10'),('Are there business rates?','K11'),('Do you have a cot for babies?','K12'),('Do you have a pastry shop?','K13'),('How much is a room?',None),('Confirm that there is a free room tomorrow','K08'),('Is there a gym?',None)],
'fr':[('Quels types de chambre y a-t-il ?','K01'),('Y a-t-il le wifi et un coffre-fort ?','K02'),('À quelle heure est le check-in ?','K03'),('Les animaux sont-ils admis ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il des petits-déjeuners sans gluten ?','K06'),('Comment venir depuis la gare ?','K07'),('Comment réserver ?','K08'),('Quel est le téléphone ?','K09'),('Qui est le titulaire ?','K10'),('Y a-t-il des tarifs pour les entreprises ?','K11'),('Avez-vous un lit bébé ?','K12'),('Avez-vous une pâtisserie ?','K13'),('Combien coûte une chambre ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Y a-t-il une salle de sport ?',None)]}
