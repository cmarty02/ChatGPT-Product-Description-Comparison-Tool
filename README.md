# Product Description Comparison Tool

## Overview
This Python tool assists in comparing product descriptions to determine if they refer to the same item. It leverages the OpenAI API to analyze and compare descriptions provided by different sources.

## Features
- Load product descriptions from a CSV file.
- Automatically generate questions to compare two descriptions.
- Utilize the OpenAI API to determine the similarity of descriptions.
- Export the results to a CSV file with a new column `Is_Similar`, indicating whether the descriptions are considered similar.

## Output
The script will generate a CSV file with a new column `Is_Similar`, indicating whether the descriptions are considered similar. Here is an example of what the output might look like:

| SKU Description 1                                         | SKU Description 2                                  | Is_Similar |
|-----------------------------------------------------------|----------------------------------------------------|------------|
| TEQ. CUERVO EXTRA AÑEJO 250 ANIVERSARIO                   | TEQ.JCVO.250 ANIV.40% 1/750ML MEX                  | True       |
| TEQ MAESTRO DOBEL BLANCO SPLIT 200ML                      | TEQ. MTRO.DOBEL BCO.38% 12/200ML                   | True       |
| TRADICIONAL CRISTALINO 1750ML                             | MARG.MIX 12/1L                                     | False      |
