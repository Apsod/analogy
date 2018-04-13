from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def analogies(self, queries):
        """
        Analogy query answering method. For efficiency this should handle batched queries of the form
        [(A, B, X)]
        :param queries: Analogy queries of the form A:B::X
        :return: Y that fits the query A is to B as X is to Y
        """
        pass

    @abstractmethod
    def members(self, items):
        """
        Item membership function. For efficiency this should handle batched queries of the form [W]
        :param items: items
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

