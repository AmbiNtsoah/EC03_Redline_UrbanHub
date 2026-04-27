# README.md

## Prompts de la conversation (mots pour mots)

### Prompt 1

Je veux que tu te rappelles tres brievement mais au complet ce que tu as pu recense de mon projet Urbanhub.

---

### Prompt 2

Maintenant je souhaite ajouter un nouveau microservice de validateur de donnees venant des capteur IoT. Ce nouveau microservice est sense valider que les donnees venant du microservice collecte IoT sont des donnees valide pour que le microservice de traitement puisse les exploiter.
Ce nouveau microservice de validateur de donnees recoit comme donnees d'entree un format JSON de type : {"sensor": "co2", "value" : 500.0}
Comme donnees de sories, le microservice de validateur de donnees retourne encore un format JSON de  type : {"valid": true, "level": "normal", "sensor":"co2", "value": 500.0, "threshold": 800, "timestamp": "..."}

---

### Prompt 3

les capteurs connus sont co2, temperature, noise, pm25,.
Ils ont des seuil modere et critique.

---

### Prompt 4

Maintenant, je veux que tu me guide sur l'implementation de ce microservice. L'architecture sera en feature-folder. Comme environnement, poetry a deja ete initie et les dependance FastAPI, pytest, psycopg ont ete installer. Voici la structure que j'ai:

ms_validateur_capteur$ tree -L 3
.
├── docker-compose.yml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│   ├── domain
│   │   └── __init__.py
│   ├── dto
│   │   └── __init__.py
│   ├── ms_validateur_capteur
│   │   └── __init__.py
│   ├── repositories
│   │   └── __init__.py
│   └── validator.py
└── tests
    └── __init__.py

7 directories, 11 files

---

### Prompt 5

Les tests sont insuffisante

ms-validateur-capteur-py3.12) hary@cactusjack:~/Study/MCCI/Mastere/Epreuves Certifiantes/EC_03/EC03/EC03_UrbanHub/ms_validateur_capteur$ pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
======================================================================================================= test session starts ========================================================================================================
platform linux -- Python 3.12.3, pytest-9.0.3, pluggy-1.6.0 -- /home/hary/.cache/pypoetry/virtualenvs/ms-validateur-capteur-i6N-2iOW-py3.12/bin/python
cachedir: .pytest_cache
rootdir: /home/hary/Study/MCCI/Mastere/Epreuves Certifiantes/EC_03/EC03/EC03_UrbanHub/ms_validateur_capteur
configfile: pyproject.toml
plugins: anyio-4.13.0, cov-7.1.0
collected 3 items

tests/test_validator.py::test_co2_normal PASSED
tests/test_validator.py::test_co2_moderate PASSED
tests/test_validator.py::test_co2_critical PASSED
ERROR: Coverage failure: total of 30 is less than fail-under=80

========================================================================================================== tests coverage ==========================================================================================================
_________________________________________________________________________________________ coverage: platform linux, python 3.12.3-final-0 __________________________________________________________________________________________

Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
src/domain/__init__.py                      0      0   100%
src/domain/rules.py                         1      0   100%
src/dto/__init__.py                         0      0   100%
src/dto/request.py                          4      4     0%   1-5
src/dto/response.py                         9      9     0%   1-10
src/endpoints/__init__.py                   0      0   100%
src/endpoints/routes.py                    10     10     0%   1-14
src/ms_validateur_capteur/__init__.py       0      0   100%
src/ms_validateur_capteur/service.py       12      1    92%   6
src/validator.py                            4      4     0%   1-6
---------------------------------------------------------------------
TOTAL                                      40     28    30%
FAIL Required test coverage of 80% not reached. Total coverage: 30.00%

---

### Prompt 6

Corrige moi les erreurs de lint qui pourrait causer une erreur de qualite flake8

from fastapi.testclient import TestClient

from src.validator import app
from src.ms_validateur_capteur.service import validate_sensor
from src.dto.request import SensorRequest
from src.dto.response import SensorResponse

client = TestClient(app)

def test_co2_normal():
    result = validate_sensor("co2", 500)
    assert result["level"] == "normal"


def test_co2_moderate():
    result = validate_sensor("co2", 900)
    assert result["level"] == "moderate"


def test_co2_critical():
    result = validate_sensor("co2", 1500)
    assert result["level"] == "critical"


def test_unknown_sensor():
    import pytest
    with pytest.raises(ValueError):
        validate_sensor("fake", 100)

def test_request_model():
    data = SensorRequest(sensor="co2", value=500)
    assert data.sensor == "co2"
    assert data.value == 500


def test_response_model():
    data = SensorResponse(
        valid=True,
        sensor="co2",
        value=500,
        level="normal",
        moderate_threshold=800,
        critical_threshold=1200,
        timestamp="now"
    )

    assert data.valid is True
    assert data.level == "normal"

def test_post_validate_normal():
    response = client.post(
        "/validate/",
        json={"sensor": "co2", "value": 500}
    )

    assert response.status_code == 200
    assert response.json()["level"] == "normal"


def test_post_validate_unknown_sensor():
    response = client.post(
        "/validate/",
        json={"sensor": "fake", "value": 100}
    )

    assert response.status_code == 400


def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200

---

### Prompt 7

Je veux que tu mettes dans un README les promtpes que j'ai ecris. Mots pour mots