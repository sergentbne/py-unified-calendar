from pathlib import Path
from typing import final


@final
class InvalidEmailError(Exception):
    def __init__(self, invalid_emails: list[str]):
        self.invalid_emails = invalid_emails
        super().__init__(
            f"One or more provided email is invalid: {', '.join(invalid_emails)}"
        )


@final
class LocationNotFoundError(Exception):
    def __init__(
        self,
        location: str,
    ):

        self.location = location
        super().__init__(
            f"The requested location has not been found: {location} has not been found"
        )


@final
class InvalidUrlError(Exception):
    def __init__(
        self,
        url: str,
    ):
        self.url = url
        super().__init__(f"The inputed email is invalid: {url} is invalid")


@final
class InvalidAttachementsError(Exception):
    def __init__(
        self,
        invalid_attachements: list[Path],
    ):
        self.invalid_attachements = invalid_attachements
        super().__init__(
            f"One or more than one attachement(s) is invalid: {', '.join(str(x) for x in invalid_attachements)}"
        )


@final
class ParserNotLoadedError(Exception):
    def __init__(
        self,
    ):
        super().__init__(
            "The parser was not loaded before trying to add a event/reminder to the calendar."
            + " Consider adding it with the `load_parser` method or assign it at initialisation."
        )
