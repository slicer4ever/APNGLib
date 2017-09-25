  APNGLib version 1.0
  
  This program has several tools for working with APNG files.
  The majority of the source code for this tool was written by Max Stepin 
  Wu quantizer is used for true-color files.

  Modified for python by slicer4ever.
  
  Sources used for this tool include:
  http://apng2gif.sourceforge.net/
  http://apngasm.sourceforge.net/
  maxst@users.sourceforge.net

  Copyright (c) 2016-2017 Tim Collins
  
  License: zlib license

------------------
This library is not meant to do heavy work on animated png files, as it was originally built to solve a particular problem.  as the alternatives for apng handling for python seem to be quite lacking at the moment, I have deceided to make these utility functions available in hopes that others in a similar situation will benefit from them.

------------------
Functions available:
``Decompile(SourceFileName, DestFileNaming, TransformFlag [, xOffset, yOffset, xSize, ySize])``
Takes an animated png file and rips out each individiual frame saving them at DestFileNaming#.png
if TransformFlag has TransformCrop set, then xOffset, yOffset, xSize, ySize must be passed to the program, they indicate the bounds to crop in, if those bounds are larger than the image, then no croping occurs).
returns a list of timings for each frame.

``MakeGif(SourceFileName, DestFileName, TransformFlag[, xOffset, yOffset, xSize, ySize])``
Takes an animated png file and converts it to a gif while preserving as much color and transparency information as possible.
if TransformFlag has TransformCrop set, then xOffset, yOffset, xSize, ySize must be passed to the program, they indicate the bounds to crop in, if those bounds are larger than the image, then no croping occurs).
if TransformFlag has TransformNoGif1Frame set, then the function will not create a gif if only 1 frame is found to be in the png file.
  
------------------
Pip installation:
pip install APNGLib

Building for python from scratch:

run: 
python setup.py build
python setup.py install

