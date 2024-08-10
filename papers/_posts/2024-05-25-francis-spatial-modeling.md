---
layout: paper
title: 'Spatial Modeling Algorithms for Reactions and Transport (SMART) in Biological Cells'
image: 
authors: 'E. A. Francis<sup>*</sup>, J. Laughlin<sup>*</sup>, J. S. Dokken, H. Finsberg, C. T. Lee, M. E. Rognes<sup>$</sup>, and P. Rangamani<sup>$</sup>'

journal: 'unpublished'
doi: 
shortcite: Francis et al., 2024 unpublished
citation: 

biorxiv: 10.1101/2024.05.23.595604
arxiv: 
chemrxiv: 

github: 
zenodo: 

date: 2024-05-25

status: 'Submitted'
inprep: True
---

# Abstract

Biological cells rely on precise spatiotemporal coordination of biochemical reactions to control their many functions. Such cell signaling networks have been a common focus for mathematical models, but they remain challenging to simulate, particularly in realistic cell geometries. Herein, we present our software, Spatial Modeling Algorithms for Reaction and Transport (SMART), a package that takes in high-level user specifications about cell signaling networks and molecular transport, and then assembles and solves the associated mathematical and computational systems. SMART uses state-of-the-art finite element analysis, via the FEniCS Project software, to efficiently and accurately resolve cell signaling events over discretized cellular and subcellular geometries. We demonstrate its application to several different biological systems, including YAP/TAZ mechanotransduction, calcium signaling in neurons and cardiomyocytes, and ATP generation in mitochondria. Throughout, we utilize experimentally-derived realistic cellular geometries represented by well-conditioned tetrahedral meshes. These scenarios demonstrate the applicability, flexibility, accuracy and efficiency of SMART across a range of temporal and spatial scales.
