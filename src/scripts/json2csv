#!/usr/bin/env python
import os
import io
import csv
import json
import click


def dict_select(data, path):
    if path:
        for path in path.split("."):
            data = data[path]
    return data

def data_clean(data, keys):
    new_data = []
    for row in data:
        new_row = []
        if isinstance(row, dict):
            for key in keys:
                new_row.append(row.get(key, ""))
        else:
            new_row = row
        new_data.append(new_row)
    return new_data

@click.command()
@click.option("-f", "--file", default="-", type=click.File("rb"), help="Input file name, use - for stdin.")
@click.option("--file-encoding", default="utf-8", help="Input file encoding.")
@click.option("-o", "--output", default="-", type=click.File("wb"), help="Output file name, use - for stdout.")
@click.option("--output-encoding", default="utf-8", help="Output file encoding.")
@click.option("-k", "--keys", help="Output field names. Comma separated string list.")
@click.option("-p", "--path", help="Path of the data.")
def convert(file, file_encoding, output, output_encoding, keys, path):
    text = file.read().decode(file_encoding)
    data = json.loads(text)
    data = dict_select(data, path)
    keys = keys and [key.strip() for key in keys.split(",")] or []
    data = data_clean(data, keys)
    output = io.TextIOWrapper(output, encoding=output_encoding)
    writer = csv.writer(output)
    for row in data:
        writer.writerow(row)
    output.close()


if __name__ == "__main__":
    convert()
