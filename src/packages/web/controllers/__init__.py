from .healthy_controller import HealthyController
from .movies_controller import MovieController
from os import getenv

healthy_controller = HealthyController(getenv)
movies_controller = MovieController()
