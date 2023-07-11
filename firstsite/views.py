from django.http import HttpResponse
from django.shortcuts import render 
from math import exp, pow, sqrt, log, pi
import numpy as np
from scipy.stats import norm 

def HomeView(request):
    return render (request, "home.html")

# function to open N Step Given Volatility form 
# followed by the logic for calculating the option price
def N_STEP_WITH_VOLATILITY(request):
    return render(request, "n_step_vola.html")

def n_step_option_price(request):
    
    S = float((request.GET)['S'])
    K = float((request.GET)['K'])
    r = float((request.GET)['r'])
    r = r/100
    sigma = float((request.GET)['sigma'])
    T = float((request.GET)['T'])
    n = int((request.GET)['n'])
    op_code = ((request.GET)['op_code'])

    dt = T / n
    u = exp(sigma * pow(dt, 0.5))
    d = 1 / u
    p = (exp(r * dt) - d) / (u - d)
    q = 1 - p

    tree = []
    for i in range(n+1):
        tree.append([])
        for j in range(i+1):
            tree[i].append(0)
    tree[0][0] = S
    for i in range(1, n+1):
        for j in range(i+1):
            tree[i][j] = S * pow(u, j) * pow(d, i-j)

    option = []
    for i in range(n+1):
        option.append([])
        for j in range(i+1):
            option[i].append(0)
    for j in range(n+1):
        option[n][j] = max(tree[n][j] - K, 0)
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            option[i][j] = exp(-r * dt) * (q * option[i+1][j] + p * option[i+1][j+1])
    
    price = option[0][0]
    if(op_code == "PUT"):
        price =  price + K*exp(-r*T)-S
    return render(request, "n_step_vola.html", {'option_price': price})

# function to open N Step form 
# followed by the logic for calculating the option price
def N_STEP(request):
    return render(request, "n_step.html")

def n_step_option_price_without(request):
    
    S = float((request.GET)['S'])
    K = float((request.GET)['K'])
    r = float((request.GET)['r'])
    r = r/100
    u = float((request.GET)['u'])
    d = float((request.GET)['d'])
    T = float((request.GET)['T'])
    n = int((request.GET)['n'])
    op_code = ((request.GET)['op_code'])

    dt = T / n
    p = (exp(r * dt) - d) / (u - d)
    q = 1 - p

    tree = []
    for i in range(n+1):
        tree.append([])
        for j in range(i+1):
            tree[i].append(0)
    tree[0][0] = S

    for i in range(1, n+1):
        for j in range(i+1):
            tree[i][j] = S * pow(u, j) * pow(d, i-j)

    option = []
    for i in range(n+1):
        option.append([])
        for j in range(i+1):
            option[i].append(0)
    for j in range(n+1):
        option[n][j] = max(tree[n][j] - K, 0)
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            option[i][j] = exp(-r * dt) * (q * option[i+1][j] + p * option[i+1][j+1])
        
    price = option[0][0]

    if(op_code == "PUT"):
        price =  price + K*exp(-r*T)-S
    return render(request, "n_step.html", {'option_price': price})


# function to open 2 Step form 
# followed by the logic for calculating the option price
def TWO_STEP(request):
    return render(request, "two_step.html")

def two_step_option_price_without(request):
    
    S = float((request.GET)['S'])
    K = float((request.GET)['K'])
    r = float((request.GET)['r'])
    r = r/100
    u = float((request.GET)['u'])
    d = float((request.GET)['d'])
    T = float((request.GET)['T'])
    n = 2
    op_code = ((request.GET)['op_code'])
    
    dt = T/n
    p = (exp(r * dt) - d) / (u - d)
    q = 1 - p
    
    S_up_up = S*u*u
    S_up_down = S*u*d
    S_down_up = S*d*u
    S_down_down = S*d*d
    payoff_up_up = max(S_up_up - K, 0)
    payoff_up_down = max(S_up_down - K, 0)
    payoff_down_up = max(S_down_up - K, 0)
    payoff_down_down = max(S_down_down - K, 0)
    price = (p*(((p*payoff_up_up)+ (q*payoff_up_down))*exp(-r*dt)) + q*(((p*payoff_down_up)+ (q*payoff_down_down))*exp(-r*dt)))*exp(-r*dt)
    
    if(op_code == "PUT"):
        price =  price + K*exp(-r*T)-S

    return render(request, "n_step.html", {'option_price': price})


# function to open 2 Step given volatility form 
# followed by the logic for calculating the option price
def two_step_with_volatility(request):
    return render(request, "two_step_vola.html")

def two_step_option_price(request):
    
    S = float((request.GET)['S'])
    K = float((request.GET)['K'])
    r = float((request.GET)['r'])
    r = r/100
    sigma = float((request.GET)['sigma'])
    T = float((request.GET)['T'])
    n = 2
    op_code = ((request.GET)['op_code'])
    
    dt = T / n
    u = exp(sigma * pow(dt, 0.5))
    d = 1 / u
    p = (exp(r * dt) - d) / (u - d)
    q = 1 - p

    S_up_up = S*u*u
    S_up_down = S*u*d
    S_down_up = S*d*u
    S_down_down = S*d*d
    payoff_up_up = max(S_up_up - K, 0)
    payoff_up_down = max(S_up_down - K, 0)
    payoff_down_up = max(S_down_up - K, 0)
    payoff_down_down = max(S_down_down - K, 0)
    price = (p*(((p*payoff_up_up)+ (q*payoff_up_down))*exp(-r*dt)) + q*(((p*payoff_down_up)+ (q*payoff_down_down))*exp(-r*dt)))*exp(-r*dt)
    
    if(op_code == "PUT"):
        price =  price + K*exp(-r*T)-S

    return render(request, "two_step_vola.html", {'option_price': price})


# function to open BS form 
# followed by the logic for calculating the option price
def bs_value(request):
    return render(request, "bs.html")

def bs_option(request):
    S = float((request.GET)['S'])
    K = float((request.GET)['K'])
    r = float((request.GET)['r'])
    r = r/100
    sigma = float((request.GET)['sigma'])
    T = float((request.GET)['T'])
    op_code = ((request.GET)['op_code'])
    d1 = (log(S/K)+(r+ sigma*sigma/2)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    price =  S*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)
    if(op_code == "PUT"):
        price =  price + K*exp(-r*T)-S

    return render(request, "bs.html", {'option_price': price})
        
