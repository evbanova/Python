class  Material:
    def __init__(self, mass, density):
        self.mass = mass
        self.density = density
        self._volume = self.mass / self.density
        self._valid = True

    def validate(self):
         self._valid = False

    @property
    def volume(self):
        return self._volume
  

class Concrete(Material):
    def __init__(self, mass):
       super().__init__(mass, 2500)

    def __str__(self):
        return "Concrete"


class Brick(Material):
    def __init__(self, mass):
       super().__init__(mass, 2000)

    def __str__(self):
        return "Brick"


class Stone(Material):
    def __init__(self, mass):
       super().__init__(mass, 1600)

    def __str__(self):
        return "Stone"


class Wood(Material):
    def __init__(self, mass):
       super().__init__(mass, 600)

    def __str__(self):
        return "Wood"


class Steel(Material):
    def __init__(self, mass):
       super().__init__(mass, 7700)

    def __str__(self):
        return "Steel"


materials = {"Concrete" : Concrete, "Brick" : Brick, "Stone" : Stone, "Wood" : Wood, "Steel" : Steel}


class Factory:
    _instances = []

    def __init__(self):
        self._total_volume = 0
        self._materials = []
        Factory._instances.append(self)

    def __call__(self, *args, **kwargs):
        if bool(args) == bool(kwargs):
            raise ValueError("greshkaaaa soriii")
        if bool(kwargs):
            result = []
            for key, value in kwargs.items():
                if key not in materials:
                    raise ValueError("greshkaaaa soriii")
                current = materials[key](value)
                if current._valid:
                    self._total_volume += current.volume
                result.append(current)
                self._materials.extend(result)
            return tuple(result)
        if bool(args):
            mass = 0
            density = 0
            count = []
            number = 1
            names = []
            for material in args:
                if not material._valid:
                    raise AssertionError("greshkaaaa soriii")
                material.validate()
                mass += material.mass
                density += material.density
                names.append(str(material))
                self._total_volume += material.volume
            for met, val in materials.items():
                counter = 0
                for material in args:
                    if met in str(material) and met != str(material):
                        counter += 1
                count.append(counter)
            for c in count:
                if c != 0:
                    number = 0
                    break
            for c in count:
                if c != 0:
                    number += 1
            names = sorted(names)
            class_name = "_".join(names)
            if class_name in materials:
                Fusion = materials[class_name]
            else:
                Fusion = type(class_name, (Material,), 
                              {"__init__": lambda self, *_args, **kwargs: Material.__init__(self, mass, density / number)})
                materials[class_name] = Fusion
            fused_material = Fusion(mass)
            self._materials.append(fused_material)
            return Fusion()
            
    def can_build(self, needed_volume):
        return self._total_volume >= needed_volume 

    @classmethod
    def can_build_together(cls, needed_volume):
         total_volume = sum(mat.volume for inst in cls._instances for mat in inst._materials if mat._valid)
         return total_volume >= needed_volume 


