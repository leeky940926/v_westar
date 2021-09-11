MY_SECRET_KEY = 'django-insecure-35%+41*o4hffjw6)v9q*puz%*j4o+p3q9jughkae)wmn*3p(fi'

MY_DATABASE = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'v_westar', #데이터베이스명
        'USER': 'root', #DB접속 계정명
        'PASSWORD': '1234', #mysql 로그인 할 때 쓰는 DB접속용 비밀번호
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}