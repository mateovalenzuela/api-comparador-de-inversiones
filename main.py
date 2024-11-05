from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services import calculate_fixed_term_without_reinvestment, calculate_fixed_term_with_monthly_reinvestment, \
    calculate_money_market_investment
from schemas import FixedInvestmentWithoutReinvestment, FixedInvestmentWithReinvestmentResponse, \
    FixedInvestmentWithReinvestment, FixedInvestmentWithoutReinvestmentResponse, MoneyMarketInvestmentResponse, \
    MoneyMarketInvestment
from typing import List

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/money_market_investment", response_model=List[MoneyMarketInvestmentResponse])
async def money_market_investment(data: MoneyMarketInvestment):
    result = calculate_money_market_investment(
        data.amount, data.interest_rate, data.months_duration
    )
    return result


@app.post("/fixed_term_with_reinvestment", response_model=List[FixedInvestmentWithReinvestmentResponse])
async def fixed_term_with_reinvestment(data: FixedInvestmentWithReinvestment):
    investment_growth = calculate_fixed_term_with_monthly_reinvestment(
        data.amount, data.interest_rate, data.months_duration
    )

    return investment_growth


@app.post("/fixed_term_without_reinvestment", response_model=list[FixedInvestmentWithoutReinvestmentResponse])
async def fixed_term_without_reinvestment(data: FixedInvestmentWithoutReinvestment):
    amounts = calculate_fixed_term_without_reinvestment(
        data.amount, data.interest_rate, data.months_duration
    )
    return amounts
