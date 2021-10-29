# umpy
Simple unit of measure conversion for python, optimized for manufacturing contexts.  (Unit of Measure Pie...)

umpy does not currently contain universal conversion logic, but would welcome pull requests.  We do not have a formal style guide, but emulate what you see.

umpy was created in the spirit of PEP 20, especially the bit about being explicity simple, but chuckling at the bits about ambiguity and there only being one way to do good.

## Usage
umpy is designed to be imported into your application, rather than being called on the commandline.  I suppose it would be nice to have a variety of uis eventually -- from (ba)sh and dos/ps compatable, and whatever RFCs you want to play with.

In any event, simply pass an amount (must be able to be coerced into a `Decimal`), "from unit" and "to unit" (strings) as positional arguments like this:
```
from umpy import convert
convert(1, 'ltr', 'ml')
```

The "from unit" and "to unit" can either be a full unit, like "liter", or a common abbreviation, like "ltr". It will be *slightly* faster if you pass the full name, since umpy doesn't have to figure out what you meant by your abbreviation.

`convert` takes a numeric thing, and two strings that express the notions of `from` and `to`

It will return a Decimal instance with trailing zeros trimmed off of whole numbers.

You may optionally pass in, as a keyword argument, `unit_type`, which can be one of "count", "length", "area", "weight", or "volume".
It is not required to pass this argument in, as umpy will attempt to figure it out -- but it's going to be *slightly* faster, since it doesn't have to do that if you pass it in, so pass it if you know it.

### Exceptions

umpy will raise `TypeError` or `ValueError` if you feed it bad data, or if it can't figure out what you meant.  So you should probably wrap calls to catch these exceptions...


## Compatability

We remain generally compatible with all currently-supported versions of Python; we do not deliberately remove compatibility without careful study.

umpy runs on all modern versions of Python, and probably some older ones...  (3....x?)
