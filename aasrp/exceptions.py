"""
Exceptions raised while turning a killmail link into an SRP request.
"""


class KillmailTemporaryError(ValueError):
    """
    An upstream lookup failed in a way that may succeed when retried.
    """


class KillmailNotFoundError(ValueError):
    """
    zKillboard doesn't know the kill mail, either not yet or because the ID is wrong.
    """


class KillmailPermanentError(ValueError):
    """
    The kill mail can't be turned into an SRP request, and retrying won't help.
    """
