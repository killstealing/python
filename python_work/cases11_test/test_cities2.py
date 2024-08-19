from city_functions2 import city_functions
def test_city_country():
    values=city_functions('Santiago','Chile',1000000)
    assert values=='Santiago, Chile - population 1000000'