liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def getAmountOut(amountIn, reserve0, reserve1):
    amountInWithFee = amountIn*997
    numerator = amountInWithFee*reserve1
    denominator = reserve0*1000 + amountInWithFee
    amountOut = numerator / denominator
    return amountOut

def print_output(path, checktokenBtokens):
    # 輸出路徑&換取的amount
    path_str = '->'.join(path)
    print(f"path: {path_str}, tokenB balance={checktokenBtokens:.6f}")

def find_next_token(graph, current_token, start_token):
    next_token = None
    max_ratio = 0

    # go through all 鄰居
    for neighbor, ratio in graph[current_token].items():
        # 排除與起始 token 相同的鄰居
        if neighbor == start_token:
            continue
        
        # 找可以換取最多 token 比例的鄰居
        if ratio > max_ratio:
            max_ratio = ratio
            next_token = neighbor
    
    return next_token

# 所有 token 之間的交易路徑
graph = {
    "tokenA": {"tokenB": 10, "tokenC": 7, "tokenD": 9, "tokenE": 5},
    "tokenB": {"tokenA": 17, "tokenC": 4, "tokenD": 6, "tokenE": 3},
    "tokenC": {"tokenA": 11, "tokenB": 36, "tokenD": 12, "tokenE": 8},
    "tokenD": {"tokenA": 15, "tokenB": 13, "tokenC": 30, "tokenE": 25},
    "tokenE": {"tokenA": 21, "tokenB": 25, "tokenC": 10, "tokenD": 60}
}

# 尋找路徑
start_token = "tokenB"
tokensBefore = 5
current_token = start_token
shortestPath = ["tokenB"]
# while(start_token != "tokenB" or tokensBefore < 20):
#     next_token = find_next_token(graph, current_token, start_token)
#     if next_token is None:
#         break
#     print(f"{current_token}->{next_token}") #tokenB->tokenA
#     shortestPath.append(next_token)
#     print(f"before_liquidity: {graph[next_token][current_token]}, {graph[current_token][next_token]}, {graph[next_token][current_token]*graph[current_token][next_token]}") #10,17
#     tokensAfter =  getAmountOut(tokensBefore, graph[next_token][current_token], graph[current_token][next_token])
#     print(f"amountIn: {tokensBefore}, amountOut: {tokensAfter}") #5,5.655321988655322
#     graph[next_token][current_token] += tokensBefore
#     graph[current_token][next_token] -= tokensAfter
#     print(f"after_liquidity: {graph[next_token][current_token]},{graph[current_token][next_token]}, {graph[next_token][current_token]*graph[current_token][next_token]}")
#     # print(graph)
#     tokensBefore = tokensAfter
#     current_token = next_token
#     # print("current_token", current_token, "tokensBefore", tokensBefore)
#     checktokenBtokens = getAmountOut(tokensBefore, graph["tokenB"][current_token], graph[current_token]["tokenB"])
#     # print("checktokenBtokens:", checktokenBtokens)
#     if (checktokenBtokens > 20):
#         print(f"{current_token}->tokenB") 
#         print(f"amountIn: {tokensBefore}, amountOut: {checktokenBtokens}")
#         graph["tokenB"][next_token] += tokensBefore
#         graph[next_token]["tokenB"] -= checktokenBtokens
#         shortestPath.append("tokenB")
#         print_output(shortestPath, checktokenBtokens)
#         exit()
amountOut = getAmountOut(1, 10, 100)
print("liquidity(10,100),", "amountIn = 1,","amountOut:", getAmountOut(1, 10, 100), "tokenA:tokenB = 1:", getAmountOut(1, 10, 100))
print("liquidity(10,100),", "amountIn = 9,","amountOut:", getAmountOut(9, 10, 100), "tokenA:tokenB = 1:", getAmountOut(9, 10, 100))
