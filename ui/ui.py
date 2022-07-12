from repository.repo import Repository
from repository.repo import RepoExc
import copy
class UI():
    def __init__(self):
        self._repo=Repository()

    def start(self):
        f=True
        while True:
            year = copy.copy(self._repo._year)

            try:

                print(self._repo._year)
                print("\n")
                if f==False:
                    print("The game is over over half of your population starved!")
                    break

                if self._repo._year._year==5:
                    p=self._repo.win_or_lose()
                    if p==True:
                        print("GAME OVER. You did very well. Good job!")
                        break
                    else:
                        print("GAME OVER. You did not do well.")
                        break

                print("Acres to buy/sell(+/-)-> ")
                inp=input()



                self._repo.buy_sell(int(inp))

                print("Units to feed the population -> ")
                i=input()
                f=self._repo.feed(int(i))
                print("Acres to plant -> ")
                inpt = input()
                self._repo.plant(int(inpt))

                self._repo.price()

                self._repo.harvest()
                self._repo._year._year+=1
            except RepoExc as re:

                self._repo._year=year
                print(re)
            except ValueError as ve:
                self._repo._year = year
                print(ve)

u=UI()
u.start()
