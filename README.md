Python Middle Layer
===================

[![Build Status](https://travis-ci.org/willrogers/pml.svg?branch=master)](https://travis-ci.org/willrogers/pml)
[![Coverage Status](https://coveralls.io/repos/github/willrogers/pml/badge.svg?branch=master)](https://coveralls.io/github/willrogers/pml?branch=master)

This a prototype Python interface to the Diamond accelerator.  It borrows
heavily from Matlab Middle Layer and NSLS-II's aphla python module.

Structure:

* A lattice is a list of elements
* An element is one physical or virtual piece of a lattice
* An element may have multiple 'devices' that control or read using PVs
* Each device may be in one or more families
* Each device is attached to a 'field', e.g. bpm.x
* Each device has a unit conversion object

Unit conversion:

* Linear interpolation
* Polynomial fitting
* Cubic spline fitting

Details:

* there are global settings for:
 * default online or offline (sim) retrieval of data
 * default hardware or physics units

Assumptions:

* PVs are associated with one physics parameter, allowing hw2physics conversion
* An element has only one device associated with a field

Questions:

* Should elements store their own location?
* Does a family require any information itself?
