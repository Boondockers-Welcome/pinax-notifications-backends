from pinax.notifications.backends.base import BaseBackend as DefaultBaseBackend


class BaseBackend(DefaultBaseBackend):
    """
    Our custom base backend. Includes a deliver_bulk option which DefaultBaseBackend does not.
    """

    def deliver_bulk(self, recipients, sender, notice_type, extra_context):
        """
        Deliver a notification to the given recipient.
        """
        raise NotImplementedError()
