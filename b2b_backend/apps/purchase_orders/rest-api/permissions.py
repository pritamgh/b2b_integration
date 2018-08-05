from rest_framework import permissions

from .exceptions import UserIsNotFacilityOwner

__all__ = ('IsFacilityOwner',)


class IsFacilityOwner(permissions.BasePermission):
    """Ensure that current user is facility owner

    For this it compares request.user.company and

    """

    def _check_permission(self, user, company):
        if company and user.company == company:
            return True
        raise UserIsNotFacilityOwner

    def has_permission(self, request, view):
        """Checks if user can create ``FacilityListing`` for specified facility
        """
        if view.action not in ['create']:
            return True

        company = request.user.company

        if not company:
            raise UserIsNotFacilityOwner

        # TODO: move this check into serializer
        # use PrimaryKeyRelatedField to filter input facilities
        # to show
        facility_id = request.data.get('facility')

        if company.facilities.filter(pk=facility_id).exists():
            return True

        raise UserIsNotFacilityOwner

    def has_object_permission(self, request, view, obj):
        """Checks permissions on ``FacilityListing`` object
        """
        company = obj.facility.company
        if company and request.user.company == company:
            return True
        raise UserIsNotFacilityOwner
