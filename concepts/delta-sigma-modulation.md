---
title: Delta Sigma Modulation
created: 2026-04-28
updated: 2026-05-06
sources:
  - "raw/papers/permaculture-a-designers-manual-bill-mollison.md"
type: concept
tags: [reference]
---

# Delta-Sigma Modulation

## Overview
Delta-sigma modulation is a signal-conversion technique that trades amplitude precision for time precision.
It is most often used in analog-to-digital converters and digital-to-analog converters.
The method samples a signal far above the minimum Nyquist rate.
It then uses feedback to push much of the quantization noise away from the frequency band of interest.
A digital or analog filter can later remove the out-of-band noise.
The result is high effective resolution from relatively simple low-resolution quantizers.
Many delta-sigma converters use a one-bit or few-bit internal quantizer.
The Greek letter delta refers to differencing or measuring change.
The Greek letter sigma refers to summation or integration.
Together they describe a loop that integrates the difference between input and feedback.
Delta-sigma modulation is also called sigma-delta modulation.
Both names are common, although delta-sigma emphasizes the chronological order of operations in many designs.

## Core principle
A delta-sigma modulator compares an input signal with a reconstructed feedback signal.
The difference, or error, is accumulated by one or more integrators.
A quantizer converts the accumulated value into a low-resolution output stream.
That output is fed back through a digital-to-analog element in the loop.
If the feedback output is too low, the integrator tends to force future bits upward.
If the feedback output is too high, the integrator tends to force future bits downward.
Over time, the density of ones and zeros represents the input amplitude.
For a one-bit modulator, a larger positive input produces a higher fraction of ones.
A smaller input produces a lower fraction of ones.
The instantaneous output is noisy, but its average over many samples is accurate.
This averaging is useful only when the signal bandwidth is much smaller than the sampling rate.

## Oversampling
Oversampling means sampling faster than twice the highest signal frequency.
In a delta-sigma converter, the oversampling ratio may be tens, hundreds, or thousands.
Oversampling spreads quantization noise over a wider frequency range.
Only a small part of that noise then falls inside the desired signal band.
A decimation filter keeps the desired band and reduces the sample rate.
For audio conversion, the modulator may run in the megahertz range.
The final output may still be ordinary 44.1 kHz, 48 kHz, or 96 kHz audio.
For precision sensors, the final bandwidth may be only a few hertz.
High oversampling can therefore produce very high resolution for slow measurements.
Oversampling alone improves noise performance gradually.
Noise shaping is what makes delta-sigma modulation especially powerful.

## Noise shaping
Quantization converts a continuous-valued signal into discrete levels.
The difference between the exact value and the quantized value is quantization error.
In a simple converter, this error is often modeled as roughly white noise.
A delta-sigma feedback loop changes where that noise appears in frequency.
The signal transfer function ideally passes the input through the modulator.
The noise transfer function pushes quantization error toward high frequencies.
This is called noise shaping.
A first-order modulator shapes noise with a rising high-frequency spectrum.
Higher-order modulators can push noise away from the signal band more aggressively.
The price of stronger shaping is greater risk of instability and idle tones.
Designers choose loop order, quantizer bits, and coefficients to balance these effects.

## Modulator orders
A first-order delta-sigma modulator has one integrator in its loop.
It is conceptually simple and usually stable.
Its in-band noise decreases substantially as oversampling increases.
A second-order modulator uses two integrators or an equivalent loop filter.
It can achieve much better in-band noise suppression.
Third-order and higher-order modulators are common in high-performance systems.
However, high-order nonlinear feedback loops can become unstable for large inputs.
Practical designs often use simulations, conservative gain margins, and overload detection.
Multi-stage noise-shaping architectures split high-order behavior into cascaded stages.
These are sometimes known as MASH converters.
MASH designs can improve stability by digitally canceling quantization errors from earlier stages.
Their accuracy depends on good matching between analog and digital paths.

## One-bit and multi-bit designs
Early delta-sigma converters were often one-bit systems.
A one-bit feedback DAC is inherently linear because it has only two output levels.
This removes many mismatch errors that plague multi-bit feedback DACs.
One-bit designs are attractive for high linearity.
Their disadvantage is relatively high quantization noise before shaping.
Multi-bit modulators use quantizers with several internal levels.
They reduce quantization noise and ease loop stability requirements.
However, a multi-bit feedback DAC can introduce distortion if its elements are mismatched.
Dynamic element matching is often used to randomize or shape mismatch errors.
Modern integrated circuits frequently use multi-bit delta-sigma modulators.
The choice depends on resolution, bandwidth, power, process technology, and cost.

## Digital filtering and decimation
The raw output of a delta-sigma modulator is not usually the final signal.
It contains the desired information plus shaped high-frequency noise.
A low-pass digital filter removes most out-of-band noise.
Decimation then reduces the sample rate to a practical value.
A sinc filter is common in precision measurement converters.
Finite impulse response filters are common in audio [[tompkins-plant-electrical-signals]]
- mollison-permaculture-two-sound-walls-noise-control

See also: [[natural-building]]
## See Also
- [[cannabis-immune-modulation]]
