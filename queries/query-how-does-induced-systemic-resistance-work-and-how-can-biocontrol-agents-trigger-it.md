---
title: How Does Induced Systemic Resistance Work and How Can Biocontrol Agents Trigger It
tags: [induced-systemic-resistance, biocontrol, plant-immunity, trichoderma, pgpr, jasmonic-acid, salicylic-acid, ipm]
date: 2026-04-28
updated: 2026-04-28
sources:
  - Pieterse CMJ, Zamioudis C, Berendsen RL, et al. Induced systemic resistance by beneficial microbes. Annual Review of Phytopathology. 2014;52:347-375.
  - Van Wees SCM, Van der Ent S, Pieterse CMJ. Plant immune responses triggered by beneficial microbes. Current Opinion in Plant Biology. 2008;11(4):443-448.
  - Shoresh M, Harman GE, Mastouri F. Induced systemic resistance and plant responses to fungal [[dighton-mycorrhizae-pathogen-biocontrol-interactions|biocontrol agents]]. Annual Review of Phytopathology. 2010;48:21-43.
  - Ryu CM, Farag MA, Hu CH, et al. Bacterial volatiles promote growth in Arabidopsis. Proceedings of the National Academy of Sciences. 2003;100(8):4927-4932.
  - Verhagen BWM, Trotel-Aziz P, Couderchet M, Höfte M, Aziz A. Pseudomonas spp.-[[endophytic-mycorrhizal-induced-systemic-resistance|induced systemic resistance]] to Botrytis cinerea is associated with induction and priming of [[mycorrhiza-induced-resistance-defense-priming|defense responses]] in grapevine. Journal of Experimental Botany. 2010;61(1):249-260.
  - Conrath U, Beckers GJM, Flors V, et al. Priming: getting ready for battle. Molecular Plant-Microbe Interactions. 2006;19(10):1062-1071.
type: query
created: 2026-04-28
---

# How Does Induced Systemic Resistance (ISR) Work and How Can Biocontrol Agents Trigger It

## What is Induced Systemic Resistance?

Induced systemic resistance (ISR) is a plant's enhanced defensive capacity triggered by prior exposure to a beneficial microorganism. Unlike Systemic Acquired Resistance (SAR), which is activated after actual pathogen infection and depends on salicylic acid (SA) signaling, ISR is activated by non-pathogenic rhizobacteria and fungi and primarily depends on jasmonic acid (JA) and ethylene (ET) signaling pathways. A key distinction: ISR does not directly activate defenses — it **primes** the plant to respond faster and stronger when a real pathogen attack occurs.

Think of it as a fire drill. The plant doesn't expend energy maintaining full defensive readiness at all times (which would reduce growth), but when ISR is active, the alarm system is pre-wired to trigger faster when actual danger is detected.

## How ISR Differs from Systemic Acquired Resistance (SAR)

| Feature | ISR | SAR |
|---|---|---|
| **Trigger** | Beneficial rhizosphere microbes (PGPR, Trichoderma, mycorrhizae) | Pathogen infection causing tissue damage and necrosis |
| **Primary hormones** | Jasmonic acid (JA) and ethylene (ET) | Salicylic acid (SA) |
| **Key regulatory protein** | NPR1 (same as SAR, but different signaling upstream) | NPR1 |
| **Defense spectrum** | Effective against necrotrophic fungi, herbivores, some bacteria | Effective against biotrophic pathogens and viruses |
| **Growth cost** | Minimal — priming is metabolically cheap | Moderate — SA accumulation can reduce growth |
| **Transgenerational** | No evidence for inherited priming in most cases | Some evidence in *Arabidopsis* for SAR-derived priming |
| **Speed of onset** | 24–72 hours after root colonization | 48–96 hours after initial infection |

## The Molecular Signaling Cascade

### Step 1: Root Colonization and Microbe Recognition

When a biocontrol agent like *Trichoderma harzianum* or *Pseudomonas fluorescens* colonizes plant roots, the plant detects conserved microbial molecules called microbe-associated molecular patterns (MAMPs):

- **Flagellin** (from bacteria): Detected by FLS2 receptor kinase
- **Lipopolysaccharide (LPS)** (from Gram-negative bacteria): Detected by LORE receptor
- **Chitin fragments** (from fungi): Detected by CERK1/LYK5 receptor complex
- **Ergosterol** (from fungi): Detected by yet-unidentified G-protein-coupled receptors
- **Surfactants and lipopeptides** (from *Bacillus* spp.): Detected by membrane-associated receptors

This recognition is intentionally weak — enough to signal "friend" but not strong enough to trigger a full defense response (which would reject the beneficial organism).

### Step 2: Hormonal Signaling

MAMP recognition activates a cascade that shifts the plant's hormonal balance:

1. **JA biosynthesis is upregulated**: Lipoxygenase (LOX) enzymes convert linolenic acid to 13-HPOT, which is then converted to jasmonic acid through the AOS and AOC enzymes
2. **ET biosynthesis is upregulated**: ACC synthase and ACC oxidase convert S-adenosylmethionine to ethylene
3. **SA pathway is mildly modulated**: NPR1 protein translocates from cytoplasm to nucleus (same as SAR) but through JA/ET signaling rather than SA accumulation
4. **Crosstalk is managed**: The JA and SA pathways are antagonistic — when one is active, it suppresses the other. ISR walks a fine line, activating JA/ET enough to prime defenses without completely suppressing SA-mediated pathogen defenses

### Step 3: Defense Priming

The nuclear translocation of NPR1 is the central event. In the nucleus, NPR1 interacts with TGA transcription factors to alter chromatin structure at defense gene loci. The genes aren't fully activated yet — instead:

- Histone acetylation marks are placed at defense gene promoters (making them ready for rapid transcription)
- RNA polymerase II is pre-recruited but paused
- Transcription factor proteins accumulate in inactive forms

When a pathogen eventually attacks, the primed gene loci are transcribed 2–10× faster than in non-primed plants, and the defense response reaches full intensity within hours rather than days.

## What Biocontrol Agents Trigger ISR?

### Fungal Biocontrol Agents

| Agent | MAMPs/Signals | ISR Effectiveness | Best Against |
|---|---|---|---|
| *Trichoderma harzianum* | Chitin oligomers, xylanase, swollenin | Strong — among the best-studied ISR triggers | *Fusarium*, *Botrytis*, *Rhizoctonia*, leaf pathogens |
| *Trichoderma asperellum* | Chitin, cell wall glycoproteins | Strong — root colonization specialist | Root pathogens, some foliar diseases |
| *Trichoderma virens* | Gliotoxin (at sub-toxic levels), peptaibols | Moderate to strong | Damping-off, soil-borne fungi |
| Arbuscular mycorrhizal fungi | Lipochitooligosaccharides (Myc-LCOs) | Moderate — slower onset than Trichoderma | Root pathogens, herbivores |
| *Pythium oligandrum* | Elicitin-like proteins (POD-1, Oligandrin) | Moderate | *Phytophthora*, *Botrytis* |

### Bacterial Biocontrol Agents

| Agent | MAMPs/Signals | ISR Effectiveness | Best Against |
|---|---|---|---|
| *Pseudomonas fluorescens* WCS417 | Flagellin, lipopeptides (massetolide) | Very strong — model ISR organism | *Fusarium*, *Alternaria*, *Pseudomonas syringae* |
| *Bacillus subtilis* FB17 | Surfactin, fengycin, iturin lipopeptides | Strong — also produces VOCs | Damping-off, foliar pathogens |
| *Bacillus amyloliquefaciens* | Surfactin, bacillomycin D | Strong | *Rhizoctonia*, *Fusarium*, leaf spot diseases |
| *Bacillus velezensis* | Iturin, fengycin, bacillaene | Strong — broad-spectrum ISR | Multiple pathogens and herbivores |
| *Serratia marcescens* | Chitinase, prodigiosin | Moderate | Soil-borne fungi, some insects |

### Volatile-Mediated ISR

Some biocontrol agents trigger ISR without physical contact, through volatile organic compounds (VOCs):

- **2,3-butanediol** (from *Bacillus subtilis* and *Pseudomonas chlororaphis*): Triggers ISR through airborne signals; effective across chamber-divided experiments
- **Acetoin** (from *Bacillus* spp.): Similar ISR-triggering capacity to 2,3-butanediol
- **6-Pentyl-α-pyrone** (from *Trichoderma* spp.): Coconut-scented VOC with both direct antifungal and ISR-inducing properties

VOC-mediated ISR is particularly relevant for greenhouse production, where enclosed environments allow volatile accumulation.

## Practical Application Guide

### For Trichoderma-Based ISR

1. **Apply early**: ISR requires 5–14 days of root colonization before the plant is fully primed. Apply at seeding or transplanting, not after disease symptoms appear
2. **Use adequate inoculum**: 10⁶–10⁸ CFU/g for soil applications; insufficient colonization fails to trigger ISR
3. **Minimize fungicide use**: Most fungicides kill or suppress Trichoderma before ISR can be established. If fungicides are necessary, apply Trichoderma first and allow 2+ weeks before any chemical treatment
4. **Support root health**: Healthy roots = more colonization surface = stronger ISR. Ensure adequate aeration, moderate moisture, and balanced nutrition (especially calcium and silicon, which strengthen cell walls for the primed defenses to work with)

### For PGPR-Based ISR

1. **Combine strains**: *Pseudomonas* + *Bacillus* combinations often provide stronger ISR than single-strain applications, as they produce complementary MAMPs
2. **Use seed treatment**: Seed coating with PGPR ensures the bacteria are present at the earliest root emergence, maximizing colonization time
3. **Add carbon sources**: Drenching with a dilute molasses or humic acid solution after PGPR application feeds the bacteria and extends rhizosphere persistence from days to weeks
4. **Avoid excessive nitrogen**: High ammonium fertilization suppresses ISR by disrupting JA signaling. Moderate N rates and preference for nitrate over ammonium support ISR priming

### Monitoring ISR Activation

There is no simple field test for ISR status, but these indicators suggest successful priming:

- **Gene expression markers** (lab test): Elevated PR-1, PDF1.2, and VSP2 transcript levels in leaf tissue, detectable by qPCR 7–14 days after inoculation
- **Enhanced callose deposition** (lab test): Stronger callose response to flg22 peptide treatment in leaf tissue samples
- **Field observation**: Inoculated plants show less disease severity than uninoculated controls when both are exposed to the same pathogen pressure, even though the biocontrol agent may never contact the foliar pathogen directly

## Frequently Asked Questions

**Does ISR protect against all diseases?**

No. ISR primarily enhances defense against **necrotrophic fungi** (*Botrytis*, *Alternaria*, *Sclerotinia*), some **bacterial pathogens**, and **chewing herbivores**. It is generally less effective against biotrophic pathogens (*powdery mildew*, *downy mildew*, rusts) and viruses, which are better controlled through SA-dependent SAR.

**Can I over-apply biocontrol agents?**

Yes. Excessive colonization can trigger a full MAMP-triggered immunity (MTI) response instead of the mild recognition needed for ISR. This causes growth reduction and may paradoxically make plants more susceptible to pathogens that exploit JA/ET signaling. Follow product label rates and avoid combining multiple ISR inducers at full rates simultaneously.

**How long does ISR last?**

Priming typically persists for 2–6 weeks after the initial colonization event. In annual crops, a single early application may not protect through the entire growing season. Booster applications every 3–4 weeks are recommended for long-season crops. In perennials, established root colonization provides more sustained ISR.

**Is ISR compatible with chemical disease control?**

Partially. Systemic acquired resistance activators like acibenzolar-S-methyl (Actigard) can synergize with biocontrol ISR, but their SA-dependent pathway may antagonize JA/ET-dependent ISR if applied simultaneously. Space applications by at least 7 days. Copper-based and sulfur-based fungicides are the most compatible with ISR-active biocontrol programs.

**Does ISR reduce yield?**

Unlike constitutive defense activation, properly induced ISR through biocontrol agents typically does not reduce yield and may even increase it by 5–15%. The priming mechanism is metabolically inexpensive — the plant only invests in full defense when a real pathogen is detected. However, poorly calibrated applications (excessive inoculum, multiple simultaneous ISR inducers) can cause growth penalties.
