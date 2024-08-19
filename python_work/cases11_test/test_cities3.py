from city_functions3 import city_functions
def test_city_country():
    values=city_functions('Santiago','Chile')
    assert values=='Santiago, Chile - population 1000000'