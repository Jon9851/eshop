from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    """
    this test is to check that the view_bag view is rendering
    the correct template when used
    """

    def test_get_view_wishlist(self):
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')