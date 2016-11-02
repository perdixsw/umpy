# umpy
Simple unit of measure conversion for python, optimized for manufacturing contexts.

### OK, so what's a "manufacturing context"?
Glad you asked!  At [Perdix Software](https://www.perdixsw.com/), our core product, MOLI, is a mini-ERP system for SMB manufacturing.  We needed a way to simply convert units commonly used in manufacturing.  After reviewing the available options, we decided to write our own simple unit converter, rather than delving into complicated scientific / statistical packages.  This also means that umpy doesn't support units that aren't commonly used in manufacturing. For example, we don't support electrical or temperature based measurements, like amperage, wattage, or degrees. While some manufacturers may make electrical components, it's rare that we'd ever need to convert these types of units *in situ*.

## Usage
umpy is designed to be imported into your application, rather than being called on the commandline.

Simply pass an amount (must be able to be coerced into a `Decimal`), "from unit" and "to unit" (strings) as positional arguments like this:
```
from umpy import convert
convert(1, 'ltr', 'ml')
```

The "from unit" and "to unit" can either be a full unit, like "liter", or a common abbreviation, like "ltr". It will be *slightly* faster if you pass the full name, since umpy doesn't have to figure out what you meant by your abbreviation.

You may optionally pass in, as a keyword argument, `unit_type`, which can be one of "count", "length", "area", "weight", or "volume".
It is not required to pass this argument in, as umpy will attempt to figure it out.  But it's going to be *slightly* faster, since it doesn't have to do that if you pass it in.

### Exceptions

umpy will raise `TypeError` or `ValueError` if you feed it bad data, or if it can't figure out what you meant.  So you should probably wrap calls to catch these exceptions...


## Compatability
umpy is compatible with Python 2.x and 3.x.  It has been tested in 2.7 and 3.5, but should work on other versions. YMMV.

NOTE:  This is extremely young, buggy software. Pull requests are welcome!
