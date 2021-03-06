"""
This module contains the material class.
"""

import asvp

from ..utilities.exceptions import ParameterError


class Material():
    """
    This class acts as a unified descriptor for an adsorbent material.
    Its purpose is to store properties such as adsorbent name,
    and batch.


    Parameters
    ----------
    name : str
        The name of the material.
    batch : str
        A batch number or secondary identifier for the material.

    Other Parameters
    ----------------
    density : float
        Material density.
    molar_mass : float
        Material molar mass.

    Notes
    -----

    The members of the properties are left at the discretion
    of the user. There are, however, some unique properties
    which can be set as seen above.

    """

    def __init__(self, name, batch, **properties):
        """
        Instantiation is done by passing all the parameters.
        """

        #: Material name
        self.name = name

        #: Material batch
        self.batch = batch

        #: Rest of material properties
        self.properties = properties

        return

    def __repr__(self):
        return ' '.join([self.name, self.batch])

    def __str__(self):
        """
        Prints a short summary of all the material parameters.
        """
        string = ""

        if self.name:
            string += ("Material:" + self.name + '\n')
        if self.batch:
            string += ("Batch:" + self.batch + '\n')

        if self.properties:
            for prop in self.properties:
                string += (prop + ':' + str(self.properties.get(prop)) + '\n')

        return string

    @classmethod
    def find(cls, material_name, material_batch):
        """
        Gets the material from the master list using its name

        Parameters
        ----------
        material_name : str
            The name of the material to search.
        material_batch : str
            The batch of the material to search.

        Returns
        -------
        Material
            Instance of class.

        Raises
        ------
        ``ParameterError``
            if it does not exist or cannot be calculated.
        """
        # Checks to see if material exists in master list
        material = next(
            (material for material in asvp.MATERIAL_LIST
             if material_name == material.name
             and material_batch == material.batch),
            None)

        if material is None:
            raise ParameterError(
                "Material {0} {1} does not exist in list of materials. "
                "First populate asvp.MATERIAL_LIST "
                "with required material class".format(
                    material_name, material_batch))

        return material

    def to_dict(self):
        """
        Returns a dictionary of the material class
        Is the same dictionary that was used to create it.

        Returns
        -------
        dict
            Dictionary of all parameters.
        """

        parameters_dict = {
            'name': self.name,
            'batch': self.batch
        }

        parameters_dict.update(self.properties)

        return parameters_dict

    def get_prop(self, prop):
        """
        Returns a property from the 'properties' dictionary.
        Or a named property if requested.

        Parameters
        ----------
        prop : str
            Property name desired.

        Returns
        -------
        str/float
            Value of property in the properties dict.

        Raises
        ------
        ``ParameterError``
            if it does not exist.
        """

        req_prop = self.properties.get(prop)
        if req_prop is None:
            try:
                req_prop = getattr(self, prop)
            except AttributeError:
                raise ParameterError("The {0} entry was not found in the "
                                     "material properties "
                                     "for material {1} {2}".format(
                                         prop, self.name, self.batch))

        return req_prop
