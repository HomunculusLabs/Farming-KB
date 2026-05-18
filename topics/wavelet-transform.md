---
title: Wavelet Transform
subtitle: A multiscale method for analyzing signals with localized waves
tags: [signal-processing, mathematics, data-analysis, compression, time-frequency-analysis]
date: 2026-05-02
updated: 2026-05-02
sources:
  - /Users/t3rpz/wiki/concepts/wavelet-transform.md
related_concepts:
  - wavelet-transform
  - kalman-filter
  - fourier-transform
  - signal-processing
  - multiresolution-analysis
---
# Wavelet Transform
The wavelet transform is a family of mathematical techniques for representing data at multiple scales.
It analyzes a signal by comparing it with short oscillatory functions known as wavelets.
Each wavelet is shifted across the signal and stretched or compressed to examine different levels of detail.
The resulting coefficients describe where particular patterns occur and at what scale they occur.
This makes the wavelet transform especially useful for data whose behavior changes over time, space, or resolution.
[[decomposition]].
This nested structure is often called a wavelet pyramid.
An inverse transform recombines the coefficients to reconstruct the original data.
## Multiresolution Analysis
Multiresolution analysis is the mathematical framework that explains how wavelet spaces fit together.
It treats a signal as something that can be viewed at successive levels of resolution.
At a coarse level, only broad averages and slow variations are visible.
At finer levels, additional details are added back in.
The approximation at one scale plus the details at that scale yields the approximation at the next finer scale.
This structure mirrors common human perception of images and sounds.
People often notice overall shape before texture, and long rhythms before short attacks.
Wavelets formalize that intuition in a computationally efficient way.
The framework also explains why wavelets are valuable for adaptive approximation.
Smooth regions can be represented with few coefficients.
Irregular regions can receive more coefficients without forcing high resolution everywhere.
This selective allocation of detail is a major reason wavelets are useful for compression and simulation.
## Major Wavelet Families
The Haar wavelet is the simplest wavelet and uses a step-like positive and negative shape.
It is easy to compute and excellent for illustrating the basic idea.
Its discontinuity can be a disadvantage for representing smooth data.
Daubechies wavelets are compactly supported orthogonal wavelets with varying numbers of vanishing moments.
They became important because they combine exact reconstruction, locality, and mathematical regularity.
Coiflets are related wavelets designed with additional moment conditions.
Symlets modify Daubechies wavelets to improve symmetry while preserving many useful properties.
Biorthogonal wavelets use different wavelets for decomposition and reconstruction.
They are common in image compression because they can provide nearly symmetric filters.
Morlet wavelets resemble complex sinusoids inside a Gaussian envelope.
They are often used for time-frequency analysis of oscillatory signals.
The Mexican hat wavelet is related to the second derivative of a Gaussian.
It is useful for detecting peaks, blobs, and scale-dependent features.
The choice of wavelet affects localization, smoothness, symmetry, computational cost, and interpretability.
## Mathematical Properties
Compact support means a wavelet is nonzero only on a finite interval.
This property makes computations local and can reduce boundary effects.
Orthogonality means that wavelet basis functions do not contain redundant information.
An orthogonal basis supports energy preservation and straightforward coefficient interpretation.
Biorthogonality relaxes strict orthogonality in exchange for design flexibility.
Vanishing moments describe a wavelet's ability to ignore low-degree polynomial trends.
A wavelet with more vanishing moments represents smooth functions with greater sparsity.
Regularity describes the smoothness of the wavelet and its scaling function.
Symmetry is desirable for images because asymmetric filters can shift or distort edges.
No single wavelet optimizes all properties at once.
Practical wavelet design is therefore a balance among locality, smoothness, phase behavior, and numerical stability.
Boundary handling is another important implementation issue.
Finite signals require assumptions beyond their endpoints, such as zero padding, periodic extension, or symmetric reflection.
Poor boundary choices can create artificial coefficients near the edges of a signal.
## Historical Development
The earliest recognizable wavelet basis was introduced by Alfred Haar in 1909.
For much of the [[coleman-louis-savier-twentieth-century-maraicher]].
Alex Grossmann helped provide a mathematical formulation of the continuous wavelet transform.
Yves Meyer developed major theoretical foundations for wavelet bases.
Ingrid Daubechies constructed compactly supported orthonormal wavelets that made many applications practical.
Stephane Mallat connected wavelets with filter banks and multiresolution analysis.
This connection produced efficient algorithms that could be used by engineers and programmers.
By the 1990s, wavelets had become a major field spanning pure mathematics and applied technology.
Their rise coincided with increasing interest in sparse representations and computationally efficient data compression.
## Applications
Image compression is one of the best-known applications of wavelets.
Images usually contain smooth areas separated by edges, and wavelets represent this structure efficiently.
The JPEG 2000 standard uses wavelet-based methods rather than the block cosine methods associated with older JPEG compression.
Wavelet denoising removes noise by shrinking or discarding small coefficients while preserving large structural coefficients.
This approach is used in audio restoration, spectroscopy, microscopy, astronomy, and medical measurements.
Biomedical signal analysis uses wavelets to examine electrocardiograms, electroencephalograms, gait signals, and other nonstationary data.
Seismology uses wavelets to identify events that occur at particular times and scales.
Remote sensing uses wavelet transforms for image fusion, feature extraction, and multiresolution mapping.
Computer vision uses wavelet-like filters to detect edges, textures, orientations, and local patterns.
Numerical analysis uses wavelet bases for adaptive solution of differential equations.
Statistics uses wavelet shrinkage to estimate functions from noisy samples.
Finance has used wavelets to separate short-term volatility from longer-term trend structure.
Computer graphics uses wavelets for level-of-detail models, texture representation, and progressive transmission.
Scientific computing uses wavelets to compress simulation outputs while retaining important localized features.
## Wavelets and Other Methods
The wavelet transform is often compared with the Fourier transform.
[[pulsatile-transport-fourier-analysis-fungi]] provides precise frequency information but weak localization for sudden changes.
Short-time Fourier analysis adds localization by using a fixed window.
Wavelet analysis uses windows that change with scale, giving long windows for low frequencies and short windows for high frequencies.
This variable resolution is one of its defining advantages.
Wavelets can also complement state-estimation methods such as the [[kalman-filter]] estimates hidden states through time using a dynamical model and noisy observations.
A wavelet transform reorganizes observed data into scale-localized coefficients.
The two methods answer different questions, but both are used for noisy, time-varying signals.
Hybrid systems may use wavelets for denoising or feature extraction before statistical filtering.
## Limitations
Wavelet analysis is not automatically superior to Fourier analysis or model-based estimation.
It requires choosing a wavelet family, decomposition level, thresholding rule, and boundary convention.
Bad choices can obscure features or create artifacts.
Some signals are naturally sinusoidal and are better described by Fourier methods.
Some systems are governed by explicit dynamics and are better handled by state-space filters.
Continuous wavelet transforms can be redundant and computationally heavier than discrete transforms.
Discrete transforms can be less visually intuitive and depend strongly on sampling structure.
Interpretation also requires care because scale is related to but not identical with frequency.
Despite these limitations, wavelets remain valuable because they combine locality, scale, sparsity, and reconstruction.

## See Also
- [[query-what-is-a-wavelet-transform-used-for]]
