import pyupbit

access = "acbyMdLd6qOklJyIHkiPufGwGTXYpQxx2J8weLnM"          # 본인 값으로 변경
secret = "gEA5KXPCYTWYD2JrTi02sLO0c2hwUDk841kbSiKX"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-EMC2"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회