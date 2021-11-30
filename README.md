# Assignment7-YY

원티드x위코드 백엔드 프리온보딩 과제7
- 과제 출제 기업 정보
  - 기업명 : 카닥

## Member
| 이름  | github                                   |
|-------|------------------------------------------|
|고유영 |[lunayyko](https://github.com/lunayyko)     | 


## 과제 내용


### 1. 배경 및 공통 요구사항

<aside>
😁 **카닥에서 실제로 사용하는 프레임워크를 토대로 타이어 API를 설계 및 구현합니다.**

</aside>

- 데이터베이스 환경은 별도로 제공하지 않습니다.
 **RDB중 원하는 방식을 선택**하면 되며, sqlite3 같은 별도의 설치없이 이용 가능한 in-memory DB도 좋으며, 가능하다면 Docker로 준비하셔도 됩니다.
- 단, 결과 제출 시 README.md 파일에 실행 방법을 완벽히 서술하여 DB를 포함하여 전체적인 서버를 구동하는데 문제없도록 해야합니다.
- 데이터베이스 관련처리는 raw query가 아닌 **ORM을 이용하여 구현**합니다.
- Response Codes API를 성공적으로 호출할 경우 200번 코드를 반환하고, 그 외의 경우에는 아래의 코드로 반환합니다.

200 | OK	| 성공 

400 | Bad Request	| Parameter가 잘못된 (범위, 값 등). 

401 | Unauthorized	| 인증을 위한 Header가 잘못됨. 

500 | Internal Server Error	| 기타 서버 에러. 


### 2. 사용자 생성 API

🎁 **요구사항**

- ID/Password로 사용자를 생성하는 API.
- 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출할 수 있다.

```jsx
/* Request Body 예제 */

 { "id": "candycandy", "password": "ASdfdsf3232@" }
```


## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MySQL 8.0-0064a5?style=for-the-badge&logo=MySQL&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>&nbsp;

## 모델링

<img width="810" alt="Screen Shot 2021-11-27 at 5 47 58 PM" src="https://user-images.githubusercontent.com/8315252/143674824-6c31f6c7-2ce3-400f-8de1-0f9f1f3351a6.png">

## API

<img width="1044" alt="Screen Shot 2021-11-28 at 7 42 46 PM" src="https://user-images.githubusercontent.com/8315252/143765334-6ac87fc4-edde-4ab9-b775-d08cb05ac0a7.png">

## 구현 기능

주어진 과제 4개 중 2번까지 수행하고 주어진 데이터셋을 디비에 업로드하였습니다.

## 배포정보
|구분   |  정보          |비고|
|-------|----------------|----|
|배포플랫폼 | AWS EC2    |    |
|API 주소 |http://3.38.150.162:8061/          |    |


## 설치 및 실행 방법
<details>
<summary>설치 및 실행 방법 자세히 보기</summary>
<div markdown="1">
  
###  Local 개발 및 테스트용

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment7-YY
    cd Assignment7-YY
    ```

2. 가상 환경을 만들고 프로젝트에 사용한 python package를 받는다.
    ```bash
    conda create --name cardoc python=3.8
    conda actvate cardoc
    pip install -r requirements.txt
    ```

3. db를 table 구조를 최신 model에 맞게 설정한다.
    ```bash
    python manage.py migrate
    ```

4. 서버를 실행한다.
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
</details>

# Reference
- 이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 카닥에서 출제한 과제를 기반으로 만들었습니다.
- 본 과제는 저작권의 보호를 받으며, 문제에 대한 정보를 배포하는 등의 행위를 금지 합니다.
