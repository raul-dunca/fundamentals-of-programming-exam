class Year():
    def __init__(self,nr,p_s,p_c,population,land,harvest,rat,land_p,g_s):
        self._year=nr
        self._people_starved=p_s
        self._new_people=p_c
        self._population=population
        self._land=land
        self._harvest=harvest
        self._rats=rat
        self._land_price=land_p
        self._grain_stock=g_s

    def __str__(self):
        return "In year "+str(self._year)+" , "+str(self._people_starved)+" people starved."+"\n"+str(self._new_people)+" people came to the city."+"\n"+"City population is "+str(self._population)+"\n"+"City owns "+str(self._land)+" acres of land."+"\n"+"Harvest was "+str(self._harvest)+" units per acre."+"\n"+"Rats ate "+str(self._rats)+" units."+"\n"+"Land price is "+str(self._land_price)+" units per acre."+"\n"+"Grain stock are "+str(self._grain_stock)+" units"




