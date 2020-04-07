import random
from collections import deque


# 심리학의 정의 #"
q1 = [
    ["심리학의 정의 : 개인의 ~ ","'개인'의 행동과 정신과정에 대한 '과학적 방법'을 이용한 연구"],
    ["심리학의 정의 세 가지", "과학적 방법, 행동, 정신과정"],
    ["과학적 방법1 : OO를 분석하고 OO하기 위한 일련의 단계들", "문제를 분석하고 해결하기 위한 일련의 단계들"],
    ["과학적 방법2 : OO의 OO을 위해 OOO으로 OOO OO 이용", "'결론의 도출'을 위해 '객관적으로 수집된 정보' 이용"],
    ["행동1 : 유기체가 'OO에 OO'하는 수단", "환경에 적응하는 수단"],
    ["행동2 : 심리학에서는 인간/동물의 'OO 가능한 OO'을 다룸", "관찰 가능한 행동"],
    ["정신과정", "사고, 계획, 추론, 꿈 등"],
    ["얼마나 OOO이고, 어떻게 OO했는지", "객관적, 처리"]
]

# 심리학의 목표 #
q2 = [
    ["심리학의 목표1", "무엇이 일어나는가를 '기술하기'"],
    ["심리학의 목표2", "무엇이 발생했는가를 '설명하기'"],
    ["심리학의 목표3", "무엇이 일어날것인지 '예측하기'"],
    ["심리학의 목표4", "행동 '통제하기'"],
    ["무엇이 일어나는가를 '기술하기'1 : OO의 OO한 OO", "행동의 정확한 관찰"],
    ["무엇이 일어나는가를 '기술하기'2 : 기술을 위한 다양한 OOOO 사용 가능", "분석수준"],
    ["무엇이 일어나는가를 '기술하기'3 : 각 수준의 OOO적 기술은 서로 다른 OO에 대한 O을 제공 할 수 있음",
        "각 수준의 심리학적 기술은 서로 다른 질문에 대한 답을 제공 할 수 있음"],
    ["무엇이 발생했는가를 '설명하기'1 : OO/OOOO에서의 OO적인 OO 규명", "행동/정신과정에서의 규칙적인 패턴 규명"],
    ["무엇이 발생했는가를 '설명하기'2 : OOO 변인 : OO의 OO적 결정인",
     "유기체 변인 : 행동의 내부적 결정인 (유전적 체질, 내적 동기, 지능, 자존감 등)"],
    ["무엇이 발생했는가를 '설명하기'3 : OO 변인 : OO에 OO을 미치는 OO적 요인들",
        "상황 변인 : 행동에 영향을 미치는 외부적 요인들 (사회적 압력, 환경적 변화 등)"],
    ["무엇이 일어날 것인지 '예측하기'1 : 특정 OO이 일어나거나 특정 OO를 발견 할 OOO에 대한 진술",
        "특정 행동이 일어나거나 특정관계를 발견 할 가능성에 대한 진술"],
    ["무엇이 일어날 것인지 '예측하기'2 : OO OO하도록 OO하게 OO되어야", "검증 가능하도록 정확하게 기술되어야"],
    ["무엇이 일어날 것인지 '예측하기'3 : OO들이 OOO하다면 OO되어야", "증거들이 불충분하다면 기각되어야"],
    ["행동 통제하기1 : 행동이 ~", "행동이 일어나거나 일어나지 않도록 하려는 시도"],
    ["행동 통제하기2", "삶의 질 향상을 도울 수 있으므로 중요"]
]

# 내적 변인 #

q3 = [
    ["내적 변인의 예 1", "정서조절"],
    ["마시멜로우 게임, 선물포장 뜯기 실험, 무표정 상황에서의 개인차 : OOOO에서의 OOO", "만족지연에서의 개인차"],
    ["만족지연도 OO이 될 수 있다.", "훈련"],
    ["내적 변인의 예 2", "성취동기"],
    ["성취동기란 : 아동이 OO을 OO 했을 때, 어떤 OO으로 OO을 OO하는가",
        "아동이 실패를 경험 했을 때, 어떤 방식으로 행동을 추진하는가"],
    ["OOOOO 반응(OOO OO으로 OO) vs OOOO 반응", "숙달지향적 반응(새로운 전략으로 시도), 무기력한 반응"],
    ["OO 목표(OO가 중요) vs OO 목표(OOOO가 중요)", "평가목표(결과가 중요), 학습목표(과정자체가 중요)"],
    ["OOO 특질 이론", "암묵적"],
    ["불변론자 : ~ 반응, ~ 목표", "무기력한 반응, 평가목표"],
    ["가변론자 : ~ 반응, ~ 목표", "숙달지향적 반응, 학습목표"],
    ["불변론자 : OO능력이나 OO은 ~", "지적 능력이나 성격은 결정되고 변하지 않는다.(믿음과 신념)"]
]

# 상황 변인 #

q4 = [
    ["상황 변인의 예 1", "동조"],
    ["동조의 예 : 앞 사람들이 ~", "앞 사람들이 다 오답을 말 할 때 얼마나 그 압력에 굴복 할 수 있는지"],
    ["동조의 원인1 : OOO 원인", "규범적 원인"],
    ["동조의 원인2 : 내가 OO OO에 OOOO 싶음", "내가 속한 집단에 수용되고 싶음"],
    ["동조의 원인3 : OO적 OO", "사회적 욕구"],
    ["동조가 증가하는 조건1 : 나를 제외하고 ~", "나를 제외하고 만장일치 같은 오답이면 동조 증가"],
    ["동조가 증가하는 조건2 : 집단의 인원수가 ~", "집단의 인원수가 적어도 3명은 있어야 동조 증가"],
    ["동조가 증가하는 조건3 : 집단이 OO적인 집단일수록 ~", "매력적인"],
    ["상황 변인의 예 2", "권위"],
    ["권위의 예 : OO이 OO에 미치는 효과에 관한 연구 : ", "처벌이 학습에 미치는 영향"],
    ["권위 - 어떤 OO에 놓여 있냐가 중요", "상황"]
]

# 의식의 심리 #

q5 = [
    ["의식 : OO를 담은, OO이 있는 일련의 행동", "의미를 담은, 규칙이 있는 일련의 행동"],
    ["의식의 예 : 먹기 전에 행하는", "먹기 전에 행하는 일종의 의식이 실제로 음식 맛을 돋구는 효과가 있다."],
    ["깔끔한 방", "선하고 건강한 생활. Classic 선택"],
    ["지저분한 방", "창의적 사고. New 선택"]
]

# 문화에 따른 관점의 차이 #

q6 = [
    ["동양인 : OO, OO, OO을 생각. OO를 많이 사용", "관계, 맥락, 입장을 생각. 동사를 많이 사용"],
    ["서양인 : OO 중심. OO를 많이 사용. 영어는 OOO를 중요하게 생각",
        "객체 중심. 명사를 많이 사용. 영어는 단복수를 중요하게 생각"]
]

# 심리학의 종류 #

q7 = [
    ["심리학의 종류 11가지", "인지, 발달, 행동신경과학, 성격, 사회, 임상, 건강, 교육, 산업/조직, 스포츠, 법"],
    ["인지 심리학 : OOO에 사용되는 OO에 따라 OO가 다름", "질문지에 사용되는 동사에 따라 결과가 다름"],
    ["성격 심리학1 : 바넘효과", "심리테스트 다 내 얘기"],
    ["성격 심리학2-1 : Big Five 모델(OCEAN)",
     "Openess, Conscientiousness, Extraversion, Agreeableness, Neuroticism"],
    ["성격 심리학2-2 : Big Five 모델(OCEAN)",
     "개방성, 성실성, 외향성, 우호성, 신경증적 경향성"],
    ["성격 심리학3 : OO의 차이지, OO의 차이가 아니다. OOO이 있을 뿐 어떤 성격이 더 좋은 것은 아니다.",
        "정도의 차이지, 종류의 차이가 아니다. 장단점만 있을 뿐 어떤 성격이 더 좋은 것은 아니다"],
    ["사회 심리학 : 실제나 상상에서 OO OO의 OO가 ~",
        "실제나 상상에서 다른 사람의 존재가 사고와 감정 및 행동에 어떤 영향을 미치는가를 연구"]
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

# practice #
def prac(q1,q2,q3,q4,q5,q6,q7):
    while(1):
        print("0 = 종료")
        print("1. 심리학의 정의")
        print("2. 심리학의 목표")
        print("3. 내적 변인")
        print("4. 상황 변인")
        print("5. 의식의 심리")
        print("6. 문화에 따른 관점의 차이")
        print("7. 심리학의 종류")

        c = int(input())
        if c == 1:
            m(q1)
        elif c == 2:
            m(q2)
        elif c == 3:
            m(q3)
        elif c == 4:
            m(q4)
        elif c == 5:
            m(q5)
        elif c == 6:
            m(q6)
        elif c == 7:
            m(q7)

        else:
            break

def test(q1,q2,q3,q4,q5,q6,q7):
    while(1):
        c = random.randrange(0, 7)
        if c == 1:
            t(q1)
        elif c == 2:
            t(q2)
        elif c == 3:
            t(q3)
        elif c == 4:
            t(q4)
        elif c == 5:
            t(q5)
        elif c == 6:
            t(q6)
        elif c == 7:
            t(q7)

def z(q1, q2, q3, q4, q5, q6, q7):
    m(q1)
    m(q2)
    m(q3)
    m(q4)
    m(q5)
    m(q6)
    m(q7)
    

while(1):
    print("p : practice")
    print("t : test")
    print("z : zook")
    k = input()
    if k == 'p':
        prac(q1, q2, q3, q4, q5, q6, q7)
    elif k == 't':
        test(q1, q2, q3, q4, q5, q6, q7)
    elif k == 'z':
        z(q1, q2, q3, q4, q5, q6, q7)
    else:
        break
