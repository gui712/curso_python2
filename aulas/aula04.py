# valores Padrão


def soma(x,y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x+y+z )
    else:
        print(f'{x=}  {y=}', x+y)


soma(1,2)
soma(5,3)
soma(100, 150)
soma(7,9,0)