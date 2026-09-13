#!/usr/bin/env python3
"""Extract a flat <cities> table from a Football Manager editor Database.xml.

The editor file stores every change as a record in the ``db_changes`` list:

    <record>
        <integer id="database_table_type" value="2"/>      <!-- 2 = city -->
        <large   id="db_unique_id"        value="..."/>    <!-- city id -->
        <unsigned id="property"           value="..."/>    <!-- 4-char code -->
        <string|float|integer|record id="new_value" .../>
        <integer id="version"             value="..."/>
        ...
    </record>

Only the final value of each city property is kept (highest ``version``,
last one in file order on ties).  Reference fields (nation, language, local
region, weather) are written as the referenced DBID plus the 64-bit unique id
of the referenced record; no lookup tables are produced.

Usage:
    python3 extract_cities.py Database.xml cities.xml
"""
import sys
import xml.etree.ElementTree as ET

CITY_TABLE = "2"

# property code -> (output column, kind)
#   scalar : new_value is a <string>/<float>/<integer> element
#   ref    : new_value is a <record> holding <integer id="DBID"> and a <large>
PROPERTIES = {
    "Cnam": ("name", "scalar"),
    "Cnti": ("nation", "ref"),
    "Clgi": ("language", "ref"),
    "Clri": ("local_region", "ref"),
    "Clat": ("latitude", "scalar"),
    "Clon": ("longitude", "scalar"),
    "Cinh": ("inhabitants_range", "scalar"),
    "Catt": ("altitude", "scalar"),
    "Cwea": ("weather", "ref"),
}
COLUMNS = [col for col, _ in PROPERTIES.values()]


def prop_code(value):
    """Decode the unsigned property id into its 4-character code."""
    return int(value).to_bytes(4, "big").decode("latin1")


def child(rec, id_):
    return rec.find("*[@id='%s']" % id_)


def extract(src):
    cities = {}          # uid -> {column: value}
    versions = {}        # (uid, column) -> version used
    for rec in ET.parse(src).getroot().iter("record"):
        table = child(rec, "database_table_type")
        if table is None or table.get("value") != CITY_TABLE:
            continue
        prop = child(rec, "property")
        if prop is None or prop_code(prop.get("value")) not in PROPERTIES:
            continue
        column, kind = PROPERTIES[prop_code(prop.get("value"))]
        uid = child(rec, "db_unique_id").get("value")
        ver = int(child(rec, "version").get("value"))
        new = child(rec, "new_value")
        if new is None:
            continue

        if kind == "scalar":
            value = {column: new.get("value")} if new.tag != "null" else {column: None}
        else:  # reference record: <large id="Nnat"/> + <integer id="DBID"/>
            if new.tag == "null":
                value = {column: None, column + "_uid": None}
            else:
                dbid = child(new, "DBID")
                ref = next((c for c in new if c.tag == "large"), None)
                value = {
                    column: dbid.get("value") if dbid is not None else None,
                    column + "_uid": ref.get("value") if ref is not None else None,
                }

        # keep only the latest version (file order breaks ties)
        if ver >= versions.get((uid, column), -1):
            versions[(uid, column)] = ver
            cities.setdefault(uid, {}).update(value)
    return cities


def write(cities, dst):
    root = ET.Element("cities")
    for uid in sorted(cities, key=int):
        row = cities[uid]
        el = ET.SubElement(root, "city", id=uid)
        for col in COLUMNS:
            if row.get(col) is not None:
                el.set(col, row[col])
            if row.get(col + "_uid") is not None:
                el.set(col + "_uid", row[col + "_uid"])
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write(dst, encoding="utf-8", xml_declaration=True)


def main(argv):
    if len(argv) != 3:
        sys.exit("usage: extract_cities.py Database.xml cities.xml")
    cities = extract(argv[1])
    write(cities, argv[2])
    print("wrote %d cities to %s" % (len(cities), argv[2]))


if __name__ == "__main__":
    main(sys.argv)
