"""crockery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from apps.game.views import router as game_router
from apps.question.views import game_question_router, question_router
from apps.crock.views import router as crock_router


game_api = NinjaAPI(title="Game", urls_namespace="Game")
game_router.add_router("", game_question_router)
game_router.add_router("", crock_router)
game_api.add_router("", game_router)

question_api = NinjaAPI(title="Question", urls_namespace="Question")
question_api.add_router("", question_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/game/", game_api.urls),
    path("api/question/", question_api.urls),
]
