---
title: Photoreceptors in Plants — Phytochrome, Cryptochrome, and Phototropin
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [cannabis, lighting, indoor, vegetative]
sources: [raw/papers/grahamholmes-what-a-plant-knowsindd.md]
---

# Photoreceptors in Plants — Phytochrome, Cryptochrome, and Phototropin

## Overview

Plants possess a sophisticated array of photoreceptor proteins that allow them to perceive light across a broader spectral range than human eyes. While humans see only the visible spectrum (approximately 400-700 nm) using rod and cone cells, plants have evolved specialized photoreceptors that detect ultraviolet, blue, red, and far-red light. These receptors drive virtually every aspect of plant development — from seed germination to flowering — and operate through distinct molecular mechanisms. The three [[ascomycota-phylogeny-major-classes-lineages]] of plant photoreceptors are phytochromes (red/far-red), cryptochromes (blue/UV-A), and phototropins (blue light).

## Comparison to Animal Vision

Understanding plant photoreception requires appreciating how it differs from and in some ways exceeds animal vision:

- **Human photoreceptors**: Rods (all light, night vision) and three types of cones (red, green, blue) — approximately 125 million rods and 6 million cones on a retina the size of a passport photo
- **Plant photoreceptors**: Multiple receptor families spanning UV-B to far-red (280-750 nm), distributed throughout the plant body rather than concentrated in a single organ
- **Key difference**: Plants don't form images; instead, they perceive light intensity, direction, color, and duration to guide developmental decisions

Plants can detect ultraviolet light (which gives us sunburn), infrared/far-red light (which we feel as heat), extremely low light levels (from a candle), the direction of light sources, whether another plant is shading them, and precisely how long the dark period has lasted. By any reasonable definition, this constitutes a form of vision — one that is in many ways more informationally rich than our own.

## Phytochromes: Red and Far-Red Sensors

### Structure and Function

Phytochromes are the primary photoreceptors for red (660 nm) and far-red (730 nm) light. They are large proteins (~125 kDa) consisting of:

- An N-terminal photosensory domain that covalently binds a chromophore called **phytochromobilin** (a linear tetrapyrrole related to the heme group in hemoglobin)
- A C-terminal output domain with [[gadd-two-component-signalling-histidine-kinase-fungi]] activity that initiates signaling cascades

### The Pr/Pfr Switch

Phytochromes exist in two photo-interconvertible forms:

- **Pr (P660)**: Absorbs red light maximally at ~660 nm; biologically inactive form
- **Pfr (P730)**: Absorbs far-red light maximally at ~730 nm; biologically active form

Red light converts Pr → Pfr (activating the system). Far-red light converts Pfr → Pr (deactivating). In darkness, Pfr slowly reverts to Pr through thermal relaxation (dark reversion). The Pfr form also triggers its own degradation, providing an additional timer mechanism.

### Phytochrome Family

Arabidopsis has five phytochrome genes (PHYA-PHYE) with distinct roles:

| Gene | Peak Sensitivity | Primary Functions |
|---|---|---|
| PHYA | Far-red continuous | Seedling de-etiolation, [[phytochrome-red-far-red-ratio-shade-detection-plants]] under canopy |
| PHYB | Red/far-red reversible | Photoperiodic flowering, [[shade-avoidance-syndrome]], seed germination |
| PHYC | Red | Modulates flowering time, interacts with PHYB |
| PHYD | Red | Redundant with PHYB for shade avoidance |
| PHYE | Red/far-red | Far-red high-irradiance responses |

### Phytochrome Responses

Phytochromes regulate an enormous range of plant processes:

- **Seed germination**: Many seeds require red light to germinate; far-red inhibits germination
- **De-etiolation**: When a seedling emerges from soil, phytochrome detects light and switches from etiolated (pale, elongated) to green, photosynthetically competent growth
- **Shade avoidance**: Low red:far-red ratio (caused by canopy filtering) triggers stem elongation and leaf hyponasty
- **Photoperiodic flowering**: Pfr reversion during the night measures dark period length
- **Circadian clock entrainment**: Phytochrome signals help synchronize the plant's [[chrysanthemum-coronarium]] to external light-dark cycles

## Cryptochromes: Blue and UV-A Sensors

### Structure and Function

Cryptochromes are flavoprotein photoreceptors that absorb blue light (~450 nm) and UV-A light (~320-400 nm). They share [[psilocybin-serotonin-structural-homology-endogenous-familiarity-argument]] with DNA photolyases (enzymes that repair UV-damaged DNA) but have lost DNA repair function and instead serve as photoreceptors.

The chromophore is **flavin adenine dinucleotide (FAD)**, the same cofactor used in many metabolic enzymes. In Arabidopsis, two cryptochromes have been well characterized:

- **CRY1**: Primarily mediates de-etiolation responses — inhibits hypocotyl elongation in blue light
- **CRY2**: Primarily mediates photoperiodic flowering — promotes flowering in response to blue light

### Cryptochrome Activation Mechanism

Unlike phytochromes, which use a simple Pr/Pfr switch, cryptochrome activation is more complex:

1. Blue light absorption causes electron transfer within the FAD chromophore
2. This triggers conformational changes in the protein
3. The activated cryptochrome undergoes nuclear import
4. In the nucleus, it interacts with transcription factors (COP1/SPA complex) to regulate gene expression
5. CRY2 is degraded after activation, providing a built-in desensitization mechanism

### Cryptochrome Responses

- **Inhibition of stem elongation**: Blue light sensed by CRY1 suppresses hypocotyl elongation
- **Photoperiodic flowering**: CRY2 promotes flowering independently of phytochrome
- **Circadian clock**: Cryptochromes are essential components of the plant circadian oscillator
- **Stomatal opening**: Blue light triggers stomatal opening through cryptochrome and phototropin pathways
- **Magnetoreception**: There is evidence that cryptochromes may mediate sensitivity to magnetic fields in plants (and animals)

## Phototropins: Blue Light Directional Sensors

### Structure and Function

Phototropins are the photoreceptors specifically responsible for detecting the **direction** of blue light and mediating phototropic bending. They contain two chromophore-binding domains called LOV (Light, Oxygen, or Voltage) domains:

- **LOV1**: Binds FMN (flavin mononucleotide); modulates overall sensitivity
- **LOV2**: Binds FMN; primary phototropic signaling domain — undergoes a conformational change upon blue light absorption that unfolds an attached C-terminal kinase domain

### Phototropin Types

- **phot1**: Mediates phototropism under low to moderate blue light intensities
- **phot2**: Activates at higher blue light intensities; mediates chloroplast avoidance response (moving chloroplasts to cell walls to reduce photodamage under intense light)

### Additional Phototropin Functions

Beyond phototropism, phototropins regulate chloroplast positioning, stomatal opening, leaf flattening, and rapid inhibition of stem elongation in blue light.

## UV-B Receptors

A fourth class, UVR8, specifically detects UV-B radiation (280-315 nm). It is a homodimer that monomerizes upon UV-B absorption and mediates UV protection responses including flavonoid production and DNA repair enzyme activation. Unlike other photoreceptors, UVR8 uses tryptophan amino acids as chromophores rather than an external cofactor.

## Integration of Light Signals

In nature, plants simultaneously receive signals from all photoreceptor classes. The developmental outcome depends on the integration of these signals:

- **Full sunlight**: Red + blue + UV-B → compact growth, photosynthetic development, protective pigment production
- **Canopy shade**: Far-red enriched, blue reduced → stem elongation, upward leaf movement, suppressed branching
- **End of day**: Far-red enriched → phytochrome deactivation, preparation for dark period
- **Dawn**: Red + blue → phytochrome activation, cryptochrome activation, phototropin activation, clock reset

## Applications for Indoor Growers

Understanding plant photoreceptors directly informs grow light selection and lighting strategy:

- **Red light (660 nm)**: Drives photosynthesis via chlorophyll absorption AND activates phytochrome — essential for vegetative growth and flowering trigger
- **Blue light (450 nm)**: Drives photosynthesis AND activates cryptochrome and phototropin — essential for compact growth, stomatal function, and phototropism
- **Far-red (730 nm)**: Not useful for photosynthesis but critical for phytochrome regulation — end-of-day far-red can improve flowering and reduce inter-node stretching
- **Full-spectrum LEDs** that include all these wavelengths more closely mimic natural light and support all photoreceptor pathways
- **Narrow-band LEDs** (e.g., red-only or red+blue only) may create imbalances if photoreceptor pathways other than photosynthesis are under-stimulated

## Related Concepts

- [[photoperiodism-phytochrome-red-far-red]]
- [[plant-phototropism-darwin-experiments]]
- light spectrum grow lights photosynthesis
- par ppfd light measurement grow lights

## See Also

- Chamovitz D. (2012) "What a Plant Knows." Oneworld Publications.
- Christie JM. (2007) "Phototropin Blue-Light Receptors." Annual Review of Plant Biology 58: 21-45.
- Rockwell NC, Martin SS, Lagarias JC. (2006) "Phytochrome Structure and Signaling Mechanisms." Annual Review of Plant Biology 57: 837-858.
