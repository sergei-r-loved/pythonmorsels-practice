from collections import UserDict
class EasyDict():

    def __init__(self, mapping={}, **kwargs):
        self.__dict__.update(mapping)
        self.__dict__.update(**kwargs)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, item):
        setattr(self, key, item)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EasyDict):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def get(self, key, default=None):
        return getattr(self, key, default)


person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})

person.location = "Portland"
print(person.location)
person['location'] = "pedo"
print(person['location'])
person['city'] = 'Saratov'
print(person.city)
person.district = 'Zavod'
print(person.district)
person.c = 4
# print(person.mapping)
person = EasyDict(name="Trey Hunner", location="San Diego")
print(person.name)