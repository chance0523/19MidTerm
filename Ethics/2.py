import random
from collections import deque

# 심리적 이기주의와 윤리적 이기주의 #

q1 = [
    ["OO적 이기주의와 OO적 이기주의", "심리적 이기주의와 윤리적 이기주의"],
    ["OO은 OO상 OO OO을 OO하는 OO이고,", "인간은 본성상 자기 이익을 추구하는 존재이고"],
    ["OO의 모든 OO는 OOO OO에서 행해진다.", "인간의 모든 행위는 이기적 동기에서 행해진다."],
    ["OO적 이기주의의 주장이다.", "심리적 이기주의의 주장이다."],
    ["확실히 OO은 OOO으로 OOO인 OO을 가지고 있다.",
     "확실히 인간은 본성적으로 이기적인 성향을 가지고 있다."],
    ["하지만 그렇다고 OO의 모든 OO이 오로지 OO OO을 위해서 행해진다는 말은 사실이 될 수 있을까?",
     "하지만 그렇다고 인간의 모든 행동이 오로지 자기 이익을 위해서 행해진다는 말은 사실이 될 수 있을까?"],
    ["예를 들어 OO의 OO OO이나 OO를 OO기 위해 OO가 OO하는 OO들의 OO을 OO적 OOOO로 설명 할 수 있을까?",
     "예를 들어 부모의 자식 사랑이나 전우를 구하기 위해 자기가 희생하는 군인들의 모습을 심리적 이기주의로 설명 할 수 있을까?"],
    ["이러한 OO이 나오게 된 OO에는 OO의 OO을 OO하는 지나친 OOOO가 있어서",
     "이러한 주장이 나오게 된 배경에는 인간의 본성을 억압하는 지나친 도덕주의가 있어서"],
    ["아마 이를 주장하는 사람들은 OO OO을 OO하는 OO의 OO적 OO을 OO적으로만 볼 것 이 아니라 오히려 OO적으로 바라볼 필요가 있다고 생각 할 것이다.",
     "아마 이를 주장하는 사람들은 자기 이익을 추구하는 인간의 자연적 본성을 부정적으로만 볼 것 이 아니라 오히려 긍정적으로 바라볼 필요가 있다고 생각 할 것이다."],
    ["OO적 이기주의는 OO은 OO의 OO을 OO하는 것이 OOO하다 라고 말한다.",
     "윤리적 이기주의는 인간은 자기의 이익을 추구하는 것이 바람직하다 라고 말한다."],
    ["이들은 OO OO을 OO하는 OO의 OO적 OO을 일단 OO한 다음,",
     "이들은 자기 이익을 추구하는 인간의 자연적 본성을 일단 인정한 다음,"],
    ["그 OO OO이라는 OO를 어떻게 OO적으로 OO할 것인지를 OO적으로 OO해 본 결과 나오게 된 이론이다.",
     "그 자기 이익이라는 목표를 어떻게 효과적으로 달성할 것인지를 이성적으로 생각해 본 결과 나오게 된 이론이다."],
    ["이것을 우리는 OO적인 이기주의와 OO하여 OO적 이기주의라고 부를 수 있다.",
     "이것을 우리는 충동적인 이기주의와 구분하여 합리적 이기주의라고 부를 수 있다."]
]

# 합리적 이기주의 #

q2 = [
    ["OO적 이기주의", "합리적 이기주의"],
    ["합리적 이기주의는 OO은 OO적 OO이기 때문에 OO적이고 OO적인 OO를 OO하면서",
     "합리적 이기주의는 인간은 이성적 존재이기 때문에 충동적이고 본능적인 욕구를 통제하면서"],
    ["OO적으로 OO에게 OO의 OO이 되는 것을 행해야 한다고 한다.",
     "장기적으로 자기에게 최선의 이익이 되는 것을 행해야 한다고 한다."],
    ["즉, OOO적인 OO적 OOO이 아니라 OO 있는 OOO를 OO하게 될것이다.",
     "즉, 근시안적인 배타적 이기심이 아니라 분별 있는 자기애를 지향하게 될것이다."],
    ["여기서 OO적 OO이란 OO의 OO적 OO을 OO하게 OO 할 줄 아는 OO적인 OO을 의미한다.",
     "여기서 이성적 능력이란 자기의 궁극적 이익을 냉철하게 계산 할 줄 아는 타산적인 능력을 의미한다."],
    ["만약 우리가 이러한 OO적 이기주의를 모두 행할 수 있으면 좋겠지만,",
     "만약 우리가 이러한 합리적 이기주의를 모두 행할 수 있으면 좋겠지만,"],
    ["우리 대부분은 OO적 OO와 OO 등을 OO 만큼의 OO한 OO을 지니고 있지 못하다.",
     "우리 대부분은 본능적 욕구와 충동 등을 이길 만큼의 냉철한 이성을 지니고 있지 못하다."],
    ["또한 우리의 OOO적인 OOO과 OO이 OO적인 OOO를 OO할 것이다.",
     "또한 우리의 근시안적인 이기심과 욕심이 장기적인 자기애를 압도할 것이다."],
    ["아쉽게도 OO적인 OO보다는 OO적 OO의 O에 더 크게 OO되는 것이 OO의 OO적인 OO인 것 같다.",
     "아쉽게도 이성적인 모습보다는 본능적 욕망의 힘에 더 크게 좌우되는 것이 인간의 현실적인 모습인 것 같다."]
]


# 홉스 사회 계약론의 한계 #

q3 = [
    ["홉스 사회계약론의 한계",
     "홉스 사회계약론의 한계"],
    ["윤리나 법을 지키는 것은 그것이 자기 이익에 도움이 되기 때문이다.",
     "윤리나 법을 지키는 것은 그것이 자기 이익에 도움이 되기 때문이다."],
    ["한계, 문제점) 규범과 자기 이익이 충돌하는 경우 - 규범을 지킬 근거 사라진다.",
     "한계, 문제점) 규범과 자기 이익이 충돌하는 경우 - 규범을 지킬 근거 사라진다."],
    ["홉스 : 국가는 규범을 강제할 절대적 권리를 갖는다.",
     "홉스 : 국가는 규범을 강제할 절대적 권리를 갖는다."],
    ["사회계약론에 따르면 각 개인은 자기의 생존과 이익을 확보하기 위해 법과 규범을 세운다.",
     "사회계약론에 따르면 각 개인은 자기의 생존과 이익을 확보하기 위해 법과 규범을 세운다."],
    ["그리고 이 법과 규범을 지키는 것은 그것이 자기 이익에 도움이 되기 때문이다.",
     "그리고 이 법과 규범을 지키는 것은 그것이 자기 이익에 도움이 되기 때문이다."],
    ["하지만 만약 이와 같은 법을 지키는 행위와 자기의 이익이 충돌할 경우 우리는 어떻게 하여야 하는가?",
     "하지만 만약 이와 같은 법을 지키는 행위와 자기의 이익이 충돌할 경우 우리는 어떻게 하여야 하는가?"],
    ["이에 대해 홉스는 주장한다. 일단 계약이 성립된 후에는 법을 집행하는데에 있어 절대권을 가져야 한다는 것이다.",
     "이에 대해 홉스는 주장한다. 일단 계약이 성립된 후에는 법을 집행하는데에 있어 절대권을 가져야 한다는 것이다."],
    ["즉, 법을 위반하는 행위는 단호히 처벌함으로써 사회 질서를 유지해야 한다는 것이다.",
     "즉, 법을 위반하는 행위는 단호히 처벌함으로써 사회 질서를 유지해야 한다는 것이다."],
    ["그러나 이에도 명확한 한계가 존재하는데 왜냐하면 우리가 애초에 계약에 동의했던 이유는 오로지 자기의 생존과 이익을 확보하기 위함이었는데도,",
     "그러나 이에도 명확한 한계가 존재하는데 왜냐하면 우리가 애초에 계약에 동의했던 이유는 오로지 자기의 생존과 이익을 확보하기 위함이었는데도,"],
    ["이제는 그 계약의 결과인 법(규범)을 지키는 것이 그것의 근거인 자기 생존과 이익에 위배될 가능성을 지니게 되었기 때문이다.",
     "이제는 그 계약의 결과인 법(규범)을 지키는 것이 그것의 근거인 자기 생존과 이익에 위배될 가능성을 지니게 되었기 때문이다."]
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
    m(q1)
    m(q2)
    m(q3)
    