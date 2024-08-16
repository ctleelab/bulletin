---
layout: paper
title: 'Independent Markov Decomposition: Towards modeling kinetics of biomolecular complexes'
authors: 'T. Hempel, M. J. Razo<sup>*</sup>, C. T. Lee<sup>*</sup>, B. C. Taylor<sup>*</sup>, R. E. Amaro<sup>$</sup>, and F. Noé<sup>$</sup>'

journal: 'Proc. Natl. Acad. Sci.'
doi: 10.1073/pnas.2105230118
shortcite: Hempel et al., 2021 Proc. Natl. Acad. Sci.
citation: '118.31 (July 2021)'

image: hempel-independent-msm.png
pdf: 
supplement: 

biorxiv: 10.1101/2021.03.24.436806
arxiv: 
chemrxiv: 

github: 
zenodo: 

date: 2021-07-28

status: 
inprep: False
---

# Abstract

To advance the mission of in silico cell biology, modeling the interactions of large and complex biological systems becomes increasingly relevant. The combination of molecular dynamics (MD) simulations and Markov state models (MSMs) has enabled the construction of simplified models of molecular kinetics on long timescales. Despite its success, this approach is inherently limited by the size of the molecular system. With increasing size of macromolecular complexes, the number of independent or weakly coupled subsystems increases, and the number of global system states increases exponentially, making the sampling of all distinct global states unfeasible. In this work, we present a technique called independent Markov decomposition (IMD) that leverages weak coupling between subsystems to compute a global kinetic model without requiring the sampling of all combinatorial states of subsystems. We give a theoretical basis for IMD and propose an approach for finding and validating such a decomposition. Using empirical few-state MSMs of ion channel models that are well established in electrophysiology, we demonstrate that IMD models can reproduce experimental conductance measurements with a major reduction in sampling compared with a standard MSM approach. We further show how to find the optimal partition of all-atom protein simulations into weakly coupled subunits.
