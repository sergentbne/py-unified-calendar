from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import override

from .inner import CalendarEvent, CalendarReminder


class Parser(ABC):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    @abstractmethod
    def parse(unparsed_data: object) -> object:
        pass

    @staticmethod
    @abstractmethod
    def batch_parse(list_of_unparsed_data: Sequence[object]) -> Sequence[object]:
        pass


class ReminderParser(Parser, ABC):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    @abstractmethod
    @override
    def parse(unparsed_data: object) -> CalendarReminder:
        pass

    @staticmethod
    @abstractmethod
    @override
    def batch_parse(
        list_of_unparsed_data: Sequence[object],
    ) -> Sequence[CalendarReminder]:
        pass


class EventParser(Parser, ABC):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    @abstractmethod
    @override
    def parse(unparsed_data: object) -> CalendarEvent:
        pass

    @staticmethod
    @abstractmethod
    @override
    def batch_parse(list_of_unparsed_data: Sequence[object]) -> Sequence[CalendarEvent]:
        pass
