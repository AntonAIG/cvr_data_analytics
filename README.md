# Conservation Voltage Reduction (CVR) evaluation
**[Link to the analysis report](https://github.com/AntonAIG/cvr_data_analytics/blob/main/reports/analysis_report.md)**

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
