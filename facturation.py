class Facturation:
    totalMin = 1000 #le montant minimale tu totale a payer pour chaque facture
    total = 0 # total a payer initialise a zero 
    """
        Proprietes  de la classe Facturation:
        -produits:  liste des produits avec leurs prix unitaires
        -quantites: liste des quantites des produits
        -patient:   nom du patient
        -hopitale:  nom de l'hopitale
        -date:      date de l'operation de facturation
        -solde:     solde du patient
        -totalMin:  montant minimale 
    """
    def __init__(self, patient, hopitale, produits, quantites, date, soldeClient):
        assert isinstance(patient, str)             #doit etre une chaine de caracteres
        assert isinstance(hopitale, str)            #doit etre une chaine de caracteres
        assert isinstance(date, str)                #doit etre une chaine de caracteres
        assert isinstance(soldeClient, int)         #doit etre un entier
        assert isinstance(produits, list)           #doit etre une liste
        assert isinstance(quantites, list)          #doit etre une liste
        assert len(produits) == len(quantites)      #doivent etre de mm longueur
        
        self.patient = patient
        self.hopitale = hopitale
        self.produits = produits
        self.quantites = quantites
        self.date = date
        self.soldeClient = soldeClient
    
    def calculTotal(self):
        result = 0
        for i in range(len(self.produits)):
            result += self.quantites[i] * self.produits[i][1]
        return result
    
    def facturer(self):
        self.total = 0
        for i in range(len(self.produits)):
            self.total += self.quantites[i] * self.produits[i][1]
        # print(self.total)
        if self.total < 0:                       # si le total a payer est negatif
            return "total negatif"
        for p in self.produits:
            if p[1] < 0:                    # si l'un des montants est negatif
                return "montant negatif"
        if self.total < self.totalMin:      #si le solde est insuffisant
            return "Montant total inferieur au montant minimale"
        if self.total > self.soldeClient:   #si le total n'atteind pas le seil
            return "solde insufisant"
        return "facturation reussite"

    def afficher(self):
        print("Hopitale: "+self.hopitale+"\t client: "+self.patient)
        print("qantites \t prix Unitaires \t total")
        t = 0
        for i in range(len(self.produits)):
            print(self.quantites[i] +" \t " + self.produits[i][1] + " \t " + self.produits[i][0])
            t += self.quantites[i] * self.produits[i][1]
        print("Total a payer: \t" + t)