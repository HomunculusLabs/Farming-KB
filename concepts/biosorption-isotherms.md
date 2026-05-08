---
title: Biosorption Isotherms and Equilibrium Modeling
created: 2026-04-18
updated: 2026-04-18
type: concept
tags: [reference]
sources: [raw/papers/singh-harbhajan_-mycoremediation-_-fungal-bioremediation.md]
---

# Biosorption Isotherms and Equilibrium Modeling

Biosorption isotherms are mathematical models that describe the distribution of adsorbed contaminants between a biosorbent surface and the surrounding solution at equilibrium.

These models are fundamental tools for designing and optimizing biosorption-based water treatment systems, providing quantitative relationships between contaminant concentration in solution and the amount sorbed per unit mass of biosorbent.

The study of biosorption isotherms draws on principles from physical chemistry, surface science, and environmental engineering, and is central to understanding the mechanisms described in [[fungal-biosorption-mechanisms]] and [[fungal-metal-biosorption]]. These models are essential for engineering [[mycoremediation-bioreactor-design]] systems and inform field-scale [[bioremediation-using-fungi]] where real-world conditions deviate significantly from laboratory isotherm predictions.

## Langmuir Isotherm Model

The Langmuir isotherm is the most widely used model for biosorption equilibrium data.

It assumes monolayer adsorption onto a surface containing a finite number of identical binding sites, with no interaction between adsorbed molecules.

The Langmuir model is expressed as q = qmax * b * Cf / (1 + b * Cf), where q is the amount of metal adsorbed per unit mass of biosorbent (mg/g), qmax is the maximum adsorption capacity corresponding to complete monolayer coverage, Cf is the equilibrium concentration of metal in solution (mg/L), and b is a constant related to the affinity of the binding sites.

The Langmuir model works well for systems where adsorption occurs on a relatively homogeneous surface with uniform binding sites.

For [[fungal-metal-biosorption]] systems, Langmuir fits often describe data well for single-metal systems where binding occurs primarily through specific functional groups such as carboxyl or phosphate groups on the fungal cell wall.

A dimensionless separation factor, RL, derived from the Langmuir constant b, indicates whether adsorption is favorable (0 < RL < 1), unfavorable (RL > 1), linear (RL = 1), or irreversible (RL = 0).

Maximum biosorption capacities reported for fungal biomass typically fall in the range of 0.1 to 1.0 mmol metal per gram dry weight, depending on the metal, fungal species, and experimental conditions.

## Freundlich Isotherm Model

The Freundlich isotherm is an empirical model that describes adsorption on heterogeneous surfaces with non-uniform binding site energies.

The Freundlich equation is q = K * Cf^(1/n), where K is the Freundlich constant related to adsorption capacity and n is an empirical parameter related to adsorption intensity.

The Freundlich model does not predict a maximum adsorption capacity, which is both a limitation and an advantage: it can describe multilayer adsorption but cannot indicate when saturation occurs.

For biosorption systems with heterogeneous binding sites, such as fungal biomass containing multiple types of functional groups with different affinities for metal ions, the Freundlich model often provides a better fit than the Langmuir model.

The parameter n typically ranges from 1 to 10 for favorable adsorption, with values closer to 1 indicating more linear isotherm behavior.

The Freundlich equation can be linearized in logarithmic form as log(q) = log(K) + (1/n) * log(Cf), allowing easy determination of the constants from experimental data plots.

The Freundlich model is particularly useful for describing biosorption in systems where multiple mechanisms operate simultaneously, including ion exchange, complexation, and surface precipitation.

## Other Equilibrium Models

Several additional isotherm models have been applied to biosorption data, each capturing different aspects of the adsorption process.

The Redlich-Peterson isotherm incorporates features of both Langmuir and Freundlich models and approaches the Freundlich isotherm at high concentration and the Langmuir isotherm at low concentration.

The Sips isotherm is another three-parameter model that reduces to the Langmuir equation at low concentrations and the Freundlich equation at high concentrations, providing flexibility for describing adsorption over wide concentration ranges.

The Temkin isotherm accounts for indirect adsorbate-adsorbate interactions and assumes that the heat of adsorption decreases linearly with coverage.

The Dubinin-Radushkevich (DR) isotherm is based on the theory of volume filling of micropores and can be used to estimate the mean free energy of adsorption, which helps distinguish between physical and chemical adsorption mechanisms.

The Brunauer-Emmett-Teller (BET) isotherm extends the Langmuir model to multilayer adsorption, which may be relevant for biosorption systems where contaminants accumulate in multiple layers on the biomass surface.

The Scatchard-Langmuir model provides a means of analyzing binding site heterogeneity by plotting q/Cf against q, where linear segments indicate distinct classes of binding sites.

## Factors Affecting Biosorption Isotherms

Multiple experimental and environmental factors influence the shape and parameters of biosorption isotherms.

Solution pH is often the most important variable because it affects both the speciation of metal ions in solution and the ionization state of functional groups on the biosorbent surface.

Most fungal biosorption studies show maximum metal uptake in the pH range of 4 to 6, where carboxyl groups on the cell wall are deprotonated and available for metal binding, but metal hydrolysis and precipitation have not yet begun.

Temperature affects biosorption isotherms through its influence on thermodynamic parameters including the Gibbs free energy, enthalpy, and entropy of adsorption.

Biomass concentration and particle size influence the accessibility of binding sites and the rate at which equilibrium is achieved, though they do not change the intrinsic binding capacity.

Initial metal concentration determines whether the system operates in the linear, transitional, or saturation region of the isotherm, affecting the observed distribution coefficient.

The presence of competing ions in multimetal systems significantly alters biosorption isotherms compared to single-metal systems.

Ion selectivity in multimetal biosorption depends on factors including ionic radius, electronegativity, charge density, and the specific coordination chemistry of each metal with the available functional groups.

Biosorption data for multimetal systems are far less abundant than for single-metal systems, and predictive modeling of competitive biosorption remains an active research area.

## Biosorption Kinetics and Column Design

While isotherms describe equilibrium conditions, the rate at which equilibrium is approached is equally important for practical system design.

Biosorption kinetics are commonly modeled using pseudo-first-order and pseudo-second-order rate equations.

The pseudo-second-order model often provides a better fit for biosorption data, suggesting that chemisorption or ion exchange is the rate-limiting step in many fungal biosorption systems.

Film diffusion, intraparticle diffusion, and pore diffusion may all contribute to the overall rate of biosorption, with the relative importance depending on biomass characteristics and mixing conditions.

For continuous-flow treatment systems, biosorption isotherm data are combined with mass transfer models to design fixed-bed or fluidized-bed columns.

The breakthrough curve, which describes the effluent concentration as a function of time or volume treated, is the key performance indicator for column operation.

Empty bed contact time (EBCT) and bed depth are the primary design parameters derived from isotherm and kinetic data.

Column regeneration using acid or chelating agent eluents allows repeated use of the biosorbent, which is critical for economic viability.

The number of adsorption-desorption cycles that a biosorbent can withstand without significant loss of capacity determines the operational lifetime and cost-effectiveness of the treatment system.

## Applications in Wastewater Treatment

Biosorption isotherms provide the engineering basis for designing treatment systems for metal-contaminated wastewater streams from mining, electroplating, tannery, and textile industries.

Fungal biosorbents including Rhizopus arrhizus, Mucor meihi, Aspergillus niger, and Saccharomyces cerevisiae have been studied extensively for metal removal from industrial effluents. Studies of [[singh-chromium-bioremediation-fungi]] demonstrate how species-specific differences in cell wall chemistry affect biosorption capacity. The underlying [[fungal-bioremediation-mechanisms]] -- including ion exchange, complexation, and microprecipitation -- directly determine which isotherm model best fits a given system.

Non-living fungal biomass offers several advantages for biosorption applications: it does not require nutrients, is not affected by metal toxicity, and can be produced as a byproduct of industrial fermentation processes.

Pretreatment of biomass with acids, bases, or heat can enhance biosorption capacity by removing masking compounds and exposing additional binding sites.

Immobilization of fungal biomass on inert supports such as alginate beads, polyurethane foam, or silica gel improves mechanical strength, reusability, and suitability for column operation.

Integration of biosorption with other treatment technologies, including [[fungal-bioreactor-effluent-treatment]] and [[constructed-wetlands-wastewater-treatment]], can improve overall treatment efficiency for complex waste streams.

[[fungal-biosorption-desorption-regeneration]] studies provide essential data for evaluating the economic viability of biosorption processes and optimizing regeneration protocols for different metal-biosorbent combinations.
- [[fungal-treatment-of-textile-dyes-mechanisms]]
- [[constructed-wetlands-wastewater-treatment]]
- [[fungal-industrial-wastewater-treatment]]

## See Also

- [[staycare-fungal-biosorption-of-heavy-metals]] — comprehensive review of metal biosorption capacities across fungal species
- [[staycare-fungal-metal-biosorption-reactor-systems]] — engineering design of continuous-flow biosorption columns
- [[staycare-chitosan-and-fungal-biomass-derivatives-in-biosorption]] — chemical modification of fungal biomass to enhance sorption
- [[staycare-bioavailability-pollutants-fungal-bioremediation]] — how pollutant bioavailability affects isotherm behavior in situ

[[staycare-fungal-biosorption-of-heavy-metals]] | [[staycare-fungal-metal-biosorption-reactor-systems]] | [[staycare-chitosan-and-fungal-biomass-derivatives-in-biosorption]] | [[staycare-bioavailability-pollutants-fungal-bioremediation]]
[[fungal-biosorption-mechanisms]] | [[fungal-metal-biosorption]] | [[mycoremediation-bioreactor-design]] | [[fungal-bioremediation-mechanisms]] | [[fungal-industrial-wastewater-treatment]]
