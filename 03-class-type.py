# class type


class Human:
    def age(self) -> int:
        return 26


jaekwan: Human = Human()


def ins_age(ins: Human) -> int:
    return ins.age()


print(ins_age(jaekwan))
