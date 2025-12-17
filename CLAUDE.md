# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`seaconfig` is a configuration file handling module for the seafront microscopy system. It provides Pydantic models for defining acquisition protocols, wellplate specifications, and machine configuration items.

## Build and Installation

This is a pure Python package using pyproject.toml. Install with:
```bash
pip install -e .
```

No build step required. Dependencies: pydantic 2.9.2

## Architecture

The package exports all public models from `seaconfig/__init__.py` via wildcard imports from four modules:

- **acquisition.py**: Core acquisition configuration models
  - `AcquisitionConfig` - Main protocol definition (project name, plate, channels, wells, autofocus settings)
  - `AcquisitionChannelConfig` - Per-channel settings (illumination, exposure, z-stack, filters)
  - `AcquisitionWellSiteConfiguration` - Grid configuration for imaging sites within wells
  - `PlateWellConfig` - Which wells to image on a plate

- **wellplates.py**: `Wellplate` model defining physical wellplate characteristics (dimensions, well offsets, spacing). Includes methods for calculating well positions by name (e.g., "A1", "B12").

- **plates.py**: `Plates` list containing pre-defined wellplate specifications from various manufacturers (Revvity, ThermoFisher, Corning, Agilent, Greiner, Thorlabs).

- **config_item.py**: `ConfigItem` model for machine-specific configuration options with typed value access (int, float, str, bool) and option lists.

## Key Conventions

- All distances are in millimeters (mm) unless otherwise noted in field names (e.g., `_um` for micrometers, `_ms` for milliseconds)
- Well naming follows standard format: letter + number (e.g., "A1", "F05", "O24")
- Wellplate coordinates: columns = x axis, rows = y axis
- Offsets are measured from the top-left corner of the plate to the top-left corner of well A1
- Version follows semantic versioning via the `Version` model; current spec version is 6.0.0
