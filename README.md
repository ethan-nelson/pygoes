Pyxrad
======

This repository contains scripts useful for querying and obtaining data from the Amazon Web Services GOES archive.

The `example()` script contains an example sequence to use all of the functions. 

Functions
---------

### `get_filenames(product, year, dayofyear, hour)`

This function queries AWS for a GOES product on a given hour and date (using day of year instead of month and day). For example, ABI Level 1b data at 02 UTC on January 3rd, 2018 would be called as `get_filenames('ABI-L1b-RadC', '2018', '003', '02')`.

The output is the returned XML body from the AWS query.

### `parse_xml(content)`

This function takes the returned XML from `get_filenames` and extracts all of the file names.

The output is a list of full file names on AWS for the given product, date, and hour.

### `get_files(filelist, save_path='')`

This function downloads files supplied in a `filelist` list. An optional `save_path` will specify the path where files should be saved; by default, files will be downloaded into the current working directory.

The output is a list of files saved with their local paths.
