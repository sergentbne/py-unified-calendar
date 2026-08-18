from abc import ABC, abstractmethod

from Calendar.exceptions import ParserNotLoadedError
from Calendar.parsers import EventParser, ReminderParser

from .inner import CalendarEvent, CalendarReminder


class Calendar(ABC):
    def __init__(
        self,
        source: str | None = None,
        event_parser: EventParser | None = None,
        reminder_parser: ReminderParser | None = None,
    ) -> None:
        self._source: str | None = source
        self._events: list[CalendarEvent] = []
        self._reminders: list[CalendarReminder] = []
        self._is_authentificated: bool = False
        self._loaded_event_parser: EventParser | None = event_parser
        self._loaded_reminder_parser: ReminderParser | None = reminder_parser

    @abstractmethod
    def authentificate(self) -> None:
        pass

    @abstractmethod
    def is_authentificated(self) -> bool:
        pass

    def sync_calendar(self) -> None:
        self.pull_calendar()
        self.push_calendar()

    @abstractmethod
    def pull_calendar(self) -> None:
        pass

    @abstractmethod
    def push_calendar(self) -> None:
        pass

    def sync_reminders(self) -> None:
        self.pull_reminders()
        self.push_reminders()

    @abstractmethod
    def pull_reminders(self) -> None:
        pass

    @abstractmethod
    def push_reminders(self) -> None:
        pass

    def sync_all(self) -> None:
        self.pull_all()
        self.push_all()

    def pull_all(self) -> None:
        self.pull_calendar()
        self.pull_reminders()

    def push_all(self) -> None:
        self.push_calendar()
        self.push_reminders()

    @property
    def _event_parser(self) -> EventParser:
        if not self._loaded_event_parser:
            raise ParserNotLoadedError()
        return self._loaded_event_parser

    @_event_parser.setter
    def load_event_parser(self, parser: EventParser) -> None:
        self._loaded_event_parser = parser

    @property
    def _reminder_parser(self) -> ReminderParser:
        if not self._loaded_reminder_parser:
            raise ParserNotLoadedError()
        return self._loaded_reminder_parser

    @_reminder_parser.setter
    def load_reminder_parser(self, parser: ReminderParser) -> None:
        self._loaded_reminder_parser = parser

    def add_event(self, event: CalendarEvent | object):
        if isinstance(event, CalendarEvent):
            self._events.append(event)
        else:
            assert isinstance(self._event_parser, EventParser)
            parsed_event = self._event_parser.parse(event)
            self._events.append(parsed_event)

    def add_reminder(self, event: CalendarReminder | object):
        if isinstance(event, CalendarReminder):
            self._reminders.append(event)
        else:
            assert isinstance(self._event_parser, ReminderParser)
            parsed_event = self._reminder_parser.parse(event)
            self._reminders.append(parsed_event)
