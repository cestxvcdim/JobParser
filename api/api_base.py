from abc import abstractmethod, ABC


class APIbase(ABC):
    @abstractmethod
    def get_vacancies(self, search_request: str) -> list:
        pass

    @abstractmethod
    def _pretty_view(self, data: list):
        pass

    @abstractmethod
    def get_top_n_vacancies(self, n: int, search_request: str) -> list:
        pass
