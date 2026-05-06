---
title: Bayesian Inference
created: 2026-04-28
updated: 2026-05-06
sources: []
type: concept
tags: [reference]
---

# Bayesian Inference

## Overview
Bayesian inference is a framework for updating beliefs in light of evidence.
It represents uncertainty with probabilities.
A prior distribution describes what is believed before observing new data.
A likelihood describes how probable the observed data are under different hypotheses or parameter values.
Bayes' theorem combines the prior and likelihood to produce a posterior distribution.
The posterior becomes the updated state of knowledge.
Bayesian inference is not only a formula.
It is a way of reasoning about uncertainty, evidence, models, and decisions.
Its central strength is that it keeps uncertainty visible instead of reducing it too early to a point estimate.

## Bayes' theorem
Bayes' theorem relates conditional probabilities.
In one common form, posterior probability is proportional to likelihood times prior probability.
The missing proportionality constant is the evidence or marginal likelihood.
The evidence ensures that the posterior probabilities sum or integrate to one.
For hypotheses, the theorem compares how well each hypothesis predicted the data.
For continuous parameters, it updates a probability density over possible values.
Its importance comes from the interpretation of each term.
The prior encodes assumptions before the data.
The likelihood encodes the statistical model of measurement or observation.
The posterior encodes what the model says after the data are taken into account.

## Priors
A prior distribution can be informative, weakly informative, or intended to be diffuse.
An informative prior uses substantial previous knowledge.
A weakly informative prior rules out implausible values without dominating ordinary data.
A diffuse prior attempts to express little prior preference.
No prior is completely assumption-free.
Good Bayesian practice makes prior assumptions explicit.
In scientific settings, priors may come from previous experiments, physical constraints, or expert knowledge.
In regularized statistical modeling, priors can stabilize estimates and reduce overfitting.

## Likelihoods
The likelihood links parameters or hypotheses to possible observations.
A Gaussian likelihood may model measurement error around a continuous value.
A binomial likelihood may model successes in a fixed number of trials.
A Poisson likelihood may model counts over time or space.
The likelihood is not the probability distribution of the parameters.
It is a function of the parameters given the observed data.
Mis-specified likelihoods can produce misleading posteriors even with reasonable priors.
Model checking is therefore as important in Bayesian statistics as in any other statistical approach.
Robust likelihoods can reduce sensitivity to outliers.
Hierarchical likelihoods can represent grouped data and partial pooling.

## Posteriors
The posterior distribution is the main output of Bayesian inference.
It can be summarized by means, medians, modes, intervals, probabilities, or predictions.
A credible interval gives a range containing a specified posterior probability.
This differs from a frequentist confidence interval, which has a long-run coverage interpretation.
Posterior probabilities can answer direct questions such as the probability that a treatment effect is positive.
They can also describe uncertainty about latent variables, missing data, or future observations.
The posterior is conditional on the model, prior, and data.
If any of these are poor, the posterior may be precise but wrong.
Bayesian workflow therefore includes sensitivity analysis and model criticism.
A posterior can also serve as the prior for later data.
This sequential updating is natural in monitoring, learning systems, and adaptive experiments.

## Computation
Simple Bayesian models sometimes have closed-form solutions.
Conjugate priors are priors that produce posteriors in the same mathematical family.
A beta prior with a binomial likelihood is a classic example.
Many realistic models require numerical methods.
Markov chain Monte Carlo samples from complex posterior distributions.
Gibbs sampling updates blocks of variables from conditional distributions.
Variational inference approximates the posterior with a simpler distribution.
Sequential Monte Carlo represents changing uncertainty with particles.
Modern Bayesian practice depends heavily on computation.
Software systems have made sophisticated models accessible to non-specialists.

## History and context
The theorem is named after Thomas Bayes, an eighteenth-century minister and mathematician.
Pierre-Simon Laplace independently developed and expanded inverse probability methods.
Bayesian reasoning was influential in early probability theory.
During the twentieth century, frequentist methods became dominant in many scientific fields.
Critics objected that priors could be subjective.
Bayesians responded that all statistical modeling contains assumptions and that explicit assumptions are preferable.
The late twentieth century brought renewed Bayesian growth through better computation.
MCMC methods made previously impossible models practical.
Today Bayesian and frequentist methods coexist, compete, and often complement each other.
The historical debate continues, but practical modeling often matters more than philosophical labels.

## Applications in science
Bayesian inference is used to estimate physical constants from experimental measurements.
It is used in astronomy to infer cosmological parameters from telescope data.
It helps combine evidence from multiple clinical trials in medical research.
Ecologists use hierarchical Bayesian models for population estimates and species distributions.
Neuroscientists use Bayesian models to describe perception and [[savory-holistic-decision-making]].
Geneticists use Bayesian methods for association studies and phylogenetics.
Climate scientists use Bayesian calibration to compare models with observations.
Epidemiologists use it to estimate transmission rates and forecast outbreaks.
The framework is especially useful when data are sparse, indirect, noisy, or structured.
It allows scientific knowledge to accumulate coherently across studies.

## Applications in technology
Spam filters historically used naive Bayes classifiers.
Robotics uses Bayesian filtering to estimate location and map uncertain environments.
Kalman filters can be interpreted within a Bayesian state-estimation framework.
Machine learning systems use Bayesian optimization to tune expensive experiments or models.
Reliability engineering uses Bayesian updating as failures or tests are observed.
Computer vision uses probabilistic models for tracking and scene interpretation.
Natural language processing uses Bayesian methods in topic models and latent-variable models.
A/B testing platforms can use Bayesian decision rules for experiment monitoring.

## Decision-making
Bayesian inference separates uncertainty estimation from decision-making.
A posterior distribution says what is believed after evidence.
A utility or loss function says what outcomes matter.
Bayesian decision theory chooses actions by expected utility or expected loss.
This is valuable when errors have unequal costs.
A medical test may prioritize avoiding false negatives.
An industrial inspection system may prioritize avoiding catastrophic failures.
Bayesian decisions can incorporate the value of additional information.
This helps determine whether collecting more data is worth the cost.
The decision-theoretic view makes assumptions about values explicit.

## Criticisms and cautions
Bayesian inference can appear more objective than it is if priors are hidden.
Different priors can produce different conclusions when data are weak.
Complex models can be computationally expensive.
MCMC diagnostics are necessary because poor sampling can mimic certainty.
Model misspecification can dominate posterior uncertainty.
A narrow posterior under a bad model is not reliable knowledge.
Communicating priors and credible intervals requires care.
Good practice includes prior sensitivity, posterior predictive checks, and transparent reporting.

## Significance
Bayesian inference gives a disciplined language for learning from evidence.
It connects logic, probability, computation, and decision theory.
It is powerful because it treats uncertainty as something to be modeled rather than ignored.
It supports cumulative science by allowing previous knowledge and new data to interact.
It supports engineering by providing real-time updating under uncertainty.

## Related concepts
- probability theory
- statistical inference
- markov chain monte carlo
- hierarchical models
- [[kalman-filter]]
## Related

- [[mescaline-reference]]
- [[ibogaine-reference]]
