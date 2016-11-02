# -*- coding: utf-8 -*-
from decimal import Decimal, ROUND_HALF_UP

# Big dict of units.  Yes, there's a bit of redundancy wrt SI units...
# If you can improve readability / length while keeping the *speed* of a dict... submit a pull request!
UNITS = {
	'count': {
		'each': {
			'symbols': ['ea',],
			'factor': 1,
		},
		'dozen': {
			'symbols': ['doz', 'dzn',],
			'factor': 12,
		},
		'gross': {
			'symbols': ['gr', 'gro',],
			'factor': 144,
		},
	},
	'length': {
		'thou': {
			'symbols': ['th',],
			'factor': Decimal(0.001),
		},
		'inch': {
			'symbols': ['in',],
			'factor': 1,
		},
		'foot': {
			'symbols': ['ft',],
			'factor': 12,
		},
		'yard': {
			'symbols': ['yd',],
			'factor': 36,
		},
		'mile': {
			'symbols': ['mi',],
			'factor': 63360,
		},
		'meter': {
			'symbols': ['m',],
			'factor': 39.3700787402E0,
		},
		'yottameter': {
			'symbols': ['Ym',],
			'factor': 39.3700787402E24,
		},
		'zettameter': {
			'symbols': ['Zm',],
			'factor': 39.3700787402E21,
		},
		'exameter': {
			'symbols': ['Em',],
			'factor': 39.3700787402E18,
		},
		'petameter': {
			'symbols': ['Pm',],
			'factor': 39.3700787402E15,
		},
		'terameter': {
			'symbols': ['Tm',],
			'factor': 39.3700787402E12,
		},
		'gigameter': {
			'symbols': ['Gm',],
			'factor': 39.3700787402E9,
		},
		'megameter': {
			'symbols': ['Mm',],
			'factor': 39.3700787402E6,
		},
		'kilometer': {
			'symbols': ['km',],
			'factor': 39.3700787402E3,
		},
		'hectometer': {
			'symbols': ['hm',],
			'factor': 39.3700787402E2,
		},
		'decameter': {
			'symbols': ['dam',],
			'factor': 39.3700787402E1,
		},
		'decimeter': {
			'symbols': ['dm',],
			'factor': 39.3700787402E-1,
		},
		'centimeter': {
			'symbols': ['cm',],
			'factor': 39.3700787402E-2,
		},
		'milimeter': {
			'symbols': ['mm',],
			'factor': 39.3700787402E-3,
		},
		'micrometer': {
			'symbols': ['µm', 'um', 'mcm'],
			'factor': 39.3700787402E-6,
		},
		'nanometer': {
			'symbols': ['nm',],
			'factor': 39.3700787402E-9,
		},
		'picometer': {
			'symbols': ['pm',],
			'factor': 39.3700787402E-12,
		},
		'femtometer': {
			'symbols': ['fm',],
			'factor': 39.3700787402E-15,
		},
		'attometer': {
			'symbols': ['am',],
			'factor': 39.3700787402E-18,
		},
		'zeptometer': {
			'symbols': ['zm',],
			'factor': 39.3700787402E-21,
		},
		'yoctometer': {
			'symbols': ['ym',],
			'factor': 39.3700787402E-24,
		},
	},
	'area': {
		'square thou': {
			'symbols': ['sq th', 'th2',],
			'factor': 0.001,
		},
		'square inch': {
			'symbols': ['sq in', 'in2',],
			'factor': 1,
		},
		'square foot': {
			'symbols': ['sq ft', 'ft2',],
			'factor': 12,
		},
		'square yard': {
			'symbols': ['sq yd', 'yd2',],
			'factor': 36,
		},
		'square mile': {
			'symbols': ['sq mi', 'mi2',],
			'factor': 63360,
		},
		'square meter': {
			'symbols': ['sq m', 'm2',],
			'factor': 39.3700787402E0,
		},
		'square yottameter': {
			'symbols': ['sq Ym', 'Ym2',],
			'factor': 39.3700787402E24,
		},
		'square zettameter': {
			'symbols': ['sq Zm', 'Zm2',],
			'factor': 39.3700787402E21,
		},
		'square exameter': {
			'symbols': ['sq Em', 'Em2',],
			'factor': 39.3700787402E18,
		},
		'square petameter': {
			'symbols': ['sq Pm', 'Pm2',],
			'factor': 39.3700787402E15,
		},
		'square terameter': {
			'symbols': ['sq Tm', 'Tm2',],
			'factor': 39.3700787402E12,
		},
		'square gigameter': {
			'symbols': ['sq Gm', 'Gm2',],
			'factor': 39.3700787402E9,
		},
		'square megameter': {
			'symbols': ['sq Mm', 'Mm2',],
			'factor': 39.3700787402E6,
		},
		'square kilometer': {
			'symbols': ['sq km', 'km2',],
			'factor': 39.3700787402E3,
		},
		'square hectometer': {
			'symbols': ['sq hm', 'hm2',],
			'factor': 39.3700787402E2,
		},
		'square decameter': {
			'symbols': ['sq dam', 'dam2',],
			'factor': 39.3700787402E1,
		},
		'square decimeter': {
			'symbols': ['sq dm', 'dm2',],
			'factor': 39.3700787402E-1,
		},
		'square centimeter': {
			'symbols': ['sq cm', 'cm2',],
			'factor': 39.3700787402E-2,
		},
		'square milimeter': {
			'symbols': ['sq mm', 'mm2',],
			'factor': 39.3700787402E-3,
		},
		'square micrometer': {
			'symbols': ['sq µm', 'sq um', 'sq mcm' 'µm2', 'um2', 'mcm2',],
			'factor': 39.3700787402E-6,
		},
		'square nanometer': {
			'symbols': ['sq nm', 'nm2',],
			'factor': 39.3700787402E-9,
		},
		'square picometer': {
			'symbols': ['sq pm', 'pm2',],
			'factor': 39.3700787402E-12,
		},
		'square femtometer': {
			'symbols': ['sq fm', 'fm2',],
			'factor': 39.3700787402E-15,
		},
		'square attometer': {
			'symbols': ['sq am', 'am2',],
			'factor': 39.3700787402E-18,
		},
		'square zeptometer': {
			'symbols': ['sq zm', 'zm2',],
			'factor': 39.3700787402E-21,
		},
		'square yoctometer': {
			'symbols': ['sq ym', 'ym2',],
			'factor': 39.3700787402E-24,
		},
	},
	'weight': {
		'ounce': {
			'symbols': ['oz',],
			'factor': 1,
		},
		'pound': {
			'symbols': ['lb',],
			'factor': 16,
		},
		'ton': {
			'symbols': ['t',],
			'factor': 32000,
		},
		'gram': {
			'symbols': ['g',],
			'factor': 0.035273961949581,
		},
		'yottagram': {
			'symbols': ['Yg',],
			'factor': 0.035273961949581E24,
		},
		'zettagram': {
			'symbols': ['Zg',],
			'factor': 0.035273961949581E21,
		},
		'exagram': {
			'symbols': ['Eg',],
			'factor': 0.035273961949581E18,
		},
		'petagram': {
			'symbols': ['Pg',],
			'factor': 0.035273961949581E15,
		},
		'teragram': {
			'symbols': ['Tg',],
			'factor': 0.035273961949581E12,
		},
		'gigagram': {
			'symbols': ['Gg',],
			'factor': 0.035273961949581E9,
		},
		'megagram': {
			'symbols': ['Mg',],
			'factor': 0.035273961949581E6,
		},
		'kilogram': {
			'symbols': ['kg',],
			'factor': 0.035273961949581E3,
		},
		'hectogram': {
			'symbols': ['hg',],
			'factor': 0.035273961949581E2,
		},
		'decagram': {
			'symbols': ['dag',],
			'factor': 0.035273961949581E1,
		},
		'decigram': {
			'symbols': ['dg',],
			'factor': 0.035273961949581E-1,
		},
		'centigram': {
			'symbols': ['cg',],
			'factor': 0.035273961949581E-2,
		},
		'miligram': {
			'symbols': ['mg',],
			'factor': 0.035273961949581E-3,
		},
		'microgram': {
			'symbols': ['µg', 'ug', 'mcg',],
			'factor': 0.035273961949581E-6,
		},
		'nanogram': {
			'symbols': ['ng',],
			'factor': 0.035273961949581E-9,
		},
		'picogram': {
			'symbols': ['pg',],
			'factor': 0.035273961949581E-12,
		},
		'femtogram': {
			'symbols': ['fg',],
			'factor': 0.035273961949581E-15,
		},
		'attogram': {
			'symbols': ['ag',],
			'factor': 0.035273961949581E-18,
		},
		'zeptogram': {
			'symbols': ['zg',],
			'factor': 0.035273961949581E-21,
		},
		'yoctogram': {
			'symbols': ['yg',],
			'factor': 0.035273961949581E-24,
		},
	},
	'volume': {
		'fluid ounce': {
			'symbols': ['fl oz',],
			'factor': 1,
		},
		'cup': {
			'symbols': ['c',],
			'factor': 8,
		},
		'pint': {
			'symbols': ['pt',],
			'factor': 16,
		},
		'quart': {
			'symbols': ['qt',],
			'factor': 32,
		},
		'gallon': {
			'symbols': ['gl', 'gal',],
			'factor': 128,
		},
		'cubic inch': {
			'symbols': ['cu in', 'in3', 'ci',],
			'factor': (73728/77)/12,
		},
		'cubic foot': {
			'symbols': ['cu ft', 'ft3', 'cf',],
			'factor': (73728/77),
		},
		'cubic yard': {
			'symbols': ['cu yd', 'yd3', 'cy',],
			'factor': (73728/77)*3,
		},
		'cubic meter': {
			'symbols': ['cu m', 'm3', 'cum',],
			'factor': 33814.022701842997,
		},
		'cubic yottameter': {
			'symbols': ['cu Ym', 'Ym3', 'cYm',],
			'factor': 33814.022701842997E24,
		},
		'cubic zettameter': {
			'symbols': ['cu Zm', 'Zm3', 'cZm',],
			'factor': 33814.022701842997E21,
		},
		'cubic exameter': {
			'symbols': ['cu Em', 'Em3', 'cEm',],
			'factor': 33814.022701842997E18,
		},
		'cubic petameter': {
			'symbols': ['cu Pm', 'Pm3', 'cPm'],
			'factor': 33814.022701842997E15,
		},
		'cubic terameter': {
			'symbols': ['cu Tm', 'Tm3', 'cTm',],
			'factor': 33814.022701842997E12,
		},
		'cubic gigameter': {
			'symbols': ['cu Gm', 'Gm3', 'cGm',],
			'factor': 33814.022701842997E9,
		},
		'cubic megameter': {
			'symbols': ['cu Mm', 'Mm3', 'cMm',],
			'factor': 33814.022701842997E6,
		},
		'cubic kilometer': {
			'symbols': ['cu km', 'km3', 'ckm',],
			'factor': 33814.022701842997E3,
		},
		'cubic hectometer': {
			'symbols': ['cu hm', 'hm3', 'chm',],
			'factor': 33814.022701842997E2,
		},
		'cubic decameter': {
			'symbols': ['cu dam', 'dam3', 'cdam',],
			'factor': 33814.022701842997E1,
		},
		'cubic decimeter': {
			'symbols': ['cu dm', 'dm3', 'cdm',],
			'factor': 33814.022701842997E-1,
		},
		'cubic centimeter': {
			'symbols': ['cu cm', 'cm3', 'ccm', 'cc', ],
			'factor': 33814.022701842997E-2,
		},
		'cubic milimeter': {
			'symbols': ['cu mm', 'mm3', 'cmm',],
			'factor': 33814.022701842997E-3,
		},
		'cubic micrometer': {
			'symbols': ['cu µm', 'cu um', 'cu mcm', 'µm3', 'um3', 'mcm3', 'cµm', 'cuum', 'cmcm',],
			'factor': 33814.022701842997E-6,
		},
		'cubic nanometer': {
			'symbols': ['cu nm', 'nm3', 'cnm',],
			'factor': 33814.022701842997E-9,
		},
		'cubic picometer': {
			'symbols': ['cu pm', 'pm3', 'cpm',],
			'factor': 33814.022701842997E-12,
		},
		'cubic femtometer': {
			'symbols': ['cu fm', 'fm3', 'cfm',],
			'factor': 33814.022701842997E-15,
		},
		'cubic attometer': {
			'symbols': ['cu am', 'am3', 'cam',],
			'factor': 33814.022701842997E-18,
		},
		'cubic zeptometer': {
			'symbols': ['cu zm', 'zm3', 'czm',],
			'factor': 33814.022701842997E-21,
		},
		'cubic yoctometer': {
			'symbols': ['cu ym', 'ym3', 'cym',],
			'factor': 33814.022701842997E-24,
		},
		'liter': {
			'symbols': ['L', 'l', 'ltr',],
			'factor': 33.814022701842997,
		},
		'yottaliter': {
			'symbols': ['YL', 'Yl', 'Yltr',],
			'factor': 33.814022701842997E24,
		},
		'zettaliter': {
			'symbols': ['ZL', 'Zl', 'Zltr',],
			'factor': 33.814022701842997E21,
		},
		'exaliter': {
			'symbols': ['EL', 'El', 'Eltr',],
			'factor': 33.814022701842997E18,
		},
		'petaliter': {
			'symbols': ['PL', 'Pl', 'Pltr',],
			'factor': 33.814022701842997E15,
		},
		'teraliter': {
			'symbols': ['TL', 'Tl', 'Tltr',],
			'factor': 33.814022701842997E12,
		},
		'gigaliter': {
			'symbols': ['GL', 'Gl', 'Gltr',],
			'factor': 33.814022701842997E9,
		},
		'megaliter': {
			'symbols': ['ML', 'Ml', 'Mltr',],
			'factor': 33.814022701842997E6,
		},
		'kiloliter': {
			'symbols': ['kL', 'kl', 'kltr',],
			'factor': 33.814022701842997E3,
		},
		'hectoliter': {
			'symbols': ['hL', 'hl', 'hltr',],
			'factor': 33.814022701842997E2,
		},
		'decaliter': {
			'symbols': ['daL', 'dal', 'daltr',],
			'factor': 33.814022701842997E1,
		},
		'deciliter': {
			'symbols': ['dL', 'dl', 'dltr'],
			'factor': 33.814022701842997E-1,
		},
		'centiliter': {
			'symbols': ['cL', 'cl', 'cltr',],
			'factor': 33.814022701842997E-2,
		},
		'mililiter': {
			'symbols': ['mL', 'ml', 'mltr',],
			'factor': 33.814022701842997E-3,
		},
		'microliter': {
			'symbols': ['µL', 'uL', 'mcL', 'µl', 'ul', 'mcl', 'µltr', 'ultr', 'mcltr',],
			'factor': 33.814022701842997E-6,
		},
		'nanoliter': {
			'symbols': ['nL', 'nl', 'nltr',],
			'factor': 33.814022701842997E-9,
		},
		'picoliter': {
			'symbols': ['pL', 'pl', 'pltr',],
			'factor': 33.814022701842997E-12,
		},
		'femtoliter': {
			'symbols': ['fL', 'fl', 'fltr',],
			'factor': 33.814022701842997E-15,
		},
		'attoliter': {
			'symbols': ['aL', 'al', 'altr',],
			'factor': 33.814022701842997E-18,
		},
		'zeptoliter': {
			'symbols': ['zL', 'zl', 'zltr',],
			'factor': 33.814022701842997E-21,
		},
		'yoctoliter': {
			'symbols': ['yL', 'yl', 'yltr',],
			'factor': 33.814022701842997E-24,
		},
	},
}

SI_PREFIXES = ('yotta', 'zetta', 'exa', 'peta', 'tera', 'giga', 'mega', 'kilo', 'hecto', 'deca', 'deci', 'centi', 'milli', 'micro', 'nano', 'pico', 'femto', 'atto', 'zepto', 'yocto', 'meter', 'liter',)

def convert(amount, from_unit, to_unit, unit_type=''):
	# Clean up all parameters and bail out as appropriate.
	#	All parameters: remove trailing / leading spaces
	#	Amount: convert to Decimal
	#	Units: also remove periods (convert "sq. in." to "sq in") and de-pluralize. Then, convert symbols to long form.
	#		NOTE: We could use something like inflect here, but I'm trying to make this not have dependences
	#	Unit Type: if passed, validate. If not passed, try to infer.
	try:
		amount = Decimal(str(amount).strip())
	except ValueError:
		raise ValueError("Invalid amount. Amount can contain digits and at most one period.")


	unit_type = str(unit_type).strip().lower()
	if unit_type and unit_type not in UNITS.keys():
		raise TypeError("Invalid unit_type. Must be one of: %s" % ", ".join(UNITS.keys()))
	if not unit_type:
		if from_unit.endswith('2') or from_unit.startswith('sq'):
			unit_type = 'area'
		elif from_unit.endswith('3') or from_unit.startswith('cu'):
			unit_type = 'volume'
		else:
			for utype, utypedict in UNITS.items():
				if from_unit in utypedict.keys():
					unit_type = utype
					break
				else:
					for unit, udict in utypedict.items():
						if from_unit in udict['symbols']:
							unit_type = utype
							break
	if not unit_type:
		raise TypeError("Unable to determine unit_type. Must be one of: %s" % ", ".join(UNITS.keys()))

	from_unit = str(from_unit).strip().replace('.', '').replace('inches', 'inch').replace('feet', 'foot').replace('metre', 'meter',).replace('litre', 'liter',)
	to_unit = str(to_unit).strip().replace('.', '').replace('inches', 'inch').replace('feet', 'foot').replace('metre', 'meter',).replace('litre', 'liter',)
	if from_unit and from_unit not in ['gross',]:
		if len(from_unit) > 1 and from_unit.endswith('s'):
			from_unit = from_unit[:-1]
	if to_unit and to_unit not in ['gross',]:
		if len(to_unit) > 1 and to_unit.endswith('s'):
			to_unit = to_unit[:-1]

	# Convert symbols to long names if required
	long_names = UNITS[unit_type].keys()
	if from_unit not in long_names or to_unit not in long_names:
		for unit_name, unit_dict in UNITS[unit_type].items():
			if from_unit in unit_dict['symbols']:
				from_unit = unit_name
			if to_unit in unit_dict['symbols']:
				to_unit = unit_name

	if not from_unit:
		raise TypeError("No valid from_unit found.")
	if not to_unit:
		raise TypeError("No valid to_unit found.")

	# Lookup conversion factor and do some arithmetic.	
	converted = amount*(Decimal(UNITS[unit_type][from_unit]['factor'])/(Decimal(UNITS[unit_type][to_unit]['factor'])))

	# If to_unit is SI, assume we want sanity...
	for si in SI_PREFIXES:
		if si in to_unit:
			# Attempt to figure out how many decimal places of quantization we should use
			try:
				quantize_digits = len(str(amount).split('.')[1])
			except IndexError:
				quantize_digits = 0
			# Build a quantize factor based on quantize_digits
			qfactor = '0.0' + "0"*quantize_digits + "1"
			converted = converted.quantize(Decimal(qfactor), rounding=ROUND_HALF_UP)
			break

	# Trim trailing zeros
	if converted == converted.to_integral_value():
		converted = Decimal(int(converted))

	return converted

