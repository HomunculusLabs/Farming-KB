---
title: "Plant Immune System: PTI and ETI"
created: 2026-04-28
updated: 2026-05-06
aliases: [plant immunity, pattern-triggered immunity, effector-triggered immunity, zig-zag model, plant defense]
tags: [plant-science, plant-pathology, immunology, agriculture, crop-protection, molecular-biology]
type: concept
sources:
  sources: []
---

Plants lack an adaptive immune system (no antibodies or T-cells) and instead rely on a sophisticated two-tiered innate immune system to detect and respond to pathogens. This system was formalized by Jones and Dangl in 2006 as the **zig-zag model** of plant-pathogen coevolution. The two tiers are **Pattern-Triggered Immunity (PTI)** — a broad-spectrum basal defense activated by membrane-localized receptors — and **Effector-Triggered Immunity (ETI)** — a stronger, more specific defense triggered by intracellular receptors that detect pathogen [[fungal-virulence-factors-host-immune-evasion]]. Recent work has shown PTI and ETI are not independent but form a mutual amplification loop, with NLR activation enhancing PRR signaling components.

## Pattern-Triggered Immunity (PTI)

PTI is activated when **Pattern Recognition Receptors (PRRs)** detect conserved microbial signatures called **PAMPs/MAMPs** (Pathogen/Microbe-Associated Molecular Patterns) or host-derived **DAMPs** (Damage-Associated Molecular Patterns). PAMPs are evolutionarily ancient molecules essential for microbial fitness, making them difficult for pathogens to alter without cost.

Key PAMPs include flagellin (detected by FLS2), bacterial EF-Tu (detected by EFR), fungal chitin (detected by the LYK5-CERK1 LysM receptor complex), and peptidoglycan. Important DAMPs include oligogalacturonides from cell wall degradation (detected by WAK1), extracellular ATP (detected by P2K1/DORN1), and endogenous Pep peptides (detected by PEPR1/PEPR2). The rice XA21 receptor detects the Ax21 peptide from Xanthomonas bacteria.

PRRs are typically **Receptor-Like Kinases (RLKs)** with extracellular ligand-binding domains, transmembrane regions, and intracellular kinase domains, or **Receptor-Like Proteins (RLPs)** that lack kinase domains. RLPs like Cf-4 and Cf-9 in tomato require the adaptor SOBIR1 and co-receptor BAK1 for signaling. Most LRR-RLK PRRs require the co-receptor **BAK1/SERK3** (part of the SERK1-5 family), which forms ligand-induced heterodimers with the PRR.

Upon ligand binding, BAK1 transphosphorylates the PRR and recruits **BIK1** (Botrytis-Induced Kinase 1) and related PBL kinases. BIK1 is phosphorylated, dissociates from the complex, and phosphorylates downstream targets including RBOHD (for ROS burst), calcium channels, and other signaling components. The PRR-BAK1-BIK1 module is the core initiation complex for PTI signaling.

## Early PTI Signaling

Within seconds to minutes of PAMP detection, multiple parallel signaling cascades activate. **Calcium influx** occurs through CNGC2/CNGC4 cyclic nucleotide-gated channels, raising cytosolic Ca2+ concentration. This activates calmodulin, calcium-dependent protein kinases (CDPKs/CPKs), and CBL-CIPK complexes. The calcium signal is decoded by specific CML (calmodulin-like) proteins.

A **reactive oxygen species (ROS) burst** is produced by RBOHD (Respiratory Burst Oxidase Homolog D), an NADPH oxidase activated by BIK1 phosphorylation and Ca2+-dependent CDPK phosphorylation. Apoplastic ROS (primarily H2O2 and superoxide) serve as direct antimicrobials, cell wall cross-linking agents (via peroxidases), and secondary signaling molecules that amplify defense responses.

Ion fluxes accompany these events: K+ and Cl- efflux, Ca2+ and H+ influx, and extracellular alkalization. **MAPK cascades** activate within 5-30 minutes, primarily MEKK1 to MKK4/MKK5 to MPK3/MPK6, phosphorylating WRKY transcription factors (WRKY22, WRKY29, WRKY33) that regulate defense gene expression. MPK4 normally negatively regulates defense; its inactivation releases SUMM2-mediated surveillance.

Physical defenses follow: callose (beta-1,3-glucan) is deposited at cell walls as papillae via PMR4/GSL5 callose synthase, attempting to physically block pathogen entry. Cell wall proteins are cross-linked by peroxidases using ROS, and lignin deposition reinforces cell walls at infection sites.

## Hormone Biosynthesis and Defense Gene Activation

PTI initiates **salicylic acid (SA)** biosynthesis via the isochorismate pathway (catalyzed by ICS1/SID2 in chloroplasts) and activates jasmonic acid (JA) and ethylene (ET) pathways. CAMTA transcription factors regulate early SA-related gene expression. Hundreds to thousands of defense genes are activated, regulated by WRKY, MYB, bZIP/TGA, ERF, and NAC transcription factor families.

Defense outputs include antimicrobial peptides (defensins, thionins), Pathogenesis-Related (PR) proteins (PR1 antifungal, PR2 glucanase, PR5 thaumatin-like), cell wall reinforcement enzymes, and phytoalexin biosynthesis (e.g., camalexin in Arabidopsis). SA is primarily effective against biotrophic pathogens that require living tissue, while JA/ET defend against necrotrophs and herbivores.

## Effectors and the Zig-Zag Model

Pathogens deliver **effectors** into the plant apoplast or cytoplasm to suppress PTI and facilitate infection, creating 'Effector-Triggered Susceptibility' (ETS). Apoplastic effectors (e.g., fungal Avr2, bacterial AvrPto) target extracellular components, while cytoplasmic effectors (delivered via type III secretion systems in bacteria or haustoria in fungi/oomycetes) target intracellular signaling.

Key PTI-suppressing effectors include AvrPto and AvrPtoB (targeting FLS2, BAK1, BIK1, and RBOHD; AvrPtoB also has E3 ubiquitin ligase activity), HopAI1 (dephosphorylating MAPKs), HopF2 (ADP-ribosylating MAPKKs), and coronatine (a JA-Ile mimic that activates JA signaling to suppress SA via cross-talk). Pathogens also mask PAMPs through glycosylation or sequence diversification.

The zig-zag model describes four phases of coevolution: PTI activates basal defense; pathogens deploy effectors causing ETS; plants evolve NLR receptors that detect effectors (triggering ETI); pathogens lose or mutate recognized effectors, potentially restoring PTI effectiveness. This creates an evolutionary arms race driving diversity at both interfaces.

## Effector-Triggered Immunity (ETI)

## The Gene-for-Gene Hypothesis

The gene-for-gene hypothesis, proposed by Harold Flor in 1971 based on flax-rust interactions, predates the zig-zag model. It states that for each **avirulence (Avr) gene** in the pathogen, there is a corresponding **resistance (R) gene** in the host plant. If the plant possesses the R gene and the pathogen possesses the matching Avr gene, the result is resistance; if either is absent, the result is susceptibility. This was the foundational model for understanding plant-pathogen specificity and was molecularly explained by NLR-effector recognition. Flor's work established the [[holmgren-permaculture-flower-conceptual-framework]] for breeding disease-resistant cultivars and understanding pathogen [[aspergillus-fumigatus-population-genetics]].

ETI is triggered when intracellular **NLR receptors** (Nucleotide-binding Leucine-rich Repeat proteins, NB-LRR) detect pathogen effectors. NLRs are classified as **CNLs** (coiled-coil N-terminal domain, e.g., ZAR1, RPM1, RPS2, RPS5) and **TNLs** (TIR N-terminal domain, e.g., RPS4, RPS6, N). TNL TIR domains possess NADase activity, hydrolyzing NAD+ to produce v-cADPR and ADPR signaling molecules.

**RNL helper NLRs** (NRG1, ADR1) with RPW8-like domains function as downstream signaling hubs, particularly for TNLs, forming their own oligomeric complexes. NLRs exist in an ADP-bound OFF state; effector detection triggers ADP/ATP exchange, conformational change, and oligomerization. Recognition modes include direct binding (RPS5-AvrPphB), the guardee model (RPM1/RPS2 guarding RIN4), and the decoy model (RRS1 with integrated WRKY domain).

## The ZAR1 Resistosome

The **ZAR1 resistosome**, solved by Wang et al. (2019), was the first plant NLR structure demonstrated to function as an ion channel. In resting state, the ZAR1-RKS1 complex is inactive with ADP bound. Pathogen effectors HopZ1a (acetyltransferase) or AvrAC (uridylyltransferase) modify host proteins PBL2 or RIN4. Modified PBL2UMP is recognized by the RKS1-ZAR1 complex, triggering ADP/ATP exchange.

Five activated subunits oligomerize into a **pentameric wheel-like complex** (~2 MDa). The N-terminal alpha-helices restructure into a funnel that inserts into the plasma membrane, forming a **Ca2+-permeable cation channel** — the first demonstrated channel activity for any NLR. Calcium influx triggers downstream defense signaling, ROS production, and cell death. Additional solved resistosomes include the ROQ1 tetramer (TNL) and Sr33 pentamer (wheat stem rust NLR).

## Hypersensitive Response and Programmed Cell Death

ETI typically culminates in the **hypersensitive response (HR)** — rapid, localized PCD at infection sites that deprives biotrophic pathogens of living tissue. HR morphology includes membrane integrity loss, chromatin condensation, DNA laddering, cytoplasmic shrinkage, and vacuole rupture. ROS (H2O2) and nitric oxide (NO) serve as both signals and executors of PCD.

Key HR regulators include RNL helper NLRs (essential for execution), the EDS1-PAD4/SAG101 modules (central TNL signaling hubs), metacaspases (AtMC1 promotes PCD, AtMC2 inhibits it), vacuolar processing enzymes (VPEs), cathepsin B proteases, and LOX1. The negative regulator LSD1 (zinc finger protein) prevents uncontrolled cell death spread. Lesion-mimic mutants (acd2, lsd1) demonstrate the consequences of deregulated HR.

## EDS1 Signaling Hubs

**EDS1** (Enhanced Disease Susceptibility 1) is a central signaling hub downstream of TNL activation. EDS1 forms heterodimers with different partners that channel signaling into distinct outputs. The **EDS1-PAD4** complex amplifies SA production and promotes defense gene expression, while the **EDS1-SAG101** complex partners with **NRG1** helper NLRs to execute cell death. NDR1 (Non-race-specific Disease Resistance 1) serves an analogous role for many CNL-mediated responses. Together, these hubs ensure that TNL and CNL activation produces appropriate immune outputs ranging from defense gene activation to localized cell death. EDS1 signaling is essential for TNL-mediated resistance but is also recruited by some CNLs under specific conditions, highlighting the interconnectedness of plant immune signaling networks.

## Systemic Acquired Resistance (SAR)

SAR is a whole-plant, long-lasting defense activated after localized infection, effective primarily against biotrophs and lasting weeks to months. It requires **salicylic acid** signaling and is regulated by **NPR1** (Nonexpressor of PR Genes 1), the master regulator of SA-mediated defense. NPR1 contains an N-terminal BTB/POZ domain, central NPR1-like domain, and C-terminal ankyrin repeats.

In uninfected plants, NPR1 exists as disulfide-bonded oligomers in the cytoplasm. SA accumulation induces thioredoxin (TRX-h5) to reduce disulfide bonds, producing monomers that translocate to the nucleus. Nuclear NPR1 interacts with TGA transcription factors (TGA2, TGA3, TGA5, TGA6, TGA7) via ankyrin repeats, recruiting chromatin remodeling complexes (MED21, GCN5/ADA2b) to activate PR gene expression.

NPR1 turnover is controlled by CUL3-based E3 ligase with NPR3/NPR4 as SA-dependent substrate adaptors — NPR3 degrades NPR1 at high SA levels (preventing over-activation), NPR4 at low SA (maintaining basal turnover). This dual-receptor system creates a SA concentration-dependent switch. NPR3 and NPR4 also function as direct SA receptors.

Mobile SAR signals travel through the phloem to uninfected tissues. The strongest candidate is **N-hydroxypipecolic acid (NHP)**, derived from L-lysine via ALD1 to pipecolic acid to FMO1 hydroxylation. NHP accumulates systemically and can induce SAR without prior infection, partly by amplifying SA biosynthesis through positive feedback on ICS1. Other signals include MeSA (methyl salicylate, [[integrated-pest-management]] — practical pest management framework combining biological, cultural, and chemical approaches
- [[rhizosphere-ecology]] — root zone [[edaphic-factors-microbial-community-structure]] dynamics and plant-microbe interactions
- systemic acquired resistance — detailed SAR [[plant-signaling-pathways]] and agricultural deployment
- [[plant-defense-mechanisms]] — overview of constitutive and induced plant defenses including physical barriers and [[antifungal-secondary-metabolites-coprophilous-fungi]]
