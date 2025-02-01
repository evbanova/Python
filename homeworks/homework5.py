import re


class Singleton(type):
    __instances = {}
   
    def __call__(cls, *args, **kwargs):
        if not cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class Santa (metaclass=Singleton):
    __wish_list = []
    __children = []
    __children_and_ages = {}
    __children_and_wishes = {}
    __most_desired = ''

    def __call__(self, child, _wish):
        wish = re.search(r'[\'\"]([\w\t])+[\'\"]', _wish)
        self.__wish_list.append(wish)
        if child.id() not in self.__children:
            self.__children.append(child.id())
            self.__children_and_ages[child.id()] = 1
        self.__children_and_wishes[child.id()] = wish

    def __matmul__(self, letter):
        child_id = re.search('(\s*)([0-9])+(\s*)', letter)
        wish = re.search(r'[\'\"]([\w\t])+[\'\"]', letter)
        self.__wish_list.append(wish)
        if child_id not in self.__children:
            self.__children.append(child_id)
            self.__children_and_ages[child_id] = 1
        self.__children_and_wishes[child_id] = wish

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num < len(self.__wish_list):
            result = self.__wish_list[self.num]
            self.num += 1
            return result
        else:
            raise StopIteration

    def __get_most_desired(self):
        count = {}
        for wish in self.__wish_list:
            count[wish] = self.__wish_list.count(wish)
        __most_desired = max(count, key=count.get)
        self.__wish_list = []
        self.__children = []
        self.__children_and_wishes = {}

    def xmas(self):
        for child in self.__children:
            if self.__children_and_ages[child] <= 5:
                if child not in self.__children_and_wishes:
                    kid(self.__most_desired)
                elif ():
                    kid(self.__children_and_wishes[child])
                else:
                    kid('coal')
            self.__children_and_ages[child] += 1
        self.__get_most_desired()


class Kid:
    pass

