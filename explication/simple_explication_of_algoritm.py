# Imaginează-ți o Grădină cu Flori
#
# Gândește-te la o grădină în care vrei să plantezi flori. Fiecare floare are nevoie de anumite condiții pentru a crește. De exemplu:
#
# 	•	Floarea roșie are nevoie de soare și apă.
# 	•	Floarea albastră are nevoie de umbră și îngrășământ.
# 	•	Floarea galbenă are nevoie de apă și umbră.
#
# Aici, florile reprezintă clauze, iar condițiile lor (soare, apă, umbră, îngrășământ) reprezintă variabilele pe care trebuie să le alegi.
#
# Scopul
#
# Scopul tău este să găsești o combinație de condiții (adevărat sau fals) astfel încât toate florile să crească frumos. Acesta este un joc de a decide cum să îngrijim grădina, și asta fac algoritmii SAT!
#
# Algoritmii și Cum Lucrează Ei
#
# 	1.	DPLL (Davis-Putnam-Logemann-Loveland):
# 	•	Imaginează-ți că DPLL este un grădinar care începe prin a alege o floare și a vedea ce condiții îi trebuie.
# 	•	Dacă floarea crește bine cu condițiile alese, grădinarul merge mai departe la următoarea floare.
# 	•	Dacă o floare nu crește, grădinarul schimbă o condiție (de exemplu, decide că floarea roșie va primi mai mult soare) și încearcă din nou.
# 	•	Dacă găsește o combinație care funcționează pentru toate florile, a câștigat!
# 	2.	CDCL (Conflict-Driven Clause Learning):
# 	•	CDCL este un grădinar și mai deștept! Acesta învață din greșelile sale.
# 	•	Dacă o floare nu crește și află că e din cauza unei anumite condiții (de exemplu, floarea roșie nu-i place să fie în umbră), CDCL își va aminti asta pentru viitor și nu va mai face aceeași greșeală.
# 	•	Așa că, de fiecare dată când are o problemă, își amintește ce a învățat și încearcă să facă lucrurile diferit.
# 	3.	Max-SAT:
# 	•	Max-SAT este un grădinar care știe că nu toate florile pot crește, așa că decide să facă tot posibilul să aibă cele mai multe flori sănătoase.
# 	•	El alege combinații de condiții pentru a vedea câte flori pot crește.
# 	•	Chiar dacă unele flori nu cresc, grădinarul încearcă să aibă cât mai multe flori sănătoase, nu neapărat toate.
# 	4.	GSAT (Greedy SAT):
# 	•	GSAT este un grădinar care începe cu o combinație de condiții aleatorii pentru flori.
# 	•	Dacă vede că o floare nu crește, va schimba rapid o condiție pentru a încerca să o facă să crească.
# 	•	Acest grădinar își folosește instinctele și încearcă diferite combinații până când găsește una care face cele mai multe flori să crească bine.
#
# Concluzie
#
# Deci, toți acești algoritmi sunt ca niște grădinari care încearcă să găsească cea mai bună combinație de condiții pentru a face florile să crească. Fiecare are o strategie diferită, dar scopul final este același: să aibă o grădină plină de flori frumoase!