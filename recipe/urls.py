from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 클래스 호출
    # 대문 페이지
    path('', views.index),
    #
    path('nutrient_list/', views.nutrient_list),
    # 오늘의 식품 News
    path('todayNews/', views.todayNews),
    # About 페이지(소개 페이지)
    path('about/', views.about),
    #
    # 레시피 목록
    path('recipe/', views.RecipeList.as_view()),
    # 레시피 상세
    path('recipe/<int:pk>/', views.RecipeDetail.as_view()),
    # 레시피 작성
    path('writeRecipe/', views.WriteRecipe.as_view()),
    # 레시피 삭제
    path('recipeDelete/<int:pk>/', views.RecipeDelete.as_view()),
    # 레시피 수정
    path('recipeUpdate/<int:pk>/', views.RecipeUpdate.as_view()),
    #
    # 자신이 쓴 게시글 보기
    path('mypost/', views.mypost),
    # 식품 영양 정보 csv파일을 DB로 옮기는 페이지
    path('nutrients/', views.add_nutrients)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)