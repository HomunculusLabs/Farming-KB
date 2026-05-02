---
title: Tryptophan Decarboxylase
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [reference]
sources:
  - "raw/papers/growth-promoting-effect-of-a-brassinosteroid-in-mycelial-cultures-of-the-fungus-psilocybe-cubensis-gartz-adam-vorbrodt.md"
---
# Tryptophan Decarboxylase

Tryptophan decarboxylase (TDC) is the enzyme that catalyzes the conversion of the amino acid tryptophan into tryptamine by removing a carboxyl group. This is the critical enzymatic step that bridges primary amino acid metabolism (via the [[shikimate-pathway-in-fungi]]) with the biosynthesis of all tryptamine-derived alkaloids, including [[psilocybin-biosynthesis-pathway]], [[5-meo-dmt-compound-profile]], and the ergot alkaloids. See [[psilocybin-biosynthesis-pathway]] for the complete biosynthetic context and [[fungal-enzymatic-capabilities]] for related fungal enzyme systems.

## Chemical Reaction

```
Tryptophan → Tryptamine + CO2
```

The enzyme removes the alpha-carboxyl group from L-tryptophan, producing tryptamine (an indoleethylamine) and carbon dioxide. This is a pyridoxal phosphate (PLP)-dependent reaction -- the enzyme requires PLP (vitamin B6 derivative) as a cofactor, which is typical of amino acid decarboxylases.

## Enzyme Classification

- **EC Number**: EC 4.1.1.28
- **Type**: Aromatic L-amino acid decarboxylase
- **Cofactor**: Pyridoxal phosphate (PLP, derived from vitamin B6)
- **Location**: Cytosol of fungal cells (where the Shikimate pathway operates)
- **Reaction type**: Decarboxylation (lyase)

## Role in Psilocybin Biosynthesis

In the [[psilocybin-biosynthesis-pathway]], tryptophan decarboxylase occupies the position just after tryptophan is produced from the Shikimate pathway:

1. Glucose → (glycolysis + pentose phosphate pathway) → PEP + E4P
2. PEP + E4P → (Shikimate pathway) → Chorismate → Anthranilate → Tryptophan
3. **Tryptophan → Tryptamine** (tryptophan decarboxylase)
4. Tryptamine → (multiple steps, not fully elucidated) → Norbaeocystin → Baeocystin → Psilocin → Psilocybin

Tryptophan decarboxylase is the **last well-characterized enzyme** in the pathway. The steps from tryptamine to psilocybin involve multiple enzymatic transformations including hydroxylation, methylation, and phosphorylation, but the specific enzymes and their order are still being investigated.

## Inhibition and Regulation

Tryptophan decarboxylase is subject to significant self-feedback downregulation. When too much of a downstream product accumulates in the fungal cells, the enzyme reduces or stops converting tryptophan to tryptamine. This is a natural regulatory mechanism that prevents wasteful overproduction of metabolites.

### Known Inhibitors

Research compiled from the Lycaeum and published sources has identified several compounds that inhibit tryptophan decarboxylase:

| Inhibitor | Type of Inhibition | % Inhibition |
|-----------|-------------------|-------------|
| N,N-dimethyltryptamine (DMT) | Competitive | 65% |
| Indole-3-acetic acid (IAA) | Competitive | 60% |
| Tryptamine | Unknown mechanism | 62% |
| 5-Hydroxytryptamine (serotonin) | Unknown mechanism | 45% |
| Indole-3-acetaldehyde | Unknown mechanism | 50% |

### Non-Inhibitors

Not all tryptamine derivatives inhibit the enzyme:

| Compound | Inhibition |
|----------|-----------|
| 5-Methoxy-N,N-dimethyltryptamine (5-MeO-DMT) | 0% |
| 5-Methoxytryptamine | 0% |
| Indole-3-pyruvic acid | 0% |

The inhibition pattern reveals important structure-activity relationships. Competitive inhibitors like DMT and IAA likely compete with tryptophan for the enzyme's active site. The fact that 5-methoxylated tryptamines (5-MeO-DMT, 5-methoxytryptamine) do not inhibit the enzyme, while the unmethoxylated and hydroxylated analogues do, suggests the enzyme has specific binding requirements.

## Practical Implications for Cultivation

### The Gartz Method

Jochen Gartz demonstrated that adding tryptamine hydrochloride directly to the mushroom-substrates|substrate increases total alkaloid production in [[psilocybe-cubensis-potency-variation-by-flush]]. The added tryptamine feeds directly into the biosynthetic pathway, bypassing the tryptophan decarboxylase bottleneck:

- **Bypassing feedback inhibition**: Exogenous tryptamine is downstream of the regulated step, so the natural feedback mechanism does not limit its conversion to downstream compounds
- **Phosphorylase bottleneck**: However, adding tryptamine reveals that a later step -- the phosphorylation of psilocin to psilocybin -- becomes rate-limiting at higher concentrations
- **Result**: Higher psilocin:psilocybin ratios, suggesting downregulation or saturation of the phosphorylase enzyme
- **Evolutionary insight**: This pattern suggests psilocybin production is naturally maintained at modest levels, possibly because the energetic cost of phosphorylation limits overproduction

### Substrate Optimization

Since tryptophan decarboxylase converts tryptophan (produced via the Shikimate pathway) to tryptamine, factors that affect tryptophan availability indirectly affect alkaloid production:

- Substrates rich in aromatic amino acids or their precursors may support higher alkaloid production
- The Shikimate pathway's upstream regulation (DAHP synthase feedback inhibition) can be a bottleneck
- [[growing-gourmet-tree-species-guide-mushroom-cultivation]] that favor overall metabolic activity may increase flux through the entire pathway

## Distribution Among Fungi

Tryptophan decarboxylase activity has been documented in:

- **Psilocybe species**: P. cubensis, P. tampanensis, P. mexicana, P. semilanceata, P. azurescens, and others
- **Ergot fungi** (Claviceps spp.): Tryptophan decarboxylase feeds into the ergoline alkaloid pathway (leading to ergotamine, lysergic acid, and eventually LSD)
- **Other Basidiomycetes**: Various genera produce tryptamine derivatives as defensive compounds or signaling molecules
- **Plants**: TDC also occurs in plants like Catharanthus roseus (Madagascar periwinkle), where it produces tryptamine precursors for terpenoid indole alkaloids including vinblastine and vincristine (anti-cancer drugs)

## Research History

- The enzyme was first characterized in plants and bacteria before being studied in fungi
- Niels Jensen attempted molecular cloning of tryptophan decarboxylase from *Psilocybe tampanensis*, contributing to the effort to identify all enzymes in the psilocybin biosynthesis pathway
- The 2017-2018 discovery and characterization of the psilocybin biosynthetic gene cluster (PsiM, PsiH, PsiK, PsiD) in Psilocybe species by researchers including Dirk Hoffmeister's group at Friedrich Schiller University Jena represented a major advance -- PsiD encodes an L-tryptophan decarboxylase specific to psilocybin-producing fungi
- The identification of the complete gene cluster has enabled heterologous expression of psilocybin biosynthesis in yeast and bacteria, opening new avenues for [[mushroom-submerged-fermentation-pharmaceutical]]

## See Also

- [[psilocybin-biosynthesis-pathway]] -- Complete pathway from glucose to psilocybin
- [[shikimate-pathway-in-fungi]] -- Upstream pathway producing tryptophan
- [[fungal-enzymatic-capabilities]] -- Broader context of fungal enzyme systems
- [[psilocybin-mushroom-chemistry]] -- Alkaloid profiles across species
- [[mushroom-substrates]] -- How substrate composition affects alkaloid production
