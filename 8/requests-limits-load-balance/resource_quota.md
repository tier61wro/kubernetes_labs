https://go.skillbox.ru/education/course/devops-kubernetes/8a160947-b911-4c2e-9953-bc3f8baf009f/videolesson

# 8.2 ResourceQuota:

1. `ResourceQuota` устанавливает ограничения на использование ресурсов в NS
    1. Количество создаваемых объектов (например, pods, services, replication controllers)
    2. Запросы CPU и памяти
    3. Лимиты CPU и памяти
    4. Количество persistent volume claims
    5. Количество сервисов
    6. Количество секретов
    7. Количество config maps
    8. Количество ресурсов для конкретных namespace'ов
2. `kubectl apply -f ./8.2/resource-quota.yaml` - resourcequota/compute-resources created
    `pods: "4"` - лимит на создание 4 подов
    При создании деплоймента с 10 подами - создастся только 4, а остальные 6 будут с ошибкой в RS: `forbidden, quota limited: pods=4`
3. `kubectl describe resourcequotas` - посмотреть квоту