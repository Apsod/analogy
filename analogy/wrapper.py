from abc import ABC, abstractmethod


class Wrapper(ABC):
    @abstractmethod
    def analogy(self, query):
        """
        analogy query answering method
        :param query: Analogy query of the form A:B::X
        :return: Y that fits the query A is to B as X is to Y
        """
        pass

    @abstractmethod
    def __contains__(self, item):
        """
        item membership function.
        :param item: item
        :return: if the item has a representation in the model
        """
        pass

    @staticmethod
    @abstractmethod
    def load(path):
        """
        Loads the model from file.
        :param path: path to file
        :return:
        """
        pass

