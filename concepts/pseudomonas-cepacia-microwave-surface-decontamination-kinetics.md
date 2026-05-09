---
title: "pseudomonas cepacia in challenge-microorganisms-microwave-surface-sterilization Decontamination Kinetics"
tags:
  - microbiology
  - microwave-sterilization
  - dose-response
  - pseudomonas
  - kill-curve
  - nasa-msap
  - surface-decontamination
  - spacecraft
  - eclss
  - challenge-organisms
source:
  - NASA Tech Brief MSC-22484
  - Lyndon B. Johnson Space Center, Houston, Texas
  - Innovators: James E. Atwater, Neil D. Streech, Frank C. Garmon
---

# Pseudomonas cepacia in Microwave Surface Decontamination Kinetics

## Overview

_Pseudomonas cepacia_ (now reclassified as _Burkholderia cepacia_) served as one of three
primary [[mixed-microbial-challenge-organisms-surface-sterilization-testing]] in the NASA [[microwave-sterilizable-access-port-nasa-space-biology|Microwave Sterilizable Access Port]] (MSAP) development
program at the Lyndon B. Johnson Space Center. Alongside _Bacillus pumilus_ and _Escherichia
coli_, it was selected to represent a broad spectrum of microbial resistance profiles relevant
to spacecraft [[eclss-environmental-control-life-support]] and Life Support System (ECLSS) contamination scenarios.
The MSAP program tested 2.45 GHz [[microwave-surface-sterilization|microwave surface sterilization]] as an alternative to
conventional autoclaving, gamma irradiation, UV exposure, and chemical disinfectants.

## Why Pseudomonas cepacia Was Selected

_Pseudomonas cepacia_ is a Gram-negative, non-fermenting, motile bacterium with notable
environmental persistence and intrinsic resistance to many antimicrobial agents. Its selection
as a challenge organism for the MSAP program was driven by several factors that make it
particularly relevant to closed-system water contamination in spacecraft environments:

1. **Oxidative stress tolerance**: _P. cepacia_ possesses catalase and superoxide dismutase
   enzymes that confer resistance to reactive oxygen species generated during microwave-induced
   water heating, making it a stringent test of the [[microwave-sterilization|microwave sterilization]] mechanism.
2. **Biofilm formation**: The organism readily colonizes wetted surfaces and forms protective
   biofilms, simulating the type of persistent contamination encountered in ECLSS water lines
   and mating fixture geometries.
3. **Clinical significance**: Known as an opportunistic pathogen, its presence in potable water
   systems represents a genuine crew health concern during extended-duration spaceflight.
4. **Gram-negative cell wall complexity**: The outer membrane of _P. cepacia_ provides an
   additional permeability barrier compared to Gram-positive organisms, testing whether
   microwave energy can achieve lethal intracellular effects through thermal and non-thermal
   mechanisms.

## Mixed-Species Kill Curve Methodology

The MSAP testing protocol inoculated surface coupons with mixed populations containing
_P. cepacia_, _B. pumilus_, and _E. coli_ at defined ratios. Surfaces were prepared with
approximately 9 µL/cm² of trace water to enable microwave coupling with the rotational
transitions of dipolar water molecules at 2.45 GHz. [[microbial-kill-curve-microwave-exposure-dose-response]] was delivered at
an effective intensity of 3.6 W/cm², with total accumulated energy measured in watt-hours
(W-hr). Viable counts were determined by serial dilution and plate assay at defined energy
intervals to construct kill curves showing log₁₀ reduction versus cumulative dose.

## Dose-Response Kinetics

The mixed-species kill curves generated during MSAP testing demonstrated the following
key dose-response relationships relevant to _P. cepacia_ decontamination:

- **4 W-hr cumulative exposure**: Approximately 10⁶ (six-log) reduction in viable count
  for the mixed population. At this dose level, the more sensitive _E. coli_ cells were
  largely eliminated, while surviving populations were dominated by the more resistant
  _P. cepacia_ and _B. pumilus_ organisms.
- **8 W-hr cumulative exposure**: Approximately 10⁸ (eight-log) reduction, achieving
  near-complete sterilization of the mixed-species challenge. This dose level was sufficient
  to overcome the resistance mechanisms of _P. cepacia_ including its outer membrane
  barrier and oxidative stress defenses.
- **13.1 W-hr total exposure**: The full MSAP sterilization protocol at 3.6 W/cm² effective
  intensity, providing a wide safety margin beyond the demonstrated kill thresholds.
- **Sterilization mechanism**: Microwave energy couples with trace water on the surface,
  causing rapid localized heating. For _P. cepacia_, the lethal mechanism involves both
  thermal denaturation of cellular proteins and membranes, as well as potential non-thermal
  effects from electromagnetic field interactions with charged cellular components.
- **Steam contribution**: At sufficient energy density, microwave-induced steam generation
  on damp surfaces provides an additional sterilization pathway through heat transfer to
  organisms in surface irregularities and shadowed geometries.

## Relative Resistance Among Challenge Organisms

Within the three-organism test panel, the relative microwave resistance followed a pattern
where _P. cepacia_ exhibited intermediate-to-high resistance:

- _Escherichia coli_ (Gram-negative, mesophilic): Generally the most sensitive of the
  three organisms to microwave exposure, showing rapid log reduction at lower energy doses.
- _Pseudomonas cepacia_ (Gram-negative, oxidative-stress tolerant): Demonstrated greater
  resistance than _E. coli_ due to its more robust stress response systems and biofilm
  association, requiring higher cumulative energy to achieve equivalent log reductions.
- _Bacillus pumilus_ (Gram-positive, spore-forming): The most resistant organism in
  the panel, as its endospore form provides exceptional protection against heat and
  electromagnetic stress, establishing the upper bound of the sterilization requirement.

The inclusion of _P. cepacia_ alongside a non-spore-forming mesophile (_E. coli_) and a
spore-forming bacterium (_B. pumilus_) ensured the kill curves captured the full range of
microbial susceptibility expected in spacecraft environmental systems.

## Relevance to Spacecraft ECLSS Surface Contamination

The microwave surface decontamination kinetics established using _P. cepacia_ and the other
challenge organisms have direct implications for maintaining sterile water systems aboard
spacecraft and orbital platforms:

- **Closed-loop water systems**: ECLSS water recovery and distribution systems present
  extensive internal surface area where organisms like _P. cepacia_ can establish persistent
  colonies, particularly at joints, valves, and low-flow sections where biofilm accumulates.
- **Mating fixture contamination**: Each physical connection between components (sampling
  ports, nutrient addition lines, experiment chambers) represents a potential contamination
  pathway where surface sterilization must be verified before and after each operation.
- **Water chemistry constraints**: Unlike chemical disinfectants such as [[cervantes-hydrogen-peroxide-sterilization]],
  elemental iodine, or quaternary amines, microwave sterilization leaves no chemical residues
  that could degrade water quality or interfere with downstream analytical instrumentation.
- **Rapid turnaround**: The demonstrated kill kinetics at moderate energy doses allow for
  practical sterilization cycles compatible with the operational tempo of space biology
  experiments, where frequent [[eclss-water-system-aseptic-access-space-biology]] to sterile systems is required.

## Key Parameters Affecting P. cepacia Kill Rates

Several controllable parameters influence the efficiency of microwave decontamination against
_P. cepacia_ and related organisms in the MSAP framework:

- **Duration**: Longer exposure allows cumulative energy to overcome cellular repair
  mechanisms and achieve deeper thermal penetration into biofilm matrices.
- **Intensity**: Higher power density (W/cm²) increases the rate of energy delivery
  and the peak surface temperatures achieved, directly accelerating microbial kill.
- **Water amount**: Trace moisture (~9 µL/cm²) is essential for microwave energy coupling;
  insufficient water reduces effectiveness, while excess water can create thermal gradients
  that shield organisms from lethal temperatures.
- **Surface geometry**: Complex geometries with shadowed regions or crevices may receive
  uneven energy distribution, potentially harboring surviving organisms if not adequately
  addressed by steam penetration or repositioning during the sterilization cycle.
- **Initial bioburden**: Higher starting populations require proportionally greater energy
  input to achieve the target sterility assurance level, as described by the classic
  first-order inactivation kinetics observed in the kill curve data.

## Significance for Controlled Environment Agriculture

While developed for spacecraft applications, the microwave surface decontamination kinetics
characterized using _P. cepacia_ are directly transferable to controlled environment
agriculture and mycological research contexts. _Burkholderia cepacia_ complex organisms are
known contaminants in hydroponic and aeroponic growing systems, where they can persist on
wetted surfaces, tubing, and reservoir walls. The demonstrated dose-response relationships
provide a quantitative basis for adapting microwave sterilization protocols to sanitize
growing system components, inoculation tools, and environmental surfaces without the thermal
damage, chemical residues, or material degradation associated with conventional methods.
