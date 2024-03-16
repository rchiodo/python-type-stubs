from sympy.physics.units.dimensions import Dimension, DimensionSystem
from sympy.physics.units.unitsystem import UnitSystem
from sympy.physics.units.util import convert_to
from sympy.physics.units.quantities import Quantity
from sympy.physics.units.definitions.dimension_definitions import acceleration, action, amount_of_substance, area, capacitance, charge, conductance, current, energy, force, frequency, impedance, inductance, length, luminous_intensity, magnetic_density, magnetic_flux, mass, momentum, power, pressure, temperature, time, velocity, voltage, volume
from sympy.physics.units.prefixes import atto, centi, deca, deci, exa, exbi, femto, gibi, giga, hecto, kibi, kilo, mebi, mega, micro, milli, nano, pebi, peta, pico, tebi, tera, yocto, yotta, zepto, zetta
from sympy.physics.units.definitions import A, Bq, C, D, Da, F, G, Gy, H, Hz, J, K, L, N, Pa, R, S, T, V, W, Wb, Z0, acceleration_due_to_gravity, ampere, amperes, amu, amus, angstrom, angstroms, angular_mil, angular_mils, anomalistic_year, anomalistic_years, astronomical_unit, astronomical_units, atm, atmosphere, atmospheres, atomic_mass_constant, atomic_mass_unit, au, avogadro, avogadro_constant, avogadro_number, bar, bars, becquerel, bit, bits, boltzmann, boltzmann_constant, byte, c, cL, candela, candelas, cd, centiliter, centiliters, centimeter, centimeters, cl, cm, common_year, common_years, coulomb, coulomb_constant, coulombs, dHg0, dL, dalton, day, days, deciliter, deciliters, decimeter, decimeters, deg, degree, degrees, dioptre, dl, dm, draconic_year, draconic_years, e0, eV, electric_constant, electric_force_constant, electron_rest_mass, electronvolt, electronvolts, elementary_charge, exbibyte, exbibytes, farad, faraday_constant, farads, feet, foot, ft, full_moon_cycle, full_moon_cycles, g, gaussian_year, gaussian_years, gee, gees, gibibyte, gibibytes, gram, grams, gravitational_constant, gray, h, ha, hbar, hectare, henry, henrys, hertz, hour, hours, hz, inch, inches, josephson_constant, joule, joules, julian_year, julian_years, kPa, kat, katal, kelvin, kelvins, kg, kibibyte, kibibytes, kilogram, kilograms, kilometer, kilometers, km, l, lightyear, lightyears, liter, liters, lux, lx, ly, m, mL, magnetic_constant, me, mebibyte, mebibytes, meter, meters, metric_ton, mg, mho, mhos, mi, microgram, micrograms, micrometer, micrometers, micron, microns, microsecond, microseconds, mil, mile, miles, milli_mass_unit, milligram, milligrams, milliliter, milliliters, millimeter, millimeters, millisecond, milliseconds, minute, minutes, ml, mm, mmHg, mmu, mmus, mol, molar_gas_constant, mole, moles, ms, nanometer, nanometers, nanosecond, nanoseconds, nautical_mile, nautical_miles, newton, newtons, nm, nmi, ns, ohm, ohms, optical_power, pa, pascal, pascals, pebibyte, pebibytes, percent, percents, permille, picometer, picometers, picosecond, picoseconds, planck, planck_acceleration, planck_angular_frequency, planck_area, planck_charge, planck_current, planck_density, planck_energy, planck_energy_density, planck_force, planck_impedance, planck_intensity, planck_length, planck_mass, planck_momentum, planck_power, planck_pressure, planck_temperature, planck_time, planck_voltage, planck_volume, pm, pound, pounds, ps, psi, quart, quarts, rad, radian, radians, s, second, seconds, sidereal_year, sidereal_years, siemens, speed_of_light, sr, stefan, stefan_boltzmann_constant, steradian, steradians, t, tebibyte, tebibytes, tesla, teslas, tonne, torr, tropical_year, tropical_years, u0, ug, um, us, v, vacuum_impedance, vacuum_permeability, vacuum_permittivity, volt, volts, von_klitzing_constant, watt, watts, wb, weber, webers, yard, yards, yd, year, years
from sympy.physics.units.systems import mks, mksa, si

"""
Dimensional analysis and unit systems.

This module defines dimension/unit systems and physical quantities. It is
based on a group-theoretical construction where dimensions are represented as
vectors (coefficients being the exponents), and units are defined as a dimension
to which we added a scale.

Quantities are built from a factor and a unit, and are the basic objects that
one will use when doing computations.

All objects except systems and prefixes can be used in SymPy expressions.
Note that as part of a CAS, various objects do not combine automatically
under operations.

Details about the implementation can be found in the documentation, and we
will not repeat all the explanations we gave there concerning our approach.
Ideas about future developments can be found on the `Github wiki
<https://github.com/sympy/sympy/wiki/Unit-systems>`_, and you should consult
this page if you are willing to help.

Useful functions:

- ``find_unit``: easily lookup pre-defined units.
- ``convert_to(expr, newunit)``: converts an expression into the same
    expression expressed in another unit.

"""
Unit = Quantity
speed = ...
luminosity = ...
magnetic_flux_density = ...
amount = ...
def find_unit(quantity, unit_system=...) -> list[str]:
    """
    Return a list of matching units or dimension names.

    - If ``quantity`` is a string -- units/dimensions containing the string
    `quantity`.
    - If ``quantity`` is a unit or dimension -- units having matching base
    units or dimensions.

    Examples
    ========

    >>> from sympy.physics import units as u
    >>> u.find_unit('charge')
    ['C', 'coulomb', 'coulombs', 'planck_charge', 'elementary_charge']
    >>> u.find_unit(u.charge)
    ['C', 'coulomb', 'coulombs', 'planck_charge', 'elementary_charge']
    >>> u.find_unit("ampere")
    ['ampere', 'amperes']
    >>> u.find_unit('angstrom')
    ['angstrom', 'angstroms']
    >>> u.find_unit('volt')
    ['volt', 'volts', 'electronvolt', 'electronvolts', 'planck_voltage']
    >>> u.find_unit(u.inch**3)[:9]
    ['L', 'l', 'cL', 'cl', 'dL', 'dl', 'mL', 'ml', 'liter']
    """
    ...

__all__ = ['Dimension', 'DimensionSystem', 'UnitSystem', 'convert_to', 'Quantity', 'amount_of_substance', 'acceleration', 'action', 'area', 'capacitance', 'charge', 'conductance', 'current', 'energy', 'force', 'frequency', 'impedance', 'inductance', 'length', 'luminous_intensity', 'magnetic_density', 'magnetic_flux', 'mass', 'momentum', 'power', 'pressure', 'temperature', 'time', 'velocity', 'voltage', 'volume', 'Unit', 'speed', 'luminosity', 'magnetic_flux_density', 'amount', 'yotta', 'zetta', 'exa', 'peta', 'tera', 'giga', 'mega', 'kilo', 'hecto', 'deca', 'deci', 'centi', 'milli', 'micro', 'nano', 'pico', 'femto', 'atto', 'zepto', 'yocto', 'kibi', 'mebi', 'gibi', 'tebi', 'pebi', 'exbi', 'percent', 'percents', 'permille', 'rad', 'radian', 'radians', 'deg', 'degree', 'degrees', 'sr', 'steradian', 'steradians', 'mil', 'angular_mil', 'angular_mils', 'm', 'meter', 'meters', 'kg', 'kilogram', 'kilograms', 's', 'second', 'seconds', 'A', 'ampere', 'amperes', 'K', 'kelvin', 'kelvins', 'mol', 'mole', 'moles', 'cd', 'candela', 'candelas', 'g', 'gram', 'grams', 'mg', 'milligram', 'milligrams', 'ug', 'microgram', 'micrograms', 't', 'tonne', 'metric_ton', 'newton', 'newtons', 'N', 'joule', 'joules', 'J', 'watt', 'watts', 'W', 'pascal', 'pascals', 'Pa', 'pa', 'hertz', 'hz', 'Hz', 'coulomb', 'coulombs', 'C', 'volt', 'volts', 'v', 'V', 'ohm', 'ohms', 'siemens', 'S', 'mho', 'mhos', 'farad', 'farads', 'F', 'henry', 'henrys', 'H', 'tesla', 'teslas', 'T', 'weber', 'webers', 'Wb', 'wb', 'optical_power', 'dioptre', 'D', 'lux', 'lx', 'katal', 'kat', 'gray', 'Gy', 'becquerel', 'Bq', 'km', 'kilometer', 'kilometers', 'dm', 'decimeter', 'decimeters', 'cm', 'centimeter', 'centimeters', 'mm', 'millimeter', 'millimeters', 'um', 'micrometer', 'micrometers', 'micron', 'microns', 'nm', 'nanometer', 'nanometers', 'pm', 'picometer', 'picometers', 'ft', 'foot', 'feet', 'inch', 'inches', 'yd', 'yard', 'yards', 'mi', 'mile', 'miles', 'nmi', 'nautical_mile', 'nautical_miles', 'angstrom', 'angstroms', 'ha', 'hectare', 'l', 'L', 'liter', 'liters', 'dl', 'dL', 'deciliter', 'deciliters', 'cl', 'cL', 'centiliter', 'centiliters', 'ml', 'mL', 'milliliter', 'milliliters', 'ms', 'millisecond', 'milliseconds', 'us', 'microsecond', 'microseconds', 'ns', 'nanosecond', 'nanoseconds', 'ps', 'picosecond', 'picoseconds', 'minute', 'minutes', 'h', 'hour', 'hours', 'day', 'days', 'anomalistic_year', 'anomalistic_years', 'sidereal_year', 'sidereal_years', 'tropical_year', 'tropical_years', 'common_year', 'common_years', 'julian_year', 'julian_years', 'draconic_year', 'draconic_years', 'gaussian_year', 'gaussian_years', 'full_moon_cycle', 'full_moon_cycles', 'year', 'years', 'G', 'gravitational_constant', 'c', 'speed_of_light', 'elementary_charge', 'hbar', 'planck', 'eV', 'electronvolt', 'electronvolts', 'avogadro_number', 'avogadro', 'avogadro_constant', 'boltzmann', 'boltzmann_constant', 'stefan', 'stefan_boltzmann_constant', 'R', 'molar_gas_constant', 'faraday_constant', 'josephson_constant', 'von_klitzing_constant', 'Da', 'dalton', 'amu', 'amus', 'atomic_mass_unit', 'atomic_mass_constant', 'me', 'electron_rest_mass', 'gee', 'gees', 'acceleration_due_to_gravity', 'u0', 'magnetic_constant', 'vacuum_permeability', 'e0', 'electric_constant', 'vacuum_permittivity', 'Z0', 'vacuum_impedance', 'coulomb_constant', 'electric_force_constant', 'atmosphere', 'atmospheres', 'atm', 'kPa', 'bar', 'bars', 'pound', 'pounds', 'psi', 'dHg0', 'mmHg', 'torr', 'mmu', 'mmus', 'milli_mass_unit', 'quart', 'quarts', 'ly', 'lightyear', 'lightyears', 'au', 'astronomical_unit', 'astronomical_units', 'planck_mass', 'planck_time', 'planck_temperature', 'planck_length', 'planck_charge', 'planck_area', 'planck_volume', 'planck_momentum', 'planck_energy', 'planck_force', 'planck_power', 'planck_density', 'planck_energy_density', 'planck_intensity', 'planck_angular_frequency', 'planck_pressure', 'planck_current', 'planck_voltage', 'planck_impedance', 'planck_acceleration', 'bit', 'bits', 'byte', 'kibibyte', 'kibibytes', 'mebibyte', 'mebibytes', 'gibibyte', 'gibibytes', 'tebibyte', 'tebibytes', 'pebibyte', 'pebibytes', 'exbibyte', 'exbibytes', 'mks', 'mksa', 'si']
