# Conservation Voltage Reduction (CVR) evaluation
**[Link to the analysis report](https://github.com/AntonAIG/cvr_data_analytics/blob/main/reports/cvrf_analysis.ipynb)**

## Background
The increase in demand for power due to the increase in urban and rural development, electric vehicles, cooling and heating demand, and overall economic development has stretched the current electricity distribution network to its maximum capacity to the point that new dis-tributed generations (DG) are facing difficulties with gird integration. Network expansion is always met with increasing capital cost, thus giving the network operators the opportunity of seeking for cheaper alternatives. Integrating DG into the grid requires a substantial apparatus for voltage stabilization and ensuring the quality of the voltage supplied. Optimizing power supply by deploying demand response (DR) and Volt/Var Optimization (VVO) can save huge infrastructure costs in additional generation and expansion, while achieving set emission reduction targets by 2050. The cost benefits of such actions are very substantial and feasible enough to investigate.
CVR is a technique (such as VVO) that involves using a reduced voltage setpoint to reduce load demand from residential and industrial con-sumers in a distribution grid. It determines the load demand reduction during peak, and total energy savings achieved for a specific duration. By carrying out this operation regularly or based on a scheme, the utility can channel the excess power towards critical demand areas or new expansion. A CVR factor is the ratio between a percentage change in power or energy corresponding to a percentage change in voltage. A transformer equipped with a load tap changer can regulate voltage by a switching mechanism that alters voltage levels step-by-step. It is called a voltage regulated distribution transformer (VRDT).

## Motivation
Achieving voltage reduction goals comes with significant financial benefits for both the network operator and the consumers. More network operators are willing to test this concept on a pilot project on their selected test fields. The key testing equipment, a voltage-regulated distribution transformer (VRDT) equipped with an OLTC on a single phase, is prevalent in the LV distribution network. Since this asset is a viable regulating device before the end-of-line, it can directly influence the magnitude of change in voltage more than the MV stations. At the EOL, there is a higher potential of experiencing voltage limit violations due to voltage reduction and stability issues. Due to this issue and the need for the network to expand beyond the EOL, there is a growing demand for new transformers to ensure quality voltage supply. The key idea is that we can achieve this expansion by using VRDTs equipped with an OLTC and using this setup to further achieve CVR without incurring additional costs. Therefore, the business case of CVR on VRDTs is a strong one that can be proven by showing the amount of energy savings and demand reduction achieved by deploying it on any distribution network. This is the core focus of this thesis project. ECOTAP® VPD® is one such OLTC that can deliver a reliable tapping operation.
In other to estimate the benefits of CVR, an evaluation of the measurement results obtained from our testing sites will be carried out so that we can be able to answer the following scientific questions:
* How much power and energy can be saved by implementing CVR through VRDTs?
* What amount of power is consumed by the testing center?
* Can CVR alone replace network expansion efforts?

## Testing setup

![substation](https://2hfybu1lrdue3x9wnu1dvw7s-wpengine.netdna-ssl.com/wp-content/uploads/2020/05/Qualitrol-Transmission-Distribution-Substation-Monitoring.jpg)

A site was selected for measurement, and voltage (U), active power (P) and reactive power (Q) on three phases of the feeder was taken.
The baseline measurement is applied towards developing the best statistical model that can estimate energy demand during CVR-off for the test periods. The accuracy of this type of model depends on the correlation between energy and environmental factors during testing. The test was carried out for a one-year period in a site in Germany. This network is made up of more than 98 and 10 residential and commerical customers.
The granularity of the data is 6 seconds.
Nominal voltage setpoint is 230V with bossibility of 2.5% voltage reduction. This will be verified in the dataset.

## Data Analysis
The evaluation report can be found [here](https://github.com/AntonAIG/cvr_data_analytics/blob/main/reports/analysis_report.md)

Tools used: `SQL`, `Python`, `Excel`, and `Tableau`

The data source is reliable and unbiased because they were taken form a functioning substation.
However, there are some uncertainties in the data such as empty data points, noisy data, and measurement uncertainties

## Visualizations
The evalauated CVR factors for power can be shown bellow
![image](https://github.com/AntonAIG/cvr_data_analytics/blob/main/reports/newplot.png)

## Energy savings evaluation
CVR factors for energy savings can be further evaluated using a regression based model. This involves the use of environmental factors to estimate the nominal power consumption during a CVR operation. The estimation process that I deployed can be illustrated in the image below:

![mlr](https://github.com/AntonAIG/cvr_data_analytics/blob/main/reports/mlr.JPG)

The dataset for energy savings was further visuallized (and can be viewed) in [**Tableau**](https://public.tableau.com/views/cvr_f_viz/CVRf_summary?:language=de-DE&:display_count=n&:origin=viz_share_link)

![tableau](https://github.com/AntonAIG/cvr_data_analytics/blob/main/energy_savings/CVRf_summary.png)

This image shows the relationships between voltage reduction and energy savings for a residential low voltage network in Germany.

* The *(2019 vs. 2021 Voltage profile)* voltage was first lowered from the nominal operating level (236V) in 2019 to reduced setopoint (224V) in 2021. This was carried out in April, 2021.
* This voltage reduction resulted to a *Measured energy (kWh)*, which represents the actual consumption in 2021. Using multivariate linear regression, we computed the *Estimated energy (kWh)* which represents the power consumption without CVR in the same testing period.
* The bar plot shows the average CVR factors for each day of the week. The result shows that Monday has the highest factor ar 1.05 and Tuesday has the lowest factor at 0.81.
* The scatter plot shows the *Percentage voltage change* versus *CVR factors*. This plot shows that the average voltage reduction during CVR deployment was 5.2%. Therefore Monday with a CVR factor of 1.05% can produce energy savings of (5.2 x 1.05) 5.46%.

## LSTM Load Demand Forecasting
The load demand forecasting model predicts the load profile of a given test sample. The test sample can contain multiple features such as temperature, day of the week, time of day, holiday, pressure, humidity, wind speed, etc. This evaluation is the final stage of my master's thesis.

> The goal is to show that we can produce more acccurate estimation of power using an LSTM model instead of multivariate linear regression.

LSTMs is a type of RNN capable of learning order dependence in sequence prediction problems. The bi-directional LSTM recurrent neural networks present discrete training data sequences in forwards and backwards steps to two separate recurrent nets, both of which are connected to the same output layer. This means that for every point in a given sequence, the bidirectional LSTM has complete, sequential information about all points before and after it. This characteristic can be implemented for timeseries forecasting, using historical profiles to predict future profiles in a stepwise manner.
