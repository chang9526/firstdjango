# forms.py를 이용해 폼을 생성할 때 반드시 아래 코드 작성
from django import forms
# Post 모델에 대한 폼믈 생성하기 위해 Post 모델 로드
from .models import Post

# 모델에서 models.Model를 괄호 안에 넣었듯이
# 촘 생성에서도 class 폼이름(forms.ModleForm): 으로 시작해야함
class PostForm(forms.ModelForm):

    # 폼의 상세정보 성정을 위해 class PostForm내부에
    # class Meta를 다시 만들어야함. Meta에 정의한 정보대로 폼이 생성됨.
    class Meta:
        # 이 폼의 타겟이 Post 모델(Post모뎅에 적재 예정)
        model = Post
        # 실제로 사용자에게 입력받을 컬럼은 title과 text만
        # author은 자동으로 계정 연동, create_date는 서버시간
        # published_date는 퍼블리싱할 때 추후 입력
        # pk는 자동으로 글 하나 생성시마다 하나씩 부여
        fields = ('title', 'text',)