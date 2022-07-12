import unittest

from domain.main import Year
from random import randint
class RepoExc(Exception):
    pass
class Repository():
    def __init__(self):
        self._year=Year(1,0,0,100,1000,3,200,20,2800)
        self._planted_land=0
    def buy_sell(self,nr):
        """
        buy and sell function verify if the land cand be sold/bought and update the land and the grain stock
        :param nr: the number (negative if you want to sell) positive if you wANT TO BUY

        """
        nr=int(nr)

        if nr<0:
            if int(-nr)>int(self._year._land):
                raise RepoExc("Cant sell more land than you have!")


        if nr<0:
            self._year._grain_stock+=(-nr)*self._year._land_price

        if int(nr) * int(self._year._land_price) > int(self._year._grain_stock):
            raise RepoExc("Cant buy more land than you have grain for!")
        if int(nr)>0:
            self._year._grain_stock += (-nr) * self._year._land_price

        self._year._land+=nr


    def feed(self,nr):
        """
        checks if we have enought grain to feed the people if so we update the grain stock
        :param nr: the number os grain units you want to feed the population

        """
        ok=True
        self._year._people_starved=0
        self._year._new_people=0
        if int(nr)>int(self._year._grain_stock):
            raise RepoExc("Cant feed people with grain you do not have!")
        if nr//20>=self._year._population and nr%20==0:
            self._year._new_people+=randint(0,10)
            self._year._population +=self._year._new_people
        else:
            self._year._people_starved=(self._year._population)-nr//20
            if self._year._people_starved>=(self._year._population//2):
                self._year._population -= self._year._people_starved
                ok=False

            self._year._population-=self._year._people_starved


        self._year._grain_stock-=nr
        if ok==False:
            return False
    def plant(self,nr):
        """
        plant nr acres of land updates the grain stock and check if we can plant grain on that many lands
        :param nr: the number of acres of land

        """
        self._planted_land=nr
        if int(nr)>int(self._year._land):
            raise RepoExc("Cant plant more acres than you have!")

        if int(nr)>int(self._year._grain_stock):
            raise RepoExc("Cant plant grain that you do not have!")
        self._year._grain_stock-=nr
    def price(self):
        """
        just generates a random land price

        """
        self._year._land_price=randint(15,25)
    def win_or_lose(self):
        if int(self._year._population>100) and int(self._year._land)>1000:
            return True
        return False
    def harvest(self):
        self._year._grain_stock+=self._planted_land*self._year._harvest
        self._year._harvest=randint(1,6)

class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository()

    def test_but_and_sell(self):
        self._repo.buy_sell(-100)
        self.assertEqual(self._repo._year._grain_stock, 4800)
        self.assertEqual(self._repo._year._land,900)
        self._repo.buy_sell(100)
        self.assertEqual(self._repo._year._land, 1000)
        self.assertEqual(self._repo._year._grain_stock,2800)
        self.assertRaises(RepoExc,self._repo.buy_sell,9999)
    def test_plant(self):
        self.assertRaises(RepoExc, self._repo.plant, 1001)
        self._repo.plant(800)
        self.assertEqual(self._repo._year._grain_stock,2000)
    def test_feed(self):
        self.assertRaises(RepoExc, self._repo.feed, 3000)
        self._repo.feed(2000)
        self.assertEqual(self._repo._year._grain_stock, 800)

    def tearDown(self):
        self._repo=None


