BMI_SHAPE = (
    (40, 'затлъстяване III степен'),
    (35, 'затлъстяване II степен'),
    (30, 'затлъстяване I степен'),
    (25, 'наднормено тегло'),
    (18.5, 'нормално тегло'),
    (16, 'леко недохранване'),
    (15, 'средно недохранване'),
    (0, 'тежко недохранване'),
)


def body_mass_index(weight, height):
    return round(weight / height ** 2, 1)


def shape_of(weight, height):
    bmi = body_mass_index(weight, height)
    for body_type in BMI_SHAPE:
        if bmi > body_type[0]:
            return body_type[1]
