from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 레시피
class Recipe(models.Model):
    # 제목 (30자로 최대 길이 제한)
    title = models.CharField(max_length=30)
    # 생성 날짜, 시간 (자동 생성)
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 날짜, 시간
    updated_at = models.DateTimeField(auto_now=True)
    # 내용 (무한대. 길이제한 없음)
    content = models.TextField()
    # 작성자의 uid
    #uid = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # 작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    # 상세 페이지랑 연결
    def get_absolute_url(self):
        return f'/recipe/{self.pk}'


# 식품 영양 정보
class Nutrient(models.Model):
    fname = models.CharField(max_length=30)
    cl1 = models.CharField(max_length=10)
    cl2 = models.CharField(max_length=30)
    svs = models.CharField(max_length=10)
    kcal = models.CharField(max_length=10)
    protein_g = models.CharField(max_length=10)
    fat_g = models.CharField(max_length=10)
    carbo_g = models.CharField(max_length=10)
    sugar_g = models.CharField(max_length=10)
    calc_mg = models.CharField(max_length=10)
    pota_mg = models.CharField(max_length=10)
    salt_mg = models.CharField(max_length=10)

    class Meta:
        db_table = 'foodNutrientsdb'
    
    def __str__(self):
        return f'[{self.pk}]{self.fname}'
