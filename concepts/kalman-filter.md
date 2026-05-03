# Kalman Filter
## Overview
The Kalman filter is a recursive algorithm for estimating the hidden state of a dynamic system.
It combines predictions from a mathematical model with noisy measurements from sensors or observations.
The result is an updated estimate that is often better than either the model or the measurement alone.
It is central to control theory, signal processing, robotics, navigation, and econometrics.
The classic form assumes linear dynamics and Gaussian noise.
Under those assumptions it is the optimal minimum-variance estimator.
The filter tracks both a state estimate and an uncertainty estimate.
Uncertainty is represented by a covariance matrix that changes as evidence accumulates.
The method is recursive, so it does not need to store the full history of measurements.
This makes it useful for real-time systems with limited memory and processing power.
## Core idea
A Kalman filter alternates between prediction and correction.
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
This uncertainty-weighted fusion is the algorithm's essential insight.
## State-space formulation
The system state is usually written as a vector x.
For a vehicle, x might include position, velocity, acceleration, and heading.
For a financial model, x might include latent trend and volatility components.
The state transition matrix maps the previous state into the next predicted state.
A control-input matrix can include known commands, such as thrust or steering.
The process-noise covariance models disturbances not captured by the transition model.
The measurement matrix maps hidden state variables into observable measurements.
The measurement-noise covariance describes sensor error or observation error.
Together these matrices define a probabilistic state-space model.
The filter can be interpreted as Bayesian inference performed sequentially.
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
The standard Kalman filter assumes linear system dynamics.
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
In industrial control, they estimate variables that cannot be measured directly.
In audio and communications, they recover signals corrupted by noise.
## Practical design issues
The hardest part is often choosing a good state representation.
A state vector should include variables needed to predict the future.
Adding too many variables can make estimation slow or poorly conditioned.
Adding too few variables can force the filter to explain dynamics as noise.
Process-noise covariance captures model uncertainty and unmodeled acceleration.
Measurement-noise covariance captures sensor accuracy and calibration quality.
Initial covariance should express genuine uncertainty at startup.
Numerical stability matters because covariance matrices must remain symmetric and positive.
Engineers often monitor residuals to detect model mismatch.
Real deployments may require saturation limits, fault detection, and reset logic.
## Interpretation
The Kalman filter is sometimes described as a machine for disciplined compromise.
It never simply averages a model and a measurement.
Instead it asks how uncertain each source is.
It makes uncertainty operational rather than rhetorical.
This is why it remains important despite its age.
The same pattern appears in broader bayesian inference and probabilistic modeling.
Beliefs are predicted forward, confronted with evidence, and revised quantitatively.
The filter also illustrates why good models and good measurements complement each other.
A weak model can be rescued by frequent accurate measurements.
Sparse or noisy measurements can be rescued by a strong dynamical model.
## Limitations
The standard filter can perform poorly with nonlinear dynamics.
It can underestimate uncertainty when linearization errors accumulate.
It is sensitive to incorrect noise models.
It can be misled by biased sensors because bias is not the same as random noise.
It can diverge if the system is not observable from available measurements.
It may require careful scaling when state variables have very different units.
It does not automatically understand constraints unless they are modeled.
It is not a universal substitute for system identification.
It estimates states within a model; it does not guarantee that the model is true.
Recognizing these limits is part of competent use.
## Related concepts
bayesian inference
control theory
signal processing
state space models
sensor fusion
least squares estimation
particle filter
hidden markov models
- [[byzantine-fault-tolerance]]
- [[synthetic-data-generation]]
- [[turbulence-modeling-fluid-dynamics]]
