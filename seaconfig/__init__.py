from .acquisition import *
from .wellplates import *
from .config_item import *

Plates=[
    Wellplate(
        # https://www.revvity.com/se-en/product/phenoplate-96-tc-lid-case-2x20b-6055302#overview
        Manufacturer="Revvity",
        Model_name="PhenoPlate 96-well",
        Model_id_manufacturer="6055302",
        Model_id="revvity-phenoplate-96",

        Num_wells_y=8,
        Num_wells_x=12,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=6.4,
        Well_size_y_mm=6.4,

        Offset_A1_x_mm=11.24-6.4/2, # offset is from center of the well
        Offset_A1_y_mm=14.38-6.4/2, # offset is from center of the well
        Well_distance_x_mm=9,
        Well_distance_y_mm=9,

        Offset_bottom_mm=0.118+0.210, # foil + bottom height
    ),
    Wellplate(
        # https://www.revvity.com/se-en/product/ula-phenoplate-384-lid-case-10x1b-6057800#overview
        Manufacturer="Revvity",
        Model_name="PhenoPlate 384-well",
        Model_id_manufacturer="6057800",
        Model_id="revvity-phenoplate-384",

        Num_wells_x=24,
        Num_wells_y=16,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=3.26,
        Well_size_y_mm=3.26,

        Offset_A1_x_mm=12.13-3.26/2, # offset is from center of the well
        Offset_A1_y_mm=8.99-3.26/2, # offset is from center of the well
        Well_distance_x_mm=4.5,
        Well_distance_y_mm=4.5,

        Offset_bottom_mm=0.118+0.210, # foil + bottom height
    ),
    Wellplate(
        # https://www.revvity.com/se-en/product/phenoplate-1536-tc-lid-case-2x25b-6054305
        Manufacturer="Revvity",
        Model_name="PhenoPlate 1536-well",
        Model_id_manufacturer="6054305",
        Model_id="revvity-phenoplate-1536",

        Num_wells_y=32,
        Num_wells_x=48,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=1.53,
        Well_size_y_mm=1.53,

        Offset_A1_x_mm=11.01-1.53/2, # offset is from center of the well
        Offset_A1_y_mm=7.87-1.53/2, # offset is from center of the well
        Well_distance_x_mm=2.25,
        Well_distance_y_mm=2.25,

        Offset_bottom_mm=0.118+0.210, # foil + bottom height
    ),

    Wellplate(
        # https://www.thermofisher.com/order/catalog/product/165305
        Manufacturer="ThermoFischer",
        Model_name="Nunc 96-well",
        Model_id_manufacturer="165305",
        Model_id="thermofischer-nunc-96",

        Num_wells_y=8,
        Num_wells_x=12,
        Length_mm=127.76,
        Width_mm=85.47,
        Well_size_x_mm=6.3,
        Well_size_y_mm=6.3,

        Offset_A1_x_mm=11.25-6.3/2, # offset is from center of the well
        Offset_A1_y_mm=14.32-6.3/2, # offset is from center of the well
        Well_distance_x_mm=9,
        Well_distance_y_mm=9,

        Offset_bottom_mm=2.2,
    ),
    Wellplate(
        # https://www.thermofisher.com/order/catalog/product/A58941
        Manufacturer="ThermoFischer",
        Model_name="Nunc 384-well",
        Model_id_manufacturer="A58941",
        Model_id="thermofischer-nunc-384",

        Num_wells_x=24,
        Num_wells_y=16,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=3.26,
        Well_size_y_mm=3.26,

        Offset_A1_x_mm=12.13-3.26/2, # offset is from center of the well
        Offset_A1_y_mm=8.99-3.26/2, # offset is from center of the well
        Well_distance_x_mm=4.5,
        Well_distance_y_mm=4.5,

        Offset_bottom_mm=2.2, # from thermofischer-nunc-96
    ),
    Wellplate(
        # https://www.thermofisher.com/order/catalog/product/253601
        Manufacturer="ThermoFischer",
        Model_name="Nunc 1536-well",
        Model_id_manufacturer="253601",
        Model_id="thermofischer-nunc-1536",

        Num_wells_y=32,
        Num_wells_x=48,
        Length_mm=127.8,
        Width_mm=85.5,
        Well_size_x_mm=1.7, # seems to be at top of well
        Well_size_y_mm=1.7, # seems to be at top of well

        Offset_A1_x_mm=11.0-1.7/2, # offset is from center of the well
        Offset_A1_y_mm=7.9-1.7/2, # offset is from center of the well
        Well_distance_x_mm=2.2,
        Well_distance_y_mm=2.2,

        Offset_bottom_mm=7.4-5.1, # plate height - well depth
    ),

    # tech specs for corning 96,384,1536 plates:
    # https://www.corning.com/catalog/cls/documents/drawings/MicroplateDimensions96-384-1536.pdf
    Wellplate(
        # https://ecatalog.corning.com/life-sciences/b2c/US/en/Microplates/Assay-Microplates/96-Well-Microplates/Falcon%C2%AE-96-well-Polystyrene-Microplates/p/353072
        Manufacturer="Corning",
        Model_name="Falcon 96-well",
        Model_id_manufacturer="353072",
        Model_id="corning-falcon-96",

        Num_wells_y=8,
        Num_wells_x=12,
        Length_mm=127.76,
        Width_mm=85.11,
        Well_size_x_mm=6.35,
        Well_size_y_mm=6.35,

        Offset_A1_x_mm=11.34-6.35/2, # offset is from center of the well
        Offset_A1_y_mm=14.38-6.35/2, # offset is from center of the well
        Well_distance_x_mm=8.99,
        Well_distance_y_mm=8.99,

        Offset_bottom_mm=14.30-10.76, # plate height - well depth
    ),
    Wellplate(
        # https://ecatalog.corning.com/life-sciences/b2b/NO/en/Microplates/Assay-Microplates/384-Well-Microplates/Falcon%C2%AE-384-well-Microplates/p/353961
        Manufacturer="Corning",
        Model_name="Falcon 384-well",
        Model_id_manufacturer="353961",
        Model_id="corning-falcon-384",

        Num_wells_x=24,
        Num_wells_y=16,
        Length_mm=127.76,
        Width_mm=85.48,
        Well_size_x_mm=3.26,
        Well_size_y_mm=3.26,

        Offset_A1_x_mm=12.13-3.26/2, # offset is from center of the well
        Offset_A1_y_mm=8.99-3.26/2, # offset is from center of the well
        Well_distance_x_mm=4.5,
        Well_distance_y_mm=4.5,

        Offset_bottom_mm=14.30-10.76, # plate height - well depth (from corning-falcon-96)
    ),
    Wellplate(
        # https://ecatalog.corning.com/life-sciences/b2c/US/en/Microplates/Assay-Microplates/1536-well-Microplates/Corning%C2%AE1536-well-Standard-Polystyrene-Microplates-and-Low-Base/p/3832
        Manufacturer="Corning",
        Model_name="Corning 1536-well", # not falcon
        Model_id_manufacturer="3832",
        Model_id="corning-falcon-1536",

        Num_wells_y=32,
        Num_wells_x=48,
        Length_mm=127.8,
        Width_mm=85.5,
        Well_size_x_mm=1.5,
        Well_size_y_mm=1.5,

        Offset_A1_x_mm=11.0-1.5/2, # offset is from center of the well
        Offset_A1_y_mm=7.86-1.5/2, # offset is from center of the well
        Well_distance_x_mm=2.25,
        Well_distance_y_mm=2.25,

        Offset_bottom_mm=0.08+1.72, # bottom thickness + distance to bottom
    ),
]
""" a list of known wellplates """