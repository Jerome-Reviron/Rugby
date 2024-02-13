import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

def count_nb_line():
    return 117389

def count_nb_column():
    return 10

class CustomTestResult(unittest.TestResult):
    def __init__(self, *args, **kwargs):
        """
        Initialisation de la classe CustomTestResult.
        Cette classe hérite de unittest.TestResult et ajoute des fonctionnalités de suivi personnalisées.

        Args:
            *args: Arguments positionnels.
            **kwargs: Arguments clés-valeurs.
        """
        super().__init__(*args, **kwargs)
        self.successful_tests = []
        self.failed_tests = []

    def addSuccess(self, test):
        """
        Méthode appelée lorsqu'un test réussit.

        Args:
            test (TestCase): Objet de test réussi.
        """
        super().addSuccess(test)
        self.successful_tests.append(test)

    def addFailure(self, test, err):
        """
        Méthode appelée lorsqu'un test échoue.

        Args:
            test (TestCase): Objet de test échoué.
            err (tuple): Tuple contenant les détails de l'erreur.
        """
        super().addFailure(test, err)

        # Formater le message d'erreur pour l'ajouter à la liste
        error_message = str(err[1])
        self.failed_tests.append((test, error_message))

class TestClub(unittest.TestCase):
    def setUp(self):
        """
        Méthode setUp : exécutée avant chaque test.
        Initialise les ressources nécessaires pour le test.
        """
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")

    def test_count_nb_line(self):
        """
        Test pour vérifier le nombre de lignes dans app_club.
        """
        count = count_nb_line()
        element = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p")
        count_text = element.text
        actual_count = int(count_text.split(":")[-1].strip())
        self.actual_count = actual_count
        self.assertEqual(count, actual_count, f"Le nombre de lignes dans app_club est {actual_count}, et non pas {count}")

    def test_nb_columns(self):
        """
        Test pour vérifier le nombre d'éléments <tr> dans le thead de la table.
        """
        count = count_nb_column()
        tr_elements = self.driver.find_elements(By.CSS_SELECTOR, "body > div > table > thead > tr")
        actual_count = sum(len(tr.find_elements(By.TAG_NAME, "th")) for tr in tr_elements)
        self.actual_count = actual_count
        # Vérifier que le nombre d'éléments <tr> dans le thead est égal à la valeur attendue
        self.assertEqual(count, actual_count, f"Le nombre de lignes dans app_club est {actual_count}, et non pas {count}")

    def tearDown(self):
        """
        Méthode tearDown : exécutée après chaque test.
        Ferme les ressources utilisées pour le test.
        """
        self.driver.quit()

if __name__ == "__main__":
    # Utilisez la classe CustomTestResult pour obtenir des informations sur les résultats des tests
    test_result = CustomTestResult()

    # Créez un test loader
    test_loader = unittest.TestLoader()

    # Chargez les tests
    test_suite = test_loader.loadTestsFromTestCase(TestClub)

    # Exécutez les tests avec le résultat personnalisé
    test_suite.run(test_result)

    # Affichez la liste des tests réussis et échoués
    print("Tests réussis:")
    for test in test_result.successful_tests:
        print(f"  {test.id()} - la valeur est {test.actual_count}")

    print("\nTests échoués:")
    for test, error_message in test_result.failed_tests:
        print(f"  {test.id()} - {error_message}")

# assertEqual(first, second, msg=None)
# Vérifie que first est égal à second.

# assertNotEqual(first, second, msg=None)
# Vérifie que first n'est pas égal à second.

# assertTrue(expr, msg=None)
# Vérifie que expr est évalué comme True.

# assertFalse(expr, msg=None)
# Vérifie que expr est évalué comme False.

# assertIsNone(obj, msg=None)
# Vérifie que obj est None.

# assertIsNotNone(obj, msg=None)
# Vérifie que obj n'est pas None.

# assertIn(member, container, msg=None)
# Vérifie que member est dans container.

# assertNotIn(member, container, msg=None)
# Vérifie que member n'est pas dans container.

# assertIs(instance, cls, msg=None)
# Vérifie que instance est une instance de la classe cls.

# assertIsNot(instance, cls, msg=None)
# Vérifie que instance n'est pas une instance de la classe cls.

# assertRaises(exc, callable, *args, **kwargs)
# Vérifie que l'appel de callable(*args, **kwargs) génère une exception de type exc.

# assertAlmostEqual(first, second, places=None, msg=None, delta=None)
# Vérifie que first est presque égal à second jusqu'au nombre de décimales spécifié par places ou dans la limite du delta.

# assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)
# Vérifie que first n'est pas presque égal à second jusqu'au nombre de décimales spécifié par places ou dans la limite du delta.