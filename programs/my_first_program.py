from nada_dsl import *

def nada_main():
    jatin = Party(name="Jatin")  
    jayesh = Party(name="Jayesh") 
    anirudh = Party(name="Anirudh") 

    jatin_salary = SecretInteger(Input(name="jatin_salary", party=jatin))
    jayesh_salary = SecretInteger(Input(name="jayesh_salary", party=jayesh))
    anirudh_salary = SecretInteger(Input(name="anirudh_salary", party=anirudh))

    largest_position = (
        (jatin_salary > jayesh_salary).if_else(
            (jayesh_salary > anirudh_salary).if_else(Integer(0), Integer(2)),
            (anirudh_salary > jatin_salary).if_else(Integer(1), Integer(2))
        )
    )

    out = Output(largest_position, "largest_position", jatin)

    return [out]