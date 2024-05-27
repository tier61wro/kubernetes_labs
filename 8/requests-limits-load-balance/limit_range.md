https://go.skillbox.ru/education/course/devops-kubernetes/8a160947-b911-4c2e-9953-bc3f8baf009f/videolesson

# 8.2 LimitRange and Priority-классы:

## LimitRange:
1. `kubectl apply -f ./8.2/limit-range.yaml`:
    limitrange/resource-limits created
2. `kubectl apply -f nginx-pod.yaml`
    Создаст pod с default limits:
    ```
    default:
        cpu: 300m
        memory: 200Mi
    defaultRequest:
        cpu: 200m
        memory: 100Mi
    ```
3. `kubectl apply -f nginx-pod-big.yaml` - создать под с лимитом выше заданного в ./8.2/limit-range.yaml
    В таком случае под не создастся с ошибкой: `forbidden, max mem usage is 1Gi`

## Priority-классы:
1. `PriorityClass`:
    Создаёт класс `high-priority` для возможности создания высоко-приоритетных подов
    ```
    apiVersion: scheduling.k8s.io/v1
    kind: PriorityClass
    metadata:
    name: high-priority
    value: 1000000
    globalDefault: false
    description: "High priority class for important pods"
    ```
2. `Pod with PriorityClassName`:
    Под с высоким приоритетом, который будет создан даже при отсутствии ресурсов на ноде, удаляя низко-приоретные под/поды
    ```
    apiVersion: v1
    kind: Pod
    metadata:
    name: nginx-pod
    spec:
    containers:
    - name: nginx
        image: nginx
    priorityClassName: high-priority
    ```