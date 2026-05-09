# Environmental Control and Life Support System (ECLSS)

## Overview

An Environmental Control and Life Support System (ECLSS) is a critical subsystem of crewed spacecraft and space stations that regulates the spacecraft environment to sustain human life. ECLSS manages atmospheric composition, temperature, humidity, pressure, water recovery, waste management, and fire detection/suppression. The system must operate reliably in the extreme conditions of space — vacuum, radiation, microgravity, and extreme temperature cycles — while maintaining conditions within narrow tolerances required for human health and comfort.

## Core Functions

### Atmospheric Management
- **Oxygen supply**: Generating and distributing breathable oxygen (typically 20.1–23.5% partial pressure)
- **Carbon dioxide removal**: Scrubbing CO₂ from cabin air to maintain levels below 5.3 mmHg (0.7%)
- **Nitrogen management**: Maintaining total cabin pressure at approximately 14.7 psi ([[vegetable-storage-conditions-by-temperature-and-humidity]] Control
- **Cabin temperature**: Maintained at 18–27°C (64–80°F), nominally 22°C
- **Relative humidity**: Controlled to 30–70%, nominally 40–60%
- **Heat rejection**: Collecting and rejecting waste heat from crew, equipment, and solar radiation to the space environment via radiators
- **Condensate management**: Collecting and processing water condensed from humid cabin air

### Water Recovery and Management
- **Urine processing**: Converting crew urine into potable water through distillation and filtration
- **Washwater recovery**: Processing water from hygiene activities (handwashing, showering)
- **Condensate processing**: Recoveri [[mollison-designers-soil-water-storage-in-forest-systems]] trict potability standards
- **Water storage**: Managing clean and waste water storage tanks

### Waste Management
- **Solid waste**: Collecting, processing, and storing solid waste (feces, food waste, trash)
- **Liquid waste**: Processing urine and other liquid wastes for water recovery or disposal
- **Hygiene waste**: Managing personal hygiene products and medical waste

## Sterilization Challenges in ECLSS

The need for reliable surface sterilization within ECLSS systems was a primary motivation for NASA's development of the Microwave Sterilizable Access Po [[pf-tek-low-humidity-symptoms-and-remediation]]

### Flight Experiment Access
- Biological experiments aboard spacecraft require sterile handling
- Sample extraction and reagent addition must maintain experimental integrity
- The enclosed spacecraft environment makes traditional sterilization (autoclave, gamma) impractical for in-situ access

## ECLSS on Major Spacecraft

### International Space Station (ISS)
The ISS ECLSS is the most sophisticated life support system ever operated in space:

- **Oxygen generation**: Electrolysis of water using the Oxygen Generation Assembly (OGA)
- **CO₂ removal**: Four-bed molecular sieve (Sabatier reaction also converts CO₂ to methane and water)
- **Water recovery**: Approximately 90% of all water is recovered, including urine (98% recovery from urine alone)
- **Air revitalization**: Trace Contaminant Control System (TCCS) removes volatile organics
- **Temperature control**: Internal Thermal Control System (ITCS) with water-glycol coolant loops

### Space Shuttle
- Less sophisticated than ISS ECLSS
- Used lithium hydroxide canisters for CO₂ removal (consumable, not regenerative)
- Fuel cells provided both electrical power and drinking water as a byproduct
- Limited water recycling capability

### Future Systems (Artemis, Mars Transit)
- Planned closed-loop systems targeting 98%+ water recovery
- Integration of biological waste processing (bioreactors)
- In-situ resource utilization (ISRU) for lunar and Martian water extraction
- Advanced air revitalization using solid amine sorbents

## Microbial Considerations

### Microbial Ecology in Spacecraft
The closed environment of a spacecraft creates a unique microbial ecology:

- **Initial microbiome**: Introduced by crew, cargo, and pre-launch contamination
- **Selection pressure**: Microgravity, radiation, and closed conditions select for adapted organisms
- **Virulence changes**: Some bacteria show increased virulence and antibiotic resistance in spaceflight
- **Biofilm enhancement**: Biofilms form more readily and are often thicker in microgravity

### Common Spacecraft Contaminants
- **Bacteria**: *[[greg-green-water-quality-and-hard-water]] throughout the habitable volume

## Water Quality Standards

Spacecraft drinking water must meet stringent standards equivalent to or exceeding Earth-based potable water regulations:

- **Total organic carbon (TOC)**: < 500 μg/L
- **Conductivity**: < 50 μS/cm
- **pH**: 4.5–8.0
- **Microbial count**: < 50 CFU/mL (total heterotrophic bacteria)
- **Coliform bacteria**: Must be non-detectable
- **Heavy metals**: Below WHO drinking water guideline levels

Water quality is monitored continuously using onboard sensors, with periodic laboratory analysis of returned samples. The water recovery systems on the ISS consistently produce water that meets or exceeds these standards, though taste complaints from crew members are common (the water is described as "medicinal" or "iodine-tasting" due to residual biocides).

## Challenges for Long-Duration Missions

Missions to Mars and beyond will require ECLSS systems far more reliable and autonomous than current ISS systems:

- **Duration**: Mars transit takes 6–9 months each way; total mission may exceed 2 years
- **Resupply delay**: No possibility of emergency resupply; all consumables and spares must be carried or manufactured in-situ
- **Radiation effects**: Long-duration exposure may degrade ECLSS materials, seals, and membranes
- **Reduced gravity**: Lunar (1/6 g) and Martian (1/3 g) environments create different fluid behavior than microgravity, requiring redesign of liquid-gas separation systems
- **Dust exposure**: Lunar regolith and Martian dust pose contamination risks for [[greg-green-odor-control-and-air-filtration]] and water systems

## References

- NASA (2010). "International Space Station Environmental Control and Life Support System Overview." NASA Technical Report.
- Atwater, J.E., Streech, N.D., Garmon, F.C. (1990). "Sterilizing Surfaces by Irradiation with Microwaves." NASA MSC-22484.
