import unittest
from api1 import search_film, getNameOfFilm, getFilmByID

class BestFilmsTests(unittest.TestCase):
    def test_searchFilm(self):
        test = search_film('мстители')['name']
        self.assertEqual(test, 'Мстители')
        test = search_film('криминальное чтиво')['country']
        self.assertEqual(test, 'США')

    def test_getNameOfFilm(self):
        self.assertEqual(getNameOfFilm(1309570), 'Человек-паук: Нет пути домой')
        self.assertEqual(getNameOfFilm(1294123), 'Матрица: Воскрешение')

    def test_getFilmById(self):
        test = getFilmByID(1309570)['name']
        self.assertEqual(test, 'Человек-паук: Нет пути домой')
        test = getFilmByID(1294123)['name']
        self.assertEqual(test, 'Матрица: Воскрешение')


if __name__ == '__main__':
    unittest.main()