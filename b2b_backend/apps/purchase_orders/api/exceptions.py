from django.utils.translation import ugettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException

__all__ = (
    'UserIsNotFacilityOwner',
)


class UserBuyerIsNotPurchaseOrderOwner(APIException):
    """ This User is Buyer but not owner of this Purchase Order

    Should return status_code HTTP 403

    """
    status_code = status.HTTP_403_FORBIDDEN
    default_code = 'you_are_not_purchase_order_owner'
    default_detail = _('You are not Purchase Order owner.')
