import unittest
from facturation import *

#notre classe de test herite de la classe unittest.TestCase
class FacturationTestCase (unittest.TestCase):

    #pour tester l'instanciation de la classe facturation 
    def testFacturationIsInstanceOfFacturation(self):
        p = [['quinine', 300], ['paracetamole', 100], ['albendazole', 250]]
        q = [1, 2, 3]
        patient = 'Jonh Doe'
        h = "Centre Hospitalier universitaire"
        date = '20/02/2021'
        solde = 3000
        f = Facturation(patient, h, p, q, date, solde)
        self.assertIsInstance(f, Facturation)
    
    #pour tester le cas ou l'un des montants est negatif
    def testFacturationMontantNegatif(self):
        p = [['quinine', -100], ['paracetamole', 100], ['albendazole', 250]]
        q = [1, 2, 3]
        patient = 'Jonh Doe'
        h = "Centre Hospitalier universitaire"
        date = '20/02/2021'
        solde = 100000
        f = Facturation(patient, h, p, q, date, solde)
        self.assertEqual(f.facturer(), "montant negatif")

    #pour tester le cas ou le total est negatif
    def testFacturationTotalNegatif(self):
        p = [['quinine', -10000], ['paracetamole', 100], ['albendazole', 250]]
        q = [1, 2, 3]
        patient = 'Jonh Doe'
        h = "Centre Hospitalier universitaire"
        date = '20/02/2021'
        solde = 100000
        f = Facturation(patient, h, p, q, date, solde)
        self.assertEqual(f.facturer(), "total negatif")

    #pour tester le cas ou le totale a payer est inferieur au total minimale 
    def testFacturationMontantMinimale(self):
        p = [['quinine', 10], ['paracetamole', 10], ['albendazole', 20]]
        q = [1, 2, 3]
        patient = 'Jonh Doe'
        h = "Centre Hospitalier universitaire"
        date = '20/02/2021'
        solde = 102000
        f = Facturation(patient, h, p, q, date, solde)
        self.assertEqual(f.facturer(), "Montant total inferieur au montant minimale")

    #pour tester le cas ou toutes les conditions sont valides
    def testFacturationValide(self):
        p = [['quinine', 1000], ['paracetamole', 100], ['albendazole', 250]]
        q = [1, 2, 3]
        patient = 'Jonh Doe'
        h = "Centre Hospitalier universitaire"
        date = '20/02/2021'
        solde = 10000108768465132
        f = Facturation(patient, h, p, q, date, solde)
        self.assertEqual(f.facturer(), "facturation reussite")

    #pour tester le cas ou le solde du client est insuffisant
    def testFacturationSoldeInsuffisant(self):
        p = [['quinine', 10000], ['paracetamole', 10000], ['albendazole', 2500]]
        q = [1, 2, 3]
        patient = 'Jonh Doe'
        h = "Centre Hospitalier universitaire"
        date = '20/02/2021'
        solde = 10
        f = Facturation(patient, h, p, q, date, solde)
        self.assertEqual(f.facturer(), "solde insufisant")
    
if __name__ == '__main__':
    unittest.main()