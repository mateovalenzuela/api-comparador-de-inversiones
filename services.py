from typing import List
from schemas import InvestmentResponse


def calculate_fixed_term_without_reinvestment(principal: float, interest_rate: float, months: int) -> List[InvestmentResponse]:
    # TNA mensual
    monthly_interest_rate = (interest_rate / 100) / 12
    fixed_investments = []

    # Agregar importe inicial en el mes 0
    fixed_investments.append(InvestmentResponse(
        amount=round(principal, 2),
        month=0,
    ))

    current_amount = principal

    # Calcular monto sin reinversión de intereses
    for month in range(1, months + 1):
        # Si el mes es un múltiplo de 12, se aplica el interés
        if month % 12 == 0:
            current_amount *= (1 + interest_rate / 100)  # Capitalización anual
        # Se agrega el monto del mes actual
        fixed_investments.append(InvestmentResponse(
            amount=round(current_amount, 2),
            month=month,
        ))

    return fixed_investments


def calculate_fixed_term_with_monthly_reinvestment(principal: float, interest_rate: float, months_duration: int) -> \
        List[InvestmentResponse]:
    # Convertimos la tasa anual en decimal
    annual_rate = interest_rate / 100
    # Calculamos la tasa nominal mensual
    monthly_rate = annual_rate / 12

    investment_growth = []
    current_amount = principal

    # Agregado de importe inicial al resultado
    investment_growth.append(InvestmentResponse(
        month=0,
        amount=round(current_amount, 2)
    ))

    for month in range(1, months_duration + 1):
        # Capitalización mensual con interés compuesto
        current_amount *= (1 + monthly_rate)
        investment_growth.append(InvestmentResponse(
            month=month,
            amount=round(current_amount, 2)
        ))

    return investment_growth


def calculate_money_market_investment(principal: float, interest_rate: float, months: int) -> List[InvestmentResponse]:
    daily_interest_rate = (interest_rate / 100) / 365  # TNA diaria
    investments = []

    # agregado de importe inicial al resulatdo
    investments.append(InvestmentResponse(
        amount=round(principal, 2),
        month=0,
    ))

    for month in range(1, months + 1):
        # Calcula el monto con interés compuesto diario hasta el mes actual
        amount = principal * ((1 + daily_interest_rate) ** (365 * month / 12))
        investments.append(InvestmentResponse(
            amount=round(amount, 2),
            month=month,
        ))

    return investments
