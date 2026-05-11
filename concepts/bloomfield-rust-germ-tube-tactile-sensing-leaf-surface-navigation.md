---
title: Rust Germ Tube Tactile Sensing and ingham-leaf-surface-biology-exudates Navigation
created: 2026-04-28
tags:
  - mycology
  - rust-fungi
  - puccinia
  - tactile-sensing
  - plant-pathology
  - germ-tube
  - mechanosensation
  - plant-immunity
date: 2026-04-28
updated: 2026-04-28
sources:
  - Mr. Bloomfield's Orchard: The Mysterious World of Mushrooms, Molds, and Mycologists (Nicholas P. Money, 2002), Chapter 9, pp. 169-177
type: concept
---

# Rust Germ Tube Tactile Sensing and Leaf Surface Navigation

[[biodiversity-rust-fungi-urediniomycetes]] of the genus Puccinia are among the most destructive plant [[fungal-pathogens-in-agriculture]]. Black stem rust of wheat (Puccinia graminis) has caused crop losses of staggering proportions throughout history, and the ongoing evolutionary arms race between rust fungi and their cereal hosts drives one of the most intensively studied pathogen-plant interactions in biology. A remarkable aspect of rust infection is the ability of the microscopic germ tube — the first hypha emerging from a germinating spore — to navigate the complex topography of a leaf surface and locate stomatal pores using tactile sensing alone.

## The Infection Challenge

To infect a healthy wheat plant, a rust uredospore must accomplish a multi-step process with extraordinary precision:

1. **Germination**: The spore germinates on the waxy leaf surface, typically in the morning when humidity is highest and stomata are open. The plant closes its stomata later as air temperature rises.
2. **Surface navigation**: The germ tube must locate a stoma (stomatal pore) among the microscopic landscape of epidermal cells.
3. **Recognition and appressorium formation**: Upon detecting the stoma, the germ tube inflates over the opening and plunges into the moist interior of the leaf.

The challenge is formidable. The leaf surface is a microscopic terrain of hills and valleys formed by epidermal cell boundaries, with stomata distributed along only some of the cell files — as few as one in five or even fewer parallel rows of epidermal cells contain stomata. A germ tube that simply grew along the first valley it encountered might never find an opening.

## Leaf Surface Topography

The cereal leaf surface presents two scales of topographic features:

- **Major ridges**: Perceptible to human touch when drawing the leaf blade between finger and thumb, these mark the positions of underlying veins that transport water and nutrients through the leaf.
- **Microscopic ridges**: Created by the undulating files of epidermal cells, these form parallel rows of hills and valleys at a scale measured in micrometers.

The stomatal lips — the raised guard cells bordering each pore — project less than 0.5 µm above the leaf surface. For scale, a stray bacterium is taller than this feature. Yet the rust germ tube can detect these minuscule elevations and distinguish them from the broader topography of the epidermal cell boundaries.

## Harvey Hoch's Surface Recognition Experiments

**Harvey Hoch**, a plant pathologist at Cornell University, conducted a series of elegant experiments that demonstrated the [[bloomfield-rust-fungus-life-cycles-puccinia-haustoria-spermatia]]'s ability to locate stomata using purely physical cues. His work stands as a model of creative [[lightproof-cap-experimental-design-phototropism]] in plant pathology.

### Plastic Leaf Replicas

Hoch fabricated plastic replicas of leaf surfaces using the actual surfaces of cereal leaves as molds. When rust uredospores were germinated on these artificial surfaces, the germ tubes recognized and swelled over the model stomata. This was a critical finding because it proved the fungus could find its entry point using physical topography alone, without needing to detect gas flux through the stomata or any other chemical signal emanating from the pore.

### Defined Ridge Experiments

Hoch went further by manufacturing films with microscopic ridges of precisely controlled height. On these counterfeit landscapes, the rust germ tubes recognized ridges matching the height of stomatal lips (approximately 0.5 µm) but crawled indiscriminately over lower or higher ridges. This demonstrated that the fungus possesses a calibrated tactile sensor tuned to a specific topographic feature size — a biological micrometer capable of measuring features smaller than many bacteria.

### Fungal Mazes

Once he understood the physical features that rusts use to negotiate leaf surfaces, Hoch manufactured microscopic mazes for his fungi — circuits for which he could predict the growth pattern before seeding the surface with spores. This extraordinary experimental system allowed him to direct germ tube growth along predetermined paths simply by engineering the topographic landscape, providing unprecedented control over fungal behavior.

## The Navigation Strategy

The germ tube's search strategy is a cross-pollination pattern that maximizes the probability of encountering stomata:

1. The germ tube germinates and begins extending across the leaf surface.
2. When it encounters a valley formed by the junction between epidermal cells, it recognizes this as a potential navigation path.
3. Rather than growing along the valley (which might not contain stomata), it grows across the leaf, traversing the parallel hills and descending into intervening valleys.
4. This perpendicular crossing strategy ensures the germ tube samples multiple cell files, maximizing the probability of encountering one that contains stomata.

By growing across the leaf rather than along it, the germling is far more likely to find a stoma. The strategy is analogous to a person searching for a door in a long hallway by walking perpendicular to the walls rather than following them. Only one of every six or seven parallel files of leaf cells typically contains stomata, so the cross-cutting approach provides a substantial statistical advantage.

## Cellular Mechanisms: Stretch-Activated Calcium Channels

The molecular mechanisms underlying the rust fungus's tactile perception are not fully elucidated, but current understanding points to **stretch-activated calcium channels** in the fungal [[plant-cell-membrane-transport-proteins-channels-carriers-and-pumps]]. These transmembrane proteins likely function as follows:

1. As the germ tube hypha forces itself up and over a ridge, the membrane at the contact point is stretched.
2. This mechanical deformation causes the channel proteins to open.
3. Calcium ions flood into the cell from the external medium.
4. The calcium surge triggers a cascade of intracellular biochemical reactions that "inform" the fungus about the size and nature of the topographic feature it has encountered.
5. When the calcium signature matches that produced by a 0.5 µm ridge (stomatal lip height), the fungus initiates appressorium formation over the stoma.

### Parallels with Human Touch

These fungal mechanosensory mechanisms are directly related to the processes underlying human tactile sensation. Stretch-activated channels in the nerve cells of human fingertips open and close as fingers run over a surface, generating nerve impulses that signal contact with objects — including the varicose leaf veins detectable to human touch. However, human and fungal tactile sensitivity are tuned to fundamentally different needs. Humans cannot feel epidermal hills or stomatal lips — there would be no evolutionary advantage to such fine-scale perception. Human nerve endings are spaced far more widely than stomata, and the noise from fingerprints obscures any signal at that scale. On a molecular level, the [[woronin-bodies-septal-pore-plugging-fungal-hypha]]'s contact with the leaf is more intimate than any contact a human finger can make.

## Robby Roberson's Fungal Circuits

**Robby Roberson**, working at Arizona State University, extended Hoch's methods to exert even finer control over [[brassinosteroid-fungal-growth-promotion]] patterns. Using manufactured surfaces with defined topographic features, he directed the growth of rust mycelia along specific pathways. Onc mycelium lium had developed along a prescribed route, he passed electrical currents through the hyphae, exploring the possibility of creating a biochip — a living, breathing fungal computer. While this research was largely exploratory, it demonstrated the remarkable controllability of fungal growth using physical surface cues.

## The Arms Race: Rust vs. Wheat

Following successful entry through a stoma, successive rounds of mycelial proliferation within the plant lead to pustule formation and massive uredospore production. This stage of the [[agaricus-campestris-biology-and-life-cycle]] functions like a photocopier, cloning the fungus as immense numbers of spores that can blanket entire fields after a single wind gust. With permissive winds, spores travel hundreds of miles, enabling one infected crop to spawn an epidemic.
