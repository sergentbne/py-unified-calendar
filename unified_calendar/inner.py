from .options import CalendarEventOptions, CalendarReminderOptions


class CalendarEvent:
    def __init__(self, options: CalendarEventOptions) -> None:
        self.options: CalendarEventOptions = options


class CalendarReminder:
    def __init__(self, options: CalendarReminderOptions) -> None:
        self.options: CalendarReminderOptions = options
