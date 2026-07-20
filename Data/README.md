# Health Database Schema & Datasets Reference

The data is available here:
https://drive.google.com/file/d/1gXrbZRailJFqAea6XMxFOjnSDBXGNorj/view?usp=sharing

This document provides a comprehensive overview of the tables, column schemas, row counts, and time ranges available in the `Health` database.

## Table: `aidsvu_county_newdiagnoses`
- **Row Count**: 51,552
- **Time Range**: 2008 - 2023
- **Description**: New HIV/AIDS diagnosis rates and counts by county, stratified by demographics.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `year` | *number* | Year the estimate/metric applies to. |
| `geo_id` | *number* | Geographic identifier for the county (e.g., FIPS/GEOID-style code). |
| `state` | *text* | State name for the county record. |
| `state_abbreviation` | *text* | Two-letter state abbreviation. |
| `county_name` | *text* | County name. |
| `new_diagnoses_cases` | *number* | Total number of new diagnoses (all people) for the geography and year. |
| `new_diagnoses_rate` | *number* | Overall new diagnosis rate for the geography and year. |
| `new_diagnoses_rate_stability` | *text* | Stability/quality flag for New_Diagnoses_Rate. |
| `new_diagnoses_male_rate` | *number* | New diagnosis rate for males. |
| `new_diagnoses_male_rate_stability` | *text* | Stability/quality flag for New_Diagnoses_Male_Rate. |
| `new_diagnoses_male_cases` | *number* | Number of new diagnoses among males. |
| `new_diagnoses_female_rate` | *number* | New diagnosis rate for females. |
| `new_diagnoses_female_rate_stability` | *text* | Stability/quality flag for New_Diagnoses_Female_Rate. |
| `new_diagnoses_female_cases` | *number* | Number of new diagnoses among females. |
| `new_diagnoses_black_rate` | *number* | New diagnosis rate among Black people. |
| `new_diagnoses_black_rate_stability` | *text* | Stability/quality flag for New_Diagnoses_Black_Rate. |
| `new_diagnoses_black_cases` | *number* | Number of new diagnoses among Black people. |
| `new_diagnoses_white_rate` | *number* | New diagnosis rate among White people. |
| `new_diagnoses_white_rate_stability` | *text* | Stability/quality flag for New_Diagnoses_White_Rate. |
| `new_diagnoses_white_cases` | *number* | Number of new diagnoses among White people. |
| `new_diagnoses_hispanic_rate` | *number* | New diagnosis rate among Hispanic/Latino people. |
| `new_diagnoses_hispanic_rate_stability` | *text* | Stability/quality flag for New_Diagnoses_Hispanic_Rate. |
| `new_diagnoses_hispanic_cases` | *number* | Number of new diagnoses among Hispanic/Latino people. |
| `new_diagnoses_asian_rate` | *number* | New diagnosis rate among Asian people. |
| `new_diagnoses_asian_rate_stability` | *text* | Stability/quality flag for New_Diagnoses_Asian_Rate. |
| `new_diagnoses_asian_cases` | *number* | Number of new diagnoses among Asian people. |
| `new_diagnoses_american_indian/alaska_native_rate` | *number* | New diagnosis rate among American Indian/Alaska Native people. |
| `new_diagnoses_american_indian/alaska_native_rate_stability` | *text* | Stability/quality flag for AI/AN rate. |
| `new_diagnoses_american_indian/alaska_native_cases` | *number* | Number of new diagnoses among American Indian/Alaska Native people. |
| `new_diagnoses_multiple_races_rate` | *text* | New diagnosis rate among people reporting multiple races. |
| `new_diagnoses_multiple_races_rate_stability` | *text* | Stability/quality flag for multiple-races rate. |
| `new_diagnoses_multiple_races_cases` | *number* | Number of new diagnoses among people reporting multiple races. |
| `new_diagnoses_native_hawaiian/other_pacific_islander_rate` | *number* | New diagnosis rate among Native Hawaiian/Other Pacific Islander people. |
| `new_diagnoses_native_hawaiian/other_pacific_islander_rate_stability` | *text* | Stability/quality flag for NH/OPI rate. |
| `new_diagnoses_native_hawaiian/other_pacific_islander_cases` | *number* | Number of new diagnoses among NH/OPI people. |
| `new_diagnoses_age_13-24_rate` | *number* | New diagnosis rate for ages 13–24. |
| `new_diagnoses_age_13-24_rate_stability` | *text* | Stability/quality flag for age 13–24 rate. |
| `new_diagnoses_age_13-24_cases` | *number* | Number of new diagnoses for ages 13–24. |
| `new_diagnoses_age_25-34_rate` | *number* | New diagnosis rate for ages 25–34. |
| `new_diagnoses_age_25-34_rate_stability` | *text* | Stability/quality flag for age 25–34 rate. |
| `new_diagnoses_age_25-34_cases` | *number* | Number of new diagnoses for ages 25–34. |
| `new_diagnoses_age_35-44_rate` | *number* | New diagnosis rate for ages 35–44. |
| `new_diagnoses_age_35-44_rate_stability` | *text* | Stability/quality flag for age 35–44 rate. |
| `new_diagnoses_age_35-44_cases` | *number* | Number of new diagnoses for ages 35–44. |
| `new_diagnoses_age_45-54_rate` | *number* | New diagnosis rate for ages 45–54. |
| `new_diagnoses_age_45-54_rate_stability` | *text* | Stability/quality flag for age 45–54 rate. |
| `new_diagnoses_age_45-54_cases` | *number* | Number of new diagnoses for ages 45–54. |
| `new_diagnoses_age_55-64_rate` | *number* | New diagnosis rate for ages 55–64. |
| `new_diagnoses_age_55-64_rate_stability` | *text* | Stability/quality flag for age 55–64 rate. |
| `new_diagnoses_age_55-64_cases` | *number* | Number of new diagnoses for ages 55–64. |
| `new_diagnoses_age_65+_rate` | *number* | New diagnosis rate for ages 65 and older. |
| `new_diagnoses_age_65+_rate_stability` | *text* | Stability/quality flag for age 65+ rate. |
| `new_diagnoses_age_65+_cases` | *number* | Number of new diagnoses for ages 65 and older. |
| `new_diagnoses_heterosexual_contact_percent` | *text* | Percent of new diagnoses attributed to heterosexual contact. |
| `new_diagnoses_heterosexual_contact_cases` | *number* | Number of new diagnoses attributed to heterosexual contact. |
| `new_diagnoses_idu_percent` | *text* | Percent of new diagnoses attributed to injection drug use (IDU). |
| `new_diagnoses_idu_cases` | *number* | Number of new diagnoses attributed to injection drug use (IDU). |
| `new_diagnoses_other_transmission_category_percent` | *text* | Percent of new diagnoses attributed to other transmission categories. |
| `new_diagnoses_other_transmission_category_cases` | *number* | Number of new diagnoses attributed to other transmission categories. |
| `new_diagnoses_msm_rate` | *text* | New diagnosis rate for men who have sex with men (MSM) measure (rate definition per dataset). |
| `new_diagnoses_msm_percent` | *text* | Percent of new diagnoses attributed to MSM transmission category. |
| `new_diagnoses_msm_cases` | *number* | Number of new diagnoses attributed to MSM transmission category. |
| `new_diagnoses_msm/idu_percent` | *text* | Percent of new diagnoses attributed to MSM and injection drug use (MSM/IDU). |
| `new_diagnoses_msm/idu_cases` | *number* | Number of new diagnoses attributed to MSM/IDU. |
| `new_diagnoses_male_and_msm_percent` | *text* | Percent of male new diagnoses attributed to MSM transmission category. |
| `new_diagnoses_male_and_msm_cases` | *number* | Number of male new diagnoses attributed to MSM transmission category. |
| `new_diagnoses_male_and_idu_percent` | *text* | Percent of male new diagnoses attributed to IDU. |
| `new_diagnoses_male_and_idu_cases` | *number* | Number of male new diagnoses attributed to IDU. |
| `new_diagnoses_male_and_msm/idu_percent` | *text* | Percent of male new diagnoses attributed to MSM/IDU. |
| `new_diagnoses_male_and_msm/idu_cases` | *number* | Number of male new diagnoses attributed to MSM/IDU. |
| `new_diagnoses_male_and_heterosexual_contact_percent` | *text* | Percent of male new diagnoses attributed to heterosexual contact. |
| `new_diagnoses_male_and_heterosexual_contact_cases` | *number* | Number of male new diagnoses attributed to heterosexual contact. |
| `new_diagnoses_male_and_other_transmission_category_percent` | *text* | Percent of male new diagnoses attributed to other transmission categories. |
| `new_diagnoses_male_and_other_transmission_category_cases` | *number* | Number of male new diagnoses attributed to other transmission categories. |
| `new_diagnoses_female_and_idu_percent` | *text* | Percent of female new diagnoses attributed to IDU. |
| `new_diagnoses_female_and_idu_cases` | *number* | Number of female new diagnoses attributed to IDU. |
| `new_diagnoses_female_and_heterosexual_contact_percent` | *text* | Percent of female new diagnoses attributed to heterosexual contact. |
| `new_diagnoses_female_and_heterosexual_contact_cases` | *number* | Number of female new diagnoses attributed to heterosexual contact. |
| `new_diagnoses_female_and_other_transmission_category_percent` | *text* | Percent of female new diagnoses attributed to other transmission categories. |
| `new_diagnoses_female_and_other_transmission_category_cases` | *number* | Number of female new diagnoses attributed to other transmission categories. |
| `correctional_facility_warning` | *number* | Flag/warning indicating the geography’s estimates may be affected by a correctional facility (per dataset notes). |

---

## Table: `block_groups`
- **Row Count**: 242,748
- **Time Range**: N/A
- **Description**: Geographic boundaries and geometry definitions for Census Block Groups.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `statefp` | *text* | 2-digit State FIPS code. |
| `countyfp` | *text* | 3-digit County FIPS code. |
| `tractce` | *text* | 6-digit Tract code. |
| `blkgrpce` | *text* | 1-digit Block Group code (string). Unique only within a tract. |
| `geoid` | *text* | 12-digit unique FIPS code (string). The Primary Key. Concatenation of statefp (2) + countyfp (3) + tractce (6) + blkgrpce (1). Example: '010419635002'. |
| `geoidfq` | *text* | Fully qualified GEOID (often includes a prefix such as 1500000US + GEOID). |
| `namelsad` | *text* | Name + legal/statistical area description label (e.g., “Block Group 1, Census Tract 1234.56, …”). |
| `mtfcc` | *text* | MAF/TIGER Feature Class Code describing the feature type/class (block group polygon classification code). |
| `funcstat` | *text* | Functional status of the geographic entity (e.g., “S” for statistical; codes vary by product). |
| `aland` | *number* | Land area in square meters. |
| `awater` | *number* | Water area of the feature in square meters. |
| `intptlat` | *text* | Latitude of the internal point (label point) for the polygon, stored as text/decimal degrees. |
| `intptlon` | *text* | Longitude of the internal point (label point) for the polygon, stored as text/decimal degrees. |
| `geometry` | *geometry (Polygon)* | Polygon boundary of the Block Group (subset of a tract). |

---

## Table: `cdc_county_2025`
- **Row Count**: 3,143
- **Time Range**: N/A
- **Description**: CDC PLACES health estimates (e.g., diabetes, obesity, depression) aggregated at the County level.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `stateabbr` | *Text* | State abbreviation |
| `statedesc` | *Text* | State name |
| `countyname` | *Text* | County name |
| `countyfips` | *Text* | County FIPS code |
| `totalpopulation` | *Number* | Total population of census  estimates |
| `totalpop18plus` | *Number* | Total population 18 and plus of census  estimates |
| `access2_crudeprev` | *Number* | Model-based estimate for crude prevalence of current lack of health insurance among adults aged 18-64 years,  |
| `access2_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of health insurance among adults aged 18-64 years |
| `access2_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of lack of health insurance among adults aged 18-64 years,  |
| `access2_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of lack of health insurance among adults aged 18-64 years |
| `arthritis_crudeprev` | *Number* | Model-based estimate for crude prevalence of arthritis among adults,  |
| `arthritis_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of arthritis among adults |
| `arthritis_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of arthritis among adults,  |
| `arthritis_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence estimate of arthritis among adults |
| `binge_crudeprev` | *Number* | Model-based estimate for crude prevalence of binge drinking among adults,  |
| `binge_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of binge drinking among adults |
| `binge_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of binge drinking among adults,  |
| `binge_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of binge drinking among adults |
| `bphigh_crudeprev` | *Number* | Model-based estimate for crude prevalence of high blood pressure among adults,  |
| `bphigh_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of high blood pressure among adults |
| `bphigh_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of high blood pressure among adults,  |
| `bphigh_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of high blood pressure among adults |
| `bpmed_crudeprev` | *Number* | Model-based estimate for crude prevalence of taking medicine to control high blood pressure among adults with high blood pressure,  |
| `bpmed_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of taking medicine to control high blood pressure among adults with high blood pressure |
| `bpmed_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of taking medicine to control high blood pressure among adults with high blood pressure,  |
| `bpmed_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of taking medicine to control high blood pressure among adults with high blood pressure |
| `cancer_crudeprev` | *Number* | Model-based estimate for crude prevalence of cancer (non-skin) or melanoma among adults,  |
| `cancer_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cancer (non-skin) or melanoma among adults |
| `cancer_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of cancer (non-skin) or melanoma among adults,  |
| `cancer_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of cancer (non-skin) or melanoma among adults |
| `casthma_crudeprev` | *Number* | Model-based estimate for crude prevalence of current asthma among adults,  |
| `casthma_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of current asthma among adults |
| `casthma_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of current asthma among adults,  |
| `casthma_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of current asthma among adults |
| `chd_crudeprev` | *Number* | Model-based estimate for crude prevalence of coronary heart disease among adults,  |
| `chd_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of coronary heart disease among adults |
| `chd_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of coronary heart disease among adults,  |
| `chd_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of coronary heart disease among adults |
| `checkup_crudeprev` | *Number* | Model-based estimate for crude prevalence of routine checkup within the past year among adults,  |
| `checkup_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of routine checkup within the past year among adults |
| `checkup_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of routine checkup within the past year among adults,  |
| `checkup_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of routine checkup within the past year among adults |
| `cholscreen_crudeprev` | *Number* | Model-based estimate for crude prevalence of cholesterol screening within the past 5 years among adults,  |
| `cholscreen_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cholesterol screening within the past 5 years among adults |
| `cholscreen_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of cholesterol screening within the past 5 years among adults,  |
| `cholscreen_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of cholesterol screening within the past 5 years among adults |
| `colon_screen_crudeprev` | *Number* | Model-based estimate for crude prevalence of colorectal cancer screening among adults aged 45–75 years, 2022 |
| `colon_screen_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of colorectal cancer screening among adults aged 45–75 years |
| `colon_screen_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of colorectal cancer screening among adults aged 45–75 years, 2022 |
| `colon_screen_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of colorectal cancer screening among adults aged 45–75 years |
| `copd_crudeprev` | *Number* | Model-based estimate for crude prevalence of chronic obstructive pulmonary disease among adults,  |
| `copd_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of chronic obstructive pulmonary disease among adults |
| `copd_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of chronic obstructive pulmonary disease among adults,  |
| `copd_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of chronic obstructive pulmonary disease among adults |
| `csmoking_crudeprev` | *Number* | Model-based estimate for crude prevalence of current cigarette smoking among adults,  |
| `csmoking_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of current cigarette smoking among adults |
| `csmoking_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of current cigarette smoking among adults,  |
| `csmoking_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of current cigarette smoking among adults |
| `dental_crudeprev` | *Number* | Model-based estimate for crude prevalence of visited dentist or dental clinic in the past year among adults, 2022 |
| `dental_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of visited dentist or dental clinic in the past year among adults |
| `dental_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of visited dentist or dental clinic in the past year among adults, 2022 |
| `dental_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of visited dentist or dental clinic in the past year among adults |
| `depression_crudeprev` | *Number* | Model-based estimate for crude prevalence of depression among adults,  |
| `depression_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of depression among adults |
| `depression_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of depression among adults,  |
| `depression_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of depression among adults |
| `diabetes_crudeprev` | *Number* | Model-based estimate for crude prevalence of diagnosed diabetes among adults,  |
| `diabetes_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of diagnosed diabetes among adults |
| `diabetes_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of diagnosed diabetes among adults,  |
| `diabetes_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of diagnosed diabetes among adults |
| `ghlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of fair or poor health among adults,  |
| `ghlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of fair or poor health among adults |
| `ghlth_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of fair or poor health among adults,  |
| `ghlth_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of fair or poor health among adults |
| `highchol_crudeprev` | *Number* | Model-based estimate for crude prevalence of high cholesterol among adults who have ever been screened,  |
| `highchol_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of high cholesterol among adults who have ever been screened |
| `highchol_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of high cholesterol among adults who have ever been screened,  |
| `highchol_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of high cholesterol among adults who have ever been screened |
| `lpa_crudeprev` | *Number* | Model-based estimate for crude prevalence of no leisure-time physical activity among adults,  |
| `lpa_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of no leisure-time physical activity among adults |
| `lpa_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of no leisure-time physical activity among adults,  |
| `lpa_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of no leisure-time physical activity among adults |
| `mammouse_crudeprev` | *Number* | Model-based estimate for crude prevalence of mammography use among women aged 50–74 years, 2022 |
| `mammouse_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of mammography use among women aged 50–74 years |
| `mammouse_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of mammography use among women aged 50–74 years, 2022 |
| `mammouse_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of mammography use among women aged 50–74 years |
| `mhlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of frequent mental distress among adults,  |
| `mhlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of frequent mental distress among adults |
| `mhlth_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of frequent mental distress among adults,  |
| `mhlth_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of frequent mental distress among adults |
| `obesity_crudeprev` | *Number* | Model-based estimate for crude prevalence of obesity among adults,  |
| `obesity_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of obesity among adults |
| `obesity_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of obesity among adults,  |
| `obesity_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of obesity among adults |
| `phlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of frequent physical distress among adults,  |
| `phlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of frequent physical distress among adults |
| `phlth_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of frequent physical distress among adults,  |
| `phlth_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of frequent physical distress among adults |
| `sleep_crudeprev` | *Number* | Model-based estimate for crude prevalence of short sleep duration among adults, 2022 |
| `sleep_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of short sleep duration among adults |
| `sleep_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of short sleep duration among adults, 2022 |
| `sleep_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of short sleep duration among adults |
| `stroke_crudeprev` | *Number* | Model-based estimate for crude prevalence of stroke among adults,  |
| `stroke_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of stroke among adults |
| `stroke_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of stroke among adults,  |
| `stroke_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of stroke among adults |
| `teethlost_crudeprev` | *Number* | Model-based estimate for crude prevalence of all teeth lost among adults aged >=65 years, 2022 |
| `teethlost_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of all teeth lost among adults aged >=65 years |
| `teethlost_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of all teeth lost among adults aged >=65 years, 2022 |
| `teethlost_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of all teeth lost among adults aged >=65 years |
| `hearing_crudeprev` | *Number* | Model-based estimate for crude prevalence of hearing disability among adults,  |
| `hearing_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of hearing disability among adults |
| `hearing_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of hearing disability among adults,  |
| `hearing_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of hearing disability among adults |
| `vision_crudeprev` | *Number* | Model-based estimate for crude prevalence of vision disability among adults,  |
| `vision_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of vision disability among adults |
| `vision_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of vision disability among adults,  |
| `vision_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of vision disability among adults |
| `cognition_crudeprev` | *Number* | Model-based estimate for crude prevalence of cognitive disability among adults,  |
| `cognition_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cognitive disability among adults |
| `cognition_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of cognitive disability among adults,  |
| `cognition_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of cognitive disability among adults |
| `mobility_crudeprev` | *Number* | Model-based estimate for crude prevalence of mobility disability among adults,  |
| `mobility_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of mobility disability among adults |
| `mobility_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of mobility disability among adults,  |
| `mobility_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of mobility disability among adults |
| `selfcare_crudeprev` | *Number* | Model-based estimate for crude prevalence of self-care disability among adults,  |
| `selfcare_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of self-care disability among adults |
| `selfcare_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of self-care disability among adults,  |
| `selfcare_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of self-care disability among adults |
| `indeplive_crudeprev` | *Number* | Model-based estimate for crude prevalence of independent living disability among adults,  |
| `indeplive_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of independent living disability among adults |
| `indeplive_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of independent living disability among adults,  |
| `indeplive_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of independent living disability among adults |
| `disability_crudeprev` | *Number* | Model-based estimate for crude prevalence of any disability among adults,  |
| `disability_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of any disability among adults |
| `disability_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of any disability among adults,  |
| `disability_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of any disability among adults |
| `loneliness_crudeprev` | *Number* | Model-based estimate for crude prevalence of feeling socially isolated among adults,  |
| `loneliness_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of feeling socially isolated among adults |
| `loneliness_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of feeling socially isolated among adults,  |
| `loneliness_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of feeling socially isolated among adults |
| `foodstamp_crudeprev` | *Number* | Model-based estimate for crude prevalence of received food stamps in the past 12 months among adults,  |
| `foodstamp_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of received food stamps in the past 12 months among adults |
| `foodstamp_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of received food stamps in the past 12 months among adults,  |
| `foodstamp_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of received food stamps in the past 12 months among adults |
| `foodinsecu_crudeprev` | *Number* | Model-based estimate for crude prevalence of food insecurity in the past 12 months among adults,  |
| `foodinsecu_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of food insecurity in the past 12 months among adults |
| `foodinsecu_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of food insecurity in the past 12 months among adults,  |
| `foodinsecu_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of food insecurity in the past 12 months among adults |
| `housinsecu_crudeprev` | *Number* | Model-based estimate for crude prevalence of housing insecurity in the past 12 months among adults,  |
| `housinsecu_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of housing insecurity in the past 12 months among adults |
| `housinsecu_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of housing insecurity in the past 12 months among adults,  |
| `housinsecu_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of housing insecurity in the past 12 months among adults |
| `shututility_crudeprev` | *Number* | Model-based estimate for crude prevalence of utility services threat in the past 12 months among adults,  |
| `shututility_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of utility services threat in the past 12 months among adults |
| `shututility_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of utility services threat in the past 12 months among adults,  |
| `shututility_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of utility services threat in the past 12 months among adults |
| `lacktrpt_crudeprev` | *Number* | Model-based estimate for crude prevalence of lack of reliable transportation in the past 12 months among adults,  |
| `lacktrpt_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of reliable transportation in the past 12 months among adults |
| `lacktrpt_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of lack of reliable transportation in the past 12 months among adults,  |
| `lacktrpt_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of lack of reliable transportation in the past 12 months among adults |
| `emotionspt_crudeprev` | *Number* | Model-based estimate for crude prevalence of lack of social and emotional support among adults,  |
| `emotionspt_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of social and emotional support among adults |
| `emotionspt_adjprev` | *Number* | Model-based estimate for age-adjusted prevalence of lack of social and emotional support among adults,  |
| `emotionspt_adj95ci` | *Text* | Estimated confidence interval for age-adjusted prevalence of lack of social and emotional support among adults |
| `geolocation` | *Point* | Latitude, Longitude of county centroid (Format: Point(Longitude Latitude)) |

---

## Table: `cdc_tract_2025`
- **Row Count**: 83,522
- **Time Range**: N/A
- **Description**: CDC PLACES health estimates aggregated at the Census Tract level.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `stateabbr` | *Text* | State abbreviation |
| `statedesc` | *Text* | State name |
| `countyname` | *Text* | County name |
| `countyfips` | *Text* | County FIPS code |
| `tractfips` | *Text* | Census tract FIPS code |
| `totalpopulation` | *Text* | Total population of Census 2020 |
| `totalpop18plus` | *Number* | Total population 18 and plus of Census 2020 |
| `access2_crudeprev` | *Number* | Model-based estimate for crude prevalence of lack of health insurance among adults aged 18-64 years,  |
| `access2_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of health insurance among adults aged 18-64 years |
| `arthritis_crudeprev` | *Number* | Model-based estimate for crude prevalence of arthritis among adults,  |
| `arthritis_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of arthritis among adults |
| `binge_crudeprev` | *Number* | Model-based estimate for crude prevalence of binge drinking among adults,  |
| `binge_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of binge drinking among adults |
| `bphigh_crudeprev` | *Number* | Model-based estimate for crude prevalence of high blood pressure among adults,  |
| `bphigh_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of high blood pressure among adults |
| `bpmed_crudeprev` | *Number* | Model-based estimate for crude prevalence of taking medicine to control high blood pressure among adults with high blood pressure,  |
| `bpmed_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of taking medicine to control high blood pressure among adults with high blood pressure |
| `cancer_crudeprev` | *Number* | Model-based estimate for crude prevalence of cancer (non-skin) or melanoma among adults,  |
| `cancer_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cancer (non-skin) or melanoma among adults |
| `casthma_crudeprev` | *Number* | Model-based estimate for crude prevalence of current asthma among adults,  |
| `casthma_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of current asthma among adults |
| `chd_crudeprev` | *Number* | Model-based estimate for crude prevalence of coronary heart disease among adults,  |
| `chd_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of coronary heart disease among adults |
| `checkup_crudeprev` | *Number* | Model-based estimate for crude prevalence of routine checkup within the past year among adults,  |
| `checkup_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of routine checkup within the past year among adults |
| `cholscreen_crudeprev` | *Number* | Model-based estimate for crude prevalence of cholesterol screening within the past 5 years among adults,  |
| `cholscreen_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cholesterol screening within the past 5 years among adults |
| `colon_screen_crudeprev` | *Number* | Model-based estimate for crude prevalence of colorectal cancer screening among adults aged 45–75 years, 2022 |
| `colon_screen_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of colorectal cancer screening among adults aged 45–75 years |
| `copd_crudeprev` | *Number* | Model-based estimate for crude prevalence of chronic obstructive pulmonary disease among adults,  |
| `copd_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of chronic obstructive pulmonary disease among adults |
| `csmoking_crudeprev` | *Number* | Model-based estimate for crude prevalence of current cigarette smoking among adults,  |
| `csmoking_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of current cigarette smoking among adults |
| `dental_crudeprev` | *Number* | Model-based estimate for crude prevalence of visited dentist or dental clinic in the past year among adults, 2022 |
| `dental_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of visited dentist or dental clinic in the past year among adults |
| `depression_crudeprev` | *Number* | Model-based estimate for crude prevalence of depression among adults,  |
| `depression_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of depression among adults,  |
| `diabetes_crudeprev` | *Number* | Model-based estimate for crude prevalence of diagnosed diabetes among adults,  |
| `diabetes_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of diagnosed diabetes among adults |
| `ghlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of fair or poor health among adults,  |
| `ghlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of fair or poor health among adults |
| `highchol_crudeprev` | *Number* | Model-based estimate for crude prevalence of high cholesterol among adults who have ever been screened,  |
| `highchol_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of high cholesterol among adults who have ever been screened |
| `lpa_crudeprev` | *Number* | Model-based estimate for crude prevalence of no leisure-time physical activity among adults,  |
| `lpa_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of no leisure-time physical activity among adults |
| `mammouse_crudeprev` | *Number* | Model-based estimate for crude prevalence of mammography use among women aged 50–74 years, 2022 |
| `mammouse_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of mammography use among women aged 50–74 years |
| `mhlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of frequent mental distress among adults,  |
| `mhlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of frequent mental distress among adults |
| `obesity_crudeprev` | *Number* | Model-based estimate for crude prevalence of obesity among adults,  |
| `obesity_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of obesity among adults |
| `phlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of frequent physical distress among adults,  |
| `phlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of frequent physical distress among adults |
| `sleep_crudeprev` | *Number* | Model-based estimate for crude prevalence of short sleep duration among adults, 2022 |
| `sleep_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of short sleep duration among adults |
| `stroke_crudeprev` | *Number* | Model-based estimate for crude prevalence of stroke among adults,  |
| `stroke_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of stroke among adults |
| `teethlost_crudeprev` | *Number* | Model-based estimate for crude prevalence of all teeth lost among adults aged >=65 years, 2022 |
| `teethlost_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of all teeth lost among adults aged >=65 years |
| `hearing_crudeprev` | *Number* | Model-based estimate for crude prevalence of hearing disability among adults,  |
| `hearing_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of hearing disability among adults |
| `vision_crudeprev` | *Number* | Model-based estimate for crude prevalence of vision disability among adults,  |
| `vision_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of vision disability among adults |
| `cognition_crudeprev` | *Number* | Model-based estimate for crude prevalence of cognitive disability among adults,  |
| `cognition_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cognitive disability among adults |
| `mobility_crudeprev` | *Number* | Model-based estimate for crude prevalence of mobility disability among adults,  |
| `mobility_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of mobility disability among adults |
| `selfcare_crudeprev` | *Number* | Model-based estimate for crude prevalence of self-care disability among adults,  |
| `selfcare_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of self-care disability among adults |
| `indeplive_crudeprev` | *Number* | Model-based estimate for crude prevalence of independent living disability among adults,  |
| `indeplive_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of independent living disability among adults |
| `disability_crudeprev` | *Number* | Model-based estimate for crude prevalence of any disability among adults,  |
| `disability_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of any disability among adults |
| `loneliness_crudeprev` | *Number* | Model-based estimate for crude prevalence of loneliness among adults,  |
| `loneliness_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of loneliness among adults |
| `foodstamp_crudeprev` | *Number* | Model-based estimate for crude prevalence of received food stamps in the past 12 months among adults,  |
| `foodstamp_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of received food stamps in the past 12 months among adults |
| `foodinsecu_crudeprev` | *Number* | Model-based estimate for crude prevalence of food insecurity in the past 12 months among adults,  |
| `foodinsecu_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of food insecurity in the past 12 months among adults |
| `housinsecu_crudeprev` | *Number* | Model-based estimate for crude prevalence of housing insecurity in the past 12 months among adults,  |
| `housinsecu_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of housing insecurity in the past 12 months among adults |
| `shututility_crudeprev` | *Number* | Model-based estimate for crude prevalence of utility services threat in the past 12 months among adults,  |
| `shututility_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of utility services threat in the past 12 months among adults |
| `lacktrpt_crudeprev` | *Number* | Model-based estimate for crude prevalence of lack of reliable transportation in the past 12 months among adults,  |
| `lacktrpt_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of reliable transportation in the past 12 months among adults |
| `emotionspt_crudeprev` | *Number* | Model-based estimate for crude prevalence of lack of social and emotional support among adults,  |
| `emotionspt_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of social and emotional support among adults |
| `geolocation` | *Point* | Latitude, Longitude of tract centroid (Format: Point(Longitude Latitude)) |

---

## Table: `cdc_zipcode_2025`
- **Row Count**: 32,520
- **Time Range**: N/A
- **Description**: CDC PLACES health estimates aggregated at the Zip Code (ZCTA) level.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `zcta5` | *Text* | 5 digits ZIP Code Tabulation Area (ZCTA) Code |
| `totalpopulation` | *Number* | Total population of Census 2020 |
| `totalpop18plus` | *Number* | Total population 18 and plus of Census 2020 |
| `access2_crudeprev` | *Number* | Model-based estimate for crude prevalence of lack of health insurance among adults aged 18-64 years,  |
| `access2_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of health insurance among adults aged 18-64 years |
| `arthritis_crudeprev` | *Number* | Model-based estimate for crude prevalence of arthritis among adults,  |
| `arthritis_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of arthritis among adults |
| `binge_crudeprev` | *Number* | Model-based estimate for crude prevalence of binge drinking among adults,  |
| `binge_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of binge drinking among adults |
| `bphigh_crudeprev` | *Number* | Model-based estimate for crude prevalence of high blood pressure among adults,  |
| `bphigh_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of high blood pressure among adults |
| `bpmed_crudeprev` | *Number* | Model-based estimate for crude prevalence of taking medicine to control high blood pressure among adults with high blood pressure,  |
| `bpmed_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of taking medicine to control high blood pressure among adults with high blood pressure |
| `cancer_crudeprev` | *Number* | Model-based estimate for crude prevalence of cancer (non-skin) or melanoma among adults,  |
| `cancer_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cancer (non-skin) or melanoma among adults |
| `casthma_crudeprev` | *Number* | Model-based estimate for crude prevalence of current asthma among adults,  |
| `casthma_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of current asthma among adults |
| `chd_crudeprev` | *Number* | Model-based estimate for crude prevalence of coronary heart disease among adults,  |
| `chd_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of coronary heart disease among adults |
| `checkup_crudeprev` | *Number* | Model-based estimate for crude prevalence of routine checkup within the past year among adults,  |
| `checkup_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of routine checkup within the past year among adults |
| `cholscreen_crudeprev` | *Number* | Model-based estimate for crude prevalence of cholesterol screening within the past 5 years among adults,  |
| `cholscreen_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cholesterol screening within the past 5 years among adults |
| `colon_screen_crudeprev` | *Number* | Model-based estimate for crude prevalence of colorectal cancer screening among adults aged 45–75 years, 2022 |
| `colon_screen_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of colorectal cancer screening among adults aged 45–75 years |
| `copd_crudeprev` | *Number* | Model-based estimate for crude prevalence of chronic obstructive pulmonary disease among adults,  |
| `copd_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of chronic obstructive pulmonary disease among adults |
| `csmoking_crudeprev` | *Number* | Model-based estimate for crude prevalence of current cigarette smoking among adults,  |
| `csmoking_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of current cigarette smoking among adults |
| `dental_crudeprev` | *Number* | Model-based estimate for crude prevalence of visited dentist or dental clinic in the past year among adults, 2022 |
| `dental_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of visited dentist or dental clinic in the past year among adults |
| `depression_crudeprev` | *Number* | Model-based estimate for crude prevalence of depression among adults,  |
| `depression_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of depression among adults |
| `diabetes_crudeprev` | *Number* | Model-based estimate for crude prevalence of diagnosed diabetes among adults,  |
| `diabetes_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of diagnosed diabetes among adults |
| `ghlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of fair or poor health among adults,  |
| `ghlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of fair or poor health among adults |
| `highchol_crudeprev` | *Number* | Model-based estimate for crude prevalence of high cholesterol among adults who have ever been screened,  |
| `highchol_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of high cholesterol among adults who have ever been screened |
| `lpa_crudeprev` | *Number* | Model-based estimate for crude prevalence of no leisure-time physical activity among adults,  |
| `lpa_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of no leisure-time physical activity among adults |
| `mammouse_crudeprev` | *Number* | Model-based estimate for crude prevalence of mammography use among women aged 50–74 years, 2022 |
| `mammouse_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of mammography use among women aged 50–74 years |
| `mhlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of frequent mental distress among adults,  |
| `mhlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of frequent mental distress among adults |
| `obesity_crudeprev` | *Number* | Model-based estimate for crude prevalence of obesity among adults,  |
| `obesity_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of obesity among adults |
| `phlth_crudeprev` | *Number* | Model-based estimate for crude prevalence of frequent physical distress among adults,  |
| `phlth_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of frequent physical distress among adults |
| `sleep_crudeprev` | *Number* | Model-based estimate for crude prevalence of short sleep duration among adults, 2022 |
| `sleep_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of short sleep duration among adults |
| `stroke_crudeprev` | *Number* | Model-based estimate for crude prevalence of stroke among adults,  |
| `stroke_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of stroke among adults |
| `teethlost_crudeprev` | *Number* | Model-based estimate for crude prevalence of all teeth lost among adults aged >=65 years, 2022 |
| `teethlost_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of all teeth lost among adults aged >=65 years |
| `hearing_crudeprev` | *Number* | Model-based estimate for crude prevalence of hearing disability among adults,  |
| `hearing_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of hearing disability among adults |
| `vision_crudeprev` | *Number* | Model-based estimate for crude prevalence of vision disability among adults,  |
| `vision_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of vision disability among adults |
| `cognition_crudeprev` | *Number* | Model-based estimate for crude prevalence of cognitive disability among adults,  |
| `cognition_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of cognitive disability among adults |
| `mobility_crudeprev` | *Number* | Model-based estimate for crude prevalence of mobility disability among adults,  |
| `mobility_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of mobility disability among adults |
| `selfcare_crudeprev` | *Number* | Model-based estimate for crude prevalence of self-care disability among adults,  |
| `selfcare_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of self-care disability among adults |
| `indeplive_crudeprev` | *Number* | Model-based estimate for crude prevalence of independent living disability among adults,  |
| `indeplive_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of independent living disability among adults |
| `disability_crudeprev` | *Number* | Model-based estimate for crude prevalence of any disability among adults,  |
| `disability_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of any disability among adults |
| `loneliness_crudeprev` | *Number* | Model-based estimate for crude prevalence of loneliness among adults,  |
| `loneliness_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of loneliness among adults |
| `foodstamp_crudeprev` | *Number* | Model-based estimate for crude prevalence of received food stamps in the past 12 months among adults,  |
| `foodstamp_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of received food stamps in the past 12 months among adults |
| `foodinsecu_crudeprev` | *Number* | Model-based estimate for crude prevalence of food insecurity in the past 12 months among adults,  |
| `foodinsecu_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of food insecurity in the past 12 months among adults |
| `housinsecu_crudeprev` | *Number* | Model-based estimate for crude prevalence of housing insecurity in the past 12 months among adults,  |
| `housinsecu_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of housing insecurity in the past 12 months among adults |
| `shututility_crudeprev` | *Number* | Model-based estimate for crude prevalence of utility services threat in the past 12 months among adults,  |
| `shututility_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of utility services threat in the past 12 months among adults |
| `lacktrpt_crudeprev` | *Number* | Model-based estimate for crude prevalence of lack of reliable transportation in the past 12 months among adults,  |
| `lacktrpt_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of reliable transportation in the past 12 months among adults |
| `emotionspt_crudeprev` | *Number* | Model-based estimate for crude prevalence of lack of social and emotional support among adults,  |
| `emotionspt_crude95ci` | *Text* | Estimated confidence interval for crude prevalence of lack of social and emotional support among adults |
| `geolocation` | *Point* | Latitude, Longitude of ZCTA centroid (Format: Point(Longitude Latitude)) |

---

## Table: `census_tracts`
- **Row Count**: 85,529
- **Time Range**: N/A
- **Description**: Geographic boundaries and geometry definitions for Census Tracts.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `statefp` | *text* | 2-digit State FIPS code. |
| `countyfp` | *text* | 3-digit County FIPS code. |
| `tractce` | *text* | 6-digit Tract code (string). Unique only within a county. often implies a decimal (e.g., '001902' is tract 19.02). |
| `geoid` | *text* | 11-digit unique FIPS code (string). The Primary Key. Concatenation of statefp (2) + countyfp (3) + tractce (6). Example: '11001001902'. |
| `geoidfq` | *text* | Fully qualified GEOID (often a prefix like 1400000US + GEOID). |
| `name` | *text* | Short tract name (e.g., '19.02'). |
| `namelsad` | *text* | Name + legal/statistical area description (e.g., “Census Tract 1234.56”). |
| `mtfcc` | *text* | MAF/TIGER Feature Class Code identifying the feature class for census tract polygons. |
| `funcstat` | *text* | Functional status code indicating whether the tract is statistical/active (code set depends on vintage). |
| `aland` | *number* | Land area in square meters. |
| `awater` | *number* | Water area of the tract in square meters. |
| `intptlat` | *text* | Latitude of an internal point (label point) for the tract polygon (decimal degrees, often stored as text). |
| `intptlon` | *text* | Longitude of an internal point (label point) for the tract polygon (decimal degrees, often stored as text). |
| `geometry` | *geometry (Polygon)* | Polygon boundary of the Census Tract. |

---

## Table: `counties`
- **Row Count**: 3,235
- **Time Range**: N/A
- **Description**: Geographic boundaries, FIPS codes, and geometry definitions for US Counties.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `statefp` | *text* | 2-digit State FIPS code. Foreign key to the states table. |
| `countyfp` | *text* | 3-digit County FIPS code (string). Unique ONLY within a state (e.g., '075'). WARNING: Do not use this alone to join; combine with statefp or use 'geoid'. |
| `countyns` | *text* | Census county numeric identifier (GNIS-style permanent ID for the county entity). |
| `geoid` | *text* | 5-digit unique FIPS code (string). The Primary Key. Concatenation of statefp (2 digits) + countyfp (3 digits). Example: '40075'. Use this to join with other datasets containing full county FIPS. |
| `geoidfq` | *text* | Fully qualified GEOID (often a prefix like 0500000US + GEOID). |
| `name` | *text* | Short name of the county (e.g., 'Kiowa'). Does not include the word 'County'. |
| `namelsad` | *text* | Full legal name of the county (e.g., 'Kiowa County'). |
| `lsad` | *text* | Legal/Statistical Area Description code indicating the type of county-equivalent (e.g., county, parish, borough). |
| `classfp` | *text* | FIPS class code describing the county/county-equivalent classification (administrative/statistical type). |
| `mtfcc` | *text* | MAF/TIGER Feature Class Code identifying the feature class for the county polygon. |
| `csafp` | *text* | Combined Statistical Area (CSA) code (if the county is in a CSA; otherwise blank). |
| `cbsafp` | *text* | Core Based Statistical Area (CBSA) code for metro/micro area membership (if applicable). |
| `metdivfp` | *text* | Metropolitan Division code (subdivision of certain large CBSAs; if applicable). |
| `funcstat` | *text* | Functional status of the entity (e.g., active/statistical; code set varies by vintage). |
| `aland` | *number* | Land area in square meters. |
| `awater` | *number* | Water area of the county in square meters. |
| `intptlat` | *text* | Latitude of an internal point (label point) for the county polygon (decimal degrees, often stored as text). |
| `intptlon` | *text* | Longitude of an internal point (label point) for the county polygon (decimal degrees, often stored as text). |
| `geometry` | *geometry (Polygon)* | Polygon boundary of the County. |

---

## Table: `edu_attain_pop_25plus`
- **Row Count**: 242,297
- **Time Range**: N/A
- **Description**: Educational attainment data (e.g., degrees earned) for the population aged 25 and over.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier (e.g., Census GEOID) for the area. |
| `geographic_area_name` | *text* | Human-readable name/label of the geographic area. |
| `estimate_total` | *text* | Total estimated population age 25 years and over. |
| `estimate_total_no_schooling_completed` | *text* | Estimated number age 25+ with no schooling completed. |
| `estimate_total_nursery_school` | *text* | Estimated number age 25+ whose highest level is nursery school. |
| `estimate_total_kindergarten` | *text* | Estimated number age 25+ whose highest level is kindergarten. |
| `estimate_total_1st_grade` | *text* | Estimated number age 25+ whose highest level is 1st grade. |
| `estimate_total_2nd_grade` | *text* | Estimated number age 25+ whose highest level is 2nd grade. |
| `estimate_total_3rd_grade` | *text* | Estimated number age 25+ whose highest level is 3rd grade. |
| `estimate_total_4th_grade` | *text* | Estimated number age 25+ whose highest level is 4th grade. |
| `estimate_total_5th_grade` | *text* | Estimated number age 25+ whose highest level is 5th grade. |
| `estimate_total_6th_grade` | *text* | Estimated number age 25+ whose highest level is 6th grade. |
| `estimate_total_7th_grade` | *text* | Estimated number age 25+ whose highest level is 7th grade. |
| `estimate_total_8th_grade` | *text* | Estimated number age 25+ whose highest level is 8th grade. |
| `estimate_total_9th_grade` | *text* | Estimated number age 25+ whose highest level is 9th grade. |
| `estimate_total_10th_grade` | *text* | Estimated number age 25+ whose highest level is 10th grade. |
| `estimate_total_11th_grade` | *text* | Estimated number age 25+ whose highest level is 11th grade. |
| `estimate_total_12th_grade_no_diploma` | *text* | Estimated number age 25+ with 12th grade completed but no diploma. |
| `estimate_total_regular_high_school_diploma` | *text* | Estimated number age 25+ with a regular high school diploma. |
| `estimate_total_ged_or_alternative_credential` | *text* | Estimated number age 25+ with GED or alternative credential. |
| `estimate_total_some_college_less_than_1_year` | *text* | Estimated number age 25+ with some college but less than 1 year completed. |
| `estimate_total_some_college_1_or_more_years_no_degree` | *text* | Estimated number age 25+ with some college (≥1 year) but no degree. |
| `estimate_total_associate_s_degree` | *text* | Estimated number age 25+ with an associate’s degree. |
| `estimate_total_bachelor_s_degree` | *text* | Estimated number age 25+ with a bachelor’s degree. |
| `estimate_total_master_s_degree` | *text* | Estimated number age 25+ with a master’s degree. |
| `estimate_total_professional_school_degree` | *text* | Estimated number age 25+ with a professional school degree (e.g., JD, MD). |
| `estimate_total_doctorate_degree` | *text* | Estimated number age 25+ with a doctorate degree (e.g., PhD). |

---

## Table: `employment_status`
- **Row Count**: 85,382
- **Time Range**: N/A
- **Description**: General employment metrics including labor force participation and unemployment rates.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier for the area (e.g., GEOID). |
| `geographic_area_name` | *text* | Human-readable name of the geographic area. |
| `estimate_total_population_16_years_and_over` | *text* | Estimated total population age 16 years and over. |
| `estimate_total_population_16_years_and_over_age_16_to_19_years` | *text* | Estimated population age 16–19 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_20_to_24_years` | *text* | Estimated population age 20–24 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_25_to_29_years` | *text* | Estimated population age 25–29 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_30_to_34_years` | *text* | Estimated population age 30–34 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_35_to_44_years` | *text* | Estimated population age 35–44 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_45_to_54_years` | *text* | Estimated population age 45–54 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_55_to_59_years` | *text* | Estimated population age 55–59 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_60_to_64_years` | *text* | Estimated population age 60–64 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_65_to_74_years` | *text* | Estimated population age 65–74 years (within population 16+). |
| `estimate_total_population_16_years_and_over_age_75_yea_f90a7e66` | *text* | Estimated population age 75 years and over (within population 16+). |
| `estimate_total_population_16_years_and_over_race_and_h_75b99d1e` | *text* | Estimated population 16+ who are White alone. |
| `estimate_total_population_16_years_and_over_race_and_h_b56a1d15` | *text* | Estimated population 16+ who are Black or African American alone. |
| `estimate_total_population_16_years_and_over_race_and_h_1a053977` | *text* | Estimated population 16+ who are American Indian and Alaska Native alone. |
| `estimate_total_population_16_years_and_over_race_and_h_06655271` | *text* | Estimated population 16+ who are Asian alone. |
| `estimate_total_population_16_years_and_over_race_and_h_cca8b9ee` | *text* | Estimated population 16+ who are Native Hawaiian and Other Pacific Islander alone. |
| `estimate_total_population_16_years_and_over_race_and_h_f4ece111` | *text* | Estimated population 16+ who are Some other race alone. |
| `estimate_total_population_16_years_and_over_race_and_h_b1da87b0` | *text* | Estimated population 16+ who are Two or more races. |
| `estimate_total_population_16_years_and_over_race_and_h_006dc5a1` | *text* | Estimated population 16+ who are Hispanic or Latino (of any race). |
| `estimate_total_population_16_years_and_over_race_and_h_83616f0d` | *text* | Estimated population 16+ who are White alone, not Hispanic or Latino. |
| `estimate_total_population_20_to_64_years` | *text* | Estimated total population age 20–64 years. |
| `estimate_total_population_20_to_64_years_sex_male` | *text* | Estimated male population age 20–64 years. |
| `estimate_total_population_20_to_64_years_sex_female` | *text* | Estimated female population age 20–64 years. |
| `estimate_total_population_20_to_64_years_sex_female_wi_93fba499` | *text* | Estimated females age 20–64 with own children under 18 years. |
| `estimate_total_population_20_to_64_years_sex_female_wi_ce81d8bc` | *text* | Estimated females age 20–64 with own children under 18: with own children under 6 years only. |
| `estimate_total_population_20_to_64_years_sex_female_wi_2d7a64f4` | *text* | Estimated females age 20–64 with own children under 18: with own children under 6 and 6–17 years. |
| `estimate_total_population_20_to_64_years_sex_female_wi_897e3942` | *text* | Estimated females age 20–64 with own children under 18: with own children 6–17 years only. |
| `estimate_total_population_20_to_64_years_poverty_statu_1b854bb8` | *text* | Estimated population age 20–64 below poverty level (past 12 months). |
| `estimate_total_population_20_to_64_years_poverty_statu_d5dda35e` | *text* | Estimated population age 20–64 at or above poverty level (past 12 months). |
| `estimate_total_population_20_to_64_years_disability_st_200d7c78` | *text* | Estimated population age 20–64 with any disability. |
| `estimate_total_educational_attainment_population_25_to_64_years` | *text* | Estimated total population age 25–64 years (educational attainment universe). |
| `estimate_total_educational_attainment_population_25_to_2e83c110` | *text* | Estimated population age 25–64 with less than high school graduate. |
| `estimate_total_educational_attainment_population_25_to_ad6acfe7` | *text* | Estimated population age 25–64 who are high school graduates (incl. equivalency). |
| `estimate_total_educational_attainment_population_25_to_5ae010cf` | *text* | Estimated population age 25–64 with some college or associate’s degree. |
| `estimate_total_educational_attainment_population_25_to_487d4e23` | *text* | Estimated population age 25–64 with bachelor’s degree or higher. |
| `estimate_labor_force_participation_rate_population_16_b2b6437e` | *text* | Labor force participation rate (%) for population age 16 years and over. |
| `estimate_labor_force_participation_rate_population_16_364376b8` | *text* | Labor force participation rate (%) for population age 16–19 years. |
| `estimate_labor_force_participation_rate_population_16_4d001a59` | *text* | Labor force participation rate (%) for population age 20–24 years. |
| `estimate_labor_force_participation_rate_population_16_79e283e2` | *text* | Labor force participation rate (%) for population age 25–29 years. |
| `estimate_labor_force_participation_rate_population_16_2cfbf51a` | *text* | Labor force participation rate (%) for population age 30–34 years. |
| `estimate_labor_force_participation_rate_population_16_45254299` | *text* | Labor force participation rate (%) for population age 35–44 years. |
| `estimate_labor_force_participation_rate_population_16_a4d61364` | *text* | Labor force participation rate (%) for population age 45–54 years. |
| `estimate_labor_force_participation_rate_population_16_4cd250ee` | *text* | Labor force participation rate (%) for population age 55–59 years. |
| `estimate_labor_force_participation_rate_population_16_1ca24d51` | *text* | Labor force participation rate (%) for population age 60–64 years. |
| `estimate_labor_force_participation_rate_population_16_ffb93ed0` | *text* | Labor force participation rate (%) for population age 65–74 years. |
| `estimate_labor_force_participation_rate_population_16_1ba7063f` | *text* | Labor force participation rate (%) for population age 75 years and over. |
| `estimate_labor_force_participation_rate_population_16_dea977de` | *text* | Labor force participation rate (%) for population 16+ who are White alone. |
| `estimate_labor_force_participation_rate_population_16_89135718` | *text* | Labor force participation rate (%) for population 16+ who are Black or African American alone. |
| `estimate_labor_force_participation_rate_population_16_2de6d724` | *text* | Labor force participation rate (%) for population 16+ who are American Indian and Alaska Native alone. |
| `estimate_labor_force_participation_rate_population_16_dc80857d` | *text* | Labor force participation rate (%) for population 16+ who are Asian alone. |
| `estimate_labor_force_participation_rate_population_16_27bd9275` | *text* | Labor force participation rate (%) for population 16+ who are Native Hawaiian and Other Pacific Islander alone. |
| `estimate_labor_force_participation_rate_population_16_3fe54fb8` | *text* | Labor force participation rate (%) for population 16+ who are Some other race alone. |
| `estimate_labor_force_participation_rate_population_16_ea07eb8c` | *text* | Labor force participation rate (%) for population 16+ who are Two or more races. |
| `estimate_labor_force_participation_rate_population_16_286949c7` | *text* | Labor force participation rate (%) for population 16+ who are Hispanic or Latino (any race). |
| `estimate_labor_force_participation_rate_population_16_2ac2b3c8` | *text* | Labor force participation rate (%) for population 16+ who are White alone, not Hispanic or Latino. |
| `estimate_labor_force_participation_rate_population_20_20d77ed4` | *text* | Labor force participation rate (%) for population age 20–64 years. |
| `estimate_labor_force_participation_rate_population_20_618e62e6` | *text* | Labor force participation rate (%) for males age 20–64 years. |
| `estimate_labor_force_participation_rate_population_20_a8627502` | *text* | Labor force participation rate (%) for females age 20–64 years. |
| `estimate_labor_force_participation_rate_population_20_895b477d` | *text* | Labor force participation rate (%) for females 20–64 with own children under 18 years. |
| `estimate_labor_force_participation_rate_population_20_880d598b` | *text* | Labor force participation rate (%) for females 20–64 with own children under 18: under 6 years only. |
| `estimate_labor_force_participation_rate_population_20_bdece926` | *text* | Labor force participation rate (%) for females 20–64 with own children under 18: under 6 and 6–17 years. |
| `estimate_labor_force_participation_rate_population_20_a06980bf` | *text* | Labor force participation rate (%) for females 20–64 with own children under 18: 6–17 years only. |
| `estimate_labor_force_participation_rate_population_20_2a10d65d` | *text* | Labor force participation rate (%) for population 20–64 below poverty level. |
| `estimate_labor_force_participation_rate_population_20_bb1a8c3a` | *text* | Labor force participation rate (%) for population 20–64 at or above poverty level. |
| `estimate_labor_force_participation_rate_population_20_d67ab4b5` | *text* | Labor force participation rate (%) for population 20–64 with any disability. |
| `estimate_labor_force_participation_rate_educational_at_fce0097b` | *text* | Labor force participation rate (%) for population age 25–64 years (educational attainment universe). |
| `estimate_labor_force_participation_rate_educational_at_e8e693d4` | *text* | Labor force participation rate (%) for population 25–64 with less than high school graduate. |
| `estimate_labor_force_participation_rate_educational_at_0d7750e5` | *text* | Labor force participation rate (%) for population 25–64 who are high school graduates (incl. equivalency). |
| `estimate_labor_force_participation_rate_educational_at_f736f899` | *text* | Labor force participation rate (%) for population 25–64 with some college or associate’s degree. |
| `estimate_labor_force_participation_rate_educational_at_1c902b6d` | *text* | Labor force participation rate (%) for population 25–64 with bachelor’s degree or higher. |
| `estimate_employment_population_ratio_population_16_yea_8609553c` | *text* | Employment-to-population ratio (%) for population age 16 years and over. |
| `estimate_employment_population_ratio_population_16_yea_26efed97` | *text* | Employment-to-population ratio (%) for population age 16–19 years. |
| `estimate_employment_population_ratio_population_16_yea_c741d81b` | *text* | Employment-to-population ratio (%) for population age 20–24 years. |
| `estimate_employment_population_ratio_population_16_yea_59037064` | *text* | Employment-to-population ratio (%) for population age 25–29 years. |
| `estimate_employment_population_ratio_population_16_yea_141e7075` | *text* | Employment-to-population ratio (%) for population age 30–34 years. |
| `estimate_employment_population_ratio_population_16_yea_62709327` | *text* | Employment-to-population ratio (%) for population age 35–44 years. |
| `estimate_employment_population_ratio_population_16_yea_22f6eed6` | *text* | Employment-to-population ratio (%) for population age 45–54 years. |
| `estimate_employment_population_ratio_population_16_yea_e34166e7` | *text* | Employment-to-population ratio (%) for population age 55–59 years. |
| `estimate_employment_population_ratio_population_16_yea_3b64b037` | *text* | Employment-to-population ratio (%) for population age 60–64 years. |
| `estimate_employment_population_ratio_population_16_yea_c7706d0e` | *text* | Employment-to-population ratio (%) for population age 65–74 years. |
| `estimate_employment_population_ratio_population_16_yea_bbb5e355` | *text* | Employment-to-population ratio (%) for population age 75 years and over. |
| `estimate_employment_population_ratio_population_16_yea_0b2f36e8` | *text* | Employment-to-population ratio (%) for population 16+ who are White alone. |
| `estimate_employment_population_ratio_population_16_yea_99708a4a` | *text* | Employment-to-population ratio (%) for population 16+ who are Black or African American alone. |
| `estimate_employment_population_ratio_population_16_yea_384ddda6` | *text* | Employment-to-population ratio (%) for population 16+ who are American Indian and Alaska Native alone. |
| `estimate_employment_population_ratio_population_16_yea_4e16d205` | *text* | Employment-to-population ratio (%) for population 16+ who are Asian alone. |
| `estimate_employment_population_ratio_population_16_yea_9ef11110` | *text* | Employment-to-population ratio (%) for population 16+ who are Native Hawaiian and Other Pacific Islander alone. |
| `estimate_employment_population_ratio_population_16_yea_c718dbf8` | *text* | Employment-to-population ratio (%) for population 16+ who are Some other race alone. |
| `estimate_employment_population_ratio_population_16_yea_8796bfc7` | *text* | Employment-to-population ratio (%) for population 16+ who are Two or more races. |
| `estimate_employment_population_ratio_population_16_yea_6162e1e4` | *text* | Employment-to-population ratio (%) for population 16+ who are Hispanic or Latino (any race). |
| `estimate_employment_population_ratio_population_16_yea_d8ffc4ac` | *text* | Employment-to-population ratio (%) for population 16+ who are White alone, not Hispanic or Latino. |
| `estimate_employment_population_ratio_population_20_to_64_years` | *text* | Employment-to-population ratio (%) for population age 20–64 years. |
| `estimate_employment_population_ratio_population_20_to_f526ad9a` | *text* | Employment-to-population ratio (%) for males age 20–64 years. |
| `estimate_employment_population_ratio_population_20_to_5bea6f7b` | *text* | Employment-to-population ratio (%) for females age 20–64 years. |
| `estimate_employment_population_ratio_population_20_to_689208c2` | *text* | Employment-to-population ratio (%) for females 20–64 with own children under 18 years. |
| `estimate_employment_population_ratio_population_20_to_d32d86cd` | *text* | Employment-to-population ratio (%) for females 20–64 with own children under 18: under 6 years only. |
| `estimate_employment_population_ratio_population_20_to_ee075c46` | *text* | Employment-to-population ratio (%) for females 20–64 with own children under 18: under 6 and 6–17 years. |
| `estimate_employment_population_ratio_population_20_to_adaf8165` | *text* | Employment-to-population ratio (%) for females 20–64 with own children under 18: 6–17 years only. |
| `estimate_employment_population_ratio_population_20_to_e334ece7` | *text* | Employment-to-population ratio (%) for population 20–64 below poverty level. |
| `estimate_employment_population_ratio_population_20_to_815d4bb1` | *text* | Employment-to-population ratio (%) for population 20–64 at or above poverty level. |
| `estimate_employment_population_ratio_population_20_to_8d74ba91` | *text* | Employment-to-population ratio (%) for population 20–64 with any disability. |
| `estimate_employment_population_ratio_educational_attai_008c35ed` | *text* | Employment-to-population ratio (%) for population 25–64 years (educational attainment universe). |
| `estimate_employment_population_ratio_educational_attai_ec887ad1` | *text* | Employment-to-population ratio (%) for population 25–64 with less than high school graduate. |
| `estimate_employment_population_ratio_educational_attai_bf9fc137` | *text* | Employment-to-population ratio (%) for population 25–64 who are high school graduates (incl. equivalency). |
| `estimate_employment_population_ratio_educational_attai_eb5e5d66` | *text* | Employment-to-population ratio (%) for population 25–64 with some college or associate’s degree. |
| `estimate_employment_population_ratio_educational_attai_f4ef0136` | *text* | Employment-to-population ratio (%) for population 25–64 with bachelor’s degree or higher. |
| `estimate_unemployment_rate_population_16_years_and_over` | *text* | Unemployment rate (%) for population age 16 years and over (labor force). |
| `estimate_unemployment_rate_population_16_years_and_ove_03273597` | *text* | Unemployment rate (%) for population age 16–19 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_3f4b1814` | *text* | Unemployment rate (%) for population age 20–24 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_c0eda909` | *text* | Unemployment rate (%) for population age 25–29 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_1ecd39a7` | *text* | Unemployment rate (%) for population age 30–34 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_df03c4ec` | *text* | Unemployment rate (%) for population age 35–44 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_d9201905` | *text* | Unemployment rate (%) for population age 45–54 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_42140d59` | *text* | Unemployment rate (%) for population age 55–59 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_27b14abc` | *text* | Unemployment rate (%) for population age 60–64 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_6153037b` | *text* | Unemployment rate (%) for population age 65–74 years. |
| `estimate_unemployment_rate_population_16_years_and_ove_19054e1f` | *text* | Unemployment rate (%) for population age 75 years and over. |
| `estimate_unemployment_rate_population_16_years_and_ove_8a69a580` | *text* | Unemployment rate (%) for population 16+ who are White alone. |
| `estimate_unemployment_rate_population_16_years_and_ove_a740114c` | *text* | Unemployment rate (%) for population 16+ who are Black or African American alone. |
| `estimate_unemployment_rate_population_16_years_and_ove_bd9ffe96` | *text* | Unemployment rate (%) for population 16+ who are American Indian and Alaska Native alone. |
| `estimate_unemployment_rate_population_16_years_and_ove_9ff8089b` | *text* | Unemployment rate (%) for population 16+ who are Asian alone. |
| `estimate_unemployment_rate_population_16_years_and_ove_f75c3e0c` | *text* | Unemployment rate (%) for population 16+ who are Native Hawaiian and Other Pacific Islander alone. |
| `estimate_unemployment_rate_population_16_years_and_ove_10ccf05a` | *text* | Unemployment rate (%) for population 16+ who are Some other race alone. |
| `estimate_unemployment_rate_population_16_years_and_ove_00df5c67` | *text* | Unemployment rate (%) for population 16+ who are Two or more races. |
| `estimate_unemployment_rate_population_16_years_and_ove_fb6178bb` | *text* | Unemployment rate (%) for population 16+ who are Hispanic or Latino (any race). |
| `estimate_unemployment_rate_population_16_years_and_ove_5de5f55a` | *text* | Unemployment rate (%) for population 16+ who are White alone, not Hispanic or Latino. |
| `estimate_unemployment_rate_population_20_to_64_years` | *text* | Unemployment rate (%) for population age 20–64 years. |
| `estimate_unemployment_rate_population_20_to_64_years_sex_male` | *text* | Unemployment rate (%) for males age 20–64 years. |
| `estimate_unemployment_rate_population_20_to_64_years_sex_female` | *text* | Unemployment rate (%) for females age 20–64 years. |
| `estimate_unemployment_rate_population_20_to_64_years_s_8215ac7b` | *text* | Unemployment rate (%) for females 20–64 with own children under 18 years. |
| `estimate_unemployment_rate_population_20_to_64_years_s_0f216e05` | *text* | Unemployment rate (%) for females 20–64 with own children under 18: under 6 years only. |
| `estimate_unemployment_rate_population_20_to_64_years_s_82f98857` | *text* | Unemployment rate (%) for females 20–64 with own children under 18: under 6 and 6–17 years. |
| `estimate_unemployment_rate_population_20_to_64_years_s_578f96a8` | *text* | Unemployment rate (%) for females 20–64 with own children under 18: 6–17 years only. |
| `estimate_unemployment_rate_population_20_to_64_years_p_198ad728` | *text* | Unemployment rate (%) for population 20–64 below poverty level. |
| `estimate_unemployment_rate_population_20_to_64_years_p_ba2c3d44` | *text* | Unemployment rate (%) for population 20–64 at or above poverty level. |
| `estimate_unemployment_rate_population_20_to_64_years_d_500c0eb4` | *text* | Unemployment rate (%) for population 20–64 with any disability. |
| `estimate_unemployment_rate_educational_attainment_popu_edf2f55f` | *text* | Unemployment rate (%) for population 25–64 years (educational attainment universe). |
| `estimate_unemployment_rate_educational_attainment_popu_5607b853` | *text* | Unemployment rate (%) for population 25–64 with less than high school graduate. |
| `estimate_unemployment_rate_educational_attainment_popu_129054e3` | *text* | Unemployment rate (%) for population 25–64 who are high school graduates (incl. equivalency). |
| `estimate_unemployment_rate_educational_attainment_popu_b0fac561` | *text* | Unemployment rate (%) for population 25–64 with some college or associate’s degree. |
| `estimate_unemployment_rate_educational_attainment_popu_6253472b` | *text* | Unemployment rate (%) for population 25–64 with bachelor’s degree or higher. |

---

## Table: `hh_inc_rent_pct_inc_12mo`
- **Row Count**: 242,297
- **Time Range**: N/A
- **Description**: Household income data and gross rent as a percentage of household income.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier for the area (e.g., GEOID). |
| `geographic_area_name` | *text* | Human-readable name of the geographic area. |
| `estimate_total` | *text* | Total estimated households in this table’s universe (all income × rent-to-income categories). |
| `estimate_total_less_than_10_000` | *text* | Estimated households with income less than $10,000 (all rent-to-income categories). |
| `estimate_total_less_than_10_000_less_than_20_0_percent` | *text* | Income < $10,000; gross rent is <20.0% of household income. |
| `estimate_total_less_than_10_000_20_0_to_24_9_percent` | *text* | Income < $10,000; gross rent is 20.0–24.9% of household income. |
| `estimate_total_less_than_10_000_25_0_to_29_9_percent` | *text* | Income < $10,000; gross rent is 25.0–29.9% of household income. |
| `estimate_total_less_than_10_000_30_0_to_34_9_percent` | *text* | Income < $10,000; gross rent is 30.0–34.9% of household income. |
| `estimate_total_less_than_10_000_35_0_to_39_9_percent` | *text* | Income < $10,000; gross rent is 35.0–39.9% of household income. |
| `estimate_total_less_than_10_000_40_0_to_49_9_percent` | *text* | Income < $10,000; gross rent is 40.0–49.9% of household income. |
| `estimate_total_less_than_10_000_50_0_percent_or_more` | *text* | Income < $10,000; gross rent is 50.0% or more of household income. |
| `estimate_total_less_than_10_000_not_computed` | *text* | Income < $10,000; gross rent % of income not computed. |
| `estimate_total_10_000_to_19_999` | *text* | Estimated households with income $10,000–$19,999 (all rent-to-income categories). |
| `estimate_total_10_000_to_19_999_less_than_20_0_percent` | *text* | Income $10,000–$19,999; gross rent is <20.0% of household income. |
| `estimate_total_10_000_to_19_999_20_0_to_24_9_percent` | *text* | Income $10,000–$19,999; gross rent is 20.0–24.9% of household income. |
| `estimate_total_10_000_to_19_999_25_0_to_29_9_percent` | *text* | Income $10,000–$19,999; gross rent is 25.0–29.9% of household income. |
| `estimate_total_10_000_to_19_999_30_0_to_34_9_percent` | *text* | Income $10,000–$19,999; gross rent is 30.0–34.9% of household income. |
| `estimate_total_10_000_to_19_999_35_0_to_39_9_percent` | *text* | Income $10,000–$19,999; gross rent is 35.0–39.9% of household income. |
| `estimate_total_10_000_to_19_999_40_0_to_49_9_percent` | *text* | Income $10,000–$19,999; gross rent is 40.0–49.9% of household income. |
| `estimate_total_10_000_to_19_999_50_0_percent_or_more` | *text* | Income $10,000–$19,999; gross rent is 50.0% or more of household income. |
| `estimate_total_10_000_to_19_999_not_computed` | *text* | Income $10,000–$19,999; gross rent % of income not computed. |
| `estimate_total_20_000_to_34_999` | *text* | Estimated households with income $20,000–$34,999 (all rent-to-income categories). |
| `estimate_total_20_000_to_34_999_less_than_20_0_percent` | *text* | Income $20,000–$34,999; gross rent is <20.0% of household income. |
| `estimate_total_20_000_to_34_999_20_0_to_24_9_percent` | *text* | Income $20,000–$34,999; gross rent is 20.0–24.9% of household income. |
| `estimate_total_20_000_to_34_999_25_0_to_29_9_percent` | *text* | Income $20,000–$34,999; gross rent is 25.0–29.9% of household income. |
| `estimate_total_20_000_to_34_999_30_0_to_34_9_percent` | *text* | Income $20,000–$34,999; gross rent is 30.0–34.9% of household income. |
| `estimate_total_20_000_to_34_999_35_0_to_39_9_percent` | *text* | Income $20,000–$34,999; gross rent is 35.0–39.9% of household income. |
| `estimate_total_20_000_to_34_999_40_0_to_49_9_percent` | *text* | Income $20,000–$34,999; gross rent is 40.0–49.9% of household income. |
| `estimate_total_20_000_to_34_999_50_0_percent_or_more` | *text* | Income $20,000–$34,999; gross rent is 50.0% or more of household income. |
| `estimate_total_20_000_to_34_999_not_computed` | *text* | Income $20,000–$34,999; gross rent % of income not computed. |
| `estimate_total_35_000_to_49_999` | *text* | Estimated households with income $35,000–$49,999 (all rent-to-income categories). |
| `estimate_total_35_000_to_49_999_less_than_20_0_percent` | *text* | Income $35,000–$49,999; gross rent is <20.0% of household income. |
| `estimate_total_35_000_to_49_999_20_0_to_24_9_percent` | *text* | Income $35,000–$49,999; gross rent is 20.0–24.9% of household income. |
| `estimate_total_35_000_to_49_999_25_0_to_29_9_percent` | *text* | Income $35,000–$49,999; gross rent is 25.0–29.9% of household income. |
| `estimate_total_35_000_to_49_999_30_0_to_34_9_percent` | *text* | Income $35,000–$49,999; gross rent is 30.0–34.9% of household income. |
| `estimate_total_35_000_to_49_999_35_0_to_39_9_percent` | *text* | Income $35,000–$49,999; gross rent is 35.0–39.9% of household income. |
| `estimate_total_35_000_to_49_999_40_0_to_49_9_percent` | *text* | Income $35,000–$49,999; gross rent is 40.0–49.9% of household income. |
| `estimate_total_35_000_to_49_999_50_0_percent_or_more` | *text* | Income $35,000–$49,999; gross rent is 50.0% or more of household income. |
| `estimate_total_35_000_to_49_999_not_computed` | *text* | Income $35,000–$49,999; gross rent % of income not computed. |
| `estimate_total_50_000_to_74_999` | *text* | Estimated households with income $50,000–$74,999 (all rent-to-income categories). |
| `estimate_total_50_000_to_74_999_less_than_20_0_percent` | *text* | Income $50,000–$74,999; gross rent is <20.0% of household income. |
| `estimate_total_50_000_to_74_999_20_0_to_24_9_percent` | *text* | Income $50,000–$74,999; gross rent is 20.0–24.9% of household income. |
| `estimate_total_50_000_to_74_999_25_0_to_29_9_percent` | *text* | Income $50,000–$74,999; gross rent is 25.0–29.9% of household income. |
| `estimate_total_50_000_to_74_999_30_0_to_34_9_percent` | *text* | Income $50,000–$74,999; gross rent is 30.0–34.9% of household income. |
| `estimate_total_50_000_to_74_999_35_0_to_39_9_percent` | *text* | Income $50,000–$74,999; gross rent is 35.0–39.9% of household income. |
| `estimate_total_50_000_to_74_999_40_0_to_49_9_percent` | *text* | Income $50,000–$74,999; gross rent is 40.0–49.9% of household income. |
| `estimate_total_50_000_to_74_999_50_0_percent_or_more` | *text* | Income $50,000–$74,999; gross rent is 50.0% or more of household income. |
| `estimate_total_50_000_to_74_999_not_computed` | *text* | Income $50,000–$74,999; gross rent % of income not computed. |
| `estimate_total_75_000_to_99_999` | *text* | Estimated households with income $75,000–$99,999 (all rent-to-income categories). |
| `estimate_total_75_000_to_99_999_less_than_20_0_percent` | *text* | Income $75,000–$99,999; gross rent is <20.0% of household income. |
| `estimate_total_75_000_to_99_999_20_0_to_24_9_percent` | *text* | Income $75,000–$99,999; gross rent is 20.0–24.9% of household income. |
| `estimate_total_75_000_to_99_999_25_0_to_29_9_percent` | *text* | Income $75,000–$99,999; gross rent is 25.0–29.9% of household income. |
| `estimate_total_75_000_to_99_999_30_0_to_34_9_percent` | *text* | Income $75,000–$99,999; gross rent is 30.0–34.9% of household income. |
| `estimate_total_75_000_to_99_999_35_0_to_39_9_percent` | *text* | Income $75,000–$99,999; gross rent is 35.0–39.9% of household income. |
| `estimate_total_75_000_to_99_999_40_0_to_49_9_percent` | *text* | Income $75,000–$99,999; gross rent is 40.0–49.9% of household income. |
| `estimate_total_75_000_to_99_999_50_0_percent_or_more` | *text* | Income $75,000–$99,999; gross rent is 50.0% or more of household income. |
| `estimate_total_75_000_to_99_999_not_computed` | *text* | Income $75,000–$99,999; gross rent % of income not computed. |
| `estimate_total_100_000_or_more` | *text* | Estimated households with income $100,000 or more (all rent-to-income categories). |
| `estimate_total_100_000_or_more_less_than_20_0_percent` | *text* | Income $100,000+; gross rent is <20.0% of household income. |
| `estimate_total_100_000_or_more_20_0_to_24_9_percent` | *text* | Income $100,000+; gross rent is 20.0–24.9% of household income. |
| `estimate_total_100_000_or_more_25_0_to_29_9_percent` | *text* | Income $100,000+; gross rent is 25.0–29.9% of household income. |
| `estimate_total_100_000_or_more_30_0_to_34_9_percent` | *text* | Income $100,000+; gross rent is 30.0–34.9% of household income. |
| `estimate_total_100_000_or_more_35_0_to_39_9_percent` | *text* | Income $100,000+; gross rent is 35.0–39.9% of household income. |
| `estimate_total_100_000_or_more_40_0_to_49_9_percent` | *text* | Income $100,000+; gross rent is 40.0–49.9% of household income. |
| `estimate_total_100_000_or_more_50_0_percent_or_more` | *text* | Income $100,000+; gross rent is 50.0% or more of household income. |
| `estimate_total_100_000_or_more_not_computed` | *text* | Income $100,000+; gross rent % of income not computed. |

---

## Table: `hlthins_cov_chars_us`
- **Row Count**: 85,382
- **Time Range**: N/A
- **Description**: Health insurance coverage characteristics for the US population.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier for the area (e.g., GEOID). |
| `geographic_area_name` | *text* | Human-readable name of the geographic area. |
| `estimate_total_civilian_noninstitutionalized_population` | *text* | Estimated total civilian noninstitutionalized population (all ages). |
| `estimate_total_civilian_noninstitutionalized_populatio_e8acf26b` | *text* | Estimated civilian noninstitutionalized population age under 6 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_0d6f4481` | *text* | Estimated civilian noninstitutionalized population age 6 to 18 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_89e57755` | *text* | Estimated civilian noninstitutionalized population age 19 to 25 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_26b8f29e` | *text* | Estimated civilian noninstitutionalized population age 26 to 34 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_5137d7d4` | *text* | Estimated civilian noninstitutionalized population age 35 to 44 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_d94df245` | *text* | Estimated civilian noninstitutionalized population age 45 to 54 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_fe244316` | *text* | Estimated civilian noninstitutionalized population age 55 to 64 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_888c726a` | *text* | Estimated civilian noninstitutionalized population age 65 to 74 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_e720b2d0` | *text* | Estimated civilian noninstitutionalized population age 75 years and older. |
| `estimate_total_civilian_noninstitutionalized_populatio_f3095109` | *text* | Estimated civilian noninstitutionalized population age under 19 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_b732a741` | *text* | Estimated civilian noninstitutionalized population age 19 to 64 years. |
| `estimate_total_civilian_noninstitutionalized_populatio_2e62a827` | *text* | Estimated civilian noninstitutionalized population age 65 years and older. |
| `estimate_total_civilian_noninstitutionalized_populatio_703e98eb` | *text* | Estimated male civilian noninstitutionalized population. |
| `estimate_total_civilian_noninstitutionalized_populatio_8490b9d3` | *text* | Estimated female civilian noninstitutionalized population. |
| `estimate_total_civilian_noninstitutionalized_populatio_37511219` | *text* | Estimated civilian noninstitutionalized population: White alone. |
| `estimate_total_civilian_noninstitutionalized_populatio_f98c4b38` | *text* | Estimated civilian noninstitutionalized population: Black or African American alone. |
| `estimate_total_civilian_noninstitutionalized_populatio_f50a74c8` | *text* | Estimated civilian noninstitutionalized population: American Indian and Alaska Native alone. |
| `estimate_total_civilian_noninstitutionalized_populatio_ddba49fd` | *text* | Estimated civilian noninstitutionalized population: Asian alone. |
| `estimate_total_civilian_noninstitutionalized_populatio_17cdaa64` | *text* | Estimated civilian noninstitutionalized population: Native Hawaiian and Other Pacific Islander alone. |
| `estimate_total_civilian_noninstitutionalized_populatio_2c2569c7` | *text* | Estimated civilian noninstitutionalized population: Some other race alone. |
| `estimate_total_civilian_noninstitutionalized_populatio_be381566` | *text* | Estimated civilian noninstitutionalized population: Two or more races. |
| `estimate_total_civilian_noninstitutionalized_populatio_923692e5` | *text* | Estimated civilian noninstitutionalized population: Hispanic or Latino (of any race). |
| `estimate_total_civilian_noninstitutionalized_populatio_834bd032` | *text* | Estimated civilian noninstitutionalized population: White alone, not Hispanic or Latino. |
| `estimate_total_civilian_noninstitutionalized_populatio_97012d9f` | *text* | Estimated civilian noninstitutionalized population in family households. |
| `estimate_total_civilian_noninstitutionalized_populatio_77fe53e3` | *text* | Estimated civilian noninstitutionalized population in family households in married-couple families. |
| `estimate_total_civilian_noninstitutionalized_populatio_2291d397` | *text* | Estimated civilian noninstitutionalized population in family households in other families (non–married-couple). |
| `estimate_total_civilian_noninstitutionalized_populatio_5c61e8b6` | *text* | Estimated civilian noninstitutionalized population in other families: male reference person, no spouse present. |
| `estimate_total_civilian_noninstitutionalized_populatio_c78f8ea7` | *text* | Estimated civilian noninstitutionalized population in other families: female reference person, no spouse present. |
| `estimate_total_civilian_noninstitutionalized_populatio_efbe9f02` | *text* | Estimated civilian noninstitutionalized population in non-family households and other living arrangements. |
| `estimate_total_civilian_noninstitutionalized_populatio_b511073b` | *text* | Estimated civilian noninstitutionalized population: native born. |
| `estimate_total_civilian_noninstitutionalized_populatio_1eca67d2` | *text* | Estimated civilian noninstitutionalized population: foreign born. |
| `estimate_total_civilian_noninstitutionalized_populatio_5cb08042` | *text* | Estimated civilian noninstitutionalized population: foreign born, naturalized citizen. |
| `estimate_total_civilian_noninstitutionalized_populatio_41a8e6c1` | *text* | Estimated civilian noninstitutionalized population: foreign born, not a U.S. citizen. |
| `estimate_total_civilian_noninstitutionalized_populatio_adf1e898` | *text* | Estimated civilian noninstitutionalized population with a disability. |
| `estimate_total_civilian_noninstitutionalized_populatio_55f3d83d` | *text* | Estimated civilian noninstitutionalized population with no disability. |
| `estimate_total_civilian_noninstitutionalized_populatio_b7d58764` | *text* | Estimated civilian noninstitutionalized population age 26+ (educational attainment universe). |
| `estimate_total_civilian_noninstitutionalized_populatio_8d9e9155` | *text* | Estimated civilian noninstitutionalized population age 26+ with less than high school graduate. |
| `estimate_total_civilian_noninstitutionalized_populatio_0a269abc` | *text* | Estimated civilian noninstitutionalized population age 26+ with high school graduate (incl. equivalency). |
| `estimate_total_civilian_noninstitutionalized_populatio_a717112f` | *text* | Estimated civilian noninstitutionalized population age 26+ with some college or associate’s degree. |
| `estimate_total_civilian_noninstitutionalized_populatio_bd6978cf` | *text* | Estimated civilian noninstitutionalized population age 26+ with bachelor’s degree or higher. |
| `estimate_total_civilian_noninstitutionalized_populatio_583e4a8c` | *text* | Estimated civilian noninstitutionalized population age 19–64 (employment status universe). |
| `estimate_total_civilian_noninstitutionalized_populatio_cb5a73da` | *text* | Estimated civilian noninstitutionalized population age 19–64 in labor force. |
| `estimate_total_civilian_noninstitutionalized_populatio_600b9dcc` | *text* | Estimated civilian noninstitutionalized population age 19–64 in labor force and employed. |
| `estimate_total_civilian_noninstitutionalized_populatio_389b9d74` | *text* | Estimated civilian noninstitutionalized population age 19–64 in labor force and unemployed. |
| `estimate_total_civilian_noninstitutionalized_populatio_67235b55` | *text* | Estimated civilian noninstitutionalized population age 19–64 not in labor force. |
| `estimate_total_civilian_noninstitutionalized_populatio_8b2f0a6d` | *text* | Estimated civilian noninstitutionalized population age 19–64 (work experience universe). |
| `estimate_total_civilian_noninstitutionalized_populatio_28af2fc6` | *text* | Estimated civilian noninstitutionalized population age 19–64 who worked full-time, year-round in past 12 months. |
| `estimate_total_civilian_noninstitutionalized_populatio_2d74800f` | *text* | Estimated civilian noninstitutionalized population age 19–64 who worked less than full-time, year-round in past 12 months. |
| `estimate_total_civilian_noninstitutionalized_populatio_566b551e` | *text* | Estimated civilian noninstitutionalized population age 19–64 who did not work in past 12 months. |
| `estimate_total_civilian_noninstitutionalized_populatio_a0530025` | *text* | Estimated total household population (for household income categories; 2024 inflation-adjusted dollars). |
| `estimate_total_civilian_noninstitutionalized_populatio_8e5403a3` | *text* | Estimated household population with household income under $25,000 (2024 inflation-adjusted). |
| `estimate_total_civilian_noninstitutionalized_populatio_34c7d0cd` | *text* | Estimated household population with household income $25,000 to $49,999 (2024 inflation-adjusted). |
| `estimate_total_civilian_noninstitutionalized_populatio_1a8f435c` | *text* | Estimated household population with household income $50,000 to $74,999 (2024 inflation-adjusted). |
| `estimate_total_civilian_noninstitutionalized_populatio_c8022eab` | *text* | Estimated household population with household income $75,000 to $99,999 (2024 inflation-adjusted). |
| `estimate_total_civilian_noninstitutionalized_populatio_026a9b60` | *text* | Estimated household population with household income $100,000 and over (2024 inflation-adjusted). |
| `estimate_total_civilian_noninstitutionalized_populatio_a6656b06` | *text* | Estimated population for whom poverty status is determined (ratio of income to poverty level, past 12 months). |
| `estimate_total_civilian_noninstitutionalized_populatio_7974fcfb` | *text* | Estimated population with income-to-poverty ratio below 138% of poverty threshold (past 12 months). |
| `estimate_total_civilian_noninstitutionalized_populatio_7c9696d1` | *text* | Estimated population with income-to-poverty ratio 138% to 399% of poverty threshold (past 12 months). |
| `estimate_total_civilian_noninstitutionalized_populatio_12e1e164` | *text* | Estimated population with income-to-poverty ratio at or above 400% of poverty threshold (past 12 months). |
| `estimate_total_civilian_noninstitutionalized_populatio_2d8a2c7f` | *text* | Estimated population with income-to-poverty ratio below 100% of poverty threshold (past 12 months). |
| `estimate_insured_civilian_noninstitutionalized_population` | *text* | Estimated insured civilian noninstitutionalized population (all ages). |
| `estimate_insured_civilian_noninstitutionalized_populat_39546f6f` | *text* | Estimated insured civilian noninstitutionalized population age under 6 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_5feeb28d` | *text* | Estimated insured civilian noninstitutionalized population age 6 to 18 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_f16539e4` | *text* | Estimated insured civilian noninstitutionalized population age 19 to 25 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_cf3441d6` | *text* | Estimated insured civilian noninstitutionalized population age 26 to 34 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_932d9400` | *text* | Estimated insured civilian noninstitutionalized population age 35 to 44 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_6ef328f4` | *text* | Estimated insured civilian noninstitutionalized population age 45 to 54 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_ed82e79b` | *text* | Estimated insured civilian noninstitutionalized population age 55 to 64 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_b93fcd9d` | *text* | Estimated insured civilian noninstitutionalized population age 65 to 74 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_b6e6eed2` | *text* | Estimated insured civilian noninstitutionalized population age 75 years and older. |
| `estimate_insured_civilian_noninstitutionalized_populat_6a17141f` | *text* | Estimated insured civilian noninstitutionalized population age under 19 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_faa57217` | *text* | Estimated insured civilian noninstitutionalized population age 19 to 64 years. |
| `estimate_insured_civilian_noninstitutionalized_populat_3903c72d` | *text* | Estimated insured civilian noninstitutionalized population age 65 years and older. |
| `estimate_insured_civilian_noninstitutionalized_populat_482435c6` | *text* | Estimated insured male civilian noninstitutionalized population. |
| `estimate_insured_civilian_noninstitutionalized_populat_95406325` | *text* | Estimated insured female civilian noninstitutionalized population. |
| `estimate_insured_civilian_noninstitutionalized_populat_4137c73f` | *text* | Estimated insured civilian noninstitutionalized population: White alone. |
| `estimate_insured_civilian_noninstitutionalized_populat_a04f0aae` | *text* | Estimated insured civilian noninstitutionalized population: Black or African American alone. |
| `estimate_insured_civilian_noninstitutionalized_populat_781dd0de` | *text* | Estimated insured civilian noninstitutionalized population: American Indian and Alaska Native alone. |
| `estimate_insured_civilian_noninstitutionalized_populat_20e1c452` | *text* | Estimated insured civilian noninstitutionalized population: Asian alone. |
| `estimate_insured_civilian_noninstitutionalized_populat_a4f6f60d` | *text* | Estimated insured civilian noninstitutionalized population: Native Hawaiian and Other Pacific Islander alone. |
| `estimate_insured_civilian_noninstitutionalized_populat_340d630e` | *text* | Estimated insured civilian noninstitutionalized population: Some other race alone. |
| `estimate_insured_civilian_noninstitutionalized_populat_b84c1afa` | *text* | Estimated insured civilian noninstitutionalized population: Two or more races. |
| `estimate_insured_civilian_noninstitutionalized_populat_8ecbf6eb` | *text* | Estimated insured civilian noninstitutionalized population: Hispanic or Latino (of any race). |
| `estimate_insured_civilian_noninstitutionalized_populat_0315f800` | *text* | Estimated insured civilian noninstitutionalized population: White alone, not Hispanic or Latino. |
| `estimate_insured_civilian_noninstitutionalized_populat_32458eff` | *text* | Estimated insured civilian noninstitutionalized population in family households. |
| `estimate_insured_civilian_noninstitutionalized_populat_7eece9f0` | *text* | Estimated insured civilian noninstitutionalized population in married-couple families. |
| `estimate_insured_civilian_noninstitutionalized_populat_2e3bf3ec` | *text* | Estimated insured civilian noninstitutionalized population in other families (non–married-couple). |
| `estimate_insured_civilian_noninstitutionalized_populat_5793855e` | *text* | Estimated insured civilian noninstitutionalized population in other families: male reference person, no spouse present. |
| `estimate_insured_civilian_noninstitutionalized_populat_5c49b61f` | *text* | Estimated insured civilian noninstitutionalized population in other families: female reference person, no spouse present. |
| `estimate_insured_civilian_noninstitutionalized_populat_696ecda8` | *text* | Estimated insured civilian noninstitutionalized population in non-family households and other living arrangements. |
| `estimate_insured_civilian_noninstitutionalized_populat_6043bd5c` | *text* | Estimated insured civilian noninstitutionalized population: native born. |
| `estimate_insured_civilian_noninstitutionalized_populat_ef3efa15` | *text* | Estimated insured civilian noninstitutionalized population: foreign born. |
| `estimate_insured_civilian_noninstitutionalized_populat_41add3d2` | *text* | Estimated insured civilian noninstitutionalized population: foreign born, naturalized citizen. |
| `estimate_insured_civilian_noninstitutionalized_populat_a4b21f9e` | *text* | Estimated insured civilian noninstitutionalized population: foreign born, not a U.S. citizen. |
| `estimate_insured_civilian_noninstitutionalized_populat_27a00278` | *text* | Estimated insured civilian noninstitutionalized population with a disability. |
| `estimate_insured_civilian_noninstitutionalized_populat_51f15fef` | *text* | Estimated insured civilian noninstitutionalized population with no disability. |
| `estimate_insured_civilian_noninstitutionalized_populat_ccb568b0` | *text* | Estimated insured civilian noninstitutionalized population age 26+ (educational attainment universe). |
| `estimate_insured_civilian_noninstitutionalized_populat_8334935f` | *text* | Estimated insured civilian noninstitutionalized population age 26+ with less than high school graduate. |
| `estimate_insured_civilian_noninstitutionalized_populat_8ddf4f09` | *text* | Estimated insured civilian noninstitutionalized population age 26+ with high school graduate (incl. equivalency). |
| `estimate_insured_civilian_noninstitutionalized_populat_c67c0928` | *text* | Estimated insured civilian noninstitutionalized population age 26+ with some college or associate’s degree. |
| `estimate_insured_civilian_noninstitutionalized_populat_5d5fb9ee` | *text* | Estimated insured civilian noninstitutionalized population age 26+ with bachelor’s degree or higher. |
| `estimate_insured_civilian_noninstitutionalized_populat_118ce635` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 (employment status universe). |
| `estimate_insured_civilian_noninstitutionalized_populat_7125119b` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 in labor force. |
| `estimate_insured_civilian_noninstitutionalized_populat_0ab78c0c` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 in labor force and employed. |
| `estimate_insured_civilian_noninstitutionalized_populat_beddf827` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 in labor force and unemployed. |
| `estimate_insured_civilian_noninstitutionalized_populat_019efd81` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 not in labor force. |
| `estimate_insured_civilian_noninstitutionalized_populat_39ee1506` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 (work experience universe). |
| `estimate_insured_civilian_noninstitutionalized_populat_c49921a6` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 who worked full-time, year-round in past 12 months. |
| `estimate_insured_civilian_noninstitutionalized_populat_e575baef` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 who worked less than full-time, year-round in past 12 months. |
| `estimate_insured_civilian_noninstitutionalized_populat_26373835` | *text* | Estimated insured civilian noninstitutionalized population age 19–64 who did not work in past 12 months. |
| `estimate_insured_civilian_noninstitutionalized_populat_cfea1b24` | *text* | Estimated insured household population (income categories; 2024 inflation-adjusted dollars). |
| `estimate_insured_civilian_noninstitutionalized_populat_daf65fa7` | *text* | Estimated insured household population with household income under $25,000 (2024 inflation-adjusted). |
| `estimate_insured_civilian_noninstitutionalized_populat_1cd1d17b` | *text* | Estimated insured household population with household income $25,000 to $49,999 (2024 inflation-adjusted). |
| `estimate_insured_civilian_noninstitutionalized_populat_350b7aee` | *text* | Estimated insured household population with household income $50,000 to $74,999 (2024 inflation-adjusted). |
| `estimate_insured_civilian_noninstitutionalized_populat_1a2f187a` | *text* | Estimated insured household population with household income $75,000 to $99,999 (2024 inflation-adjusted). |
| `estimate_insured_civilian_noninstitutionalized_populat_bb4a1bd0` | *text* | Estimated insured household population with household income $100,000 and over (2024 inflation-adjusted). |
| `estimate_insured_civilian_noninstitutionalized_populat_44466647` | *text* | Estimated insured population for whom poverty status is determined (income-to-poverty ratio, past 12 months). |
| `estimate_insured_civilian_noninstitutionalized_populat_ccd49806` | *text* | Estimated insured population below 138% of poverty threshold (past 12 months). |
| `estimate_insured_civilian_noninstitutionalized_populat_7d570936` | *text* | Estimated insured population 138% to 399% of poverty threshold (past 12 months). |
| `estimate_insured_civilian_noninstitutionalized_populat_7c6edbac` | *text* | Estimated insured population at or above 400% of poverty threshold (past 12 months). |
| `estimate_insured_civilian_noninstitutionalized_populat_24eca624` | *text* | Estimated insured population below 100% of poverty threshold (past 12 months). |
| `estimate_percent_insured_civilian_noninstitutionalized_10e420b6` | *text* | Estimated percent insured (%) of the civilian noninstitutionalized population (all ages). |
| `estimate_percent_insured_civilian_noninstitutionalized_bcbb96c0` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age under 6 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_2099a2b8` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 6 to 18 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_daf934d9` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 19 to 25 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_43314cec` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 26 to 34 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_fddb00d8` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 35 to 44 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_4250fe6c` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 45 to 54 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_30626455` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 55 to 64 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_9a95953d` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 65 to 74 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_56e66a19` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 75 years and older. |
| `estimate_percent_insured_civilian_noninstitutionalized_4ac0eca6` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age under 19 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_dcc24df6` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 19 to 64 years. |
| `estimate_percent_insured_civilian_noninstitutionalized_987e966f` | *text* | Estimated percent insured (%) for civilian noninstitutionalized population age 65 years and older. |
| `estimate_percent_insured_civilian_noninstitutionalized_b7d9c2ac` | *text* | Estimated percent insured (%) for male civilian noninstitutionalized population. |
| `estimate_percent_insured_civilian_noninstitutionalized_d5e3a754` | *text* | Estimated percent insured (%) for female civilian noninstitutionalized population. |
| `estimate_percent_insured_civilian_noninstitutionalized_e93cb7cb` | *text* | Estimated percent insured (%) for White alone. |
| `estimate_percent_insured_civilian_noninstitutionalized_3d654c66` | *text* | Estimated percent insured (%) for Black or African American alone. |
| `estimate_percent_insured_civilian_noninstitutionalized_c6ebc09a` | *text* | Estimated percent insured (%) for American Indian and Alaska Native alone. |
| `estimate_percent_insured_civilian_noninstitutionalized_cd461067` | *text* | Estimated percent insured (%) for Asian alone. |
| `estimate_percent_insured_civilian_noninstitutionalized_0a9125f4` | *text* | Estimated percent insured (%) for Native Hawaiian and Other Pacific Islander alone. |
| `estimate_percent_insured_civilian_noninstitutionalized_e67eed47` | *text* | Estimated percent insured (%) for Some other race alone. |
| `estimate_percent_insured_civilian_noninstitutionalized_fceba116` | *text* | Estimated percent insured (%) for Two or more races. |
| `estimate_percent_insured_civilian_noninstitutionalized_4ff0f273` | *text* | Estimated percent insured (%) for Hispanic or Latino (of any race). |
| `estimate_percent_insured_civilian_noninstitutionalized_c0216d5c` | *text* | Estimated percent insured (%) for White alone, not Hispanic or Latino. |
| `estimate_percent_insured_civilian_noninstitutionalized_ef998b97` | *text* | Estimated percent insured (%) for people in family households. |
| `estimate_percent_insured_civilian_noninstitutionalized_7750fc03` | *text* | Estimated percent insured (%) for people in married-couple families. |
| `estimate_percent_insured_civilian_noninstitutionalized_97588b18` | *text* | Estimated percent insured (%) for people in other families (non–married-couple). |
| `estimate_percent_insured_civilian_noninstitutionalized_864290d4` | *text* | Estimated percent insured (%) for other families: male reference person, no spouse present. |
| `estimate_percent_insured_civilian_noninstitutionalized_652b3985` | *text* | Estimated percent insured (%) for other families: female reference person, no spouse present. |
| `estimate_percent_insured_civilian_noninstitutionalized_8da1faeb` | *text* | Estimated percent insured (%) for non-family households and other living arrangements. |
| `estimate_percent_insured_civilian_noninstitutionalized_879756e1` | *text* | Estimated percent insured (%) for native born. |
| `estimate_percent_insured_civilian_noninstitutionalized_16942ab9` | *text* | Estimated percent insured (%) for foreign born. |
| `estimate_percent_insured_civilian_noninstitutionalized_0d663e6a` | *text* | Estimated percent insured (%) for foreign born, naturalized citizen. |
| `estimate_percent_insured_civilian_noninstitutionalized_80d2c7ce` | *text* | Estimated percent insured (%) for foreign born, not a U.S. citizen. |
| `estimate_percent_insured_civilian_noninstitutionalized_373215c8` | *text* | Estimated percent insured (%) for people with a disability. |
| `estimate_percent_insured_civilian_noninstitutionalized_2b9add7f` | *text* | Estimated percent insured (%) for people with no disability. |
| `estimate_percent_insured_civilian_noninstitutionalized_58795d36` | *text* | Estimated percent insured (%) for population age 26+ (educational attainment universe). |
| `estimate_percent_insured_civilian_noninstitutionalized_4da06759` | *text* | Estimated percent insured (%) for population age 26+ with less than high school graduate. |
| `estimate_percent_insured_civilian_noninstitutionalized_c81fe39f` | *text* | Estimated percent insured (%) for population age 26+ with high school graduate (incl. equivalency). |
| `estimate_percent_insured_civilian_noninstitutionalized_fda5c122` | *text* | Estimated percent insured (%) for population age 26+ with some college or associate’s degree. |
| `estimate_percent_insured_civilian_noninstitutionalized_ffb31434` | *text* | Estimated percent insured (%) for population age 26+ with bachelor’s degree or higher. |
| `estimate_percent_insured_civilian_noninstitutionalized_035d657f` | *text* | Estimated percent insured (%) for population age 19–64 (employment status universe). |
| `estimate_percent_insured_civilian_noninstitutionalized_5c08c9ba` | *text* | Estimated percent insured (%) for population age 19–64 in labor force. |
| `estimate_percent_insured_civilian_noninstitutionalized_27ddc490` | *text* | Estimated percent insured (%) for population age 19–64 in labor force and employed. |
| `estimate_percent_insured_civilian_noninstitutionalized_b82623bc` | *text* | Estimated percent insured (%) for population age 19–64 in labor force and unemployed. |
| `estimate_percent_insured_civilian_noninstitutionalized_9386334d` | *text* | Estimated percent insured (%) for population age 19–64 not in labor force. |
| `estimate_percent_insured_civilian_noninstitutionalized_fd4b77b4` | *text* | Estimated percent insured (%) for population age 19–64 (work experience universe). |
| `estimate_percent_insured_civilian_noninstitutionalized_22561c7e` | *text* | Estimated percent insured (%) for population age 19–64 worked full-time, year-round in past 12 months. |
| `estimate_percent_insured_civilian_noninstitutionalized_ab50a493` | *text* | Estimated percent insured (%) for population age 19–64 worked less than full-time, year-round in past 12 months. |
| `estimate_percent_insured_civilian_noninstitutionalized_514082ed` | *text* | Estimated percent insured (%) for population age 19–64 did not work in past 12 months. |
| `estimate_percent_insured_civilian_noninstitutionalized_8404bd73` | *text* | Estimated percent insured (%) by household income (total household population; 2024 inflation-adjusted). |
| `estimate_percent_insured_civilian_noninstitutionalized_089f4efa` | *text* | Estimated percent insured (%) for household income under $25,000 (2024 inflation-adjusted). |
| `estimate_percent_insured_civilian_noninstitutionalized_f82814b7` | *text* | Estimated percent insured (%) for household income $25,000 to $49,999 (2024 inflation-adjusted). |
| `estimate_percent_insured_civilian_noninstitutionalized_1c2e0e56` | *text* | Estimated percent insured (%) for household income $50,000 to $74,999 (2024 inflation-adjusted). |
| `estimate_percent_insured_civilian_noninstitutionalized_0bdeaf64` | *text* | Estimated percent insured (%) for household income $75,000 to $99,999 (2024 inflation-adjusted). |
| `estimate_percent_insured_civilian_noninstitutionalized_0320a26f` | *text* | Estimated percent insured (%) for household income $100,000 and over (2024 inflation-adjusted). |
| `estimate_percent_insured_civilian_noninstitutionalized_626ade2a` | *text* | Estimated percent insured (%) for population with determined poverty status (income-to-poverty ratio). |
| `estimate_percent_insured_civilian_noninstitutionalized_695f6093` | *text* | Estimated percent insured (%) for population below 138% of poverty threshold. |
| `estimate_percent_insured_civilian_noninstitutionalized_670b54d4` | *text* | Estimated percent insured (%) for population 138% to 399% of poverty threshold. |
| `estimate_percent_insured_civilian_noninstitutionalized_c05962a5` | *text* | Estimated percent insured (%) for population at or above 400% of poverty threshold. |
| `estimate_percent_insured_civilian_noninstitutionalized_66b23cc7` | *text* | Estimated percent insured (%) for population below 100% of poverty threshold. |
| `estimate_uninsured_civilian_noninstitutionalized_population` | *text* | Estimated uninsured civilian noninstitutionalized population (all ages). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_934cebf8` | *text* | Estimated uninsured civilian noninstitutionalized population age under 6 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_75ffbfa2` | *text* | Estimated uninsured civilian noninstitutionalized population age 6 to 18 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_1cd58567` | *text* | Estimated uninsured civilian noninstitutionalized population age 19 to 25 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_ee568307` | *text* | Estimated uninsured civilian noninstitutionalized population age 26 to 34 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_a7593f0e` | *text* | Estimated uninsured civilian noninstitutionalized population age 35 to 44 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_ca0fd1d9` | *text* | Estimated uninsured civilian noninstitutionalized population age 45 to 54 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_f8ec1d37` | *text* | Estimated uninsured civilian noninstitutionalized population age 55 to 64 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_e6372da4` | *text* | Estimated uninsured civilian noninstitutionalized population age 65 to 74 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_2bb2f995` | *text* | Estimated uninsured civilian noninstitutionalized population age 75 years and older. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_b0abbdb5` | *text* | Estimated uninsured civilian noninstitutionalized population age under 19 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_f7048159` | *text* | Estimated uninsured civilian noninstitutionalized population age 19 to 64 years. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_f53365bb` | *text* | Estimated uninsured civilian noninstitutionalized population age 65 years and older. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_b84c0dd4` | *text* | Estimated uninsured male civilian noninstitutionalized population. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_e143669e` | *text* | Estimated uninsured female civilian noninstitutionalized population. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_c23db20b` | *text* | Estimated uninsured civilian noninstitutionalized population: White alone. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_112fb2cc` | *text* | Estimated uninsured civilian noninstitutionalized population: Black or African American alone. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_710596ed` | *text* | Estimated uninsured civilian noninstitutionalized population: American Indian and Alaska Native alone. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_d55785d3` | *text* | Estimated uninsured civilian noninstitutionalized population: Asian alone. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_7333a26b` | *text* | Estimated uninsured civilian noninstitutionalized population: Native Hawaiian and Other Pacific Islander alone. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_1c285dcc` | *text* | Estimated uninsured civilian noninstitutionalized population: Some other race alone. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_3864a8c7` | *text* | Estimated uninsured civilian noninstitutionalized population: Two or more races. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_2b429a36` | *text* | Estimated uninsured civilian noninstitutionalized population: Hispanic or Latino (of any race). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_dc595acc` | *text* | Estimated uninsured civilian noninstitutionalized population: White alone, not Hispanic or Latino. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_b1f86d1a` | *text* | Estimated uninsured civilian noninstitutionalized population in family households. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_93748f7d` | *text* | Estimated uninsured civilian noninstitutionalized population in married-couple families. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_180ae246` | *text* | Estimated uninsured civilian noninstitutionalized population in other families (non–married-couple). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_aaae0cc4` | *text* | Estimated uninsured civilian noninstitutionalized population in other families: male reference person, no spouse present. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_ba8db47c` | *text* | Estimated uninsured civilian noninstitutionalized population in other families: female reference person, no spouse present. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_460aa36d` | *text* | Estimated uninsured civilian noninstitutionalized population in non-family households and other living arrangements. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_33d68416` | *text* | Estimated uninsured civilian noninstitutionalized population: native born. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_52346c83` | *text* | Estimated uninsured civilian noninstitutionalized population: foreign born. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_71a6a45b` | *text* | Estimated uninsured civilian noninstitutionalized population: foreign born, naturalized citizen. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_8ceaa818` | *text* | Estimated uninsured civilian noninstitutionalized population: foreign born, not a U.S. citizen. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_639fe918` | *text* | Estimated uninsured civilian noninstitutionalized population with a disability. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_df6cf234` | *text* | Estimated uninsured civilian noninstitutionalized population with no disability. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_62a63d10` | *text* | Estimated uninsured civilian noninstitutionalized population age 26+ (educational attainment universe). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_c2af205e` | *text* | Estimated uninsured civilian noninstitutionalized population age 26+ with less than high school graduate. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_464e9e9f` | *text* | Estimated uninsured civilian noninstitutionalized population age 26+ with high school graduate (incl. equivalency). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_3bff1308` | *text* | Estimated uninsured civilian noninstitutionalized population age 26+ with some college or associate’s degree. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_ff1ced26` | *text* | Estimated uninsured civilian noninstitutionalized population age 26+ with bachelor’s degree or higher. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_f0587118` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 (employment status universe). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_a2727428` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 in labor force. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_72e24811` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 in labor force and employed. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_71a67fd3` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 in labor force and unemployed. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_21a32517` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 not in labor force. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_f02003fd` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 (work experience universe). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_a0b93942` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 worked full-time, year-round in past 12 months. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_3afa2497` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 worked less than full-time, year-round in past 12 months. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_9c107b39` | *text* | Estimated uninsured civilian noninstitutionalized population age 19–64 did not work in past 12 months. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_4c8ec97e` | *text* | Estimated uninsured household population (income categories; 2024 inflation-adjusted dollars). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_2e60298c` | *text* | Estimated uninsured household population with household income under $25,000 (2024 inflation-adjusted). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_8a5c4566` | *text* | Estimated uninsured household population with household income $25,000 to $49,999 (2024 inflation-adjusted). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_1ee0276f` | *text* | Estimated uninsured household population with household income $50,000 to $74,999 (2024 inflation-adjusted). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_1935dc84` | *text* | Estimated uninsured household population with household income $75,000 to $99,999 (2024 inflation-adjusted). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_f53013de` | *text* | Estimated uninsured household population with household income $100,000 and over (2024 inflation-adjusted). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_c3b05476` | *text* | Estimated uninsured population for whom poverty status is determined (income-to-poverty ratio). |
| `estimate_uninsured_civilian_noninstitutionalized_popul_8796f12c` | *text* | Estimated uninsured population below 138% of poverty threshold. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_ba6bc2b0` | *text* | Estimated uninsured population 138% to 399% of poverty threshold. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_b1c5ab21` | *text* | Estimated uninsured population at or above 400% of poverty threshold. |
| `estimate_uninsured_civilian_noninstitutionalized_popul_44aedb21` | *text* | Estimated uninsured population below 100% of poverty threshold. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_5f6c24db` | *text* | Estimated percent uninsured (%) of the civilian noninstitutionalized population (all ages). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_0e6807c5` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age under 6 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_37e8d5d2` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 6 to 18 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_baa4cafc` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 19 to 25 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_57e086e7` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 26 to 34 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_a262ed96` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 35 to 44 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_e02c7911` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 45 to 54 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_f60d28a9` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 55 to 64 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_3608b6fb` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 65 to 74 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_f83217a3` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 75 years and older. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_f3d8dfd9` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age under 19 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_6d289147` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 19 to 64 years. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_4104b373` | *text* | Estimated percent uninsured (%) for civilian noninstitutionalized population age 65 years and older. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_143ef003` | *text* | Estimated percent uninsured (%) for male civilian noninstitutionalized population. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_5a927ab6` | *text* | Estimated percent uninsured (%) for female civilian noninstitutionalized population. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_a8dcb0ea` | *text* | Estimated percent uninsured (%) for White alone. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_9e8fb1ea` | *text* | Estimated percent uninsured (%) for Black or African American alone. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_22b1985d` | *text* | Estimated percent uninsured (%) for American Indian and Alaska Native alone. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_cb30acdf` | *text* | Estimated percent uninsured (%) for Asian alone. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_c4a6a94b` | *text* | Estimated percent uninsured (%) for Native Hawaiian and Other Pacific Islander alone. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_30c56d00` | *text* | Estimated percent uninsured (%) for Some other race alone. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_2d72017a` | *text* | Estimated percent uninsured (%) for Two or more races. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_650b0b0c` | *text* | Estimated percent uninsured (%) for Hispanic or Latino (of any race). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_275fb89d` | *text* | Estimated percent uninsured (%) for White alone, not Hispanic or Latino. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_21893e20` | *text* | Estimated percent uninsured (%) for people in family households. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_0a79a929` | *text* | Estimated percent uninsured (%) for people in married-couple families. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_c568b12c` | *text* | Estimated percent uninsured (%) for people in other families (non–married-couple). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_5f621555` | *text* | Estimated percent uninsured (%) for other families: male reference person, no spouse present. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_75d30af2` | *text* | Estimated percent uninsured (%) for other families: female reference person, no spouse present. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_6c737f35` | *text* | Estimated percent uninsured (%) for non-family households and other living arrangements. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_9cb70f66` | *text* | Estimated percent uninsured (%) for native born. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_75cbf5bd` | *text* | Estimated percent uninsured (%) for foreign born. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_04d0041a` | *text* | Estimated percent uninsured (%) for foreign born, naturalized citizen. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_fc0d1f7d` | *text* | Estimated percent uninsured (%) for foreign born, not a U.S. citizen. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_ca3a6312` | *text* | Estimated percent uninsured (%) for people with a disability. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_c6db23e6` | *text* | Estimated percent uninsured (%) for people with no disability. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_a4172629` | *text* | Estimated percent uninsured (%) for population age 26+ (educational attainment universe). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_cb4afdde` | *text* | Estimated percent uninsured (%) for population age 26+ with less than high school graduate. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_1f64d7ec` | *text* | Estimated percent uninsured (%) for population age 26+ with high school graduate (incl. equivalency). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_bb49031d` | *text* | Estimated percent uninsured (%) for population age 26+ with some college or associate’s degree. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_41503323` | *text* | Estimated percent uninsured (%) for population age 26+ with bachelor’s degree or higher. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_ace99ff6` | *text* | Estimated percent uninsured (%) for population age 19–64 (employment status universe). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_b1cb097a` | *text* | Estimated percent uninsured (%) for population age 19–64 in labor force. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_49aa06be` | *text* | Estimated percent uninsured (%) for population age 19–64 in labor force and employed. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_480b1180` | *text* | Estimated percent uninsured (%) for population age 19–64 in labor force and unemployed. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_3e9d6a65` | *text* | Estimated percent uninsured (%) for population age 19–64 not in labor force. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_95dff00d` | *text* | Estimated percent uninsured (%) for population age 19–64 (work experience universe). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_bec13b7c` | *text* | Estimated percent uninsured (%) for population age 19–64 worked full-time, year-round in past 12 months. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_a1da16d5` | *text* | Estimated percent uninsured (%) for population age 19–64 worked less than full-time, year-round in past 12 months. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_1fa19230` | *text* | Estimated percent uninsured (%) for population age 19–64 did not work in past 12 months. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_4e0e7d4e` | *text* | Estimated percent uninsured (%) by household income (total household population; 2024 inflation-adjusted). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_0395299c` | *text* | Estimated percent uninsured (%) for household income under $25,000 (2024 inflation-adjusted). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_ae57ba61` | *text* | Estimated percent uninsured (%) for household income $25,000 to $49,999 (2024 inflation-adjusted). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_d75c4ccd` | *text* | Estimated percent uninsured (%) for household income $50,000 to $74,999 (2024 inflation-adjusted). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_bff798bf` | *text* | Estimated percent uninsured (%) for household income $75,000 to $99,999 (2024 inflation-adjusted). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_91657b17` | *text* | Estimated percent uninsured (%) for household income $100,000 and over (2024 inflation-adjusted). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_1629fb53` | *text* | Estimated percent uninsured (%) for population with determined poverty status (income-to-poverty ratio). |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_8abb5ce8` | *text* | Estimated percent uninsured (%) for population below 138% of poverty threshold. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_b4e033e4` | *text* | Estimated percent uninsured (%) for population 138% to 399% of poverty threshold. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_1cf5cae7` | *text* | Estimated percent uninsured (%) for population at or above 400% of poverty threshold. |
| `estimate_percent_uninsured_civilian_noninstitutionaliz_37acc439` | *text* | Estimated percent uninsured (%) for population below 100% of poverty threshold. |

---

## Table: `huseholds_and_families`
- **Row Count**: 85,382
- **Time Range**: N/A
- **Description**: Demographic data regarding household types, family structures, and living arrangements.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier for the area (e.g., GEOID). |
| `geographic_area_name` | *text* | Human-readable name of the geographic area. |
| `estimate_total_households_total_households` | *text* | Estimated total number of households (all household types). |
| `estimate_total_households_average_household_size` | *text* | Average household size (persons per household) for all households. |
| `estimate_total_families_total_families` | *text* | Estimated total number of families (family households). |
| `estimate_total_families_average_family_size` | *text* | Average family size (persons per family) for all families. |
| `estimate_total_age_of_own_children_households_with_own_5d3f8ad7` | *text* | Estimated households with own children of the householder under 18 years. |
| `estimate_total_age_of_own_children_households_with_own_e52d8878` | *text* | Estimated households with own children under 18 years where children are under 6 years only. |
| `estimate_total_age_of_own_children_households_with_own_e41aa0da` | *text* | Estimated households with own children under 18 years with both under 6 and 6–17 years present. |
| `estimate_total_age_of_own_children_households_with_own_d10078ff` | *text* | Estimated households with own children under 18 years where children are 6–17 years only. |
| `estimate_total_total_households` | *text* | Estimated total number of households (overall total households line). |
| `estimate_total_total_households_selected_households_by_8910d60b` | *text* | Estimated households with one or more people under 18 years. |
| `estimate_total_total_households_selected_households_by_c4f854ef` | *text* | Estimated households with one or more people age 60 years and over. |
| `estimate_total_total_households_selected_households_by_2e2656ac` | *text* | Estimated households with one or more people age 65 years and over. |
| `estimate_total_total_households_selected_households_by_349cdc30` | *text* | Estimated households where the householder lives alone. |
| `estimate_total_total_households_selected_households_by_d7bb49f1` | *text* | Estimated households where the householder lives alone and is age 65 years and over. |
| `estimate_total_total_households_units_in_structure_1_u_fe0b5efe` | *text* | Estimated households in 1-unit structures (detached or attached). |
| `estimate_total_total_households_units_in_structure_2_o_4f0d36e8` | *text* | Estimated households in 2-or-more-unit structures (apartments/condos). |
| `estimate_total_total_households_units_in_structure_mob_15f0e5bd` | *text* | Estimated households in mobile homes and all other unit types. |
| `estimate_total_total_households_housing_tenure_owner_o_3630f672` | *text* | Estimated owner-occupied housing units (households). |
| `estimate_total_total_households_housing_tenure_renter_1f2b3043` | *text* | Estimated renter-occupied housing units (households). |
| `estimate_married_couple_family_household_households_to_055482a4` | *text* | Estimated total number of households that are married-couple family households. |
| `estimate_married_couple_family_household_households_av_4f87e24f` | *text* | Average household size for married-couple family households. |
| `estimate_married_couple_family_household_families_tota_b688f165` | *text* | Estimated total number of families that are married-couple families. |
| `estimate_married_couple_family_household_families_aver_d839aa1c` | *text* | Average family size for married-couple families. |
| `estimate_married_couple_family_household_age_of_own_ch_382353f8` | *text* | Estimated married-couple family households with own children under 18 years. |
| `estimate_married_couple_family_household_age_of_own_ch_8dfcdfbd` | *text* | Estimated married-couple family households with own children under 18: under 6 years only. |
| `estimate_married_couple_family_household_age_of_own_ch_a70b5e72` | *text* | Estimated married-couple family households with own children under 18: under 6 and 6–17 years. |
| `estimate_married_couple_family_household_age_of_own_ch_d5921912` | *text* | Estimated married-couple family households with own children under 18: 6–17 years only. |
| `estimate_married_couple_family_household_total_households` | *text* | Estimated total married-couple family households (overall total households line for this group). |
| `estimate_married_couple_family_household_total_househo_081a545d` | *text* | Estimated married-couple family households with one or more people under 18 years. |
| `estimate_married_couple_family_household_total_househo_f1f84a15` | *text* | Estimated married-couple family households with one or more people age 60 years and over. |
| `estimate_married_couple_family_household_total_househo_11381074` | *text* | Estimated married-couple family households with one or more people age 65 years and over. |
| `estimate_married_couple_family_household_total_househo_f284a465` | *text* | Estimated married-couple family households where the householder lives alone. |
| `estimate_married_couple_family_household_total_househo_36142fa1` | *text* | Estimated married-couple family households where householder lives alone and is age 65+. |
| `estimate_married_couple_family_household_total_househo_2f1510dd` | *text* | Estimated married-couple family households in 1-unit structures. |
| `estimate_married_couple_family_household_total_househo_9bbc9541` | *text* | Estimated married-couple family households in 2-or-more-unit structures. |
| `estimate_married_couple_family_household_total_househo_1db89251` | *text* | Estimated married-couple family households in mobile homes/other unit types. |
| `estimate_married_couple_family_household_total_househo_b28b7214` | *text* | Estimated married-couple family households that are owner-occupied. |
| `estimate_married_couple_family_household_total_househo_90da2f24` | *text* | Estimated married-couple family households that are renter-occupied. |
| `estimate_male_householder_no_spouse_present_family_hou_81466893` | *text* | Estimated total households that are male householder, no spouse present, family households. |
| `estimate_male_householder_no_spouse_present_family_hou_4836ceb1` | *text* | Average household size for male householder, no spouse present, family households. |
| `estimate_male_householder_no_spouse_present_family_hou_a63467f4` | *text* | Estimated total families that are male householder, no spouse present, family households. |
| `estimate_male_householder_no_spouse_present_family_hou_bdb92a47` | *text* | Average family size for male householder, no spouse present, family households. |
| `estimate_male_householder_no_spouse_present_family_hou_79b7a05e` | *text* | Estimated male householder (no spouse) family households with own children under 18 years. |
| `estimate_male_householder_no_spouse_present_family_hou_f8a3919c` | *text* | Estimated male householder (no spouse) family households with own children under 18: under 6 years only. |
| `estimate_male_householder_no_spouse_present_family_hou_d3201ea6` | *text* | Estimated male householder (no spouse) family households with own children under 18: under 6 and 6–17 years. |
| `estimate_male_householder_no_spouse_present_family_hou_00099b90` | *text* | Estimated male householder (no spouse) family households with own children under 18: 6–17 years only. |
| `estimate_male_householder_no_spouse_present_family_hou_fbf4c795` | *text* | Estimated total male householder, no spouse present, family households (overall total households line for this group). |
| `estimate_male_householder_no_spouse_present_family_hou_402b6a90` | *text* | Estimated male householder (no spouse) family households with one or more people under 18 years. |
| `estimate_male_householder_no_spouse_present_family_hou_14a52d81` | *text* | Estimated male householder (no spouse) family households with one or more people age 60 years and over. |
| `estimate_male_householder_no_spouse_present_family_hou_41b62287` | *text* | Estimated male householder (no spouse) family households with one or more people age 65 years and over. |
| `estimate_male_householder_no_spouse_present_family_hou_e7dd3dcf` | *text* | Estimated male householder (no spouse) family households where the householder lives alone. |
| `estimate_male_householder_no_spouse_present_family_hou_8e34899a` | *text* | Estimated male householder (no spouse) family households where householder lives alone and is age 65+. |
| `estimate_male_householder_no_spouse_present_family_hou_8f85e33b` | *text* | Estimated male householder (no spouse) family households in 1-unit structures. |
| `estimate_male_householder_no_spouse_present_family_hou_e2ca157a` | *text* | Estimated male householder (no spouse) family households in 2-or-more-unit structures. |
| `estimate_male_householder_no_spouse_present_family_hou_9690f6d1` | *text* | Estimated male householder (no spouse) family households in mobile homes/other unit types. |
| `estimate_male_householder_no_spouse_present_family_hou_037ebb1a` | *text* | Estimated male householder (no spouse) family households that are owner-occupied. |
| `estimate_male_householder_no_spouse_present_family_hou_6b211f88` | *text* | Estimated male householder (no spouse) family households that are renter-occupied. |
| `estimate_female_householder_no_spouse_present_family_h_b6f7d385` | *text* | Estimated total households that are female householder, no spouse present, family households. |
| `estimate_female_householder_no_spouse_present_family_h_97feea01` | *text* | Average household size for female householder, no spouse present, family households. |
| `estimate_female_householder_no_spouse_present_family_h_cf5a64ee` | *text* | Estimated total families that are female householder, no spouse present, family households. |
| `estimate_female_householder_no_spouse_present_family_h_f6d31f88` | *text* | Average family size for female householder, no spouse present, family households. |
| `estimate_female_householder_no_spouse_present_family_h_18916314` | *text* | Estimated female householder (no spouse) family households with own children under 18 years. |
| `estimate_female_householder_no_spouse_present_family_h_b7c2dcd0` | *text* | Estimated female householder (no spouse) family households with own children under 18: under 6 years only. |
| `estimate_female_householder_no_spouse_present_family_h_9f382ef5` | *text* | Estimated female householder (no spouse) family households with own children under 18: under 6 and 6–17 years. |
| `estimate_female_householder_no_spouse_present_family_h_e825df72` | *text* | Estimated female householder (no spouse) family households with own children under 18: 6–17 years only. |
| `estimate_female_householder_no_spouse_present_family_h_31a945c7` | *text* | Estimated total female householder, no spouse present, family households (overall total households line for this group). |
| `estimate_female_householder_no_spouse_present_family_h_544af2f5` | *text* | Estimated female householder (no spouse) family households with one or more people under 18 years. |
| `estimate_female_householder_no_spouse_present_family_h_28a719f4` | *text* | Estimated female householder (no spouse) family households with one or more people age 60 years and over. |
| `estimate_female_householder_no_spouse_present_family_h_2dd9b43f` | *text* | Estimated female householder (no spouse) family households with one or more people age 65 years and over. |
| `estimate_female_householder_no_spouse_present_family_h_b684b9cb` | *text* | Estimated female householder (no spouse) family households where the householder lives alone. |
| `estimate_female_householder_no_spouse_present_family_h_5f160999` | *text* | Estimated female householder (no spouse) family households where householder lives alone and is age 65+. |
| `estimate_female_householder_no_spouse_present_family_h_39f7c627` | *text* | Estimated female householder (no spouse) family households in 1-unit structures. |
| `estimate_female_householder_no_spouse_present_family_h_da5e6699` | *text* | Estimated female householder (no spouse) family households in 2-or-more-unit structures. |
| `estimate_female_householder_no_spouse_present_family_h_0fce0f2b` | *text* | Estimated female householder (no spouse) family households in mobile homes/other unit types. |
| `estimate_female_householder_no_spouse_present_family_h_2f388f99` | *text* | Estimated female householder (no spouse) family households that are owner-occupied. |
| `estimate_female_householder_no_spouse_present_family_h_b962287a` | *text* | Estimated female householder (no spouse) family households that are renter-occupied. |
| `estimate_nonfamily_household_households_total_households` | *text* | Estimated total number of nonfamily households. |
| `estimate_nonfamily_household_households_average_household_size` | *text* | Average household size for nonfamily households. |
| `estimate_nonfamily_household_families_total_families` | *text* | Estimated total families within nonfamily households (typically none; included due to table structure). |
| `estimate_nonfamily_household_families_average_family_size` | *text* | Average family size within nonfamily households (typically not applicable; included due to table structure). |
| `estimate_nonfamily_household_age_of_own_children_house_157e5bcf` | *text* | Estimated nonfamily households with own children of the householder under 18 years. |
| `estimate_nonfamily_household_age_of_own_children_house_91f3d5dd` | *text* | Estimated nonfamily households with own children under 18: under 6 years only. |
| `estimate_nonfamily_household_age_of_own_children_house_2b528166` | *text* | Estimated nonfamily households with own children under 18: under 6 and 6–17 years. |
| `estimate_nonfamily_household_age_of_own_children_house_f185b069` | *text* | Estimated nonfamily households with own children under 18: 6–17 years only. |
| `estimate_nonfamily_household_total_households` | *text* | Estimated total nonfamily households (overall total households line for this group). |
| `estimate_nonfamily_household_total_households_selected_fe9bdafa` | *text* | Estimated nonfamily households with one or more people under 18 years. |
| `estimate_nonfamily_household_total_households_selected_64435199` | *text* | Estimated nonfamily households with one or more people age 60 years and over. |
| `estimate_nonfamily_household_total_households_selected_2c3a5d11` | *text* | Estimated nonfamily households with one or more people age 65 years and over. |
| `estimate_nonfamily_household_total_households_selected_68def918` | *text* | Estimated nonfamily households where the householder lives alone. |
| `estimate_nonfamily_household_total_households_selected_b2a2ecbd` | *text* | Estimated nonfamily households where the householder lives alone and is age 65+. |
| `estimate_nonfamily_household_total_households_units_in_99c21652` | *text* | Estimated nonfamily households in 1-unit structures. |
| `estimate_nonfamily_household_total_households_units_in_bf19b75f` | *text* | Estimated nonfamily households in 2-or-more-unit structures. |
| `estimate_nonfamily_household_total_households_units_in_ed1673c0` | *text* | Estimated nonfamily households in mobile homes/other unit types. |
| `estimate_nonfamily_household_total_households_housing_9feb2b59` | *text* | Estimated nonfamily households that are owner-occupied. |
| `estimate_nonfamily_household_total_households_housing_f27ddc9c` | *text* | Estimated nonfamily households that are renter-occupied. |

---

## Table: `means_of_transportation_to_work`
- **Row Count**: 242,297
- **Time Range**: N/A
- **Description**: Commuting data describing how workers travel to their jobs (e.g., car, transit, walk).

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier for the area (e.g., GEOID). |
| `geographic_area_name` | *text* | Human-readable name of the geographic area. |
| `estimate_total` | *text* | Total estimated workers (universe for transportation to work categories). |
| `estimate_total_car_truck_or_van` | *text* | Estimated workers who commute by car, truck, or van (all driving/carpooling). |
| `estimate_total_car_truck_or_van_drove_alone` | *text* | Estimated workers who drove alone by car, truck, or van. |
| `estimate_total_car_truck_or_van_carpooled` | *text* | Estimated workers who carpooled by car, truck, or van (all carpool sizes). |
| `estimate_total_car_truck_or_van_carpooled_in_2_person_carpool` | *text* | Estimated workers in a 2-person carpool. |
| `estimate_total_car_truck_or_van_carpooled_in_3_person_carpool` | *text* | Estimated workers in a 3-person carpool. |
| `estimate_total_car_truck_or_van_carpooled_in_4_person_carpool` | *text* | Estimated workers in a 4-person carpool. |
| `estimate_total_car_truck_or_van_carpooled_in_5_or_6_pe_ed911242` | *text* | Estimated workers in a 5- or 6-person carpool. |
| `estimate_total_car_truck_or_van_carpooled_in_7_or_more_b3a9e92d` | *text* | Estimated workers in a 7-or-more-person carpool. |
| `estimate_total_public_transportation` | *text* | Estimated workers using public transportation (all public transit modes). |
| `estimate_total_public_transportation_bus` | *text* | Estimated workers commuting by bus. |
| `estimate_total_public_transportation_subway_or_elevated_rail` | *text* | Estimated workers commuting by subway or elevated rail. |
| `estimate_total_public_transportation_long_distance_tra_cac89c0e` | *text* | Estimated workers commuting by long-distance train or commuter rail. |
| `estimate_total_public_transportation_light_rail_street_9757630c` | *text* | Estimated workers commuting by light rail, streetcar, or trolley (includes carro público in Puerto Rico). |
| `estimate_total_public_transportation_ferryboat` | *text* | Estimated workers commuting by ferryboat. |
| `estimate_total_taxi_or_ride_hailing_services` | *text* | Estimated workers commuting by taxi or ride-hailing services. |
| `estimate_total_motorcycle` | *text* | Estimated workers commuting by motorcycle. |
| `estimate_total_bicycle` | *text* | Estimated workers commuting by bicycle. |
| `estimate_total_walked` | *text* | Estimated workers who walked to work. |
| `estimate_total_other_means` | *text* | Estimated workers using other means not listed (e.g., various nonstandard modes). |
| `estimate_total_worked_from_home` | *text* | Estimated workers who worked from home. |

---

## Table: `pubassist_inc_12mo_hh`
- **Row Count**: 242,297
- **Time Range**: N/A
- **Description**: Data on households receiving public assistance income or food stamps/SNAP in the past 12 months.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier for the area (e.g., GEOID). |
| `geographic_area_name` | *text* | Human-readable name of the geographic area. |
| `estimate_total` | *text* | Total estimated households (universe for public assistance income status). |
| `estimate_total_with_public_assistance_income` | *text* | Estimated households with public assistance income in the past 12 months. |
| `estimate_total_no_public_assistance_income` | *text* | Estimated households with no public assistance income in the past 12 months. |

---

## Table: `school_enroll_level_pop_3plus`
- **Row Count**: 85,382
- **Time Range**: N/A
- **Description**: School enrollment statistics by level (nursery through graduate school) for population aged 3+.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier for the area (e.g., GEOID). |
| `geographic_area_name` | *text* | Human-readable name of the geographic area. |
| `estimate_total` | *text* | Total estimated population age 3 years and over. |
| `estimate_total_enrolled_in_school` | *text* | Estimated number of people age 3+ who are enrolled in school (any level). |
| `estimate_total_enrolled_in_school_enrolled_in_nursery_2815372a` | *text* | Estimated number of people age 3+ enrolled in nursery school or preschool. |
| `estimate_total_enrolled_in_school_enrolled_in_kindergarten` | *text* | Estimated number of people age 3+ enrolled in kindergarten. |
| `estimate_total_enrolled_in_school_enrolled_in_grade_1_99016dab` | *text* | Estimated number of people age 3+ enrolled in grades 1 through 4. |
| `estimate_total_enrolled_in_school_enrolled_in_grade_5_94a76c91` | *text* | Estimated number of people age 3+ enrolled in grades 5 through 8. |
| `estimate_total_enrolled_in_school_enrolled_in_grade_9_50e0ce35` | *text* | Estimated number of people age 3+ enrolled in grades 9 through 12. |
| `estimate_total_enrolled_in_school_enrolled_in_college_50257787` | *text* | Estimated number of people age 3+ enrolled in college (undergraduate years). |
| `estimate_total_enrolled_in_school_graduate_or_professi_6713ce2c` | *text* | Estimated number of people age 3+ enrolled in graduate or professional school. |
| `estimate_total_not_enrolled_in_school` | *text* | Estimated number of people age 3+ not enrolled in school. |

---

## Table: `segregation_index`
- **Row Count**: 35,422
- **Time Range**: 2013 - 2023
- **Description**: Metrics quantifying residential segregation within geographic areas.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `county_fips` | *number* | County identifier using the FIPS code (typically 5 digits; may appear without leading zeros when stored as integer). |
| `dissimilarity` | *number* | Dissimilarity index (evenness): share of one group that would need to move across tracts to match the county-wide distribution. |
| `spatial_proximity` | *number* | Spatial proximity index: degree to which members of a group live near one another (incorporates spatial adjacency/distance between tracts). |
| `isolation` | *number* | Isolation index (exposure): probability that a typical person from the group shares a tract with someone from the same group. |
| `delta` | *number* | Delta (concentration) index: degree to which a group is concentrated into a smaller (or larger) share of geographic space than expected. |
| `tract_count` | *number* | Number of census tracts used to compute the indices for that county-year. |
| `year` | *number* | Year of the estimate / computation. |

---

## Table: `sex_occ_civemp_pop_16plus`
- **Row Count**: 242,297
- **Time Range**: N/A
- **Description**: Breakdown of occupation and employment status by sex for the civilian population aged 16+.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `geo_id` | *text* | Geographic identifier for the area (e.g., GEOID). |
| `geographic_area_name` | *text* | Display name of the geographic area. |
| `estimate_total` | *text* | Total estimated civilian employed population age 16+. |
| `estimate_total_male` | *text* | Total estimated male civilian employed population age 16+. |
| `estimate_total_male_management_business_science_and_ar_ba5e0e18` | *text* | Estimated male workers age 16+ in management, business, science, and arts occupations (overall). |
| `estimate_total_male_management_business_science_and_ar_4c57e1e4` | *text* | Estimated male workers age 16+ in management, business, and financial occupations. |
| `estimate_total_male_management_business_science_and_ar_c9a4e213` | *text* | Estimated male workers age 16+ in management occupations. |
| `estimate_total_male_management_business_science_and_ar_802af4d7` | *text* | Estimated male workers age 16+ in business and financial operations occupations. |
| `estimate_total_male_management_business_science_and_ar_691a7b5f` | *text* | Estimated male workers age 16+ in computer, engineering, and science occupations (overall). |
| `estimate_total_male_management_business_science_and_ar_65166dcd` | *text* | Estimated male workers age 16+ in computer and mathematical occupations. |
| `estimate_total_male_management_business_science_and_ar_ab90da24` | *text* | Estimated male workers age 16+ in architecture and engineering occupations. |
| `estimate_total_male_management_business_science_and_ar_3a9867a7` | *text* | Estimated male workers age 16+ in life, physical, and social science occupations. |
| `estimate_total_male_management_business_science_and_ar_1bc2493c` | *text* | Estimated male workers age 16+ in education, legal, community service, arts, and media occupations (overall). |
| `estimate_total_male_management_business_science_and_ar_b5c88051` | *text* | Estimated male workers age 16+ in community and social service occupations. |
| `estimate_total_male_management_business_science_and_ar_8881f786` | *text* | Estimated male workers age 16+ in legal occupations. |
| `estimate_total_male_management_business_science_and_ar_c7b34430` | *text* | Estimated male workers age 16+ in educational instruction and library occupations. |
| `estimate_total_male_management_business_science_and_ar_fcc3df2e` | *text* | Estimated male workers age 16+ in arts, design, entertainment, sports, and media occupations. |
| `estimate_total_male_management_business_science_and_ar_c230a718` | *text* | Estimated male workers age 16+ in healthcare practitioners and technical occupations (overall). |
| `estimate_total_male_management_business_science_and_ar_241ac150` | *text* | Estimated male workers age 16+ in health diagnosing/treating practitioners and other technical occupations. |
| `estimate_total_male_management_business_science_and_ar_3e020336` | *text* | Estimated male workers age 16+ in health technologists and technicians. |
| `estimate_total_male_service_occupations` | *text* | Estimated male workers age 16+ in service occupations (overall). |
| `estimate_total_male_service_occupations_healthcare_sup_9fc3acd7` | *text* | Estimated male workers age 16+ in healthcare support occupations. |
| `estimate_total_male_service_occupations_protective_ser_bad6a50b` | *text* | Estimated male workers age 16+ in protective service occupations (overall). |
| `estimate_total_male_service_occupations_protective_ser_55f43e99` | *text* | Estimated male workers age 16+ in firefighting/prevention and other protective service workers (incl. supervisors). |
| `estimate_total_male_service_occupations_protective_ser_536356b7` | *text* | Estimated male workers age 16+ in law enforcement workers (incl. supervisors). |
| `estimate_total_male_service_occupations_food_preparati_0fe9e020` | *text* | Estimated male workers age 16+ in food preparation and serving related occupations. |
| `estimate_total_male_service_occupations_building_and_g_95197246` | *text* | Estimated male workers age 16+ in building and grounds cleaning and maintenance occupations. |
| `estimate_total_male_service_occupations_personal_care_41dea292` | *text* | Estimated male workers age 16+ in personal care and service occupations. |
| `estimate_total_male_sales_and_office_occupations` | *text* | Estimated male workers age 16+ in sales and office occupations (overall). |
| `estimate_total_male_sales_and_office_occupations_sales_4d2d6418` | *text* | Estimated male workers age 16+ in sales and related occupations. |
| `estimate_total_male_sales_and_office_occupations_offic_e4dc761d` | *text* | Estimated male workers age 16+ in office and administrative support occupations. |
| `estimate_total_male_natural_resources_construction_and_0e63e6a0` | *text* | Estimated male workers age 16+ in natural resources, construction, and maintenance occupations (overall). |
| `estimate_total_male_natural_resources_construction_and_53f652ac` | *text* | Estimated male workers age 16+ in farming, fishing, and forestry occupations. |
| `estimate_total_male_natural_resources_construction_and_83394749` | *text* | Estimated male workers age 16+ in construction and extraction occupations. |
| `estimate_total_male_natural_resources_construction_and_42ff4ebb` | *text* | Estimated male workers age 16+ in installation, maintenance, and repair occupations. |
| `estimate_total_male_production_transportation_and_mate_23a32267` | *text* | Estimated male workers age 16+ in production, transportation, and material moving occupations (overall). |
| `estimate_total_male_production_transportation_and_mate_a0cd6c8f` | *text* | Estimated male workers age 16+ in production occupations. |
| `estimate_total_male_production_transportation_and_mate_a3df1cea` | *text* | Estimated male workers age 16+ in transportation occupations. |
| `estimate_total_male_production_transportation_and_mate_68e8b050` | *text* | Estimated male workers age 16+ in material moving occupations. |
| `estimate_total_female` | *text* | Total estimated female civilian employed population age 16+. |
| `estimate_total_female_management_business_science_and_af7d52d6` | *text* | Estimated female workers age 16+ in management, business, science, and arts occupations (overall). |
| `estimate_total_female_management_business_science_and_03f2d80b` | *text* | Estimated female workers age 16+ in management, business, and financial occupations. |
| `estimate_total_female_management_business_science_and_989ec7f7` | *text* | Estimated female workers age 16+ in management occupations. |
| `estimate_total_female_management_business_science_and_bac10f94` | *text* | Estimated female workers age 16+ in business and financial operations occupations. |
| `estimate_total_female_management_business_science_and_57e0dd7e` | *text* | Estimated female workers age 16+ in computer, engineering, and science occupations (overall). |
| `estimate_total_female_management_business_science_and_d23a68a5` | *text* | Estimated female workers age 16+ in computer and mathematical occupations. |
| `estimate_total_female_management_business_science_and_b5350ea7` | *text* | Estimated female workers age 16+ in architecture and engineering occupations. |
| `estimate_total_female_management_business_science_and_7c1cfc51` | *text* | Estimated female workers age 16+ in life, physical, and social science occupations. |
| `estimate_total_female_management_business_science_and_be2b4b81` | *text* | Estimated female workers age 16+ in education, legal, community service, arts, and media occupations (overall). |
| `estimate_total_female_management_business_science_and_0e7ce2b4` | *text* | Estimated female workers age 16+ in community and social service occupations. |
| `estimate_total_female_management_business_science_and_17d03209` | *text* | Estimated female workers age 16+ in legal occupations. |
| `estimate_total_female_management_business_science_and_60032802` | *text* | Estimated female workers age 16+ in educational instruction and library occupations. |
| `estimate_total_female_management_business_science_and_2bf1d9cb` | *text* | Estimated female workers age 16+ in arts, design, entertainment, sports, and media occupations. |
| `estimate_total_female_management_business_science_and_2d903ae3` | *text* | Estimated female workers age 16+ in healthcare practitioners and technical occupations (overall). |
| `estimate_total_female_management_business_science_and_5cf8219f` | *text* | Estimated female workers age 16+ in health diagnosing/treating practitioners and other technical occupations. |
| `estimate_total_female_management_business_science_and_af6cea19` | *text* | Estimated female workers age 16+ in health technologists and technicians. |
| `estimate_total_female_service_occupations` | *text* | Estimated female workers age 16+ in service occupations (overall). |
| `estimate_total_female_service_occupations_healthcare_s_597c0a61` | *text* | Estimated female workers age 16+ in healthcare support occupations. |
| `estimate_total_female_service_occupations_protective_s_b25c36d3` | *text* | Estimated female workers age 16+ in protective service occupations (overall). |
| `estimate_total_female_service_occupations_protective_s_9a2b4710` | *text* | Estimated female workers age 16+ in firefighting/prevention and other protective service workers (incl. supervisors). |
| `estimate_total_female_service_occupations_protective_s_b4f45ef3` | *text* | Estimated female workers age 16+ in law enforcement workers (incl. supervisors). |
| `estimate_total_female_service_occupations_food_prepara_5c6362dd` | *text* | Estimated female workers age 16+ in food preparation and serving related occupations. |
| `estimate_total_female_service_occupations_building_and_f3ce08ca` | *text* | Estimated female workers age 16+ in building and grounds cleaning and maintenance occupations. |
| `estimate_total_female_service_occupations_personal_car_ce804d93` | *text* | Estimated female workers age 16+ in personal care and service occupations. |
| `estimate_total_female_sales_and_office_occupations` | *text* | Estimated female workers age 16+ in sales and office occupations (overall). |
| `estimate_total_female_sales_and_office_occupations_sal_9ed8b850` | *text* | Estimated female workers age 16+ in sales and related occupations. |
| `estimate_total_female_sales_and_office_occupations_off_e27b05e1` | *text* | Estimated female workers age 16+ in office and administrative support occupations. |
| `estimate_total_female_natural_resources_construction_a_3b0eafa0` | *text* | Estimated female workers age 16+ in natural resources, construction, and maintenance occupations (overall). |
| `estimate_total_female_natural_resources_construction_a_88a4ecb0` | *text* | Estimated female workers age 16+ in farming, fishing, and forestry occupations. |
| `estimate_total_female_natural_resources_construction_a_5e3f8249` | *text* | Estimated female workers age 16+ in construction and extraction occupations. |
| `estimate_total_female_natural_resources_construction_a_8ea49830` | *text* | Estimated female workers age 16+ in installation, maintenance, and repair occupations. |
| `estimate_total_female_production_transportation_and_ma_f987679b` | *text* | Estimated female workers age 16+ in production, transportation, and material moving occupations (overall). |
| `estimate_total_female_production_transportation_and_ma_c41c2e17` | *text* | Estimated female workers age 16+ in production occupations. |
| `estimate_total_female_production_transportation_and_ma_72647c51` | *text* | Estimated female workers age 16+ in transportation occupations. |
| `estimate_total_female_production_transportation_and_ma_1e146c0a` | *text* | Estimated female workers age 16+ in material moving occupations. |

---

## Table: `states`
- **Row Count**: 56
- **Time Range**: N/A
- **Description**: Geographic boundaries, FIPS codes, and geometry definitions for US States.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `region` | *text* | Census region code for the state (e.g., Northeast, Midwest, South, West). |
| `division` | *text* | Census division code for the state (subdivision within a region). |
| `statefp` | *text* | 2-digit State FIPS code (string). Unique identifier for the state (e.g., '54' for West Virginia). Use this to join with 'statefp' in other tables. |
| `statens` | *text* | Census state numeric identifier (GNIS-style permanent ID for the state entity). |
| `geoid` | *text* | 2-letter State Abbreviation (e.g., 'WV', 'CA', 'NY'). Use this for filtering by state abbreviation. |
| `geoidfq` | *text* | Fully qualified GEOID (often includes a prefix such as 0400000US + GEOID). |
| `stusps` | *text* | 2-letter State Abbreviation (e.g., 'WV', 'CA', 'NY'). Use this for filtering by state abbreviation. |
| `name` | *text* | Full English name of the state (e.g., 'West Virginia'). |
| `lsad` | *text* | Legal/Statistical Area Description code for the entity (state-level LSAD code). |
| `mtfcc` | *text* | MAF/TIGER Feature Class Code identifying the feature class for state polygons. |
| `funcstat` | *text* | Functional status code (indicates the entity’s status; typically active/statistical). |
| `aland` | *number* | Land area in square meters. |
| `awater` | *number* | Water area in square meters. |
| `intptlat` | *text* | Latitude of an internal point (label point) for the state polygon (decimal degrees; often stored as text). |
| `intptlon` | *text* | Longitude of an internal point (label point) for the state polygon (decimal degrees; often stored as text). |
| `geometry` | *geometry (Polygon)* | Polygon boundary of the State. |

---

## Table: `user_uploaded_csv`
- **Row Count**: 46,882
- **Time Range**: N/A
- **Description**: User-uploaded CSV table. Replaced when a new CSV is uploaded.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `state` | *text* | N/A |
| `season` | *text* | N/A |
| `yearmonth` | *double precision* | N/A |
| `agecategory_legend` | *text* | N/A |
| `sex_label` | *text* | N/A |
| `race_label` | *text* | N/A |
| `monthlyrate` | *double precision* | N/A |
| `type` | *text* | N/A |

---

## Table: `zipcodes`
- **Row Count**: 33,791
- **Time Range**: N/A
- **Description**: ZIP code boundaries and geographic definitions.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `zcta5ce20` | *text* | N/A |
| `geoid20` | *text* | N/A |
| `classfp20` | *text* | N/A |
| `mtfcc20` | *text* | N/A |
| `funcstat20` | *text* | N/A |
| `aland20` | *bigint* | N/A |
| `awater20` | *bigint* | N/A |
| `intptlat20` | *text* | N/A |
| `intptlon20` | *text* | N/A |
| `geometry` | *USER-DEFINED* | N/A |

---
