from sklearn.preprocessing import StandardScaler
import numpy as np

# 훈련 데이터 예시
X_train = np.array([[1, 2], [3, 4], [5, 6]])

# StandardScaler 객체 생성
scaler = StandardScaler()

# fit_transform()을 사용하여 훈련 데이터 표준화
# 이 과정에서 scaler는 평균과 분산을 학습하고 데이터를 표준화합니다.
X_train_scaled = scaler.fit_transform(X_train)

print("원본 훈련 데이터:\n", X_train)
print("\n표준화된 훈련 데이터:\n", X_train_scaled)