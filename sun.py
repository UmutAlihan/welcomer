import datetime
from astral import Astral



def is_shining(your_city):
	astral = Astral()
	astral.solar_depression = "civil"
	city = astral[your_city]
	timezone = city.timezone
	now = datetime.datetime.now()

	sun = city.sun(date=datetime.date(now.year,now.month,now.day), local=True)

	sunset = sun['sunset'].hour
	sunrise = sun['sunrise'].hour

	#if sun is not shining
	if(not(now.hour > sunrise and now.hour < sunset)):
		sun_state = False
	else:
		sun_state = True
	return sun_state


print(is_shining("Ankara"))
