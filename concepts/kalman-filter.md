---
title: Kalman Filter
created: 2026-04-28
updated: 2026-05-06
sources: []
tags: []
type: concept
---
# [[pf-tek-substrate-moisture-diagnosis-and-correction]] diagnosis and correctionman filter alternates between prediction and correction.
Prediction projects the current state forward using a dynamical model.
Correction adjusts that projection using the newest measurement.
The prediction step says what should happen if the model is trusted.
The correction step says how much the new observation should change that belief.
The balance is controlled by the Kalman gain.
A high Kalman gain gives more weight to the measurement.
A low Kalman gain gives more weight to the model forecast.
The gain is computed from uncertainty, not chosen by intuition alone.
If measurements are noisy, the filter trusts them less.
If the model forecast is uncertain, the filter trusts measurements more.
This uncertainty weighted fusion is the algorithm's essential insight.
## State space formulation
The system state is usually written as a vector x.
For a vehicle, x might include position, velocity, acceleration, and heading.
For a financ [[bayesian-inference]] performed sequentially.
Each prediction is a prior distribution over the next state.
Each correction is a posterior distribution after observing new data.
## Prediction step
The predicted state is obtained by applying the state transition model.
Known control inputs are added when they are part of the system.
The predicted covariance is also propagated forward.
Process noise is added because models are never perfect.
This step usually increases uncertainty.
For example, a drone's location uncertainty grows while it flies without receiving GPS updates.
The prediction can still be valuable because it preserves continuity between measurements.
In high-rate control loops, prediction may occur more often than correction.
The model can also fill gaps when sensors temporarily fail.
Prediction is therefore both a forecasting operation and a bridge across missing data.
## Correction step
The filter receives a measurement and compares it with the predicted measurement.
The difference is called the innovation or residual.
The innovation measures surprise relative to the model's expectation.
The innovation covariance estimates how surprising the residual should be.
The Kalman gain converts the innovation into a state update.
The state covariance is reduced when measurements add useful information.
If the measurement is inconsistent with expected uncertainty, it may signal an outlier.
Many implementations use innovation tests to reject sensor faults.
The correction step is mathematically compact but conceptually powerful.
It updates the estimate only by the amount justified by uncertainty.
## Key assumptions
The standard kalman filter er er er assumes linear system dynamics.
It assumes measurement equations are linear as well.
It assumes process noise and measurement noise are Gaussian.
It assumes noise statistics are known or reasonably estimated.
It assumes the initial state and covariance are defined.
If these assumptions hold, the filter has strong optimality guarantees.
If they fail mildly, the filter may still work well in practice.
If they fail badly, estimates can diverge or become overconfident.
Good engineering practice focuses heavily on modeling the noise covariances.
Poor covariance tuning is a common cause of unreliable filters.
## Variants
The extended Kalman filter handles nonlinear systems by local linearization.
It uses Jacobian matrices to approximate dynamics near the current estimate.
The unscented Kalman filter uses sigma points to propagate uncertainty through nonlinear functions.
The ensemble Kalman filter represents uncertainty with many simulated samples.
The information filter reformulates the same logic using inverse covariance matrices.
The square-root Kalman filter improves numerical stability by factoring covariance matrices.
The Rauch-Tung-Striebel smoother applies Kalman logic backward after data have been collected.
Particle filters generalize the idea to non-Gaussian and highly nonlinear systems.
Each variant trades computational cost, accuracy, and robustness differently.
The right version depends on model structure, noise behavior, and real-time constraints.
## History and context
The filter is named after Rudolf E. Kalman.
Kalman's 1960 paper provided a state-space solution to linear filtering and prediction problems.
Related ideas were also developed by Richard S. Bucy and others.
The approach became influential during the early space age.
Apollo navigation is a famous early application of Kalman filtering.
The method fit naturally with digital computers and modern control theory.
It also helped shift engineering from frequency-domain methods toward state-space methods.
Today the filter is taught across aerospace engineering, electrical engineering, and statistics.
Its conceptual ancestors include least squares estimation and Wiener filtering.
Its descendants include many modern probabilistic inference algorithms.
## Applications
In aerospace navigation, Kalman filters fuse inertial sensors, star trackers, radar, and GPS.
In robotics, they support localization, mapping, and sensor fusion.
In autonomous vehicles, they help track objects and estimate vehicle motion.
In smartphones, they combine accelerometer, gyroscope, magnetometer, and GPS data.
In economics, state-space models use Kalman filtering to estimate hidden trends.
In weather and ocean modeling, ensemble variants support data assimilation.
In biomedical engineering, filters can estimate physiological states from noisy signals.
In computer vision, they track moving objects across video frames.

## See Also
- [[kalman-filter-vs-wavelet-transform]]
- [[jarrold-filter-can-vermiculite-air-exchange-mushroom-cultivation]]
- [[hepa-filter-selection-and-testing]]
- [[filter-can-spawn-breathing-jarrold]]
- [[boil-a-bag-filter-can-construction]]

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[dom]]
- [[kalman-filter-vs-wavelet-transform]]
- [[boil-a-bag-filter-can-construction]]
- [[cervantes-ventilation-fan-carbon-filter-setup]]
- [[laminar-flow-hood-blower-and-filter-sizing]]
