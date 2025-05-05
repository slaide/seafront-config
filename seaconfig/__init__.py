from .acquisition import *
from .config_item import *
from .wellplates import *

Plates = [

    # --- revvity plates

    Wellplate(
        # https://www.revvity.com/se-en/product/phenoplate-96-tc-lid-case-2x20b-6055302#overview
        # https://resources.revvity.com/pdfs/prd-phenoplate-96-well-microplates-hca.pdf
        Manufacturer="Revvity",
        Model_name="PhenoPlate 96-well",
        Model_id_manufacturer="6055302",
        Model_id="revvity-96-6055302",
        Num_wells_x=12,
        Num_wells_y=8,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=6.4,
        Well_size_y_mm=6.4,
        Well_edge_radius_mm=6.4/2, # circular
        Offset_A1_x_mm=14.38 - 6.4 / 2,  # offset is from center of the well
        Offset_A1_y_mm=11.24 - 6.4 / 2,  # offset is from center of the well
        Well_distance_x_mm=9,
        Well_distance_y_mm=9,
        Offset_bottom_mm=0.118 + 0.210,  # foil + bottom height
    ),
    Wellplate(
        # https://www.revvity.com/se-en/product/ula-phenoplate-384-lid-case-10x1b-6057800#overview
        # https://resources.revvity.com/pdfs/prd-phenoplate-384-well%20microplates-hca.pdf
        Manufacturer="Revvity",
        Model_name="PhenoPlate 384-well",
        Model_id_manufacturer="6057800",
        Model_id="revvity-384-6057800",
        Num_wells_x=24,
        Num_wells_y=16,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=3.26,
        Well_size_y_mm=3.26,
        Well_edge_radius_mm=0.2, # unspecified. looks like some very small radius.
        Offset_A1_x_mm=12.13 - 3.26 / 2,  # offset is from center of the well
        Offset_A1_y_mm=8.99 - 3.26 / 2,  # offset is from center of the well
        Well_distance_x_mm=4.5,
        Well_distance_y_mm=4.5,
        Offset_bottom_mm=0.118 + 0.210,  # foil + bottom height
    ),
    Wellplate(
        # https://www.revvity.com/se-en/product/phenoplate-1536-tc-lid-case-2x25b-6054305
        Manufacturer="Revvity",
        Model_name="PhenoPlate 1536-well",
        Model_id_manufacturer="6054305",
        Model_id="revvity-1536-6054305",
        Num_wells_x=48,
        Num_wells_y=32,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=1.53,
        Well_size_y_mm=1.53,
        Well_edge_radius_mm=0.1, # unspecified. probably some very small radius.
        Offset_A1_x_mm=11.01 - 1.53 / 2,  # offset is from center of the well
        Offset_A1_y_mm=7.87 - 1.53 / 2,  # offset is from center of the well
        Well_distance_x_mm=2.25,
        Well_distance_y_mm=2.25,
        Offset_bottom_mm=0.118 + 0.210,  # foil + bottom height
    ),

    # --- thermo fischer plates

    Wellplate(
        # https://www.thermofisher.com/order/catalog/product/165305
        # https://assets.thermofisher.com/TFS-Assets/LCD/Schematics-%26-Diagrams/1653xx_0713.pdf
        Manufacturer="ThermoFischer",
        Model_name="Nunc 96-well",
        Model_id_manufacturer="165305",
        Model_id="thermofischer-96-165305",
        Num_wells_x=12,
        Num_wells_y=8,
        Length_mm=127.76,
        Width_mm=85.47,
        Well_size_x_mm=6.3,
        Well_size_y_mm=6.3,
        Well_edge_radius_mm=6.3/2, # circular
        Offset_A1_x_mm=14.32 - 6.3 / 2,  # offset is from center of the well
        Offset_A1_y_mm=11.25 - 6.3 / 2,  # offset is from center of the well
        Well_distance_x_mm=9,
        Well_distance_y_mm=9,
        Offset_bottom_mm=2.2,
    ),
    Wellplate(
        # https://www.thermofisher.com/order/catalog/product/A58941
        Manufacturer="ThermoFischer",
        Model_name="384-well (A58941)",
        Model_id_manufacturer="A58941",
        Model_id="thermofischer-384-A58941",
        Num_wells_x=24,
        Num_wells_y=16,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=3.17,
        Well_size_y_mm=3.17,
        Well_edge_radius_mm=0.2, # unspecified. looks like some very small radius.
        Offset_A1_x_mm=12.13 - 3.17 / 2,  # offset is from center of the well
        Offset_A1_y_mm=8.99 - 3.17 / 2,  # offset is from center of the well
        Well_distance_x_mm=4.5,
        Well_distance_y_mm=4.5,
        Offset_bottom_mm=2.2,  # from thermofischer-nunc-96
    ),
    Wellplate(
        # https://www.thermofisher.com/order/catalog/product/253601
        # https://assets.thermofisher.com/TFS-Assets/LSG/manuals/D03007.pdf
        Manufacturer="ThermoFischer",
        Model_name="Nunc 1536-well",
        Model_id_manufacturer="253601",
        Model_id="thermofischer-1536-253601",
        Num_wells_x=48,
        Num_wells_y=32,
        Length_mm=127.8,
        Width_mm=85.5,
        Well_size_x_mm=1.7,  # seems to be at top of well
        Well_size_y_mm=1.7,  # seems to be at top of well
        Well_edge_radius_mm=0.1, # unspecified. seems like some very small radius.
        Offset_A1_x_mm=11.0 - 1.7 / 2,  # offset is from center of the well
        Offset_A1_y_mm=7.9 - 1.7 / 2,  # offset is from center of the well
        Well_distance_x_mm=2.2,
        Well_distance_y_mm=2.2,
        Offset_bottom_mm=7.4 - 5.1, # plate height - well depth
    ),

    # --- corning plates

    # tech specs for corning 96,384,1536 plates:
    # https://www.corning.com/catalog/cls/documents/drawings/MicroplateDimensions96-384-1536.pdf
    Wellplate(
        # https://ecatalog.corning.com/life-sciences/b2c/US/en/Microplates/Assay-Microplates/96-Well-Microplates/Falcon%C2%AE-96-well-Polystyrene-Microplates/p/353072
        Manufacturer="Corning",
        Model_name="Falcon 96-well",
        Model_id_manufacturer="353072",
        Model_id="corning-96-353072",
        Num_wells_x=12,
        Num_wells_y=8,
        Length_mm=127.76,
        Width_mm=85.11,
        Well_size_x_mm=6.35,
        Well_size_y_mm=6.35,
        Well_edge_radius_mm=6.35/2, # circular
        Offset_A1_x_mm=14.38 - 6.35 / 2,  # offset is from center of the well
        Offset_A1_y_mm=11.34 - 6.35 / 2,  # offset is from center of the well
        Well_distance_x_mm=8.99,
        Well_distance_y_mm=8.99,
        Offset_bottom_mm=14.30 - 10.76,  # plate height - well depth
    ),
    Wellplate(
        # https://ecatalog.corning.com/life-sciences/b2b/NO/en/Microplates/Assay-Microplates/384-Well-Microplates/Falcon%C2%AE-384-well-Microplates/p/353961
        Manufacturer="Corning",
        Model_name="Falcon 384-well",
        Model_id_manufacturer="353961",
        Model_id="corning-384-353961",
        Num_wells_x=24,
        Num_wells_y=16,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=3.30,
        Well_size_y_mm=3.30,
        Well_edge_radius_mm=0.2, # unspecified. looks like some very small radius.
        Offset_A1_x_mm=12.13 - 3.30 / 2,  # offset is from center of the well
        Offset_A1_y_mm=8.99 - 3.30 / 2,  # offset is from center of the well
        Well_distance_x_mm=4.5,
        Well_distance_y_mm=4.5,
        Offset_bottom_mm=14.30 - 10.76,  # plate height - well depth (from corning-falcon-96)
    ),
    Wellplate(
        # https://ecatalog.corning.com/life-sciences/b2c/US/en/Microplates/Assay-Microplates/1536-well-Microplates/Corning%C2%AE1536-well-Standard-Polystyrene-Microplates-and-Low-Base/p/3832
        Manufacturer="Corning",
        Model_name="Corning 1536-well",  # not falcon
        Model_id_manufacturer="3832",
        Model_id="corning-1536-3832",
        Num_wells_x=48,
        Num_wells_y=32,
        Length_mm=127.8,
        Width_mm=85.5,
        Well_size_x_mm=1.5,
        Well_size_y_mm=1.5,
        Well_edge_radius_mm=0.1, # unspecified. looks like some very small radius.
        Offset_A1_x_mm=11.0 - 1.5 / 2,  # offset is from center of the well
        Offset_A1_y_mm=7.86 - 1.5 / 2,  # offset is from center of the well
        Well_distance_x_mm=2.25,
        Well_distance_y_mm=2.25,
        Offset_bottom_mm=0.08 + 1.72, # bottom thickness + distance to bottom
    ),

    # --- glass slide carriers

    Wellplate(
        Manufacturer="Generic",
        Model_name="Glass Slide Carrier (1)",
        Model_id_manufacturer="generic-slide-carrier-1",
        Model_id="generic-slide-carrier-1",
        Num_wells_x=1,
        Num_wells_y=1,
        Length_mm=127.8,
        Width_mm=85.5,
        Well_size_x_mm=75,
        Well_size_y_mm=26,
        Well_edge_radius_mm=0, # square
        Offset_A1_x_mm=(127.8 - 75) / 2,
        Offset_A1_y_mm=(85.5 - 26) / 2,
        Well_distance_x_mm=0,  # n/a
        Well_distance_y_mm=0,  # n/a
        Offset_bottom_mm=0.08 + 1.72,  # placeholder
    ),
    Wellplate(
        # https://www.thorlabs.com/thorproduct.cfm?partnumber=C4SH01
        # https://www.thorlabs.com/drawings/d84f1745da0d3e5d-3DCAE562-D5A6-C2A7-7968BDAF035D52A2/C4SH01-AutoCADPDF.pdf
        Manufacturer="Thorlabs",
        Model_name="C4SH01",
        Model_id_manufacturer="C4SH01",
        Model_id="thorlabs-C4SH01",
        Num_wells_x=4,
        Num_wells_y=1,
        Length_mm=127.6,
        Width_mm=85.5,
        Well_size_x_mm=25,
        Well_size_y_mm=75,
        Well_edge_radius_mm=0, # square
        Offset_A1_x_mm=23.1-25/2, # offset is from center of the well
        Offset_A1_y_mm=(85.5 - 75) / 2, # offset is from center of the well
        Well_distance_x_mm=27.2, # actually not quite uniform (according to cad, 27.1-27.2)
        Well_distance_y_mm=0, # n/a
        Offset_bottom_mm=0.08 + 1.72,  # placeholder
    ),
]
""" a list of known wellplates """
