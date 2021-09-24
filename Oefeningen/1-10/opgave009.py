naam = input("Wat is uw naam?")
tickets = int(input("Hoeveel tickets wilt u kopen?"))
prijspticket = int(input("Wat is de prijs per ticket?"))
print(f"""Beste {naam}
Bedankt voor uw bestelling van {prijspticket} tickets!
De totale prijs bedraagt {prijspticket*tickets} euro.""")
