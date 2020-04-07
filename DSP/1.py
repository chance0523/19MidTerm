import random
from collections import deque

# CFT -> DFT #

q1 = [
    ["Frequency spectrum이 discrete하게 표현되기 위해 어떠한 가정을 하는가?",
     "time sequence가 반복적으로 나타난다고 가정 (강제로 주기함수로 만듬)"],
    ["FS 계수는 OOO OOO 간격마다 OO하게 나타나므로 OOO OOO 구간에 대해서만 FS를 계산한다.",
     "FS 계수는 샘플링 주파수 간격마다 동일하게 나타나므로 샘플링 주파수 구간에 대해서만 FS를 계산한다."],
    ["F0 = OOO OOO. N이 OOO (sample 수 OO져야) F0도 커짐",
     "F0 = 주파수 해상도. N이 커져야 (sample 수 많아져야) F0도 커짐"],
    ["Frequency resolution의 향상법과 설명",
     "zero-padding, 0을 앞이나 뒤에 넣어서 억지로 f_resol 만듬"],
    ["Spectral leakage이 일어나는 이유",
     "시작과 끝점이 서로 일치하지 않는 경우 불연속하게 연결."],
    ["Spectral leakage의 결과",
     "신호의 급격한 변화로 고주파 성분을 발생. 발생한 고주파 성분은 원래의 신호에는 존재하지 않는 성분임."],
    ["Leakage를 줄이는 방법과 설명",
     "Windowing. Window 함수를 사용하여 시작과 끝점을 억지로 0으로 만듬"],
    ["Window 함수와 기존 Rectangular 함수의 차이",
     "Window 함수가 Rectangular 함수보다 main rober의 폭은 넓고, side rober의 값은 작다."],
    ["주파수 분석 시 window의 차이 : Hamming window에 대해서",
     "Hamming window : side rober의 값이 작아서 7Hz의 값이 3Hz에 묻히지 않음. main rober의 폭이 넓어서 인접한 3.4Hz는 3Hz에 묻힘"],
    ["주파수 분석 시 window의 차이 : Rectangular window",
     "Rectangular Window : side rober의 값이 커서 7Hz의 값이 3Hz에 묻힌다. main rober의 폭이 작아서 인접된 3.4Hz는 3Hz에 묻히지 않는다."],
    ["추가 문제 : zero-padding은 무엇을 위한 기법인가?",
     "frequency resolution을 향상시키기 위한 기법이다."]
]

# ~ FS #

q2 = [
    ["Sampling Frequency가 크면",
     "복원된 신호와 원본 신호가 유사. 많은 데이터량. 빠른 처리속도 요구"],
    ["Sampling Frequency가 작으면",
     "복원된 신호와 원본 신호 간 차이 발생. 데이터량이 적음. 느린 처리속도로도 가능"],
    ["Nyquist Frequency",
     "fs가 주어지면 정보 손실이 없는 아날로그 신호의 최대 주파수는 fs/2(=fN)이다."],
    ["Over / Perfect / Under Sampling 중 aliasing이 나타나는 sampling은?",
     "Under Sampling"],
    ["Anti Aliasing Filter의 조건",
     "AAF는 일반적으로 LPF이다. fN보다 높은 주파수 성분을 모두 제거해야 aliasing이 발생하기 어렵다. Ideal LPF를 사용하지 않는 한 aliasing을 피할 수 없다."],
    ["AAF의 차단주파수",
     "fc=fs/2"],
    ["Aliasing을 최소화 하는 방법",
     "AAF의 차단특성을 날카롭게한다. 차수(order)가 높은 아날로그 필터 사용. 부피가 커지고 온도에 따라 특성이 변화. Oversampling 기법 사용"],
    ["왜 practical ADC에서 ideal sampling이 불가한가.",
     "짧은 기간동안 신호를 hold 할 수 없음. 짧은 기간 동안 quantization과 encoding을 할 수 없음"],
    ["Three Different sampling method. (I, N, F)",
     "Ideal, Natural, Flat-top"],
    ["A/D 변환 시 LPF의 중요성",
     "A/D 변환 시 가장 앞 단에 위치. 전체 DSP S/S의 성능에 영향."],
    ["이상적인 A/D 변환",
     "Ideal LPF. passband의 ripple = -무한대. stopband의 ripple = 0. 무한개의 길이를 갖는 impulse response -> 구현불가"],
    ["LPF의 영향을 줄이는 방법",
     "oversampling"],
    ["oversampling 기법의 장단점",
     "비교적 간단한 방법으로 LPF의 불완전한 특성을 보상 할 수 있다. stopband에서의 LPF ripple에 따라 오버샘플링 주파수를 간단하게 결정 할 수 있다. fs의 증가에 따라 정보량의 증가를 가져온다. stopband의 ripple 영향을 완벽하게 제거 할 수 없다. (무한대의 fs가 필요)"],
    ["Anti aliasing Filter의 설계 1",
     "Stopband에서의 ripple -> baseband spectrum에 영향을 준다."],
    ["Anti aliasing Filter의 설계 2",
     "즉, A/D 변환시의 LPF는 stopband에서 얼만큼 신호를 제거(reject) 할 수 있느냐가 중요하다."],
    ["Anti aliasing Filter의 설계 3",
     "Stopband의 신호제거 정도는 aliasing level을 결정한다."],
    ["1 Bit 할당 시 향상되는 SNR은?",
     "1 bit 할당 시 약 6dB의 SNR 향상."],
    ["System의 SNR이 40dB이면",
     "7 bit의 해상도를 갖는다."],
    ["16 bit의 해상도는",
     "96dB의 SNR이 요구됨"],
    ["Nonlinear PCM 1",
     "신호의 분포에 따른 양자화 레벨의 가변. 집중적으로 분포하는 곳은 작은 step size, 드물게 분포하는 곳은 큰 step size. 전체적은 quantization noise power는 감소함."],
    ["Nonlinear PCM 2",
     "신호의 주관적인 인지 특성에 따른 양자화 레벨의 가변. 인간의 귀는 작은 레벨의 신호에는 민감하고 큰 레벨의 신호는 둔감하다. 작은 레벨에 작은 step size"],
    ["FS에서 a0, an, bn의 의미",
     "a0는 한 주기의 평균, an, bn은 내적을 의미한다."],
    ["FS의 근사화",
     "무한대로 근사화해야하는데 그러지 못해서 n개로 근사화. edge 부분이 잘 근사화가 안됨. 고주파 성분이 잘 포함 안됨. cosn0, sinn0에서 n이 클수록 고주파인데 1~n은 포함, n~무한대는 포함 안 해서"],
    ["주기와 기본주파수와의 관계",
     "T와 f0는 역수 관계이다."],
    ["비 주기 함수의 주기 함수 표현",
     "T를 무한대로 limit 하면 f0가 매우 작아진다."],
    ["Fourier Transform의 장점",
     "time domain에서 복잡한 그림이 frequency domain에서는 간단한 spectrum으로 표현"],
    ["FT의 Delay",
     "Delay : phase만 변하고 magnitude는 그대로."],
    ["Parseval's theorem",
     "시간 영역의 에너지 = 주파수 영역의 에너지 -> 에너지 보존의 법칙"],
]

# 헷갈리는 것 #

q3 = [
    ["oversampling 기법의 장단점 1",
     "비교적 간단한 방법으로 LPF의 불완전한 특성을 보상 할 수 있다."],
    ["oversampling 기법의 장단점 2",
     "stopband에서의 LPF ripple에 따라 오버샘플링 주파수를 간단하게 결정 할 수 있다."],
    ["oversampling 기법의 장단점 3",
     "fs의 증가에 따라 정보량의 증가를 가져온다."],
    ["oversampling 기법의 장단점 4",
     "stopband의 ripple 영향을 완벽하게 제거 할 수 없다. (무한대의 fs가 필요)"],
    ["Anti aliasing Filter의 설계 1",
     "Stopband에서의 ripple -> baseband spectrum에 영향을 준다."],
    ["Anti aliasing Filter의 설계 2",
     "즉, A/D 변환시의 LPF는 stopband에서 얼만큼 신호를 제거(reject) 할 수 있느냐가 중요하다."],
    ["Anti aliasing Filter의 설계 3",
     "Stopband의 신호제거 정도는 aliasing level을 결정한다."],
    ["Nonlinear PCM 1-1",
     "신호의 분포에 따른 양자화 레벨의 가변."],
    ["Nonlinear PCM 1-2",
     "집중적으로 분포하는 곳은 작은 step size, 드물게 분포하는 곳은 큰 step size."],
    ["Nonlinear PCM 1-3",
     "전체적은 quantization noise power는 감소함."],
    ["Nonlinear PCM 2-1",
     "신호의 주관적인 인지 특성에 따른 양자화 레벨의 가변."],
    ["Nonlinear PCM 2-2",
     "인간의 귀는 작은 레벨의 신호에는 민감하고 큰 레벨의 신호는 둔감하다. 작은 레벨에 작은 step size"],
    ["FS의 근사화",
     "무한대로 근사화해야하는데 그러지 못해서 n개로 근사화."],
    ["FS 근사화의 문제와 이유",
     "edge 부분이 잘 근사화가 안됨. 고주파 성분이 잘 포함 안됨. cosn0, sinn0에서 n이 클수록 고주파인데 1~n은 포함, n~무한대는 포함 안 해서"],
    

]

# NEW #

q4 = [
    ["Anti aliasing Filter의 설계 1",
     "Stopband에서의 ripple -> baseband spectrum에 영향을 준다."],
    ["Anti aliasing Filter의 설계 2",
     "즉, A/D 변환시의 LPF는 stopband에서 얼만큼 신호를 제거(reject) 할 수 있느냐가 중요하다."],
    ["Anti aliasing Filter의 설계 3",
     "Stopband의 신호제거 정도는 aliasing level을 결정한다."],



]


q5 = [
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
    ["",
     ""],
]


def m(q):
    for i in range(len(q)):
        print(q[i][0])
        print("답 : ", end='')
        if input() == '0':
            break
        else:
            print("->   " + q[i][1])
            print("")


def t(q):
    i = random.randrange(0, len(q))
    print(q[i][0])
    print("답 : ", end='')
    input()
    print("->   " + q[i][1])
    print("")


def n(q):
    for i in range(len(q)):
        print(q[i][0].split()[0])
        print("답 : ", end='')
        if input() == '0':
            break
        else:
            print("->   " + q[i][1])
            print("")


while(1):
    m(q4)
