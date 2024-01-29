from flask import Flask, render_template, Response, jsonify, redirect, url_for
import cv2
from keras.models import load_model
import numpy as np
from statistics import mode
import time
from scipy.ndimage import zoom

app = Flask(__name__)

# Load the prediction model
age_model = load_model('C:\\seomiyoung\\dongguk\\3_2\\capstone\\multi20_finalcode\\model\\age_model.h5')
emotion_model = load_model('C:\\seomiyoung\\dongguk\\3_2\\capstone\\multi20_finalcode\\model\\emotion_model.h5')

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

# 배열 초기화
age_records = []
emotion_records = []
original_emotion_records = []

age_ranges = ['1-5', '6-10', '11-15', '16-20', '21-26', '27-32', '33-39', '40-48', '49-56', '57-65', '66-116']
emotion_ranges = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

def reset_data():
    global age_records
    global emotion_records
    age_records = []
    emotion_records = []
    final_age = 1
    final_emotion = 'non'

# 전체 이미지에서 찾아낸 얼굴을 추출하는 함수
def extract_face_features(gray, detected_faces, offset_coefficients=(0.075, 0.05)):
    new_face = []
    coord = []  # 추가된 부분: 얼굴의 좌표를 저장하는 리스트
    for det in detected_faces:
        # 얼굴로 감지된 영역
        x, y, w, h = det
        
        # 추가된 부분: 얼굴의 좌표를 리스트에 저장
        coord.append([x, y, w, h])

        # 이미지 경계값 받기
        horizontal_offset = int(np.floor(offset_coefficients[0] * w))
        vertical_offset = int(np.floor(offset_coefficients[1] * h))
        
        # gray scale에서 해당 위치 가져오기
        extracted_face = gray[y + vertical_offset:y + h, x + horizontal_offset:x - horizontal_offset + w]
        
        # 얼굴 이미지만 확대
        new_extracted_face = zoom(extracted_face, (48 / extracted_face.shape[0], 48 / extracted_face.shape[1]))
        new_extracted_face = new_extracted_face.astype(np.float32)
        new_extracted_face /= float(new_extracted_face.max())  # scaled
        new_face.append(new_extracted_face)
        
    return new_face, coord  # coord 추가된 부분

# 이전 프레임의 index결과 저장(moving average를 위해)
before_age_index = 0

# 가장 높은 확률값과 해당하는 라벨을 가져오는 함수
def get_highest_probability(probabilities, labels):
    highest_index = np.argmax(probabilities)
    highest_label = labels[highest_index]
    highest_prob = probabilities[highest_index]
    return highest_label, highest_prob

# def get_highest_probability_emotion(probabilities, labels):
#     # Negative로 그룹화: Angry, Disgust, Fear, Sad
#     negative_probs = sum(probabilities[0:4])
#     # Non-Negative로 그룹화: Surprise, Happy
#     non_negative_probs = sum(probabilities[4:6])
#     # Neutral은 그대로 두기
#     neutral_prob = probabilities[6]

#     grouped_probs = [negative_probs, non_negative_probs, neutral_prob]
#     grouped_labels = ['Negative', 'Non-Negative', 'Neutral']

#     highest_group_index = np.argmax(grouped_probs)
#     highest_group_label = grouped_labels[highest_group_index]
#     highest_group_prob = grouped_probs[highest_group_index]

#     return highest_group_label, highest_group_prob

def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        largest_face = (0, 0, 0, 0)
        for (x, y, w, h) in faces:
            if w * h > largest_face[2] * largest_face[3]:
                largest_face = (x, y, w, h)

        if largest_face[2] > 0 and largest_face[3] > 0:
            x, y, w, h = largest_face
            face = gray[y:y+h, x:x+w]
            # 얼굴에 움직이는 평균 적용

            # age
            age_image = cv2.resize(face, (200, 200), interpolation=cv2.INTER_AREA)
            age_input = age_image.reshape(-1, 200, 200, 1)

            # moving average적용
            if len(age_records) >= 1: # 만약에 age_records가 빈 배열이 아니라면
                age_index = np.argmax(age_model.predict(age_input))
                moving_average_index = (before_age_index + age_index) / 2
                age_index = round(moving_average_index)
            else: # age_records가 빈 배열이라면
                age_index = np.argmax(age_model.predict(age_input))

            output_age = age_ranges[age_index]
            age_records.append(output_age)

            before_age_index = age_index

            # Emotion prediction
            face_zoom, coord = extract_face_features(gray, [(x, y, w, h)])
            if face_zoom:
                face_zoom = np.reshape(face_zoom[0].flatten(), (1, 48, 48, 1))
                pred = emotion_model.predict(face_zoom)
                pred_result = np.argmax(pred)

                # # 감정을 그룹화하여 확률을 얻음
                # grouped_emotion_prob = group_emotion_probabilities(pred[0])

                # # 각 그룹별로 텍스트 생성
                # grouped_emotion_text = [f'{emotion_labels[i]}: {round(grouped_emotion_prob[i], 3)}' for i in range(3)]

                # # 각 그룹별로 확률 출력
                # for i, text in enumerate(grouped_emotion_text):
                #     cv2.putText(frame, text, (10, 50 + 40 * i), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)
            
            # if pred_result in [3, 5]:
            #     emotion_category = "Non-Negative"
            # elif pred_result == 6:
            #     emotion_category = "Neutral"
            # else:
            #     emotion_category = "Negative"

            # emotion
            # emotion_image = cv2.resize(face, (48, 48), interpolation=cv2.INTER_AREA)
            # emotion_input = emotion_image.reshape(-1, 48, 48, 1)
            # print(np.argmax(emotion_model.predict(emotion_input)))
            output_emotion=emotion_ranges[pred_result]

            # 임시 추가 -------------------------------
            original_output_emotion = output_emotion
            original_emotion_records.append(original_output_emotion)
            # /임시 추가 -------------------------------

            if output_emotion in ['angry', 'disgust', 'fear', 'sad']:
                output_emotion = 'negative'
            elif output_emotion in ['happy', 'surprise']:
                output_emotion = 'non_negative'
            else:  # neutral
                output_emotion = 'neutral'

            emotion_records.append(output_emotion)

            output_str = output_age + ',' + output_emotion
            col = (0, 255, 0)

            cv2.putText(frame, output_str, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, col, thickness=4)
            
            # Emotion 및 Age 예측 확률 가져오기
            emotions_prob = pred[0]  # 감정 예측 결과의 확률
            age_prob = age_model.predict(age_input)[0]  # 나이 예측 결과의 확률

            # 감정 레이블 및 나이 레이블 설정
            emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
            age_labels = ['1-5', '6-10', '11-15', '16-20', '21-26', '27-32', '33-39', '40-48', '49-56', '57-65', '66-116']

            

            # 감정 확률 출력 - 가장 높은 확률값 출력
            highest_emotion_label, highest_emotion_prob = get_highest_probability(emotions_prob, emotion_labels)
            if highest_emotion_label in ['Angry', 'Disgust', 'Fear', 'Sad']:
                grouped_emotion_label = 'negative'
            elif highest_emotion_label in ['Happy', 'Surprise']:
                grouped_emotion_label = 'non-negative'
            else:
                grouped_emotion_label = 'neutral'
            text_emotion = f"{grouped_emotion_label}: {str(round(highest_emotion_prob, 3))}"
            cv2.rectangle(frame, (10, 50 - 30), (500, 200), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, 'Print Confidence :', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
            cv2.putText(frame, text_emotion, (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)

            # 나이 확률 출력 - 가장 높은 확률값 출력
            highest_age_label, highest_age_prob = get_highest_probability(age_prob, age_labels)
            text_age = f"{highest_age_label}: {str(round(highest_age_prob, 3))}"
            # cv2.rectangle(frame, (10, 350 - 30), (500, 390), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, text_age, (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        data = jpeg.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n\r\n')

@app.route('/')
def index():
    reset_data() # 페이지 접속 시 데이터 초기화
    return render_template('base.html', age_records=age_records, emotion_records=emotion_records, original_emotion_records=original_emotion_records)

@app.route('/loading')
def loading():
    return render_template('loading.html')  # 새로운 loading.html 템플릿 추가

# @app.route('/predict_age', methods=['POST'])
# def predict_age():
#     final_age = mode(age_records)
#     return jsonify({'prediction': final_age})

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/menu')
def menu():
    final_age = mode(age_records)
    final_emotion = mode(emotion_records)
    original_final_emotion = mode(original_emotion_records)
    return render_template('menu.html', age_records=age_records, final_age=final_age, emotion_records=emotion_records, final_emotion=final_emotion, original_emotion_records=original_emotion_records, original_final_emotion=original_final_emotion)

if __name__ == '__main__':
    app.run(debug=True)