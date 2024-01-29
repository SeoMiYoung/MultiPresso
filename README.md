
<div align="center">
  <img width="400" alt="new_logo" src="https://github.com/SeoMiYoung/MultiPresso/assets/112063987/bbb64103-f115-4d7f-b187-3cb32e55f2ad">
</div>


## 프로젝트 소개
> 해당 프로젝트는 동국대 멀티미디어소프트웨어공학과 졸업작품으로 진행되었습니다.

여러분은 키오스크에서 메뉴를 주문하실 때, 마음에 드는 메뉴를 추천받으신적이 있으신가요?
잘 없으셨을텐데요, 저희 팀원들은 동국대학교 근처 카페인 바나프레소를 자주 이용하면서, 키오스크 화면에 뜨는 추천 메뉴들이 사용자를 고려하지 않은 일반적인 추천 메뉴들이라는 점을 발견했습니다. 이에 따라, 키오스크가 사용자를 분석하여 사용자 맞춤의 추천 메뉴를 제공한다면 사용자의 편의성을 높일 수 있을 것이라고 생각했고, 따라서 해당 주제를 졸업 작품에 적용해보기로 했습니다. 

## 프로젝트 기간
> 2023.09.05 ~ 2023.12.15

## 팀명과 팀원(Contributors)
> 팀명: 멀티20들<br/>
> 팀원: 서미영, 이유정, 안정민, 이채린

## 서비스 프로세스
![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/2e5b6e3e-99b1-4939-be5b-4eb9278c9e94)

## 연령(Age) 모델 학습
저희는 연령 모델에 대한 데이터셋을 다음의 세단계로 순차적으로 학습시켰습니다.
![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/919d61fb-9a1e-402e-892a-972ffb02ab63)
### ☑️ STEP1 - 기본 Dataset으로 학습
#### ✔️ 데이터 전처리
- 연령이 라벨링되어있는 UTK Faces 데이터셋과 Facial Age 데이터셋을 사용
- 두 데이터셋을 결합한 후, 모델 학습을 위해 train과 test 데이터셋으로 분리하였으며, 모델 성능 향상을 위해 train데이터셋을 10배 증강하여 학습을 진행
- 연령에 대해서는 총 11개의 class로 분류

![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/70d14e0f-e395-47fa-aa61-0f383d093bb5)
#### ✔️ CNN 모델 선정
- 준비한 데이터셋으로 VGG16, VGG19, ResNet 모델로 학습 진행해서 결과 비교
- VGG기반 모델들과 달리, ResNet 모델의 경우, 초기 학습 때 과적합의 문제가 발생(해결 과정에 대해서는 따로 카테고리로 빼놓음)
- 비교 결과, VGG16이 성능이 제일 좋아서, VGG16으로 최종 모델을 결정하고, 에폭 100으로 재학습시킴

![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/9fefb729-8af0-4bfa-af44-5630c3808f7e)
![image](https://github.com/SeoMiYoung/MultiPresso/assets/112063987/aa9db400-8ca5-453e-82ab-fdfd492fe6d6)

#### ✔️ STEP1 학습 결과의 문제점
- 정확한 나이가 예측되지 않았으며, 그 원인으로 웹캠 환경에서 찍어오는 데이터가 학습한 데이터와 차이가 있기 때문이라고 예상 --> 2차 학습 진행

### ☑️ STEP2 - 성능 향상을 위한 여러가지 시도: 광조 고려
#### ✔️ 기존 데이터셋의 밝기를 랜덤으로 변화시켜 재구성
- 웹캠으로 촬영하는 환경에 따라 밝기 차이가 있을 수 있다고 판단하여, 기존 데이터셋의 밝기를 랜덤으로 변화시켜 재구성한 데이터셋으로 학습 진행
- 정확도와 성능이 높아짐


