import requests
import json

class Request:
    """Producto final: representa una solicitud HTTP completamente configurada."""
    def __init__(self, method, url, headers=None, params=None, body=None, auth=None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.params = params or {}
        self.body = body
        self.auth = auth

    def send(self):
        """Ejecuta la solicitud HTTP y retorna la respuesta."""
        response = requests.request(
            method=self.method,
            url=self.url,
            headers=self.headers,
            params=self.params,
            json=self.body,
            auth=self.auth
        )
        return response

    def __str__(self):
        return f"Request({self.method} {self.url})"


class RequestBuilder:
    """Builder: construye el objeto Request paso a paso."""
    def __init__(self):
        self._method = "GET"
        self._url = None
        self._headers = {}
        self._params = {}
        self._body = None
        self._auth = None

    def set_method(self, method):
        self._method = method.upper()
        return self

    def set_url(self, url):
        self._url = url
        return self

    def add_header(self, key, value):
        self._headers[key] = value
        return self

    def add_param(self, key, value):
        self._params[key] = value
        return self

    def set_body(self, body):
        if isinstance(body, dict):
            self._body = body
        else:
            raise TypeError("El cuerpo debe ser un diccionario JSON.")
        return self

    def set_auth(self, username, password):
        self._auth = (username, password)
        return self

    def build(self):
        # Validaciones antes de construir
        if not self._url:
            raise ValueError("La solicitud necesita una URL.")
        if self._method not in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
            raise ValueError(f"Método HTTP inválido: {self._method}")
        return Request(
            self._method, self._url, self._headers, self._params, self._body, self._auth
        )


# Director (opcional): define solicitudes comunes o preconfiguradas
class ApiDirector:
    """Facilita la creación de solicitudes estándar."""
    @staticmethod
    def github_user_request(username):
        return (RequestBuilder()
                .set_method("GET")
                .set_url(f"https://api.github.com/users/{username}")
                .add_header("Accept", "application/vnd.github.v3+json")
                .build())

    @staticmethod
    def post_json_request(url, data):
        return (RequestBuilder()
                .set_method("POST")
                .set_url(url)
                .add_header("Content-Type", "application/json")
                .set_body(data)
                .build())


# Uso práctico
if __name__ == "__main__":
    # Ejemplo 1: GET a la API de GitHub
    req1 = ApiDirector.github_user_request("octocat")
    res1 = req1.send()
    print(res1.status_code)
    print(json.dumps(res1.json(), indent=2))

    # Ejemplo 2: POST con JSON personalizado
    req2 = (RequestBuilder()
            .set_method("POST")
            .set_url("https://httpbin.org/post")
            .add_header("Content-Type", "application/json")
            .set_body({"user": "Jhon", "message": "Hello!"})
            .build())

    res2 = req2.send()
    print(res2.status_code)
    print(json.dumps(res2.json(), indent=2))
