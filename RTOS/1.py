# CH 1. Introduction #

q1 = [
    ["Common definition of OS ...", "kernel + system programs"],
    ["Operating System Provide ...", "HW resources를 allocate하고 control함. 사용자에게 API 제공"],
    ["OS is designed for ...", "Usuabilty, Performance, Resource utilization"],
    ["SW booting process를 설명하시오",
        "bootstrap이 모든 시스템을 초기화. bootstrap이 OS를 메모리에 로드. 커널 로드. 시스템 프로세서 로드."],
    ["Interrupt 종류",
        "HW와 SW -generated interrupt. HW-generated interrupt는 device controller에서, SW-generated는 error나 system call에서 (Trap)"],
    ["Interrupt 과정", "Interrupt가 일어나면 CPU는 하던것을 멈추고 interrput vector로 보냄. ISR이 execute됨."],
    ["Device ~~ 의 두 가지 종류 ", "Device Controller, Device Driver. Controller는 deveice를 컨트롤. Driver는 SW인데, device controller를 컨트롤"],
    ["Multi-processor system의 장점", "Throughput, Scalability, Reliability"],
    ["Multi-processor의 두 가지 종류",
        "AMP, SMP. AMP는 각 processor가 specific task를 담당. SMP는 각 processor가 모든 task를 담당"],
    ["Multiprogramming vs Multitasking",
        "Multiprogramming - context switch, non-preemptive. Multitasking - scheduling 이용."],
    ["Duel mode operation", "User mode vs Kernel mode."],
    ["Protection - OS from errant programs",
        "OS 코드나 데이터는 커널모드에서만 접근 가능. Interrupt나 Trap을 통해서만 유저모드에서 커널모드로 진입"],
    ["Protection - Errant programs from one another",
        "Virtual memory mapping을 통해서 프로그램이 다른 프로그램들의 메모리에 접근 못하도록 함. timer이용."],
    ["Process", "시스템에서 일의 단위. 하나 또는 하나 이상의 thread를 가지고 있음."],
    ["Memory와 OS의 역할", "메모리의 어디가 지금 쓰이고 있고, 누가 쓰고 있는지 계속 알고 있어야함. 어떤 프로세스나 데이터가 메모리에 들어가고 나갈건지 결정. 필요한 메모리 공간을 결정."],
]

# CH 2. OS Structures #

q2 = [
    ["OS kernel의 종류", "Monolithic kernel, Microkernel, Loadable kernel module"],
    ["Monolithic kernel의 장단점", "overhead가 적다. 구현, 유지에 어렵다"],
    ["Microkernel의 장단점", "다루기 쉽다. overhead 때문에 performance가 떨어진다."],
]

# CH 3. Embedded SW Platform & RTOS #

q3 = [
    ["두 가지 종류의 embedded system",
        "Complex ES, Simple ES. Complex는 RTOS based. Simple은 Firmware based"],
    ["Platform", "SW가 run 하게 하는 HW architecture나 SW framework"],
    ["SW Platform consist of ...", "OS, Run-time libraries, Middleware"],
    ["Polled Loop의 장점", "쓰고 디버그 하는게 쉽다. 주기성이나 예측가능한 input에 좋다."],
    ["Polled Loop의 단점", "burst event에 취약, unpredictable하거나 fast response를 요하는 input에 취약. complex system에 사용하기 어렵다. waste of CPU time"],
    ["Code Partitioning의 문제",
        "가독성이 떨어짐. partitioning 뒤에 verification이 필요, code 수정시 다시 partitioning하고 verification 해야함"],
    ["Interrupt의 장단점", "빠른 response time. interrupt disabled section에서는 delay 될 수 있다."],
    ["Non-preemptive Scheduling", "Task state. Context switching(yield)"],
    ["RTOS", "Provide predictablity, real-time scheduling."],
    ["Requirements of RTOS",
        "Preemptive priority based scheduling. Bounded interrupt latency, bounded scheduling latency"],
]

# CH 4. Tasks #

q4 = [
    ["태스크 생성과정", "스택 할당 및 초기화. TCB 할당 및 초기화. context 생성. 스케줄링"],
    ["태스크 삭제과정", "스택 및 TCB 반환. 스케줄링"],
    ["태스크 삭제 시 주의사항", "태스크가 할당한 자원을 올바르게 반환해야 함. (메모리, 세마포어 등)"],
    ["사용자 설정 후크 함수(user-configurable hooks)",
     "특정 이벤트 발생 시 사용자 정의함수 호출. (태스크 생성 및 삭제 시, context switching 시)"],
]

# CH 5. Scheduling #

q5 = [
    ["Scheduling goals",
        "Throughput, Latency(Turnaround, response time), Fairness(Equal CPU time)"],
    ["Realtime scheduling", "Deadline guarantee"],
    ["Round-Robin scheduling",
        "assigns a fixed time unit per process. Poor average response time"],
    ["Shortest Job first", "Least average response time"],
    ["Fixed Priority Preemptive Scheduling",
        "낮은 priority process는 higher priority process에 의해 interrupt 당할 수 있다."],
    ["Rate Monotonic scheduling", "Assign higher priority to tasks with shorter period"],
    ["Earliest Deadline First",
        "Process with the earliest deadline to be next in the queue"],
]

# CH 6. Scheduler Implementaion uC/OS #

q6=[
    ["Context Switch",""],
]

# CH 7. Synchronization #

q7=[
    ["",""],
]