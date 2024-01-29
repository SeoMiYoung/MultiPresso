![wave](https://capsule-render.vercel.app/api?type=wave&color=FF9090&height=200&text=MultiPresso)

<!--
<div align="center">
  <img width="400" alt="new_logo" src="https://github.com/SeoMiYoung/MultiPresso/assets/112063987/bbb64103-f115-4d7f-b187-3cb32e55f2ad">
</div>
-->

<br/>
<br/>

## 🥤 프로젝트 소개
> 해당 프로젝트는 동국대 멀티미디어소프트웨어공학과 졸업작품으로 진행되었습니다.

![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/d784d7f8-724d-4747-9e0a-c3714c3625c8)

여러분은 키오스크에서 메뉴를 주문하실 때, 마음에 드는 메뉴를 추천받으신적이 있으신가요?
잘 없으셨을텐데요, 저희 팀원들은 동국대학교 근처 카페인 바나프레소를 자주 이용하면서, 키오스크 화면에 뜨는 추천 메뉴들이 사용자를 고려하지 않은 일반적인 추천 메뉴들이라는 점을 발견했습니다. 이에 따라, 키오스크가 사용자를 분석하여 사용자 맞춤의 추천 메뉴를 제공한다면 사용자의 편의성을 높일 수 있을 것이라고 생각했고, 따라서 해당 주제를 졸업 작품에 적용해보기로 했습니다. 

## 🗓️ 프로젝트 기간
> 2023.09.05 ~ 2023.12.15

## 👩‍💻 팀명과 팀원(Contributors)
> 팀명: 멀티20들<br/>
> 팀원: 서미영, 이유정, 안정민, 이채린

## ⚙️ 사용 툴
#### ✔️ ML(Machine Learning) / DL(Deep Learning)<br/>
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

#### ✔️ Languages
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

#### ✔️ Frameworks, Platforms and Libraries
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

#### ✔️ Developer/Forums
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)

#### ✔️ Cloud Storage
![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)

#### ✔️ IDEs/Editors
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## 📂 목차
<div>
  <div><a href='#loudspeaker-서비스-프로세스'>:loudspeaker: 서비스 프로세스</a></div>
  <div><a href="#information_desk_person-연령&lpar;Age&rpar;-모델-학습">:information_desk_person: 연령(Age) 모델 학습</a></div>
  <div><a href='#satisfied-감정&lpar;Emotion&rpar;-모델-학습'>:satisfied: 감정(Emotion) 모델 학습</a></div>
  <div><a href='#thumbsup-메뉴-추천-알고리즘'>:thumbsup: 메뉴 추천 알고리즘</a></div>
  <div><a href='#tada-서비스-시현'>:tada: 서비스 시현</a></div>
</div>

## :loudspeaker: 서비스 프로세스
![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/2e5b6e3e-99b1-4939-be5b-4eb9278c9e94)

## :information_desk_person: 연령(Age) 모델 학습
> 아래의 과정을 기반으로 학습된 연령 모델은 model/age_model.h5 입니다.

저희는 연령 모델에 대한 데이터셋을 다음의 세단계로 순차적으로 학습시켰습니다.
![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/919d61fb-9a1e-402e-892a-972ffb02ab63)
### ☑️ STEP1 - 기본 Dataset으로 학습
#### ✔️ 데이터 전처리
- 연령이 라벨링되어있는 UTK Faces 데이터셋과 Facial Age 데이터셋을 사용
- 두 데이터셋을 결합한 후, 모델 학습을 위해 train과 test 데이터셋으로 분리하였으며, 모델 성능 향상을 위해 train데이터셋을 10배 증강하여 학습을 진행
- 연령에 대해서는 총 11개의 class로 분류

![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/70d14e0f-e395-47fa-aa61-0f383d093bb5)
#### ✔️ CNN 모델 선정
- 준비한 데이터셋으로 VGG16, VGG19, ResNet 모델로 학습(에폭 30) 진행해서 결과 비교
- VGG기반 모델들과 달리, ResNet 모델의 경우, 초기 학습 때 과적합의 문제가 발생했으나, 모델의 layer를 단순화시키고 채널값을 3에서 1로 조절함으로써 해결할 수 있었음
- 세 모델의 비교 결과, VGG16이 성능이 제일 좋아서, VGG16으로 최종 모델을 결정하고, 에폭 100으로 재학습시킴

![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/9fefb729-8af0-4bfa-af44-5630c3808f7e)
![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/aa9db400-8ca5-453e-82ab-fdfd492fe6d6)

#### ✔️ STEP1 학습 결과의 문제점
- 정확한 나이가 예측되지 않았으며, 그 원인으로 웹캠 환경에서 찍어오는 데이터가 학습한 데이터와 차이가 있기 때문이라고 예상 --> 2차 학습 진행

### ☑️ STEP2 - 성능 향상을 위한 여러가지 시도: 광조 고려
#### ✔️ 기존 데이터셋의 밝기를 랜덤으로 변화시켜 재구성
- 웹캠으로 촬영하는 환경에 따라 밝기 차이가 있을 수 있다고 판단하여, 기존 데이터셋의 밝기를 랜덤으로 변화시켜 재구성한 데이터셋으로 학습 진행
- 정확도와 성능이 높아짐
  - 아래 사진을 보면 20대 학생을 STEP1 모델을 적용했을때는 66-116살로 예측했지만, STEP2 모델을 적용했을때는 33-39살로 예측되는 걸 확인할 수 있음

![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/b44aa452-f280-4026-8f6c-28c15737161a)

### ☑️ STEP3 - 성능 향상을 위한 여러가지 시도: 웹캠 환경을 고려한 웹캠 데이터 추가
#### ✔️ 웹캠으로 데이터 직접 수집
- 시현 환경이 웹캠이기 때문에 웹캠에서 찍은 얼굴이 필요하다고 판단
- 웹캠으로 데이터를 직접 수집하여 마지막으로 모델 학습 진행
- 데이터 균등을 고려하여 11개의 연령 클래스 당, 35명의 웹 캠 사진을 다음과 같이 8배 증강하여, 총 3080장에 대해 모델 학습 진행
- 정확도와 성능이 높아짐
  - 아래 사진을 보면 20대 학생을 STEP2 모델을 적용했을때는 33-39살로 예측했지만, STEP3 모델을 적용했을때는 27-32살로 예측되는 걸 확인할 수 있음

![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/a85b2cc3-030c-4431-93b6-79447cc9f6a4)

## :satisfied: 감정(Emotion) 모델 학습
> 아래의 과정을 기반으로 학습된 연령 모델은 model/emotion_model.h5 입니다.

### ☑️ 데이터셋을 결정하는데 있어서 발생한 시행착오
#### ✔️ 기존에 결정한 데이터셋: CK+
![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/9ecce563-b96d-43a5-809b-1087db969e7b)

- 기존에는 CK+ 데이터셋을 사용해서 학습 진행 --> 문제점 발견
  - [문제점1] 무표정 데이터셋이 존재하지 않음 : 키오스크를 이용하는 대부분의 사용자는 무표정인데, 무표정 데이터셋이 없다는점은 원하는 결과를 얻기에는 큰 문제였음
  - [문제점2] CK+는 데이터셋의 규모가 작아서 정확한 예측이 불가능하다고 판단
  - [문제점3] 데이터셋이 매우 중앙에 위치한 얼굴로 구성되어있어서 웹캠과 같이 얼굴 움직임이 불안정한 경우, 정확한 예측을 하는데 취약하다고 판단

#### ✔️ 바꾼 데이터셋: FER2013
![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/50d25ee2-b83a-44e9-8c93-477532f05787)

- FER2013의 경우 약 35000장의 대규모 감정 데이터셋을 가지고 있음
- 무표정 데이터셋 포함

### ☑️ FER2013 재라벨링
FER2013 데이터셋은 기존에는 7개의 감정으로 라벨링되어 있었으나, 저희의 키오스크 시스템의 경우, 손님들이 주문하는 순간의 표정이 다양하지 않을 것이라고 판단하여 아래 사진과 같이 negative, non-negative, neutral 이렇게 3가지 감정으로 재분류하였습니다.
<div>
  <img width="600" src="https://github.com/SeoMiYoung/MultiPresso/assets/112063987/93b2c065-5640-40f9-873c-63edda4953bc">
</div>

### ☑️ CNN 모델 학습
연령과 동일하게 VGG기반 모델로 학습한 결과는 다음과 같습니다.
<div>
  <img width="500" src="https://github.com/SeoMiYoung/MultiPresso/assets/112063987/3b2bf0b4-64e5-4e20-887b-e05376d7aa30">
</div>

## :thumbsup: 메뉴 추천 알고리즘
웹캠을 통해 사용자의 연령과 감정을 인식하면, 연령에 대한 음료 정렬 순서에서 상위 4개의 메뉴를 가져옵니다. 이 4개의 메뉴는 추천 메뉴로 띄우게 되는데,
감정에 따라 추천 메뉴를 화면에 띄우는 순서가 달라집니다. 예측한 감정이 긍정일 경우 당이 낮은 순서대로, 부정일 경우 당이 높은 순서대로 재정렬해서 화면에 띄우고, neutral일 경우에는 받아온 순서 그대로 화면에 띄웁니다.

![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/a5291897-9c50-4631-b072-0342df96b0e2)

## :tada: 서비스 시현
딥러닝 모델을 만들고, 성능을 높히는 과정에 초점을 두어서, 웹페이지는 테스트용으로만 간단히 제작하였습니다.

![Animation](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/f69a0dce-4730-45d6-8ee6-f6c4da62bf03)

### ☑️ 첫 시작 페이지
- 키오스크에서 사용자가 주문하기 버튼을 누름

### ☑️ 로딩 페이지 (연령과 감정 예측)
- 일정 시간동안 웹캠을 통하여 사용자의 얼굴 촬영
- OpenCV를 사용하여 웹캠으로부터 영상 캡처
- 웹캠에서 가장 앞에 있는 사람 한 명만을 감지하도록 구현
- 예측 연령 범위가 변동이 심할 수 있기 때문에 moving average 적용
- 각 프레임이 예측한 연령과 감정의 최빈값을 구해 최종적인 예측 연령과 감정 결정

### ☑️ 메뉴 페이지
- 최종적으로 결정된 예측 연령과 감정을 바탕으로, 전체 메뉴를 보여주기 전에 메뉴 페이지 상단에 추천 음료 4개를 띄움



