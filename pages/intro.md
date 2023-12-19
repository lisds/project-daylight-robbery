# Introduction

This is a data science project investigating a geographical dataset of crimes recorded by the Metropolitan Police in London. See the table of contents below for the different sections of the project.

# Data

The data used in this project is available on the [London Datastore](https://data.london.gov.uk/dataset/recorded_crime_summary) and is licensed under the [UK Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/).

There are three datasets used in this project with crimes recorded per month from 2010 to 2023. The datasets are split into three different geographical areas: Borough, Ward and LSOA:
1. Borough: crimes recorded per month for each borough in London.

    [2010-2021 download][borough-10-21] | [2021-2023 download][borough-21-23]
2. Ward: crimes recorded per month for each ward in London.

    [2010-2021 download][ward-10-21] | [2021-2023 download][ward-21-23]
3. LSOA: crimes recorded per month for each Lower [Layer Super Output Area (LSOA)][lsoa-ons] in London.

    [2010-2021 download][lsoa-10-21] | [2021-2023 download][lsoa-21-23]

[borough-10-21]: https://data.london.gov.uk/download/recorded_crime_summary/c715dfe5-5174-4ff4-be69-e0744f97575f/MPS%20Borough%20Level%20Crime%20%28Historical%29.csv
[borough-21-23]: https://data.london.gov.uk/download/recorded_crime_summary/138759e5-6365-4827-b7cc-745ea49a84ec/MPS%20Borough%20Level%20Crime%20%28most%20recent%2024%20months%29.csv

[ward-10-21]: https://data.london.gov.uk/download/recorded_crime_summary/42133db2-aff9-43cc-a88e-e4458305a7d3/MPS%20Ward%20Level%20Crime%20%28Historical%29.csv
[ward-21-23]: https://data.london.gov.uk/download/recorded_crime_summary/ed658f91-3e68-4016-aec8-1323a67fd426/MPS%20Ward%20Level%20Crime%20%28most%20recent%2024%20months%29.csv

[lsoa-10-21]: https://data.london.gov.uk/download/recorded_crime_summary/ed658f91-3e68-4016-aec8-1323a67fd426/MPS%20Ward%20Level%20Crime%20%28most%20recent%2024%20months%29.csv
[lsoa-21-23]: https://data.london.gov.uk/download/recorded_crime_summary/d788eec0-7bca-4179-8206-07de041b2ca5/MPS%20LSOA%20Level%20Crime%20%28most%20recent%2024%20months%29.csv
[lsoa-ons]: https://www.ons.gov.uk/methodology/geography/ukgeographies/censusgeographies/census2021geographies#lower-layer-super-output-areas-lsoas
