---
title: "Information Entropy"
created: 2026-05-03
updated: 2026-05-03
type: concept
tags: [science, physics, systems-thinking]
sources: []
---

# Information Entropy

## Overview

Information entropy is a measure of uncertainty, surprise, or average information content.
In information theory, it quantifies how unpredictable a source of messages is.
A perfectly predictable source has low entropy.
A source with many equally likely outcomes has high entropy.

The concept was formalized by Claude Shannon in 1948.
It became a foundation for communications engineering, coding, cryptography, statistics, and machine learning.
Entropy does not simply mean disorder in this context.
It is a precise mathematical quantity associated with probability distributions.
If a symbol is rare, observing it carries more information than observing a common symbol.
If all symbols are equally likely, each observation resolves more uncertainty.

The most familiar unit is the bit.
One bit is the information gained by distinguishing between two equally likely alternatives.
Information entropy links probability theory, communication theory, and statistical mechanics.
## Key Definition

For a discrete random variable, Shannon entropy is the expected value of self-information.
Self-information is often written as negative the logarithm of probability.

The logarithm base determines the unit of measurement.
Base two gives bits.
Base e gives nats.
Base ten gives hartleys.
Entropy increases when probability mass is spread more evenly across outcomes.
It decreases when one outcome dominates.

A fair coin has one bit of entropy per toss.
A biased coin has less than one bit of entropy per toss.
A deterministic coin that always lands heads has zero entropy.
Entropy is not the same as the number of possible outcomes.
A million possible outcomes can have low entropy if one outcome is overwhelmingly likely.
A small set of outcomes can have high entropy relative to its size if all are equally likely.

This distinction makes entropy useful for real systems with uneven probabilities.
## Key Aspects

Entropy is an expectation over a probability model.
Changing the model can change the entropy estimate.
Empirical entropy is computed from observed frequencies.
Model-based entropy uses assumptions about how data are generated.

Joint entropy measures uncertainty over pairs or collections of variables.
Conditional entropy measures remaining uncertainty after another variable is known.
Mutual information measures how much knowing one variable reduces uncertainty about another.
Kullback-Leibler divergence compares one probability distribution to another.
Cross-entropy combines a true distribution with a proposed coding or predictive distribution.
These related quantities form a toolkit for reasoning about information flow.

Entropy is concave as a function of probability distributions.
That means mixing distributions tends to increase uncertainty.
Entropy is maximized by a uniform distribution under no additional constraints.
With constraints, maximum entropy distributions have special importance.
The maximum entropy principle chooses the least committal distribution consistent with known facts.
This principle appears in statistical inference, physics, and natural language processing.

Entropy rate extends entropy to stochastic processes.
It measures average uncertainty per symbol in a sequence.
A language has redundancy because letters and words are not independent.
That redundancy allows compression and error correction.
## History and Context

The word entropy entered physics through thermodynamics in the nineteenth century.

Rudolf Clausius used it to describe transformations of heat and work.
Ludwig Boltzmann connected thermodynamic entropy to microscopic configurations.
That statistical interpretation inspired later information-theoretic analogies.
Claude Shannon introduced information entropy in his paper on communication.
He sought a general theory of transmitting messages through noisy channels.
Shannon showed that communication could be studied independently of message meaning.

What mattered for engineering was uncertainty, coding, and channel capacity.
John von Neumann reportedly noted the resemblance to thermodynamic entropy.
Whether or not the famous naming anecdote is exact, the mathematical analogy is deep.
Shannon's work emerged alongside wartime cryptography, telephony, and early computing.
It provided limits on data compression and reliable communication.
Later researchers extended entropy into algorithmic information theory.

Kolmogorov complexity studies the length of the shortest program that produces an object.
Jaynes developed maximum entropy methods for statistical inference.
Cybernetics, linguistics, biology, and economics adopted information-theoretic ideas.
Today entropy is a common bridge between engineering and the sciences of complexity.
## Applications and Significance

Data compression relies on entropy as a lower bound.

A source cannot be compressed losslessly below its entropy rate on average.
Huffman coding and arithmetic coding exploit unequal symbol probabilities.
Modern compressors combine statistical modeling with entropy coding.
Error-correcting codes use information theory to communicate reliably over noisy channels.
Channel capacity defines the maximum reliable communication rate.
This matters for radio, fiber optics, storage devices, satellites, and mobile networks.

Cryptography depends on entropy for secure keys.
A key generated from a predictable source is vulnerable even if the algorithm is strong.
Random number generators are evaluated partly by the entropy they can supply.
Machine learning uses entropy in multiple ways.
Decision trees use information gain to select splits.
Classification models often minimize cross-entropy loss.

Language models are evaluated with perplexity, an exponentiated form of entropy-like uncertainty.
Reinforcement learning may add entropy bonuses to encourage exploration.
Ecology uses Shannon entropy to describe species diversity.
A community with many equally abundant species has higher diversity than one dominated by a single species.
Genomics uses entropy to measure variation at sequence positions.
Neuroscience uses information measures to study neural coding.

Economics and social science use entropy to characterize concentration, inequality, and uncertainty.
Thermodynamics and information theory meet in the physics of computation.
Landauer's principle relates erasing information to heat dissipation.
Maxwell's demon became a thought experiment about measurement, memory, and entropy.
These links do not make information and physical entropy identical in every context.
They show that uncertainty, state counting, and irreversibility are mathematically connected.

Information entropy is significant because it turns ignorance into a measurable quantity.
It gives scientists and engineers a language for limits rather than just mechanisms.
It says how much can be compressed, transmitted, predicted, hidden, or learned.
## Related Concepts

probability theory
communication theory

statistical mechanics
[[laws-of-thermodynamics|thermodynamics]]
data compression
cryptography
machine learning
mutual information

maximum entropy principle
complex systems

## See Also

- [[information-paradigm-of-consciousness]]
- [[psychedelic-consciousness-models]]
