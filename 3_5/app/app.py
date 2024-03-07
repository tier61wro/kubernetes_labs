# Импортируем необходимые модули из Flask для создания веб-сервиса и работы с запросами/ответами в формате JSON
from flask import Flask, request, jsonify

# Создаем экземпляр приложения Flask
admission_controller = Flask(__name__)


# Определяем маршрут для веб-хука; он обрабатывает только POST запросы по указанному пути
@admission_controller.route('/validate/deployments', methods=['POST'])
def deployment_webhook():
    # Получаем данные из входящего JSON запроса
    request_info = request.get_json()

    # Извлекаем UID из запроса, который необходимо включить в ответ для корреляции запроса и ответа в Kubernetes
    request_uid = request_info["request"]["uid"]

    # Проверяем наличие метки 'owner' в метаданных объекта запроса
    if request_info["request"]["object"]["metadata"]["labels"].get("owner"):
        # Возвращаем положительный ответ, если метка присутствует
        return admission_response(True, "Allow label exists", request_uid)

    # Возвращаем отрицательный ответ, если метка отсутствует
    return admission_response(False, "Not allowed without 'owner' label", request_uid)


# Функция для формирования JSON ответа веб-хука
def admission_response(allowed, message, uid):
    # Указываем версию API веб-хуков Kubernetes
    # Тип объекта ответа
    # Включаем UID запроса в ответ для корреляции
    # Решение веб-хука: разрешить или запретить операцию
    # Сообщение, объясняющее решение веб-хука
    return jsonify({
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": uid,
            "allowed": allowed,
            "status": {"message": message}
        }
    })


# Запускаем сервис на 0.0.0.0:8001 с использованием SSL/TLS сертификата и ключа
if __name__ == '__main__':
    admission_controller.run(host='0.0.0.0', port=8001, ssl_context=("/app/tls.crt", "/app/tls.key"))
