from city_functions import city_functions
def test_city_country():
    values=city_functions('Santiago','Chile')
    assert values=='Santiago, Chile'
