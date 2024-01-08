from django.contrib.auth.mixins import UserPassesTestMixin

class AdminPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name='Admin'):
            return True
        return False
