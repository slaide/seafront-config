from pydantic import BaseModel

class Wellplate(BaseModel):
    """
    physical and meta characteristics of a wellplate

    on the orientation: columns are considered to be on the x axis, rows on the y axis

    Fields:
        - Manufacturer:str : name of the manufacturer of this plate. (Prefer name of the brand owner if multiple qualify otherwise)
        - Model_name:str : name of the model of this plate
        - Model_id_manufacturer:str : unique model id as provided by the manufacturer (may be empty)

        - Model_id:str : unique identifier for this plate (must NOT be manufacturer specific)

        - Offset_A1_x_mm:float : distance between upper left corner of the plate and the upper left corner of well A1, in x [mm]
        - Offset_A1_y_mm:float : distance between upper left corner of the plate and the upper left corner of well A1, in y [mm]

        - Offset_bottom_mm:float : distance between bottom of the wellplate edge (skirt) and the bottom of the well (top side of the bottom film) [mm]

        - Well_distance_x_mm:float : distance between top left corner of adjacent wells, in x [mm] (e.g. A1 - A2)
        - Well_distance_y_mm:float : distance between top left corner of adjacent wells, in y [mm] (e.g. A1 - B1)

        - Well_size_x_mm:float : largest size of a well in x dimension [mm]. this describes the area at the bottom of the well, in the image plane.

                                 note on 'largest': wells may be squares, circles, or any other shape, so size in each dimension may vary across the well

                                 note on 'bottom of the well': wells usually have slanted walls so the area is smaller at the bottom than at the top,
                                                               and technical information on plates usually only decribes the area at the top, which is not
                                                               useful when we image at the bottom.
        - Well_size_y_mm:float : largest size of a well in y dimension [mm]. this describes the area at the bottom of the well, in the image plane.

                                 note on 'largest': wells may be squares, circles, or any other shape, so size in each dimension may vary across the well

                                 note on 'bottom of the well': wells usually have slanted walls so the area is smaller at the bottom than at the top,
                                                               and technical information on plates usually only decribes the area at the top, which is not
                                                               useful when we image at the bottom.

        - Well_edge_radius_mm:float : radius of the edge of a well. e.g. a perfectly square well has radius zero, a perfectly round well has radius <[Well_size_x_mm|Well_size_y_mm]/2>

        - Num_wells_x:int : number of wells in x dimension
        - Num_wells_y:int : number of wells in y dimension

        - Length_mm:float : length of the plate [mm] (x dimension)
        - Width_mm:float : width of the plate [mm] (y dimension)

    Properties:
        - Num_total_wells : returns the total number of wells on this plate (equal to  Num_wells_x * Num_wells_y)

    """

    Manufacturer: str
    Model_name: str
    Model_id_manufacturer: str

    Model_id: str

    Offset_A1_x_mm: float
    Offset_A1_y_mm: float

    Offset_bottom_mm: float

    Well_distance_x_mm: float
    Well_distance_y_mm: float

    Well_size_x_mm: float
    Well_size_y_mm: float

    Num_wells_x: int
    Num_wells_y: int

    Length_mm: float
    Width_mm: float

    Well_edge_radius_mm: float

    @property
    def Num_total_wells(self):
        return self.Num_wells_y * self.Num_wells_x

    def get_well_offset_x(self, well_name: str) -> float:
        """
        get the offset of the top left corner of the well with name well_name, on the x axis [mm]

        well_name must be in format: '<row name as single letter, starting at A, may be lower or uppercase><column index, starting at 1, may be padded by any number of zeroes>'
            - e.g. A1, A01, F05, O24, b3
            - this function raises an exception if either index is invalid on this plate
        """

        well_name = well_name.upper()
        well_row_name, well_col_name = well_name[:1], well_name[1:]
        well_y_index = ord(well_row_name) - ord("A")
        well_x_index = int(well_col_name) - 1

        if well_y_index >= self.Num_wells_y:
            raise ValueError(f"well {well_name} is not in a valid row for plate {self}")
        if well_x_index >= self.Num_wells_x:
            raise ValueError(f"well {well_name} is not in a valid col for plate {self}")

        return self.Offset_A1_x_mm + well_x_index * self.Well_distance_x_mm

    def get_well_offset_y(self, well_name: str) -> float:
        """
        get the offset of the top left corner of the well with name well_name, on the y axis [mm]

        well_name must be in format: '<row name as single letter, starting at A, may be lower or uppercase><column index, starting at 1, may be padded by any number of zeroes>'
            - e.g. A1, A01, F05, O24, b3
            - this function raises an exception if either index is invalid on this plate
        """

        well_name = well_name.upper()
        well_row_name, well_col_name = well_name[:1], well_name[1:]
        well_y_index = ord(well_row_name) - ord("A")
        well_x_index = int(well_col_name) - 1

        if well_y_index >= self.Num_wells_y:
            raise ValueError(f"well {well_name} is not in a valid row for plate {self}")
        if well_x_index >= self.Num_wells_x:
            raise ValueError(f"well {well_name} is not in a valid col for plate {self}")

        return self.Offset_A1_y_mm + well_y_index * self.Well_distance_y_mm
