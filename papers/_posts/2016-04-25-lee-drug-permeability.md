---
layout: paper
title: 'Simulation-Based Approaches for Determining Membrane Permeability of Small Compounds'
image: 
authors: 'C. T. Lee, J. Comer<sup>$</sup>, C. Herndon, N. Leung, A. Pavlova, R. V. Swift, C. Tung, C. N. Rowley, R. E. Amaro<sup>$</sup>, C. Chipot<sup>$</sup>, Y. Wang<sup>$</sup>, and J. C. Gumbart<sup>$</sup>'

journal: 'J. Chem. Inf. Model.'
doi: 10.1021/acs.jcim.6b00022
shortcite: Lee et al., 2016 J. Chem. Inf. Model.
citation: '56.4 (April 2016), pp. 721--733'

biorxiv: 
arxiv: 
chemrxiv: 

github: 
zenodo: 

date: 2016-04-25

status: 
inprep: False
---

# Abstract

Predicting the rate of nonfacilitated permeation of solutes across lipid bilayers is important to drug design, toxicology, and signaling. These rates can be estimated using molecular dynamics simulations combined with the inhomogeneous solubility-diffusion model, which requires calculation of the potential of mean force and position-dependent diffusivity of the solute along the transmembrane axis. In this paper, we assess the efficiency and accuracy of several methods for the calculation of the permeability of a model DMPC bilayer to urea, benzoic acid, and codeine. We compare umbrella sampling, replica exchange umbrella sampling, adaptive biasing force, and multiple-walker adaptive biasing force for the calculation of the transmembrane PMF. No definitive advantage for any of these methods in their ability to predict the membrane permeability coefficient Pm was found, provided that a sufficiently long equilibration is performed. For diffusivities, a Bayesian inference method was compared to a generalized Langevin method, both being sensitive to chosen parameters and the slow relaxation of membrane defects. Agreement within 1.5 log units of the computed Pm with experiment is found for all permeants and methods. Remaining discrepancies can likely be attributed to limitations of the force field as well as slowly relaxing collective movements within the lipid environment. Numerical calculations based on model profiles show that Pm can be reliably estimated from only a few data points, leading to recommendations for calculating Pm from simulations.
