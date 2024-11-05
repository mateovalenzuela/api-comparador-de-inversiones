import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.mark.asyncio
async def test_money_market_investment():
    # Datos de prueba para Money Market Investment
    data = {
        "amount": 1000,
        "interest_rate": 30,  # TNA
        "months_duration": 12
    }

    # Esperado: cálculo de inversión con interés compuesto diario
    daily_interest_rate = (data["interest_rate"] / 100) / 365
    expected_amount = data["amount"] * ((1 + daily_interest_rate) ** (365 * data["months_duration"] / 12))

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8000") as client:
        response = await client.post("/money_market_investment", json=data)

    assert response.status_code == 200
    assert response.json()[-1]["amount"] == pytest.approx(expected_amount,
                                                          0.01), "Error en cálculo de Money Market Investment"


@pytest.mark.asyncio
async def test_fixed_term_with_reinvestment():
    # Datos de prueba para Fixed Term con reinversión
    data = {
        "amount": 1000,
        "interest_rate": 45,  # TNA
        "months_duration": 12
    }

    # Cálculo de la TEA a partir de la TNA
    monthly_rate = data["interest_rate"] / 100 / 12  # TNA mensual
    expected_amount = data["amount"] * ((1 + monthly_rate) ** data["months_duration"])  # Capitalización mensual

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8000") as client:
        response = await client.post("/fixed_term_with_reinvestment", json=data)

    assert response.status_code == 200
    assert response.json()[-1]["amount"] == pytest.approx(expected_amount,
                                                          0.01), "Error en cálculo con reinversión mensual"


@pytest.mark.asyncio
async def test_fixed_term_without_reinvestment():
    # Datos de prueba para Fixed Term sin reinversión
    data = {
        "amount": 1000,
        "interest_rate": 45,  # TNA
        "months_duration": 12
    }

    # Cálculo esperado para inversión sin reinversión
    monthly_interest_rate = (data["interest_rate"] / 100) / 12
    expected_amount = data["amount"] * (1 + monthly_interest_rate * data["months_duration"])

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8000") as client:
        response = await client.post("/fixed_term_without_reinvestment", json=data)

    assert response.status_code == 200
    assert response.json()[-1]["amount"] == pytest.approx(expected_amount, 0.01), "Error en cálculo sin reinversión"
