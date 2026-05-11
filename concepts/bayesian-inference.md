---
title: bayesian inference
created: 2026-04-28
updated: 2026-05-06
sources:
  - "raw/papers/bill-mollison-permaculture-a-designers-manual-guild-design-in-permaculture|permaculture|permaculture-a-designers-manual-bill-mollison-permaculture-a-designers-manual-animal-systems-in-permaculture|bill-mollison.md"
type: concept
tags: [reference]
---

# Bayesian Inference

## Overview
bayesian inference is a framework for updating beliefs in light of evidence. (see [[biosorption-isotherms]]).
It represents uncertainty with probabilities. (see [[fungal-species-estimation-methods-total-diversity]]).
A prior distribution describes what is believed before observing new data.
A likelihood describes how probable the observed data are under different hypotheses or parameter values.
Bayes' theorem combines the prior and likelihood to produce a posterior distribution.
The posterior becomes the updated state of knowledge.
bayesian inference is not only a formula.
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
A weakly informative prior rules out implausible values without [[dom]] inating ordinary data.
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
The posterior distribution is the main output of bayesian inference.
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
During the [[coleman-louis-savier-twentieth-century-maraicher]], frequentist methods became dominant in many scientific fields.
Critics objected that priors could be subjective.
Bayesians responded that all statistical modeling contains assumptions and that explicit assumptions are preferable.
The late twentieth century brought renewed Bayesian growth through better computation.
