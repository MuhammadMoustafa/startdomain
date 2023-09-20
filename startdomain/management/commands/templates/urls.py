from rest_framework import routers
from .apis import TemplateViewSet

templateRouter = routers.DefaultRouter()
templateRouter.register(r'', TemplateViewSet)