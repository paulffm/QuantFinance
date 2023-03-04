# QuantFinance
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
<!-- [![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
 -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/paulffm/QuantFinance">
    <img src="https://github.com/paulffm/QuantFinance/blob/main/.idea/images/QuantFinancepic.jpg" alt="Logo" width="600" height="400">
  </a>

  <h3 align="center">Quant Finance</h3>

  <p align="center">
    Project to deepen your understanding of quantitative finance
    <br />
    <a href="https://github.com/paulffm/QuantFinance/tree/main"><strong>Explore the docs »</strong></a>
    <br />
    <br />
   
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="https://github.com/paulffm/QuantFinance/blob/main/.idea/images/pythoncodepic.png" width="200" height="200" />

This project is to get a better understanding in the world of quantitative finance and to prepare myself for my internship.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![LaTeX][Latex-shield]][Latex-url] 



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
# Financial Basics
# Stocks
Ownershop of a small piece of a company. Price is determined by the value of the company and by the expectations = bid and ask behavior. \\
Volatility = stock price difference to expected value
value in holding the stock comes from dividends and any growth in the stocks value
Dividends: Cum = Buying af
# Interest rate
interest = money paid for a credit or liability = percentage of principal, amount owed to the lender \\
interest rate = percentage that is paid over a certain time period. Banks may change the interest rate to either slow down or speed up economy growth \\
Discret compounding: $M_0 * (1 + r)^n$
Continous compounding: $M_0 * (1 + \frac{r}{m})^n$ \\
PDE: $\frac{d M}{d t} = r M(t) => M(t) = M_0 \exp ^{rt}$
# Definitions:
* Volatility = Measure for variation of financial prices over time
* Security = instrument representing ownership
* Return = gain or loss of a security in a particular period
* Commodities = raw products
Options depending on strike, maturity, delta=how much option depends on underlying, implied volatility=sigma, uncertainty

# Hedging
A reduction of risk for example by combining a number of Shares S and Puts $V_p$ in a portfolio
## Value of an Option example
$\Pi (t) = V_{C, 0} - \Delta \cdot S_0$





# Options
Tiny piece of financial world, but important for modelling aspects.
An option is a contract which gives the buyer the right but not the obligation to buy or sell an underlying asset or instrument at a specified strike price prior to or on a specified date.
* In short:
  * Agreement to buy/sell at given price, to specified time
  * a premium is paid for the flexibility
### Why using Options:
* Hedge risk
* speculation
### Options Contract Terms:
* Premium: Must be paid to buy Options Contract
* Expiration Date: Date on which the owner of the option must decide to buy (call) or sell (put)
* Strike Price: is the price at which the underlying will be delivered if exercised by the owner
* Underlying: The underlying asset
* Contract Type: Call or Put: Put Option: Sell the Call: Buy underlying at a given Strike price
### Call vs Put:
The right to buy (Call)/ sell (Put) the underlying at a specified price at a specified time in the future
* Example: underlying price at t (now) $p_t = 40 $$
* Right to buy/sell the underlying at $p_t+365 = 40$  in 1 year
##### Call: (Stock Price S, Strike Price K)
* Call buy: The right to buy the underlying at a specified price K at a specified time in the future: Hoping Strike Price K is below the real future stock price S
* Call sell: Seller must pay the difference between S - K: Hoping S falls over time \\
Value of european call option at expiry T, Stock price S, Strike price K:
$ V_C(T, S_T) = max(S_T - K, 0)$
##### Put:
* Put buy: The right to sell the underlying at a specified price K at a specified time in the future: Hoping Strike Price K is above the real future stock price S
*  Put Sell: Seller must pay the difference between K - S: Hoping S rises over time
Value of european put option at expiry T, Stock price S, Strike price K:
$ V_P(T, S_T) = max(K - S_T, 0)$
### Underlying:
An underlying is a security/commodity to be bought or sold under the terms of the contract
* Shares, Futures, Anything
### Contract Multiplier:
Purchasing options have a specific quantity of underlying per contract
* Usually: Shares: 100 Shares / options contract
* Why? Example:
  * Underlying share: 10$/Share; 1% Move -> 0.1$ Change
  * Underlying is Option: 7000 Points currently and 25$/point; 1% Move -> 7000 Points * 1% * 25$/Points = 1750$
### Option Premium: Call/Put Price 
Key idea: Price at which a willing buyer and seller transact an options contract: 
* Premium = Intrinsic Value + Time Value
  * Intrinsic Value = Value that the contact has right now = Current Price - Strike Price = S - K Put: K - S
  * Time Value = Future Value that the contract could potentially have = Price Uncertainty = more uncertain -> higher
### Difference European and American Option:
#### Option Settlement:
* Call (Put): Exercised Buyer: choose to buy (sell) @ Strike Price; Assigned Seller: assigned to sell (buy) @ Strike Price
* European Contract: Can only be exercised at Expiration 
* American Contract: Can be exercised anytime between now and expiration date
* Bermudan Contract: Can be only exercised on specified dates
## Black Scholes PDE:
### Assumptions:
* Short Term interest rates are constant: risk free zinssatz gleich für Kapialaufnahme und Kapitalanlaghe
* stocks pay no dividens
* No transactions costs
* can borrow fractions
* Short selling allowed
### Method Overview
1. Price Derivative using Replication
2. Construct Risk Free Portfolio
3. C_t = C(s, t) with Itos Rule 
##### Construct Portfoio:
* 1 Option, $-alpha_t$ shares: $V_t = C_t - \alpha_t S_t$
* Assume underlying follow Geometric Brownian Motion: $dS_t = \mu S_t + G S_t dW_t$ (Drift + Diffusion) 
* $\delta C_t = \frac{\partial C_t}{\partial t} dt + \frac{\partial C_t}{\partial S} dS + \frac{T}{2} + (\frac{\partial^2 C}{\partial S^2} dS^2 + (\frac{\partial^2 C}{\partial t^2}) dt^2$
* $dV_t = frac{\partial C_t}{\partial t} dt + \frac{\partial C_t}{\partial S} dS + \frac{1}{2} + \frac{\partial^2 C}{\partial S^2} - \alpha dS_t$ 
* Option only can be exercised at expiration

# Porfolio Theory
Consists of two key components
* Risk: Variance
* Reward: Expectation of reward
This leads to an optimization problem: How do I weight different assets in my portfolio to maximize my reward while minimizing my risk
## Risk
* Unsystematic: risk that is inherent in a specific compay or industry
* Systematic: risk that is inherent to the entire market or market segment
### Important Parameters:
* correlation, p-values

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/paulffm/QuantFinance?color=green
[contributors-url]: https://github.com/paulffm

[product-screenshot]: (https://example.com)
[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://nextjs.org/](https://www.python.org
[Latex-shield]: https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white
[Latex-url]: https://www.overleaf.com

