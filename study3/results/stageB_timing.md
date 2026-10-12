# Stage B — timing projections

Measured Stage A cell time includes generation, unsteered answer perplexity, answer/trace classifier scores and three complete-sequence ratings. It excludes model loading and between-cell cleanup. Main-study LHP, entropy and trajectory recording were not run for these checks and are not included; these projections are estimates, not guaranteed full-run durations.

| Mode | a | n | Mean seconds | Sample SD seconds |
|---|---:|---:|---:|---:|
| direct | 0 | 20 | 8.431 | 2.607 |
| direct | 1 | 20 | 23.044 | 1.794 |
| think | 0 | 20 | 31.846 | 9.467 |
| think | 1 | 20 | 140.138 | 9.005 |

| Design | Cells | Projected hours | Eight-hour equivalents | Whole eight-hour nights |
|---|---:|---:|---:|---:|
| Draft v0.2 base | 1120 | 22.653 | 2.832 | 3 |
| Add neutral condition | 2240 | 45.305 | 5.663 | 6 |
| E1 pulse increment only | 240 | 9.343 | 1.168 | 2 |
| Base plus E1 pulse | 1360 | 31.995 | 3.999 | 4 |

Base formula: 80 × [direct-zero + think-zero + 6 × direct-full + 6 × think-full], divided by 3,600. The six nonzero cells per mode comprise three directions at two doses. Zero dose is shared across directions.

Only hostility at zero and full dose was timed. Full-dose time is the explicit proxy for both nonzero doses and all directions; neutral is estimated by doubling the base. E1 adds 240 cells using the full-dose thinking time as a proxy. No pulse cells were generated. Different lengths, stopping behavior, memory pressure and omitted main-study scoring may change runtime.
