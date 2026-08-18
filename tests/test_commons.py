import datetime

import pytest
from unified_calendar.commons import Calendar, CalendarEvent, CalendarReminder
from unified_calendar.options import CalendarEventOptions, CalendarReminderOptions


class ConcreteCalendar(Calendar):
    def authentificate(self):
        self._is_authentificated = True

    def is_authentificated(self) -> bool:
        return self._is_authentificated

    def pull_calendar(self):
        pass

    def push_calendar(self):
        pass

    def pull_reminders(self):
        pass

    def push_reminders(self):
        pass

    def sync_calendar(self):
        pass


def test_calendar_initial_state():
    cal = ConcreteCalendar(source="google")
    assert cal._source == "google"
    assert cal._events == []
    assert cal.is_authentificated() is False


def test_calendar_authentificate_sets_state():
    cal = ConcreteCalendar()
    assert cal.is_authentificated() is False
    cal.authentificate()
    assert cal.is_authentificated() is True


def test_calendar_is_abstract():
    with pytest.raises(TypeError):
        Calendar()


def test_event_holds_options():
    start = datetime.datetime(2026, 1, 1, 9, 0)
    options = CalendarEventOptions(
        start=start, end=start + datetime.timedelta(hours=1), event_name="Meeting"
    )
    event = CalendarEvent(options)
    assert event.options is options


def test_reminder_holds_options():
    expire = datetime.datetime(2026, 1, 1, 9, 0)
    options = CalendarReminderOptions(expire_time=expire, reminder_name="Reminder")
    reminder = CalendarReminder(options)
    assert reminder.options is options
