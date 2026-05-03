# Wavelet Transform

## Overview
The wavelet transform is a method for representing signals at multiple scales.
It decomposes data into localized wave-like functions called wavelets.
Unlike the Fourier transform, it preserves information about both frequency and position.
This makes it useful for signals whose characteristics change over time or space.
A wavelet is usually short, oscillatory, and concentrated within a finite region.
Scaled and shifted copies of a mother wavelet are used as analysis functions.
Large-scale wavelets capture slow variations and broad structures.
Small-scale wavelets capture rapid changes, edges, and fine details.
The transform can be continuous or discrete.
Continuous wavelet transforms provide dense scale-position representations.
Discrete wavelet transforms use selected scales and positions for efficient computation.
Wavelets are central to signal processing, image compression, numerical analysis, and data denoising.
They are related to [[fourier-transform]], [[signal-processing]], and [[multiresolution-analysis]].

## Key Aspects
A wavelet transform measures similarity between a signal and shifted, scaled wavelets.
The scale parameter controls the width of the wavelet.
The translation parameter controls where the wavelet is placed.
Small scales correspond to high-frequency detail.
Large scales correspond to low-frequency structure.
The mother wavelet determines the transform's shape and analytic behavior.
Common wavelets include Haar, Daubechies, Morlet, Mexican hat, and Coiflet wavelets.
The Haar wavelet is the simplest and uses step-like functions.
Daubechies wavelets are compactly supported and orthogonal.
Morlet wavelets are useful for time-frequency analysis of oscillatory signals.
The Mexican hat wavelet is related to the second derivative of a Gaussian.
Compact support means the wavelet is nonzero only over a limited interval.
Orthogonality allows coefficients to represent independent components.
Vanishing moments describe how well a wavelet ignores smooth polynomial trends.
More vanishing moments improve compression of smooth signals.
Regularity describes the smoothness of the wavelet itself.
There is often a tradeoff between compact support, smoothness, and symmetry.
The discrete wavelet transform is commonly implemented with filter banks.
A low-pass filter extracts approximations.
A high-pass filter extracts details.
Downsampling reduces the number of samples after filtering.
Repeated filtering of the approximation coefficients creates a multilevel decomposition.
This structure is called a wavelet pyramid or multiresolution hierarchy.
The inverse transform reconstructs the original signal from wavelet coefficients.
Perfect reconstruction requires compatible analysis and synthesis filters.
Biorthogonal wavelets use different wavelets for decomposition and reconstruction.
They can provide symmetry useful in image processing.
Wavelet packets generalize the standard transform by decomposing detail bands as well.
The continuous wavelet transform is redundant but highly interpretable.
The discrete transform is compact and computationally efficient.
Boundary handling matters when signals are finite.
Common boundary methods include zero padding, symmetric extension, and periodic extension.
Poor boundary choices can create artifacts near signal edges.
Thresholding wavelet coefficients is a common denoising technique.
Small coefficients are often associated with noise.
Large coefficients often represent meaningful structures or discontinuities.
Hard thresholding sets small coefficients to zero.
Soft thresholding also shrinks remaining coefficients.
Sparsity is one of the main strengths of wavelet representations.
Many natural signals have only a few large wavelet coefficients.

## History and Context
The mathematical roots of wavelets extend to early twentieth-century harmonic analysis.
Alfred Haar introduced a simple orthogonal system in 1909.
The Haar basis later became recognized as the first wavelet basis.
Fourier analysis dominated signal representation for much of the twentieth century.
Fourier methods represent signals as infinite sinusoids.
They are excellent for stationary periodic behavior.
They are less localized for transients, edges, and sudden changes.
Windowed Fourier methods improved localization by analyzing short segments.
However, a fixed window size creates a fixed time-frequency tradeoff.
Wavelets introduced variable windows that adapt to scale.
Jean Morlet developed wavelet-like methods for seismic exploration in the 1970s and 1980s.
Alex Grossmann helped formalize the continuous wavelet transform.
Yves Meyer developed key mathematical foundations.
Ingrid Daubechies constructed compactly supported orthonormal wavelets.
Stéphane Mallat connected wavelets to filter banks and multiresolution analysis.
This connection made practical fast algorithms possible.
The fast wavelet transform became analogous in importance to the fast Fourier transform.
Wavelets gained prominence in the 1980s and 1990s.
They influenced applied mathematics, engineering, statistics, and computer graphics.
The JPEG 2000 image compression standard used wavelet ideas.
Wavelets also became important in computational physics and numerical partial differential equations.
Their rise reflected a broader shift toward sparse and localized representations.
Modern machine learning has adopted related multiscale ideas.
Although deep learning often uses learned filters, wavelets remain useful as structured priors.
They continue to provide interpretable tools where locality and scale matter.

## Applications and Significance
Wavelet transforms are widely used in image compression.
Images often contain smooth regions separated by edges.
Wavelets represent such images more sparsely than global sinusoidal bases.
JPEG 2000 uses wavelet-based compression to support scalable quality and resolution.
Wavelet denoising is used in audio, biomedical signals, and scientific measurements.
Electrocardiogram analysis can use wavelets to detect short-duration features.
Electroencephalogram analysis can use wavelets to study transient rhythms.
Seismology uses wavelets to identify localized events in time-frequency space.
Geophysics helped motivate early wavelet development.
Wavelets are useful for edge detection in images.
Edges create large coefficients at particular scales and positions.
Computer vision can use wavelet features for texture analysis.
Numerical analysis uses wavelets for adaptive approximation.
Regions with complicated structure receive finer resolution.
Smooth regions can be represented coarsely.
This adaptivity can reduce computational cost.
Wavelets also support compression of scientific simulation data.
In statistics, wavelet shrinkage estimates functions from noisy observations.
In finance, wavelets can separate short-term volatility from long-term trends.
In acoustics, they help analyze chirps, impacts, and nonstationary sounds.
In astronomy, wavelets are used to detect sources and structures at multiple angular scales.
In gravitational wave data analysis, related time-frequency methods help identify transient signals.
In computer graphics, wavelets support level-of-detail representations.
In remote sensing, they assist image fusion and feature extraction.
In neuroscience, wavelets help characterize oscillations that vary through time.
Wavelet transforms are significant because they combine locality, scale, and efficient computation.
They provide a bridge between exact mathematical bases and practical data analysis.
They also illustrate how representation choices shape what patterns become visible.

## Related Concepts
Wavelets are closely related to [[fourier-analysis]], [[short-time-fourier-transform]], and [[filter-banks]].
They depend on ideas from [[linear-algebra]], [[functional-analysis]], and [[orthogonal-basis]].
Important subtopics include [[haar-wavelet]], [[daubechies-wavelets]], and [[morlet-wavelet]].
Applied topics include [[image-compression]], [[signal-denoising]], and [[time-frequency-analysis]].
Computational links include [[fast-wavelet-transform]], [[multiresolution-analysis]], and [[sparse-representation]].
Wavelet thinking also connects to [[convolutional-neural-networks]] and [[scale-space-theory]].
