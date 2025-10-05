from django.test import TestCase
from .models import ExampleModel

# test de modelos
class NombreTestCase(TestCase):
    def setUp(self):
        Nombre = ExampleModel.objects.create(name="xavier")
        return super().setUp()

    def test_names(self):
        xavier = ExampleModel.objects.get(name="xavier")
        self.assertEqual(xavier.name, "xavier")

# test de vista