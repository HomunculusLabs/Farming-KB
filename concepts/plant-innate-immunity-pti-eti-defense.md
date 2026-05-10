---
title: Plant Innate Immunity: Pattern-Triggered and Effector-Triggered Defense
category: plant-science
source: general-knowledge
mined: 2026-05-10
tags: [plant-immunity, pti, eti, pattern-recognition-receptor, effector, plant-defense, plant-pathogen-interaction, systemic-acquired-resistance, induced-systemic-resistance]
aliases: [plant-immune-system, zipper-model, guard-hypothesis, plant-disease-resistance, pamp-triggered-immunity]
---

# Plant Innate Immunity: Pattern-Triggered and Effector-Triggered Defense

## Overview

Plants lack an adaptive immune system with antibodies and memory cells. Instead, they rely on a sophisticated innate immune system consisting of two layers of receptor-mediated defense: pattern-triggered immunity (PTI) and effector-triggered immunity (ETI). This two-tiered system, described by the zigzag model, enables plants to detect and respond to the vast majority of potential pathogens.

## The Zigzag Model

The zigzag model (Jones and Dangl, 2006) provides a framework for understanding plant-pathogen co-evolution:

1. **Phase 1 — PTI**: Plants detect pathogen-associated molecular patterns (PAMPs) via pattern recognition receptors (PRRs), activating basal defense.
2. **Phase 2 — ETS**: Successful pathogens deliver effector proteins that suppress PTI, causing effector-triggered susceptibility (ETS).
3. **Phase 3 — ETI**: Plants evolve resistance (R) proteins that detect specific effectors (directly or indirectly), activating strong defense.
4. **Phase 4 — ETS2**: Pathogens evolve new effectors or modify existing ones to evade detection by R proteins.

This evolutionary arms race drives diversification in both plant resistance genes and pathogen effector repertoires.

## Pattern-Triggered Immunity (PTI)

### Pathogen-Associated Molecular Patterns (PAMPs)

PAMPs (also called MAMPs — microbe-associated molecular patterns) are conserved molecular signatures essential for microbial survival:

- **Flagellin**: The protein subunit of bacterial flagella. The conserved N-terminal 22-amino-acid peptide (flg22) is the most widely studied PAMP.
- **EF-Tu**: Bacterial elongation factor thermo-unstable. The elf18 peptide is recognized in many plant species.
- **Chitin**: A structural polysaccharide in fungal cell walls. Chitin oligomers trigger defense in most plants.
- **Lipopolysaccharides (LPS)**: Components of Gram-negative bacterial outer membranes.
- **Peptidoglycan**: Bacterial cell wall polymer.
- **β-glucans**: Structural components of oomycete cell walls.
- **Cold shock proteins**: Bacterial proteins detected by some plant species.
- **Damage-associated molecular patterns (DAMPs)**: Plant-derived molecules released during tissue damage, including:
  - Oligogalacturonides (OGs): Fragments of plant cell wall pectin.
  - Extracellular ATP: Released from damaged plant cells.
  - Systemin: An 18-amino-acid peptide hormone in tomato.
  - Cutin monomers: Released from the plant cuticle during fungal penetration.

### Pattern Recognition Receptors (PRRs)

PRRs are typically transmembrane receptor-like kinases (RLKs) or receptor-like proteins (RLPs):

- **FLS2**: Recognizes flg22. The best-characterized PRR, found in Arabidopsis and many crop species.
- **EFR**: Recognizes elf18. Present in Brassicaceae but absent from many monocots (including rice).
- **CERK1/LYK5**: Recognizes chitin. LYK5 has higher affinity; CERK1 acts as a co-receptor.
- **PEPR1/PEPR2**: Recognizes the DAMP AtPep1 and related peptides.
- **RLP23**: Recognizes nlp20, a necrosis-inducing protein motif from fungi and oomycetes.
- **XA21**: Recognizes a sulfated peptide from Xanthomonas (axYs22). An important RLP in rice bacterial blight resistance.

### PRR Structure and Activation

Most PRRs have three domains:
- An extracellular domain that binds the PAMP (leucine-rich repeat or lysin-motif domains).
- A transmembrane domain that anchors the receptor.
- An intracellular kinase domain that initiates signaling.

Upon PAMP binding, PRRs form complexes with co-receptors (e.g., BAK1/SERK3 for FLS2 and EFR). This triggers:
- Rapid receptor phosphorylation
- Recruitment of downstream signaling components
- Activation of a MAP kinase cascade
- Calcium influx and [[reactive-oxygen-species-and-oxidative-stress]] (ROS) production

### PTI Defense Responses

- **ROS burst**: NADPH oxidase (RBOHD) produces superoxide within minutes, converted to [[cervantes-hydrogen-peroxide-sterilization]]. ROS serve as antimicrobial agents and signaling molecules.
- **Callose deposition**: Callose (β-1,3-glucan) is deposited at the cell wall and in papillae at attempted penetration sites, physically blocking pathogen entry.
- **Cell wall fortification**: Lignin and suberin deposition strengthens cell walls.
- **Antimicrobial compound production**: Phytoalexins, defensins, and thionins are synthesized de novo.
- **Pathogenesis-related (PR) proteins**: Chitinases, glucanases, and other hydrolytic enzymes degrade pathogen structures.
- **Stomatal closure**: Many bacterial pathogens enter through stomata; PTI triggers abscisic acid-mediated stomatal closure to limit entry.
- **Transcriptional reprogramming**: Hundreds of defense-related genes are upregulated within hours.

## Effector-Triggered Immunity (ETI)

### Pathogen Effectors

Effectors are proteins (and some small molecules) delivered into plant cells to suppress immunity and facilitate infection:

- **Bacterial effectors**: Delivered through the Type III secretion system (T3SS) directly into the plant cytoplasm. Examples: AvrPto, AvrRpt2, AvrRpm1 (Pseudomonas syringae).
- **Fungal effectors**: Secreted into the apoplast or delivered into host cells via haustoria. Examples: Avr3a ([[bloomfield-potato-blight-phytophthora-infestans]]), AvrPm3 ([[blumeria-graminis]]).
- **Oomycete effectors**: Similar to fungal effectors; RXLR and CRN effectors are translocated into host cells.

Effector functions include:
- Suppressing PRR signaling (e.g., AvrPtoB targets FLS2 for degradation)
- Interfering with MAP kinase cascades
- Disrupting hormone signaling
- Inhibiting protease activity
- Modulating host transcription
- Suppressing cell death responses

### Resistance (R) Proteins

R proteins are intracellular receptors (mostly NLRs — nucleotide-binding leucine-rich repeat proteins) that detect effectors:

- **Direct recognition**: The R protein physically binds the effector (gene-for-gene relationship). Example: RPS5 detects AvrPphB.
- **Indirect recognition (guard model)**: The R protein monitors a host target (guardee) that is modified by the effector. Example: RIN4 is guarded by both RPS2 and RPM1.
- **Integrated decoy model**: Some R proteins have integrated domains that mimic effector targets, acting as decoys.

### ETI Defense Responses

ETI is an amplified version of PTI with additional features:
- **Hypersensitive response (HR)**: Programmed cell death at the infection site, depriving biotrophic pathogens of living tissue.
- **Stronger and more sustained ROS burst**: Higher amplitude and longer duration than PTI.
- **Systemic acquired resistance (SAR)**: Salicylic acid-dependent long-distance signaling that primes distal tissues for enhanced defense.
- **Priming**: ETI creates a primed state in which defense responses are activated more rapidly and strongly upon subsequent challenge.

## Hormonal Signaling in Plant Immunity

Defense hormones interact synergistically and antagonistically:

- **Salicylic acid (SA)**: Primarily effective against biotrophic pathogens. Drives systemic acquired resistance. Accumulates during ETI.
- **Jasmonic acid (JA)**: Primarily effective against necrotrophic pathogens and herbivorous insects. Often antagonistic to SA signaling.
- **Ethylene (ET)**: Often works with JA against necrotrophs. Involved in defense gene regulation.
- **Abscisic acid (ABA)**: Regulates stomatal closure and drought responses. Can antagonize SA/JA signaling.
- **Systemin**: An 18-amino-acid peptide in Solanaceae that activates JA signaling in response to herbivory.

## Induced Systemic Resistance (ISR)

ISR is a rhizobacteria-mediated [[mycorrhiza-induced-resistance-defense-priming]] mechanism:
- Triggered by plant growth-promoting rhizobacteria (PGPR), particularly *Pseudomonas* and *Bacillus* species.
- Unlike SAR, ISR depends on JA and ET signaling rather than SA.
- Does not typically involve direct PR gene activation; instead, primes the plant for faster/stronger defense upon pathogen attack.
- Can be combined with SAR for additive protection.
- Mycorrhizal fungi can also induce systemic resistance through similar pathways.

## Agricultural Applications

- **R gene deployment**: Breeding crops with effective R genes, often pyramided for durability.
- **PRR engineering**: Transferring PRRs between species (e.g., expressing EFR in rice or tomato) to broaden recognition capabilities.
- **[[fukuoka-textdoc-arrowhead-scale-ladybug-biological-control]]**: PGPR-based inoculants that trigger ISR.
- **Defense priming agents**: Chemical and biological agents (e.g., chitosan, BABA, silicon) that prime plant defenses.
- **Marker-assisted selection**: Breeding for broad-spectrum disease resistance using genetic markers linked to immune genes.

## See Also

- [[endophytic-mycorrhizal-induced-systemic-resistance]]
- [[powdery-mildew-cannabis]]
- [[cervantes-powdery-mildew-prevention-treatment]]
- [[pgpr-mycorrhizal-inoculants-microplant-establishment]]
