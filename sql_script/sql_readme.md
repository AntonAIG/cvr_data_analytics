### Decription

The sql script unites the dataset for each monthly data.
There are 259,200 rows per month (say April), at 10 seconds granularity.

Column headers: `timestamp`, `P_1`, `P_2`, `P_3`, `Q_1`, `Q_2`, `Q_3`, `U_1_RMS`, `U_2_RMS`, and `U_3_RMS`.

Since we want to focus on evaluating CVR factors for active power *P*, on a single phase (phase1), we have to select `timestamp`, `P_1`, and `U_1_RMS`

The data was unified and ordered by `timestamp`
