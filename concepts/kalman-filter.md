---
title: Kalman Filter
created: 2026-04-28
updated: 2026-05-06
sources:
  - "raw/papers/jarrold-mushroom-cultivation-techniques.md"
tags: []
type: concept
---
# [[bayesian-inference]] performed sequentially.
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
- [[jarrold-filter-can-vermiculite-air-exchange-mushroom-cultivation]]
- [[filter-can-spawn-breathing-jarrold]]
- [[dom]]
- [[boil-a-bag-filter-can-construction]]
- [[laminar-flow-hood-blower-and-filter-sizing]]
