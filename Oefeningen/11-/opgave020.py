naam = input('naam:')
wachtwoord = input('wachtwoord:')

bestand = open("Account.txt", "wt")
bestand.write(f"{naam}\n")
bestand.write(f"{wachtwoord}\n")
bestand.close()