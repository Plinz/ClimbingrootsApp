from enum import Enum


class RouteType(Enum):
    AID = "AID"
    ALPIN = "ALPIN"
    BIGWALL = "BIGWALL"
    BOULDER = "BOULDER"
    DWS = "DWS"
    MULTIPITCH = "MULTIPITCH"
    SPORT = "SPORT"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Grade(Enum):
    F3 = ["3", "5.3"]
    F4a = ["4a", "5.4"]
    F4b = ["4b", "5.5"]
    F4c = ["4c", "5.6"]
    F5a = ["5a", "5.7"]
    F5b = ["5b", "5.8"]
    F5c = ["5c", "5.9"]
    F6a = ["6a", "5.10a"]
    F6aP = ["6a+", "5.10b"]
    F6b = ["6b", "5.10c"]
    F6bP = ["6b*", "5.10d"]
    F6c = ["6c", "5.11a"]
    F6cP = ["6c+", "5.11c"]
    F7a = ["7a", "5.11d"]
    F7aP = ["7a+", "5.12a"]
    F7b = ["7b", "5.12b"]
    F7bP = ["7b+", "5.12c"]
    F7c = ["7c", "5.12d"]
    F7cP = ["7c+", "5.13a"]
    F8a = ["8a", "5.13b"]
    F8aP = ["8a+", "5.13c"]
    F8b = ["8b", "5.13d"]
    F8bP = ["8b+", "5.14a"]
    F8c = ["8c", "5.14b"]
    F8cP = ["8c+", "5.14c"]
    F9a = ["9a", "5.14d"]
    F9aP = ["9a+", "5.15a"]
    F9b = ["9b", "5.15b"]
    F9bP = ["9b+", "5.15c"]
    F9c = ["9c", "5.15d"]

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)