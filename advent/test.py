def dlangue():
    langue = input("Veuillez entrer une langue :\n1 : BE\n2 : LU\n")
    while langue != "1" and langue != "2":
        langue = input("Veuillez entrer une langue :\n1 : BE\n2 : LU\n")
    if langue == "1":
     langue = "BE"
    else:
        langue = "LU"
    return (langue)

def dhfnumb(langue):
    if langue == "BE":
        hfnumb = "+32 (0) 3 808 5062"
    elif langue == "LU":
        hfnumb = "+352 27 86 28 99"
    return (hfnumb)

def dreason():
    reason = input("Veuillez entrer une raison :\n1 : Absent\n2 : Refus\n")
    reason = int(reason)
    while reason != 1 and reason != 2:
        reason = input("Veuillez entrer une raison :\n1 : Absent\n2 : Refus\n")
        reason = int(reason)
    if reason == 1:
     reason = "Absent"
    else:
        reason = "Refus"
    return (reason)

def dsms(reason, hfnumb, name):
    if reason == "Absent":
        sms = f"Hello {name}, notre chauffeur a tenté de vous livrer votre box HelloFresh aujourd'hui. Hélas, il n'a trouvé personne chez vous. Notre chauffeur a donc été contraint de rentrer avec votre box. Nous vous invitons à nous contacter au {hfnumb} avant 12:00 demain. Nous trouverons une solution ensemble. Bien à vous, L'équipe HelloFresh"
    elif reason == "Refus":
        sms = f"Hello {name} , malheureusement, nous n'étions pas informés que vous ne souhaitiez pas recevoir de box aujourd'hui. Vous pouvez suspendre votre livraison ou résilier votre abonnement chaque semaine. Il nous est impossible d'annuler votre commande après l'échéance. Effectivement, nous passons commande à l'avance auprès de nos fournisseurs. Nous vous invitons à nous contacter au {hfnumb} avant 12:00 demain. Nous trouverons une solution ensemble. Bien à vous, L'équipe HelloFresh"
    print(sms)
    return (sms)

def dmail(reason, hfnumb, name):
    if reason == "Absent":
        mail = f"Hello {name},\nnotre chauffeur a tenté de vous livrer votre box HelloFresh aujourd'hui. Hélas, il n'a trouvé personne chez vous. Notre chauffeur a donc été contraint de rentrer avec votre box. Nous vous invitons à nous contacter au {hfnumb} avant 12:00 demain. Nous trouverons une solution ensemble.\nNous avons essayé de vous joindre sur votre GSM mais sans succès, pouvez-vous nous le confirmer ?\nMerci de ne pas répondre à cet email \nBien à vous, L'équipe HelloFresh"
    elif reason == "Refus":
        mail = f"Hello {name},\nmalheureusement, nous n'étions pas informés que vous ne souhaitiez pas recevoir de box aujourd'hui. Vous pouvez suspendre votre livraison ou résilier votre abonnement chaque semaine. Il nous est impossible d'annuler votre commande après l'échéance. Effectivement, nous passons commande à l'avance auprès de nos fournisseurs. Nous vous invitons à nous contacter au {hfnumb} avant 12:00 demain. Nous trouverons une solution ensemble.\nNous avons essayé de vous joindre sur votre GSM mais sans succès, pouvez-vous nous le confirmer ?\nMerci de ne pas répondre à cet email \nBien à vous, L'équipe HelloFresh"
    print(mail)
    return (mail)


langue = dlangue()
hfnumb = dhfnumb(langue)
name = input("Nom du client : \n")
reason = dreason()
sms = dsms(reason, hfnumb, name)
mail = input("Voulez vous en version mail ?\n1 : Oui\nElse : non\n")
if mail == "1":
    mail = dmail(reason, hfnumb, name)


