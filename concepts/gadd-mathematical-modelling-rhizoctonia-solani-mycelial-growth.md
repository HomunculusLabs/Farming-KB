# Mathematical Modelling of Mycelial Form and Function

**Source:** Gadd, Watkinson & Dyer, *Fungi in the Environment*, Chapter 4
**Domain:** Mycology → Fungal Ecology → Mathematical Biology

---

## Overview

Mathematical modelling of fungal mycelia complements experimental
approaches for understanding how filamentous fungi grow, explore
resources, and function in [[fungal-mycelial-foraging-heterogeneous-environments]]. Fordyce A.
Davidson's chapter presents a hybrid continuum-discrete model connecting
hyphal-level physiology (tip growth, branching, anastomosis) to
mycelial-level properties (biomass distribution, [[dighton-fungal-nutrient-translocation-element-redistribution]],
colony form). The model was calibrated against Rhizoctonia solani, a
ubiquitous soil-borne saprotroph.

The fundamental challenge is scale: fungi operate from micrometre-scale
nutrient uptake to metre-scale resource translocation, and from seconds
(tip vesicle fusion) to weeks (colony expansion).

## Scale Choices in Fungal Modelling

Two broad modelling approaches exist, each suited to different scales:

**Continuum models**: Treat biomass as a density field using PDEs. Best for
dense growth in uniform conditions (Petri dishes). Individual hyphal
properties are averaged.

**Discrete models**: Track individual hyphae as computational objects.
Reproduce realistic branching and fractal morphology but used non-
mechanistic rules and neglected anastomosis and translocation.

Both approaches had significant limitations. Continuum models ignored
the fractal nature of [[fungal-mycelial-networks-nutrient-translocation]]. Discrete models neglected
anastomosis and translocation — processes crucial for growth in
heterogeneous environments — due to computational constraints.

## The Hybrid Model

Davidson's innovation is a hybrid cellular automaton model that combines
the strengths of both approaches:

**Five state variables** tracked on a 2D grid:
1. Active hyphae (involved in metabolite translocation)
2. Inactive hyphae (moribund, not translocating)
3. Hyphal tips (growing points)
4. Internal substrate (nutrients within the fungus)
5. External substrate (nutrients in the environment)

**Key model equations:**

Change in active hyphae = new hyphae from moving tips + reactivation
of inactive hyphae − inactivation of active hyphae

Change in hyphal tips = tip movement + branching − anastomosis

Change in internal substrate = translocation (active + passive) +
uptake from environment − maintenance costs − growth costs −
translocation energy costs

Change in external substrate = diffusion − fungal uptake

The model explicitly includes both active (metabolically driven) and
passive (diffusive) translocation, and represents anastomosis (hyphal
fusion) as a tip-removal process.

## Growth Characteristics Modelled

**Tip extension**: Hyphal tips move in approximately straight lines with
small random fluctuations (due to wall incorporation patterns). Tip
growth rate depends on internal substrate concentration.

**Branching**: Modelled as proportional to internal substrate
concentration, reflecting the biological relationship between turgor
pressure, tip vesicle accumulation, and branch initiation.

**Anastomosis**: When a tip contacts an existing hypha, the tip is
absorbed into the hyphal network. This is a simplification of the
biological process of hyphal fusion but captures its population-level
effect on tip count.

**Nutrient uptake**: Depends on external substrate concentration,
internal substrate concentration (energy for active transport), and
hyphal surface area.

**Active translocation**: Moves internal substrate toward hyphal tips
(the major growth sinks) and depletes energy reserves. This is
distinguished from passive diffusion, which is energy-free.

## Calibration with Rhizoctonia solani

The model was calibrated using R. solani AG4 (R3) cultured on mineral
salts medium with 2% glucose at 30°C. Parameters were estimated from:
- Tip velocity and branching rates from 15-hour time-lapse imaging
- Diffusion coefficients from literature
- Uptake rates from literature

The calibrated model accurately predicted colony radial expansion.
The Q10-rule (metabolic rate approximately halves per 10°C decrease)
was applied by reducing tip velocity alone, and the model accurately
predicted 15°C growth rates — suggesting the complex temperature
effects on R. solani can be captured by varying a single parameter.

## Key Finding: Translocation Redundancy in Rich Media

A remarkable result emerged when active translocation was disabled in
the model: radial growth rate and biomass distribution were largely
unaffected. The model predicts that R. solani relies on energy-free
diffusion for internal metabolite redistribution in nutrient-rich,
uniform conditions. Active translocation appears to be a strategy
reserved for heterogeneous or nutrient-poor environments where
diffusion alone cannot supply distal hyphal tips.

This finding has important ecological implications: the energetic cost
of active translocation is justified only when it enables growth into
nutrient-poor zones that would otherwise be inaccessible.

## Modelling Acidity Production

The model was extended to simulate acid production by R. solani. Since
the fungus produces organic acids only in the presence of utilizable
carbon, acidity generation was linked to internal substrate
concentration. The model produced pH distribution maps matching
experimental measurements, demonstrating that fungal metabolism
directly alters its chemical environment in spatially heterogeneous
patterns.

## Acidification Patterns

Acidification is most intense behind the colony margin where biomass
density is highest, creating a pH gradient from acidic (center) to
neutral (edge). This affects [[ph-and-nutrient-availability-garden-soils]] (many nutrients
more soluble at lower pH) and [[cannabis-cultivar-microbial-community-effects]] interactions
(pH-sensitive organisms excluded from colony interior).

## Limitations and Future Directions

- Assumes single limiting substrate (carbon)
- No three-dimensional growth modelling
- Water and osmotic effects not included
- Multi-species interactions not addressed
- Continuum [[hot-water-and-hydrated-lime-substrate-treatment]] may miss soil pore-scale heterogeneity

Davidson envisions multi-scale modelling transferring information from
gene-level processes through hyphal physiology to mycelial function.

## See Also
