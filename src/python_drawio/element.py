from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element as XmlElement


class Element(ABC):

    def __init__(self):
        self.id = None

    def set_id(self, id: int) -> int:
        """
        :param id:
        :return: the amount of elements added
        """
        if self.id is not None:
            raise Exception("Id already set")
        self.id = str(id)

        return 1

    @abstractmethod
    def get_x(self) -> int:
        pass

    @abstractmethod
    def get_y(self) -> int:
        pass

    @abstractmethod
    def get_width(self) -> int:
        pass

    @abstractmethod
    def get_height(self) -> int:
        pass

    @abstractmethod
    def to_xml(self, parent_id: str = "1") -> list[XmlElement]:
        pass
