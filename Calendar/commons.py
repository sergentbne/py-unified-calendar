from abc import ABC, abstractmethod

from .options import CalendarEventOptions, CalendarReminderOptions


class Calendar(ABC):
    def __init__(self, source: str | None = None) -> None:
        self._source: str | None = source
        self._events: list[CalendarEvent] = []
        self._is_authentificated: bool = False

    @abstractmethod
    def authentificate(self):
        pass

    def is_authentificated(self):
        return self._is_authentificated

    def sync_calendar(self):
        self.pull_calendar()
        self.push_calendar()

    @abstractmethod
    def pull_calendar(self):
        pass

    @abstractmethod
    def push_calendar(self):
        pass


class CalendarEvent:
    def __init__(self, options: CalendarEventOptions) -> None:
        self.options: CalendarEventOptions = options


class CalendarReminder:
    def __init__(self, options: CalendarReminderOptions) -> None:
        self.options: CalendarReminderOptions = options
