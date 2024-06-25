from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    radius = SecretInteger(Input(name="radius", party=party1))
    
    # Compute the area of the circle
    pi = 3.141592653589793
    area = pi * (radius ** 2)

    return [Output(area, "area_output", party1)]
