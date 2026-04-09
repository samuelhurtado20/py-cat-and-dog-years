import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected_human_age: list[int]
) -> None:
    # ANN201: Anotamos el retorno como -> None para flake8
    assert get_human_age(cat_age, dog_age) == expected_human_age


def test_cat_age_increments_every_four_years_after_second_step() -> None:
    # Paso de 2 a 3 años humanos: 15 + 9 + 4 = 28
    assert get_human_age(28, 0)[0] == 3
    # Verificamos que con 27 siga siendo 2
    assert get_human_age(27, 0)[0] == 2


def test_dog_age_increments_every_five_years_after_second_step() -> None:
    # Paso de 2 a 3 años humanos: 15 + 9 + 5 = 29
    assert get_human_age(0, 29)[1] == 3
    # Verificamos que con 28 siga siendo 2
    assert get_human_age(0, 28)[1] == 2
