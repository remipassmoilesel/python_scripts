# -*- coding: utf-8 -*-

from typing import List, Optional, Tuple

from . import Square


class TypedObject():

    def sayHelloTo(self, name: str) -> str:
        hello = "Hello " + str(name) + " !"
        print(hello)
        return hello

    def useStringList(self, list: List[str]):
        print(list)

    def useSquare(self, square: Square):
        print(square)

    def optionalParam(self, optionalParam: Optional[str] = None):
        print(optionalParam)

    def multipleReturnType(self) -> Tuple[int, str]:
        return 0, "str"
