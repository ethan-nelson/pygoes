Pyxrad
======

This repository contains scripts useful for querying and obtaining data from the Amazon Web Services GOES 16/17 archives. For general information on these satellites, visit https://www.goes-r.gov/.

The `example()` script contains an example sequence to use all of the functions. 

Functions
---------

### `get_filenames(product, year, dayofyear, hour, AWS_URL)`

This function queries AWS for a GOES product on a given hour and date (using day of year instead of month and day). An optional `AWS_URL` can be set for archives besides GOES 16--see below for more info. For example, ABI Level 1b data at 02 UTC on January 3rd, 2018 would be called as `get_filenames('ABI-L1b-RadC', '2018', '003', '02')`.

The output is the returned XML body from the AWS query.

### `parse_xml(content)`

This function takes the returned XML from `get_filenames` and extracts all of the file names.

The output is a list of full file names on AWS for the given product, date, and hour.

### `get_files(filelist, save_path='', AWS_URL)`

This function downloads files supplied in a `filelist` list. An optional `save_path` will specify the path where files should be saved; by default, files will be downloaded into the current working directory. An optional `AWS_URL` can be set for archives besides GOES 16--see below for more info.

The output is a list of files saved with their local paths.

Custom `AWS_URL`
---------------

This script is really simple, so right now the url for AWS GOES data is hardcoded in as `"https://s3.amazonaws.com/noaa-goes16/"`. You can alter this url and pass it as an argument to the `get_filenames` and `get_files` functions. The most likely case for this is if you'd prefer to search for GOES 17 data, in which case you would supply `"https://s3.amazonaws.com/noaa-goes17/"`.
