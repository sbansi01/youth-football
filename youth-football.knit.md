
<!-- rnb-text-begin -->

---
title: "Youth Football Data Analysis"
output: html_notebook
---


<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI2xpYnJhcmllcyBcbmxpYnJhcnkodGlkeXZlcnNlKVxuYGBgIn0= -->

```r
#libraries 
library(tidyverse)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiUmVnaXN0ZXJlZCBTMyBtZXRob2RzIG92ZXJ3cml0dGVuIGJ5ICdkYnBseXInOlxuICBtZXRob2QgICAgICAgICBmcm9tXG4gIHByaW50LnRibF9sYXp5ICAgICBcbiAgcHJpbnQudGJsX3NxbCAgICAgIFxu4pSA4pSAIEF0dGFjaGluZyBwYWNrYWdlcyDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAgdGlkeXZlcnNlIDEuMy4yIOKUgOKUgOKclCBnZ3Bsb3QyIDMuMy42ICAgICDinJQgcHVycnIgICAxLjAuMlxu4pyUIHRpYmJsZSAgMy4yLjEgICAgIOKclCBkcGx5ciAgIDEuMS4zXG7inJQgdGlkeXIgICAxLjIuMSAgICAg4pyUIHN0cmluZ3IgMS40LjFcbuKclCByZWFkciAgIDIuMS40ICAgICDinJQgZm9yY2F0cyAwLjUuMuKUgOKUgCBDb25mbGljdHMg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAIHRpZHl2ZXJzZV9jb25mbGljdHMoKSDilIDilIBcbuKcliBkcGx5cjo6ZmlsdGVyKCkgbWFza3Mgc3RhdHM6OmZpbHRlcigpXG7inJYgZHBseXI6OmxhZygpICAgIG1hc2tzIHN0YXRzOjpsYWcoKVxuIn0= -->

```
Registered S3 methods overwritten by 'dbplyr':
  method         from
  print.tbl_lazy     
  print.tbl_sql      
── Attaching packages ──────────────────────────────────────────────────── tidyverse 1.3.2 ──✔ ggplot2 3.3.6     ✔ purrr   1.0.2
✔ tibble  3.2.1     ✔ dplyr   1.1.3
✔ tidyr   1.2.1     ✔ stringr 1.4.1
✔ readr   2.1.4     ✔ forcats 0.5.2── Conflicts ─────────────────────────────────────────────────────── tidyverse_conflicts() ──
✖ dplyr::filter() masks stats::filter()
✖ dplyr::lag()    masks stats::lag()
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxubGlicmFyeShnb29nbGVzaGVldHM0KVxubGlicmFyeShqYW5pdG9yKVxuYGBgIn0= -->

```r
library(googlesheets4)
library(janitor)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiXG5BdHRhY2hpbmcgcGFja2FnZTog4oCYamFuaXRvcuKAmVxuXG5UaGUgZm9sbG93aW5nIG9iamVjdHMgYXJlIG1hc2tlZCBmcm9tIOKAmHBhY2thZ2U6c3RhdHPigJk6XG5cbiAgICBjaGlzcS50ZXN0LCBmaXNoZXIudGVzdFxuIn0= -->

```

Attaching package: ‘janitor’

The following objects are masked from ‘package:stats’:

    chisq.test, fisher.test
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxubGlicmFyeSh0aWR5Y2Vuc3VzKVxuYGBgIn0= -->

```r
library(tidycensus)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiVGhlIGxlZ2FjeSBwYWNrYWdlcyBtYXB0b29scywgcmdkYWwsIGFuZCByZ2VvcywgdW5kZXJwaW5uaW5nIHRoZSBzcCBwYWNrYWdlLFxud2hpY2ggd2FzIGp1c3QgbG9hZGVkLCB3aWxsIHJldGlyZSBpbiBPY3RvYmVyIDIwMjMuXG5QbGVhc2UgcmVmZXIgdG8gUi1zcGF0aWFsIGV2b2x1dGlvbiByZXBvcnRzIGZvciBkZXRhaWxzLCBlc3BlY2lhbGx5XG5odHRwczovL3Itc3BhdGlhbC5vcmcvci8yMDIzLzA1LzE1L2V2b2x1dGlvbjQuaHRtbC5cbkl0IG1heSBiZSBkZXNpcmFibGUgdG8gbWFrZSB0aGUgc2YgcGFja2FnZSBhdmFpbGFibGU7XG5wYWNrYWdlIG1haW50YWluZXJzIHNob3VsZCBjb25zaWRlciBhZGRpbmcgc2YgdG8gU3VnZ2VzdHM6LlxuVGhlIHNwIHBhY2thZ2UgaXMgbm93IHJ1bm5pbmcgdW5kZXIgZXZvbHV0aW9uIHN0YXR1cyAyXG4gICAgIChzdGF0dXMgMiB1c2VzIHRoZSBzZiBwYWNrYWdlIGluIHBsYWNlIG9mIHJnZGFsKVxuV2FybmluZzogbXVsdGlwbGUgbWV0aG9kcyB0YWJsZXMgZm91bmQgZm9yIOKAmGVsaWRl4oCZV2FybmluZzogcmVwbGFjaW5nIHByZXZpb3VzIGltcG9ydCDigJhtYXB0b29sczo6ZWxpZGXigJkgYnkg4oCYc3A6OmVsaWRl4oCZIHdoZW4gbG9hZGluZyDigJh0aWdyaXPigJlcbiJ9 -->

```
The legacy packages maptools, rgdal, and rgeos, underpinning the sp package,
which was just loaded, will retire in October 2023.
Please refer to R-spatial evolution reports for details, especially
https://r-spatial.org/r/2023/05/15/evolution4.html.
It may be desirable to make the sf package available;
package maintainers should consider adding sf to Suggests:.
The sp package is now running under evolution status 2
     (status 2 uses the sf package in place of rgdal)
Warning: multiple methods tables found for ‘elide’Warning: replacing previous import ‘maptools::elide’ by ‘sp::elide’ when loading ‘tigris’
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI2luc3RhbGwucGFja2FnZXMoXCJnb29nbGVzaGVldHM0XCIpXG5cbiNBdXRoZW50aWNhdGluZyB3aXRoIEdvb2dsZSBhY2NvdW50XG4jZ3M0X2F1dGgoKVxuXG4jIExvYWQgQ2Vuc3VzIEFQSSBrZXlcblN5cy5zZXRlbnYoQ0VOU1VTX0FQSV9LRVkgPSBcIjVjYjJiOWM2MjhhMWQxMzI5YzViZjRkMzZmZTQ0MzVjNjUwMWVmYzhcIiwgb3ZlcndyaXRlID0gVFJVRSlcblxuIyBMb2FkIEFDUyBjcm9zc3dhbGtcbmFjc18yMDIxIDwtIGxvYWRfdmFyaWFibGVzKDIwMjEsIFwiYWNzNVwiKVxuXG4jIExvYWQgMjAyMCBDZW5zdXMgY3Jvc3N3YWxrXG5jZW5zdXNfMjAyMCA8LSBsb2FkX3ZhcmlhYmxlcygyMDIwLCBcInBsXCIsIGNhY2hlID0gVFJVRSlcblxuIyBIZWxwZnVsIHJlZmVyZW5jZXMgZm9yIHVzaW5nIEFDUyBhbmQgQ2Vuc3VzIEFQSXM6ICNodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy90b3BpY3MvdGFibGUtY29kZXMvXG4jaHR0cHM6Ly93YWxrZXItZGF0YS5jb20vdGlkeWNlbnN1cy9hcnRpY2xlcy9iYXNpYy11c2FnZS5odG1sXG5cbmBgYCJ9 -->

```r
#install.packages("googlesheets4")

#Authenticating with Google account
#gs4_auth()

# Load Census API key
Sys.setenv(CENSUS_API_KEY = "5cb2b9c628a1d1329c5bf4d36fe4435c6501efc8", overwrite = TRUE)

# Load ACS crosswalk
acs_2021 <- load_variables(2021, "acs5")

# Load 2020 Census crosswalk
census_2020 <- load_variables(2020, "pl", cache = TRUE)

# Helpful references for using ACS and Census APIs: #https://censusreporter.org/topics/table-codes/
#https://walker-data.com/tidycensus/articles/basic-usage.html

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jTG9hZCBmb290YmFsbCByb3N0ZXIgc2NyYXBlci4gQWxzbyBkaWQgc29tZSBjbGVhbmluZyBmb3Igc3BlY2lhbCBjYXNlcyBoZXJlLiBGb3IgdGhlIHBsYXllcnMgd2hvIHdlcmUgbWlzc2luZyBob21ldG93biBpbmZvcm1hdGlvbiwgdGhpcyB3YXMgb2J0YWluZWQgYnkgbG9va2luZyBhdCByb3N0ZXJzIGZyb20gcHJldmlvdXMgeWVhcnMuXG5mb290YmFsbF9yb3N0ZXJzIDwtIHJlYWRfY3N2KFwiZm9vdGJhbGxfcm9zdGVyLmNzdlwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgbXV0YXRlKGhvbWV0b3duID0gY2FzZV93aGVuKFxuICAgIGhvbWV0b3duID09IFwiUG9tcGFubywgQmVhY2gsIEZsYS5cIiB+IFwiUG9tcGFubyBCZWFjaCwgRmxhLlwiLFxuICAgIGhvbWV0b3duID09IFwiTGl2ZW1vcmUgQ2FsaWYuXCIgfiBcIkxpdmVtb3JlLCBDYWxpZi5cIixcbiAgICBob21ldG93biA9PSBcIldhc2hpbmd0b24gRC5DLlwiIH4gXCJXYXNoaW5ndG9uLCBELkMuXCIsXG4gICAgaG9tZXRvd24gPT0gXCJUYW1wYS4gRmxhLlwiIH4gXCJUYW1wYSwgRmxhLlwiLFxuICAgIGhvbWV0b3duID09IFwiVXBwZXIgTWFybGJvcm8uIE1kLlwiIH4gXCJVcHBlciBNYXJsYm9ybywgTWQuXCIsXG4gICAgaG9tZXRvd24gPT0gXCJOb3Jmb2xrLFZhLlwiIH4gXCJOb3Jmb2xrLCBWYS5cIixcbiAgICBob21ldG93biA9PSBcIkJyb254IE4uWS5cIiB+IFwiQnJvbngsIE4uWS5cIixcbiAgICBob21ldG93biA9PSBcIkNvY29hIEZsYS5cIiB+IFwiQ29jb2EsIEZsYS5cIixcbiAgICBob21ldG93biA9PSBcIkplZmZlcnNvblwiIH4gXCJKZWZmZXJzb24gVG93bnNoaXAsIE5KXCIsXG4gICAgaG9tZXRvd24gPT0gXCJNZWxib3VybmVcIiB+IFwiTWVsYm91cm5lLCBGTFwiLFxuICAgIGhvbWV0b3duID09IFwiQ2hpY2Fnb1wiIH4gXCJDaGljYWdvLCBJTFwiLFxuICAgIGhvbWV0b3duID09IFwiQ2luY2lubmF0aVwiIH4gXCJDaW5jaW5uYXRpLCBPSFwiLFxuICAgIGhvbWV0b3duID09IFwiQ2xldmVsYW5kXCIgfiBcIkNsZXZlbGFuZCwgT0hcIixcbiAgICBob21ldG93biA9PSBcIlN0LiBMb3Vpc1wiIH4gXCJTdC4gTG91aXMsIE1PXCIsXG4gICAgaG9tZXRvd24gPT0gXCJJbmdsZXdvb2RcIiB+IFwiSW5nbGV3b29kLCBDQVwiLFxuICAgIGhvbWV0b3duID09IFwiQ2hhdHdvcnRoLCBHYS5cIiB+IFwiQ2hhdHN3b3J0aCwgR2EuXCIsXG4gICAgaG9tZXRvd24gPT0gXCJLaW5nbGFuZCwgR2EuXCIgfiBcIktpbmdzbGFuZCwgR2EuXCIsXG4gICAgaG9tZXRvd24gPT0gXCJFYXN0IENvYmIsIEdBXCIgfiBcIk1hcmlldHRhLCBHQVwiLFxuICAgIGhvbWV0b3duID09IFwiUGxhdHZpbGxlLCBBbGEuXCIgfiBcIlByYXR0dmlsbGUsIEFsYS5cIixcbiAgICBUUlVFIH4gaG9tZXRvd24pKSAlPiVcbiAgbXV0YXRlKGhvbWV0b3duID0gY2FzZV93aGVuKFxuICAgIG5hbWUgPT0gXCJGZXlpc2F5byBPbHVsZXllXCIgfiBcIkxhbmNhc3RlciwgUEFcIixcbiAgICBuYW1lID09IFwiS3lsZSBWYWNjYXJlbGxhXCIgfiBcIkZhaXJmaWVsZCwgQ1RcIixcbiAgICBUUlVFIH4gaG9tZXRvd24pKVxuYGBgIn0= -->

```r

#Load football roster scraper. Also did some cleaning for special cases here. For the players who were missing hometown information, this was obtained by looking at rosters from previous years.
football_rosters <- read_csv("football_roster.csv") %>%
  clean_names() %>%
  mutate(hometown = case_when(
    hometown == "Pompano, Beach, Fla." ~ "Pompano Beach, Fla.",
    hometown == "Livemore Calif." ~ "Livemore, Calif.",
    hometown == "Washington D.C." ~ "Washington, D.C.",
    hometown == "Tampa. Fla." ~ "Tampa, Fla.",
    hometown == "Upper Marlboro. Md." ~ "Upper Marlboro, Md.",
    hometown == "Norfolk,Va." ~ "Norfolk, Va.",
    hometown == "Bronx N.Y." ~ "Bronx, N.Y.",
    hometown == "Cocoa Fla." ~ "Cocoa, Fla.",
    hometown == "Jefferson" ~ "Jefferson Township, NJ",
    hometown == "Melbourne" ~ "Melbourne, FL",
    hometown == "Chicago" ~ "Chicago, IL",
    hometown == "Cincinnati" ~ "Cincinnati, OH",
    hometown == "Cleveland" ~ "Cleveland, OH",
    hometown == "St. Louis" ~ "St. Louis, MO",
    hometown == "Inglewood" ~ "Inglewood, CA",
    hometown == "Chatworth, Ga." ~ "Chatsworth, Ga.",
    hometown == "Kingland, Ga." ~ "Kingsland, Ga.",
    hometown == "East Cobb, GA" ~ "Marietta, GA",
    hometown == "Platville, Ala." ~ "Prattville, Ala.",
    TRUE ~ hometown)) %>%
  mutate(hometown = case_when(
    name == "Feyisayo Oluleye" ~ "Lancaster, PA",
    name == "Kyle Vaccarella" ~ "Fairfield, CT",
    TRUE ~ hometown))
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiV2FybmluZzogT25lIG9yIG1vcmUgcGFyc2luZyBpc3N1ZXMsIGNhbGwgYHByb2JsZW1zKClgIG9uIHlvdXIgZGF0YSBmcmFtZSBmb3IgZGV0YWlscywgZS5nLjpcbiAgZGF0IDwtIHZyb29tKC4uLilcbiAgcHJvYmxlbXMoZGF0KVJvd3M6IDgxOTUgQ29sdW1uczogNuKUgOKUgCBDb2x1bW4gc3BlY2lmaWNhdGlvbiDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIBcbkRlbGltaXRlcjogXCIsXCJcbmNociAoNik6IFNjaG9vbCwgTmFtZSwgUG9zaXRpb24sIENsYXNzLCBIb21ldG93biwgSGlnaCBTY2hvb2xcbuKEuSBVc2UgYHNwZWMoKWAgdG8gcmV0cmlldmUgdGhlIGZ1bGwgY29sdW1uIHNwZWNpZmljYXRpb24gZm9yIHRoaXMgZGF0YS5cbuKEuSBTcGVjaWZ5IHRoZSBjb2x1bW4gdHlwZXMgb3Igc2V0IGBzaG93X2NvbF90eXBlcyA9IEZBTFNFYCB0byBxdWlldCB0aGlzIG1lc3NhZ2UuXG4ifQ== -->

```
Warning: One or more parsing issues, call `problems()` on your data frame for details, e.g.:
  dat <- vroom(...)
  problems(dat)Rows: 8195 Columns: 6── Column specification ─────────────────────────────────────────────────────────────────────
Delimiter: ","
chr (6): School, Name, Position, Class, Hometown, High School
ℹ Use `spec()` to retrieve the full column specification for this data.
ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI0xldCdzIGFsc28gdXNlIHRoaXMgYXMgYSB0aW1lIHRvIGxvYWQgYSBzdGF0ZSBjcm9zc3dhbGsgd2UnbGwgdXNlIGxhdGVyXG5zdGF0ZV9jcm9zc3dhbGsgPC0gcmVhZF9jc3YoXCJzdGF0ZV9jcm9zc3dhbGsuY3N2XCIpICU+JVxuICBtdXRhdGUoc3RhdGVfbmFtZV9jYXBzID0gc3RyX3RvX3VwcGVyKHN0YXRlX25hbWUpKSAlPiVcbiAgc2VsZWN0KHN0YXRlX2FiYiwgc3RhdGVfbmFtZV9jYXBzKVxuYGBgIn0= -->

```r
#Let's also use this as a time to load a state crosswalk we'll use later
state_crosswalk <- read_csv("state_crosswalk.csv") %>%
  mutate(state_name_caps = str_to_upper(state_name)) %>%
  select(state_abb, state_name_caps)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiUm93czogNTEgQ29sdW1uczogMuKUgOKUgCBDb2x1bW4gc3BlY2lmaWNhdGlvbiDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIBcbkRlbGltaXRlcjogXCIsXCJcbmNociAoMik6IHN0YXRlX2FiYiwgc3RhdGVfbmFtZVxu4oS5IFVzZSBgc3BlYygpYCB0byByZXRyaWV2ZSB0aGUgZnVsbCBjb2x1bW4gc3BlY2lmaWNhdGlvbiBmb3IgdGhpcyBkYXRhLlxu4oS5IFNwZWNpZnkgdGhlIGNvbHVtbiB0eXBlcyBvciBzZXQgYHNob3dfY29sX3R5cGVzID0gRkFMU0VgIHRvIHF1aWV0IHRoaXMgbWVzc2FnZS5cbiJ9 -->

```
Rows: 51 Columns: 2── Column specification ─────────────────────────────────────────────────────────────────────
Delimiter: ","
chr (2): state_abb, state_name
ℹ Use `spec()` to retrieve the full column specification for this data.
ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI0xldCdzIGxvYWQgc29tZSBob21ldG93bnMgdGhhdCB3ZSBwYXNzZWQgdGhyb3VnaCBhbmQgY2xlYW5lZCB3aXRoIE9wZW4gUmVmaW5lXG5ob21ldG93bnNfb3Blbl9yZWZpbmUgPC0gcmVhZF9jc3YoXCJob21ldG93bnNfb3Blbl9yZWZpbmUuY3N2XCIpXG5gYGAifQ== -->

```r
#Let's load some hometowns that we passed through and cleaned with Open Refine
hometowns_open_refine <- read_csv("hometowns_open_refine.csv")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiUm93czogMjY4NiBDb2x1bW5zOiA04pSA4pSAIENvbHVtbiBzcGVjaWZpY2F0aW9uIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgFxuRGVsaW1pdGVyOiBcIixcIlxuY2hyICgzKTogaG9tZXRvd25fY2l0eSwgaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW5cbmRibCAoMSk6IHRvdGFsXG7ihLkgVXNlIGBzcGVjKClgIHRvIHJldHJpZXZlIHRoZSBmdWxsIGNvbHVtbiBzcGVjaWZpY2F0aW9uIGZvciB0aGlzIGRhdGEuXG7ihLkgU3BlY2lmeSB0aGUgY29sdW1uIHR5cGVzIG9yIHNldCBgc2hvd19jb2xfdHlwZXMgPSBGQUxTRWAgdG8gcXVpZXQgdGhpcyBtZXNzYWdlLlxuIn0= -->

```
Rows: 2686 Columns: 4── Column specification ─────────────────────────────────────────────────────────────────────
Delimiter: ","
chr (3): hometown_city, hometown_city_clean, hometown_state_clean
dbl (1): total
ℹ Use `spec()` to retrieve the full column specification for this data.
ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI0NoZWNraW5nIHRvIHNlZSB0aGF0IHdlIGhhdmUgNjggc2Nob29scyBhbmQgdGhlIHBsYXllciBjb3VudHMgZm9yIGVhY2ggc2Nob29sXG4jIHNjaG9vbF9jaGVjayA8LSBmb290YmFsbF9yb3N0ZXJzICU+JVxuIyAgIGdyb3VwX2J5KHNjaG9vbCkgJT4lXG4jICAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpICU+JVxuIyAgIGFycmFuZ2UodG90YWxfcGxheWVycylcblxuI0NoZWNraW5nIHRvIG1ha2Ugc3VyZSB0aGVyZSBhcmUgbm8gZHVwbGljYXRlIHBsYXllcnNcbiMgcGxheWVyX2NoZWNrIDwtIGZvb3RiYWxsX3Jvc3RlcnMgJT4lXG4jICAgZ3JvdXBfYnkobmFtZSwgc2Nob29sKSAlPiVcbiMgICBzdW1tYXJpc2UodG90YWwgPSBuKCkpICU+JVxuIyAgIGFycmFuZ2UoZGVzYyh0b3RhbCkpXG5cbmBgYCJ9 -->

```r
#Checking to see that we have 68 schools and the player counts for each school
# school_check <- football_rosters %>%
#   group_by(school) %>%
#   summarise(total_players = n()) %>%
#   arrange(total_players)

#Checking to make sure there are no duplicate players
# player_check <- football_rosters %>%
#   group_by(name, school) %>%
#   summarise(total = n()) %>%
#   arrange(desc(total))

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jQ0xFQU5JTkcvU1RBTkRBUkRJWklORyBTVEFURVxuXG4jU3BsaXR0aW5nIHRoZSBob21ldG93biBjb2x1bW4gc28gd2UgY2FuIHdvcmsgd2l0aCB0aGUgc3RhdGVcbmZvb3RiYWxsX3Jvc3RlcnMgPC0gZm9vdGJhbGxfcm9zdGVycyAlPiVcbiAgbXV0YXRlKGhvbWV0b3duX2NsZWFuaW5nID0gaG9tZXRvd24pICU+JVxuICBzZXBhcmF0ZShob21ldG93bl9jbGVhbmluZywgaW50byA9IGMoXCJob21ldG93bl9jaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVcIiwgXCJob21ldG93bl9jb3VudHJ5XCIpLCBzZXAgPSBcIiwgXCIpXG5gYGAifQ== -->

```r

#CLEANING/STANDARDIZING STATE

#Splitting the hometown column so we can work with the state
football_rosters <- football_rosters %>%
  mutate(hometown_cleaning = hometown) %>%
  separate(hometown_cleaning, into = c("hometown_city", "hometown_state", "hometown_country"), sep = ", ")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiV2FybmluZzogRXhwZWN0ZWQgMyBwaWVjZXMuIE1pc3NpbmcgcGllY2VzIGZpbGxlZCB3aXRoIGBOQWAgaW4gODE2OCByb3dzIFsxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5LCAxMCwgMTEsIDEyLCAxMywgMTQsIDE1LCAxNiwgMTcsIDE4LCAxOSwgMjAsIC4uLl0uXG4ifQ== -->

```
Warning: Expected 3 pieces. Missing pieces filled with `NA` in 8168 rows [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...].
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI1doYXQga2luZCBvZiB2YWx1ZXMgYXJlIHdlIGdldHRpbmcgaW4gaG9tZXRvd25fc3RhdGU/XG5zdGF0ZV9jaGVjayA8LSBmb290YmFsbF9yb3N0ZXJzICU+JVxuICBncm91cF9ieShob21ldG93bl9zdGF0ZSkgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbCA9IG4oKSkgJT4lXG4gIGFycmFuZ2UoaG9tZXRvd25fc3RhdGUpXG5cbiNNYW55IG9mIHRob3NlIGFyZW4ndCBVLlMuIHN0YXRlcy4gTGV0J3MgbWFrZSBhIG5ldyBkYXRhZnJhbWUgdGhhdCBvbmx5IGhhcyBwbGF5ZXJzIGZyb20gdGhlIDUwIHN0YXRlczpcbmV4Y2x1ZGVkX3N0YXRlcyA8LSBjKFwiIFdlc3Rlcm4gQXVzdHJhbGlhXCIsIFwiQWxiZXJ0YVwiLCBcIkFtZXJpY2FuIFNhbW9hXCIsIFwiQXVzdHJhbGlhXCIsIFwiQmFoYW1hc1wiLCBcIkJlbGdpdW1cIiwgXCJDYW5hZGFcIiwgXCJDaGluYVwiLCBcIkNvbG9tYmlhXCIsIFwiQ29uZ29cIiwgXCJDb3VudHkgS2VycnlcIiwgXCJEZW5tYXJrXCIsIFwiRFIgb2YgdGhlIENvbmdvXCIsIFwiRW5nbGFuZFwiLCBcIkZpbmxhbmRcIiwgXCJGcmFuY2VcIiwgXCJHYWJvblwiLCBcIkdlcm1hbnlcIiwgXCJHaGFuYVwiLCBcIklyZWxhbmRcIiwgXCJKYXBhblwiLCBcIk1hbml0b2JhXCIsIFwiTWV4aWNvXCIsIFwiTi5TLlwiLCBcIk5ldyBTb3V0aCBXYWxlc1wiLCBcIk5ldyBaZWFsYW5kXCIsIFwiTmlnZXJpYVwiLCBcIk5TV1wiLCBcIk9udC5cIiwgXCJPbnRhcmlvXCIsIFwiUUNcIiwgXCJRdWUuXCIsIFwiUXVlYmVjXCIsIFwiUXXDqWJlY1wiLCBcIlF1ZWVuc2xhbmRcIiwgXCJTYXNrYXRjaGV3YW5cIiwgXCJTZXJiaWFcIiwgXCJTb3V0aCBBZnJpY2FcIiwgXCJTb3V0aCBBdXN0cmFsaWFcIiwgXCJTd2VkZW5cIiwgXCJTd2l0emVybGFuZFwiLCBcIlRoZSBOZXRoZXJsYW5kc1wiLCBcIlRvbmdhXCIsIFwiVW5pdGVkIEtpbmdkb21cIiwgXCJWaWN0b3JpYVwiLCBcIlZpY3RvcmlhIEFVXCIsIFwiV2VzdGVybiBTYW1vYVwiKVxuXG5mb290YmFsbF9yb3N0ZXJzX3VzYSA8LSBmb290YmFsbF9yb3N0ZXJzICU+JVxuICBmaWx0ZXIoIShob21ldG93bl9zdGF0ZSAlaW4lIGV4Y2x1ZGVkX3N0YXRlcykgfCBpcy5uYShob21ldG93bl9zdGF0ZSkpICU+JVxuICBtdXRhdGUoaG9tZXRvd25fc3RhdGUgPSBjYXNlX3doZW4oXG4gICAgaG9tZXRvd25fc3RhdGUgPT0gXCJNYXVpXCIgfiBcIkhJXCIsXG4gICAgaG9tZXRvd25fc3RhdGUgPT0gXCJOZXcgWW9yayBDaXR5XCIgfiBcIk5ZXCIsXG4gICAgVFJVRSB+IGhvbWV0b3duX3N0YXRlKSlcblxuI0FuZCBub3cgbGV0J3MgcmVjaGVjayB0aG9zZSBob21ldG93bl9zdGF0ZSB2YWx1ZXM6XG5zdGF0ZV9jaGVja191c2EgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX3N0YXRlKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsID0gbigpKSAlPiVcbiAgYXJyYW5nZShob21ldG93bl9zdGF0ZSlcblxuI0xldCdzIHN0YW5kYXJkaXplIHRoZXNlIHRvIHRoZSBzdGF0ZSBwb3N0YWwgYWJicmV2aWF0aW9uOlxuI0ZpcnN0LCBsZXQncyB0cnkgcmVtb3ZpbmcgcHVuY3R1YXRpb24gYW5kIG1ha2luZyBldmVyeXRoaW5nIHVwcGVyIGNhc2U6XG5mb290YmFsbF9yb3N0ZXJzX3VzYSA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgbXV0YXRlKGhvbWV0b3duX3N0YXRlX2ZpcnN0X3RyeSA9IHN0cl90b191cHBlcihnc3ViKFwiW1s6cHVuY3Q6XV1cIiwgXCJcIiwgaG9tZXRvd25fc3RhdGUpKSlcblxuI1NlY29uZCwgbGV0J3Mgc2VlIGlmIHdlIGNhbiB1c2Ugb3VyIGNyb3Nzd2FsazpcbmZvb3RiYWxsX3Jvc3RlcnNfdXNhIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBsZWZ0X2pvaW4oc3RhdGVfY3Jvc3N3YWxrLCBieT1jKFwiaG9tZXRvd25fc3RhdGVfZmlyc3RfdHJ5XCIgPSBcInN0YXRlX25hbWVfY2Fwc1wiKSlcblxuZm9vdGJhbGxfcm9zdGVyc191c2EgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIHJlbmFtZShob21ldG93bl9zdGF0ZV9zZWNvbmRfdHJ5ID0gc3RhdGVfYWJiKVxuXG4jVGhpcmQsIGxldCdzIGNvbWJpbmUgdGhlIHJlc3VsdHMgb2Ygb3VyIGZpcnN0IHR3byB0cmllcyBhbmQgY2hlY2sgdG8gc2VlIGhvdyBtdWNoIHRoYXQgcmVkdWNlZCBvdXIgdW5pcXVlIHZhbHVlc1xuZm9vdGJhbGxfcm9zdGVyc191c2EgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIG11dGF0ZShob21ldG93bl9zdGF0ZV90aGlyZF90cnkgPSBpZmVsc2UoaXMubmEoaG9tZXRvd25fc3RhdGVfc2Vjb25kX3RyeSksIGhvbWV0b3duX3N0YXRlX2ZpcnN0X3RyeSwgaG9tZXRvd25fc3RhdGVfc2Vjb25kX3RyeSkpXG5cbnN0YXRlX2NoZWNrX3VzYV91cGRhdGUgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSkgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbCA9IG4oKSkgJT4lXG4gIGFycmFuZ2UoaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5KVxuXG4jTm93IHdlJ3JlIGRvd24gdG8gbXVjaCBmZXdlciBzdGF0ZSB2YWx1ZXMuIExldCdzIG1hbnVhbGx5IHRha2UgY2FyZSBvZiB0aGUgcmVzdC5cbmZvb3RiYWxsX3Jvc3RlcnNfdXNhIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBtdXRhdGUoaG9tZXRvd25fc3RhdGVfY2xlYW4gPSBjYXNlX3doZW4oXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiQUxBXCIgfiBcIkFMXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiQVJJWlwiIH4gXCJBWlwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIkFSS1wiIH4gXCJBUlwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIkNBTEZcIiB8IGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIkNBTElGXCIgfiBcIkNBXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiQ09MXCIgfCBob21ldG93bl9zdGF0ZV90aGlyZF90cnkgPT0gXCJDT0xPXCIgfiBcIkNPXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiQ09OTlwiIH4gXCJDVFwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIkRFTFwiIH4gXCJERVwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIkZMQVwiIH4gXCJGTFwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIklMTFwiIH4gXCJJTFwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIklORFwiIH4gXCJJTlwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIktBTlwiIH4gXCJLU1wiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIk1BU1NcIiB+IFwiTUFcIixcbiAgICBob21ldG93bl9zdGF0ZV90aGlyZF90cnkgPT0gXCJNSUNIXCIgfiBcIk1JXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiTUlOTlwiIH4gXCJNTlwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIk1JU1NcIiB+IFwiTVNcIixcbiAgICBob21ldG93bl9zdGF0ZV90aGlyZF90cnkgPT0gXCJNT05UXCIgfiBcIk1UXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiTkVCXCIgfiBcIk5FXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiTkVWXCIgfiBcIk5WXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiT0tMQVwiIH4gXCJPS1wiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIk9SRVwiIH4gXCJPUlwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIlBFTk5cIiB+IFwiUEFcIixcbiAgICBob21ldG93bl9zdGF0ZV90aGlyZF90cnkgPT0gXCJURU5OXCIgfiBcIlROXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiVyBWQVwiIHwgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiV1ZBXCIgfiBcIldWXCIsXG4gICAgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiV0FTSFwiIH4gXCJXQVwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIldJU1wiIHwgaG9tZXRvd25fc3RhdGVfdGhpcmRfdHJ5ID09IFwiV0lTQ1wiIH4gXCJXSVwiLFxuICAgIGhvbWV0b3duX3N0YXRlX3RoaXJkX3RyeSA9PSBcIldZT1wiIH4gXCJXWVwiLFxuICAgIFRSVUUgfiBob21ldG93bl9zdGF0ZV90aGlyZF90cnkpKVxuXG4jV2hhdCdzIHRoZSBmaW5hbCBzdGF0ZSBicmVha2Rvd24/XG5mb290YmFsbF9yb3N0ZXJzX3VzYV9zdGF0ZXMgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnM9bigpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHRvdGFsX3BsYXllcnMpKVxuXG5gYGAifQ== -->

```r
#What kind of values are we getting in hometown_state?
state_check <- football_rosters %>%
  group_by(hometown_state) %>%
  summarise(total = n()) %>%
  arrange(hometown_state)

#Many of those aren't U.S. states. Let's make a new dataframe that only has players from the 50 states:
excluded_states <- c(" Western Australia", "Alberta", "American Samoa", "Australia", "Bahamas", "Belgium", "Canada", "China", "Colombia", "Congo", "County Kerry", "Denmark", "DR of the Congo", "England", "Finland", "France", "Gabon", "Germany", "Ghana", "Ireland", "Japan", "Manitoba", "Mexico", "N.S.", "New South Wales", "New Zealand", "Nigeria", "NSW", "Ont.", "Ontario", "QC", "Que.", "Quebec", "Québec", "Queensland", "Saskatchewan", "Serbia", "South Africa", "South Australia", "Sweden", "Switzerland", "The Netherlands", "Tonga", "United Kingdom", "Victoria", "Victoria AU", "Western Samoa")

football_rosters_usa <- football_rosters %>%
  filter(!(hometown_state %in% excluded_states) | is.na(hometown_state)) %>%
  mutate(hometown_state = case_when(
    hometown_state == "Maui" ~ "HI",
    hometown_state == "New York City" ~ "NY",
    TRUE ~ hometown_state))

#And now let's recheck those hometown_state values:
state_check_usa <- football_rosters_usa %>%
  group_by(hometown_state) %>%
  summarise(total = n()) %>%
  arrange(hometown_state)

#Let's standardize these to the state postal abbreviation:
#First, let's try removing punctuation and making everything upper case:
football_rosters_usa <- football_rosters_usa %>%
  mutate(hometown_state_first_try = str_to_upper(gsub("[[:punct:]]", "", hometown_state)))

#Second, let's see if we can use our crosswalk:
football_rosters_usa <- football_rosters_usa %>%
  left_join(state_crosswalk, by=c("hometown_state_first_try" = "state_name_caps"))

football_rosters_usa <- football_rosters_usa %>%
  rename(hometown_state_second_try = state_abb)

#Third, let's combine the results of our first two tries and check to see how much that reduced our unique values
football_rosters_usa <- football_rosters_usa %>%
  mutate(hometown_state_third_try = ifelse(is.na(hometown_state_second_try), hometown_state_first_try, hometown_state_second_try))

state_check_usa_update <- football_rosters_usa %>%
  group_by(hometown_state_third_try) %>%
  summarise(total = n()) %>%
  arrange(hometown_state_third_try)

#Now we're down to much fewer state values. Let's manually take care of the rest.
football_rosters_usa <- football_rosters_usa %>%
  mutate(hometown_state_clean = case_when(
    hometown_state_third_try == "ALA" ~ "AL",
    hometown_state_third_try == "ARIZ" ~ "AZ",
    hometown_state_third_try == "ARK" ~ "AR",
    hometown_state_third_try == "CALF" | hometown_state_third_try == "CALIF" ~ "CA",
    hometown_state_third_try == "COL" | hometown_state_third_try == "COLO" ~ "CO",
    hometown_state_third_try == "CONN" ~ "CT",
    hometown_state_third_try == "DEL" ~ "DE",
    hometown_state_third_try == "FLA" ~ "FL",
    hometown_state_third_try == "ILL" ~ "IL",
    hometown_state_third_try == "IND" ~ "IN",
    hometown_state_third_try == "KAN" ~ "KS",
    hometown_state_third_try == "MASS" ~ "MA",
    hometown_state_third_try == "MICH" ~ "MI",
    hometown_state_third_try == "MINN" ~ "MN",
    hometown_state_third_try == "MISS" ~ "MS",
    hometown_state_third_try == "MONT" ~ "MT",
    hometown_state_third_try == "NEB" ~ "NE",
    hometown_state_third_try == "NEV" ~ "NV",
    hometown_state_third_try == "OKLA" ~ "OK",
    hometown_state_third_try == "ORE" ~ "OR",
    hometown_state_third_try == "PENN" ~ "PA",
    hometown_state_third_try == "TENN" ~ "TN",
    hometown_state_third_try == "W VA" | hometown_state_third_try == "WVA" ~ "WV",
    hometown_state_third_try == "WASH" ~ "WA",
    hometown_state_third_try == "WIS" | hometown_state_third_try == "WISC" ~ "WI",
    hometown_state_third_try == "WYO" ~ "WY",
    TRUE ~ hometown_state_third_try))

#What's the final state breakdown?
football_rosters_usa_states <- football_rosters_usa %>%
  group_by(hometown_state_clean) %>%
  summarise(total_players=n()) %>%
  arrange(desc(total_players))

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jU1RBVEVTIFdJVEggUE9QVUxBVElPTiBEQVRBXG5cbiNMZXQncyB0cnkgdG8gYWRkIGluIHNvbWUgcG9wdWxhdGlvbiBkYXRhIGFuZCB0cnkgdG8gZmlndXJlIG91dCB0aGUgbnVtYmVyIG9mIFBvd2VyIDUgZm9vdGJhbGwgcGxheWVycyBwZXIgMTAwLDAwMCByZXNpZGVudHMgaW4gYSBzdGF0ZVxuI0ZpcnN0LCBsZXQncyBnZXQgb3Vyc2VsdmVzIGEgZGF0YWZyYW1lIHRoYXQgaGFzIHN0YXRlIHBvc3RhbCBhYmJyZXZpYXRpb25zIGFuZCB0aGVpciBtb3N0IHJlY2VudCBBQ1Mgc3RhdGUgcG9wdWxhdGlvbjpcbnN0YXRlX3BvcHNfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwic3RhdGVcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IFwiQjAxMDAzXzAwMVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEpXG5gYGAifQ== -->

```r

#STATES WITH POPULATION DATA

#Let's try to add in some population data and try to figure out the number of Power 5 football players per 100,000 residents in a state
#First, let's get ourselves a dataframe that has state postal abbreviations and their most recent ACS state population:
state_pops_2021 <- get_acs(geography = "state",
                           variables = "B01003_001",
                           year = 2021)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuc3RhdGVfcG9wc18yMDIxIDwtIHN0YXRlX3BvcHNfMjAyMSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgbXV0YXRlKG5hbWVfY2FwcyA9IHN0cl90b191cHBlcihuYW1lKSkgJT4lXG4gIG11dGF0ZShuYW1lX2NhcHMgPSBjYXNlX3doZW4oXG4gICAgbmFtZV9jYXBzID09IFwiRElTVFJJQ1QgT0YgQ09MVU1CSUFcIiB+IFwiV0FTSElOR1RPTiwgRENcIixcbiAgICBUUlVFIH4gbmFtZV9jYXBzXG4gICkpICU+JVxuICBsZWZ0X2pvaW4oc3RhdGVfY3Jvc3N3YWxrLCBieT1jKFwibmFtZV9jYXBzXCIgPSBcInN0YXRlX25hbWVfY2Fwc1wiKSlcblxuc3RhdGVfcG9wc18yMDIxIDwtIHN0YXRlX3BvcHNfMjAyMSAlPiVcbiAgc2VsZWN0KHN0YXRlX2FiYiwgZXN0aW1hdGUpICU+JVxuICAgIGZpbHRlcighaXMubmEoc3RhdGVfYWJiKSkgI1JlbW92ZWQgTkEgdmFsdWUsIHdoaWNoIHdhcyBQdWVydG8gUmljb1xuXG4jIE5vdywgbGV0J3Mgam9pbiBvdXIgcG9wdWxhdGlvbiBkYXRhIHRvIG91ciBzdGF0ZSBjb3VudCBvZiBmb290YmFsbCBwbGF5ZXJzIGRhdGE6XG5mb290YmFsbF9yb3N0ZXJzX3VzYV9zdGF0ZXMgPC0gZm9vdGJhbGxfcm9zdGVyc191c2Ffc3RhdGVzICU+JVxuICBpbm5lcl9qb2luKHN0YXRlX3BvcHNfMjAyMSwgYnk9YyhcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlX2FiYlwiKSlcblxuZm9vdGJhbGxfcm9zdGVyc191c2Ffc3RhdGVzIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhX3N0YXRlcyAlPiVcbiAgcmVuYW1lKHRvdGFsX3BvcCA9IGVzdGltYXRlKVxuXG5mb290YmFsbF9yb3N0ZXJzX3VzYV9zdGF0ZXMgPC0gZm9vdGJhbGxfcm9zdGVyc191c2Ffc3RhdGVzICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfaHVuZHJlZF90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX2h1bmRyZWRfdGhvdXNhbmQpKVxuXG4jIENTVlxuI3dyaXRlX2Nzdihmb290YmFsbF9yb3N0ZXJzX3VzYV9zdGF0ZXMsIGZpbGUgPSBcInN0YXRlX2NvdW50cy5jc3ZcIilcblxuYGBgIn0= -->

```r
state_pops_2021 <- state_pops_2021 %>%
  clean_names() %>%
  mutate(name_caps = str_to_upper(name)) %>%
  mutate(name_caps = case_when(
    name_caps == "DISTRICT OF COLUMBIA" ~ "WASHINGTON, DC",
    TRUE ~ name_caps
  )) %>%
  left_join(state_crosswalk, by=c("name_caps" = "state_name_caps"))

state_pops_2021 <- state_pops_2021 %>%
  select(state_abb, estimate) %>%
    filter(!is.na(state_abb)) #Removed NA value, which was Puerto Rico

# Now, let's join our population data to our state count of football players data:
football_rosters_usa_states <- football_rosters_usa_states %>%
  inner_join(state_pops_2021, by=c("hometown_state_clean" = "state_abb"))

football_rosters_usa_states <- football_rosters_usa_states %>%
  rename(total_pop = estimate)

football_rosters_usa_states <- football_rosters_usa_states %>%
  mutate(players_per_hundred_thousand = round((total_players*100000)/total_pop,1)) %>%
  arrange(desc(players_per_hundred_thousand))

# CSV
#write_csv(football_rosters_usa_states, file = "state_counts.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFNUQVJUIFRPIENMRUFOL1NUQU5EQVJESVpFIEhPTUVUT1dOU1xuXG4jIENTViAtIGdvaW5nIHRvIHRyeSBjbGVhbmluZyB0aGlzIHRocm91Z2ggT3BlbiBSZWZpbmVcbiN3cml0ZV9jc3YoZGlzdGluY3RfaG9tZXRvd25zLCBmaWxlID0gXCJob21ldG93bnNfdG9fY2xlYW4uY3N2XCIpXG5cbiNKb2luIG91ciBPcGVuIFJlZmluZSBkYXRhZnJhbWUgdG8gb3VyIGRhdGFmcmFtZSBvZiBQb3dlciBGaXZlIHBsYXllcnNcbmhvbWV0b3duc19vcGVuX3JlZmluZV9tb2RpZmllZCA8LSBob21ldG93bnNfb3Blbl9yZWZpbmUgJT4lXG4gIHNlbGVjdChob21ldG93bl9jaXR5LCBob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbilcblxuZm9vdGJhbGxfcm9zdGVyc191c2EgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGxlZnRfam9pbihob21ldG93bnNfb3Blbl9yZWZpbmVfbW9kaWZpZWQsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiKSkgJT4lXG4gIG11dGF0ZShob21ldG93bl9jaXR5X2NsZWFuID0gY2FzZV93aGVuKFxuICAgIG5hbWUgPT0gJ0RKIFVpYWdhbGVsZWknIH4gXCJSaXZlcnNpZGVcIixcbiAgICBuYW1lID09ICdBSiBEdWZmeScgfiBcIk1vcmVubyBWYWxsZXlcIixcbiAgICBuYW1lID09ICdJemF5YWggIFJlZXZlcycgfiBcIkhlbXBzdGVhZFwiLFxuICAgIG5hbWUgPT0gJ0phd2hhciBKb3JkYW4nIH4gXCJGYXJtaW5nZGFsZVwiLFxuICAgIG5hbWUgPT0gJ0FudGhvbnkgR2FuZ2knIH4gXCJPeXN0ZXIgQmF5XCIsXG4gICAgVFJVRSB+IGhvbWV0b3duX2NpdHlfY2xlYW4pKSAjVGhlc2UgbGluZXMgb2YgY29kZSBhcmUgZm9yIHR3byBwbGF5ZXJzIGZyb20gSW5sYW5kIEVtcGlyZSwgQ2FsaWZvcm5pYSwgYSBsYXJnZSByZWdpb24gb2YgQ2FsaWZvcm5pYSB0aGF0IGluY2x1ZGVzIGRvemVucyBvZiBpbmNvcnBvcmF0ZWQgY2l0aWVzLCBhbmQgdGhyZWUgcGxheWVycyBmcm9tIExvbmcgSXNsYW5kLCBOZXcgWW9yay5cblxuZGlzdGluY3RfaG9tZXRvd25zIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbCA9IG4oKSlcbmBgYCJ9 -->

```r

# START TO CLEAN/STANDARDIZE HOMETOWNS

# CSV - going to try cleaning this through Open Refine
#write_csv(distinct_hometowns, file = "hometowns_to_clean.csv")

#Join our Open Refine dataframe to our dataframe of Power Five players
hometowns_open_refine_modified <- hometowns_open_refine %>%
  select(hometown_city, hometown_city_clean, hometown_state_clean)

football_rosters_usa <- football_rosters_usa %>%
  left_join(hometowns_open_refine_modified, by = c("hometown_city", "hometown_state_clean")) %>%
  mutate(hometown_city_clean = case_when(
    name == 'DJ Uiagalelei' ~ "Riverside",
    name == 'AJ Duffy' ~ "Moreno Valley",
    name == 'Izayah  Reeves' ~ "Hempstead",
    name == 'Jawhar Jordan' ~ "Farmingdale",
    name == 'Anthony Gangi' ~ "Oyster Bay",
    TRUE ~ hometown_city_clean)) #These lines of code are for two players from Inland Empire, California, a large region of California that includes dozens of incorporated cities, and three players from Long Island, New York.

distinct_hometowns <- football_rosters_usa %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI0Zyb20gaGVyZSwgdGhlIGJlc3Qgd2F5IHRvIGNvbnRpbnVlIHdvcmtpbmcgb24gdGhpcyB3aWxsIGxpa2VseSBiZSBzdGF0ZS1ieS1zdGF0ZVxuXG5gYGAifQ== -->

```r
#From here, the best way to continue working on this will likely be state-by-state

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIEFMQUJBTUEgSE9NRVRPV05TXG5cbiMgU3RlcCAxOiBGaWx0ZXIgZm9yIHRoZSBzdGF0ZSdzIHBsYXllcnNcbmZvb3RiYWxsX3Jvc3RlcnNfYWwgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiA9PSBcIkFMXCIpXG5cbiMgU3RlcCAyOiBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc19hbCA8LSBmb290YmFsbF9yb3N0ZXJzX2FsICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbF9wbGF5ZXJzID0gbigpKVxuYGBgIn0= -->

```r

# ALABAMA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_al <- football_rosters_usa %>%
  filter(hometown_state_clean == "AL")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_al <- football_rosters_al %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfYWxfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJBTFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_al_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "AL",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzAxJyBmb3Igc3RhdGUgJ0FMJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '01' for state 'AL'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfYWxfMjAyMSA8LSBjZW5zdXNfZGF0YV9hbF8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9hbF8yMDIxIDwtIGNlbnN1c19kYXRhX2FsXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnQWxhYmFtYScgfiBcIkFMXCIpKVxuXG4jIFN0ZXAgNjogSm9pbiB0aGUgY2Vuc3VzIGRhdGEgdG8gdGhlIGxpc3Qgb2YgaG9tZXRvd25zLiBBbHNvIGNyZWF0ZSBhIGNvbHVtbiB0aGF0IHRlbGxzIHVzIGhvdyBtYW55IHBlb3BsZSBhcmUgZWxpdGUgY29sbGVnZSBmb290YmFsbCBwbGF5ZXJzIGZvciBldmVyeSAxLDAwMCByZXNpZGVudHMuXG5ob21ldG93bnNfYWxfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX2FsICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfYWxfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIFN0ZXAgNzogTm90aWNlIHRoZXJlIGFyZSBhIGZldyBOQSB2YWx1ZXMuIFRoaXMgaGFwcGVucyB3aGVuIHRoZSBjZW5zdXMgZGF0YSBkb2VzIG5vdCBqb2luIHdpdGggdGhlIGhvbWV0b3ducyBkYXRhLCBwZXJoYXBzIGJlY2F1c2UgdGhlIGhvbWV0b3duIGlzIG1pc3NwZWxsZWQgb3IgYmVjYXVzZSB0aGVyZSBpcyBubyBjZW5zdXMgZGF0YSBmb3IgdGhhdCB0b3duLiBGaXJzdCwgbGV0J3MgZmluZCB0aGUgTkEgdmFsdWVzLlxuaG9tZXRvd25zX2FsX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKVxuYGBgIn0= -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_al_2021 <- census_data_al_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_al_2021 <- census_data_al_2021 %>%
  mutate(state = case_when(
    state == 'Alabama' ~ "AL"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_al_complete <- distinct_hometowns_al %>%
  left_join(census_data_al_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_al_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjIsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMiDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsyXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE3VlN3VTdETUF4TnU1V3BrelltYlIvQUQ3UVhKTVFWQ2FFZE9DRVF1MFZaR3Rwb1dWSTFtY1pPOEMxOElWK3c0WFF4YkwxVEtZMzk3TVIrTDM2Nlgxd1BGME5DU0kvMDQ0ajBFakJKOHZMOGtOMFNRTUNKU0ora2ZuK0hwQ2tZM3BuQWlrTmdOSmRscFpndXJ1Wm1MUUo0OGNxY05icVRHdDg5bmxod3RJMzVHc2MxQ1g1NmdPOWtIM3Y4NDl2M052akMvZi94TS80SlY4emEwQ1NDdzRJNWxyODFESWlmcDZlTjJlWWFjSXM4UCtFSGRQYmRlekZwMG1wN0JLY1ZTT25NVmxNdTNZNXlKWmdPb2RsdnlEcm14RmxzNUl4aml0YUs3VVJqc1VBcGpDeXdyWkJoYWdTV2l2SFZDVEJhaTBJeVRhWG1mOCtaMXR6Uk5oTzdDRFZvTFJycUtyT3hNQUNBZDlrTlRPMmswY0F2OXJPVGRQU0xtZzV3dWRGZWp5TGoxVWF2c2h1dmNSZ09Fb1NNd3BDZ25SNUw5Zy9ocWdSSFVPaFNhbVNRS0xZVUtqaGplSnhXOXJ4dXBIYjRtSURhdkJVSUVXNFVJaTAzc3Y4QlNXTFhHeklEQUFBPSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Highland Home","2":"AL","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Watson","2":"AL","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[2]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgSGlnaGxhbmQgSG9tZSwgQUwsIHRoZSB6aXAgY29kZSAoMzYwNDEpIHNlZW1zIHRvIGJlIGEgZ29vZCBzdWJzdGl0dXRlOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTMzYwNDEtMzYwNDEvXG5jZW5zdXNfZGF0YV9oaWdobGFuZF9hbF8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgMzYwNDFcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJBTFwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDM2MDQxXCIgfiBcIkhpZ2hsYW5kIEhvbWVcIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Highland Home, AL, the zip code (36041) seems to be a good substitute: https://censusreporter.org/profiles/86000US36041-36041/
census_data_highland_al_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 36041") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "AL") %>%
  mutate(city = case_when(
    city == "ZCTA5 36041" ~ "Highland Home")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgV2F0c29uLCBBTCwgZGF0YSBvYnRhaW5lZCB1c2luZyBwb3B1bGF0aW9uIG9mIG5lYXJieSBCcm9va3NpZGUsIEFMLCB3aGljaCBzZWVtcyB0byBpbmNsdWRlIFdhdHNvbiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy8xNjAwMFVTMDEwOTczNi1icm9va3NpZGUtYWwvXG5jZW5zdXNfZGF0YV93YXRzb25fYWxfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJBTFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIkJyb29rc2lkZSB0b3duLCBBbGFiYW1hXCIpICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiQUxcIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJCcm9va3NpZGUgdG93biwgQWxhYmFtYVwiIH4gXCJXYXRzb25cIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r
# For Watson, AL, data obtained using population of nearby Brookside, AL, which seems to include Watson https://censusreporter.org/profiles/16000US0109736-brookside-al/
census_data_watson_al_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "AL",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Brookside town, Alabama") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "AL") %>%
  mutate(city = case_when(
    city == "Brookside town, Alabama" ~ "Watson")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzAxJyBmb3Igc3RhdGUgJ0FMJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '01' for state 'AL'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfYWxfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfYWxfMjAyMSwgY2Vuc3VzX2RhdGFfaGlnaGxhbmRfYWxfMjAyMSwgY2Vuc3VzX2RhdGFfd2F0c29uX2FsXzIwMjEpXG4gXG5ob21ldG93bnNfYWxfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX2FsICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfYWxfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG5ob21ldG93bnNfYWxfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpICNJZiB0aGlzIGlzIG5vdCBwcm9kdWNpbmcgYW4gZW1wdHkgZGF0YWZyYW1lLCBnbyBiYWNrIGFuZCBjb250aW51ZSB0byB3b3JrIG9uIE5BIHZhbHVlc1xuYGBgIn0= -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_al_2021 <- bind_rows(census_data_al_2021, census_data_highland_al_2021, census_data_watson_al_2021)
 
hometowns_al_complete <- distinct_hometowns_al %>%
  left_join(census_data_al_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_al_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWkxUU09rMTdFMmxxZ2VvZW9DcWxiSkRCTk1ZQlFNQ3JEU1hUNHR0cG1sWWhjMHczNHptbjhmNzYvYXAzSllJb1NYS0Z4bGE0dkJGK1BQanJYNUJnUVFuUXprcVJ2c2RramJoTXpwck5EK3dWZUt2YnJOWEFwaEo2bHdzQXJCc3FhZk5sNlU5VDlJTHE0K05DdHhkOUsvclFYQTlOVDNEVGFkNzd2VlJFU2I4aVRESnFZcWh4NytRODlUenExamx0YWVTR0VsUDNEb1EySE10V21nblptZ0RZQ2NwTy93RFZjOWJRUlVSaWdVaHlETE1reWtUdW9nYXhIQkxmS2NIUjFVYitEbVo3bDRiTDdRSzh5M0dvK0JrYjVsTndNT2d4bjIwTmVzR2RhaWZ4OTFPNGNzQjAzOHhTK1kvc1JTT3BlNjQyZ3NGRTJCSmQxeEdaeFdPTXEyOU1WWW9EMGNNMURYVGdvQXdMWUZNczZIekw3K0pyNytMQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2FsX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfYWwuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_al_complete, file = "hometowns_al.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIEFSSVpPTkEgSE9NRVRPV05TXG5cbiMgU3RlcCAxOiBGaWx0ZXIgZm9yIHRoZSBzdGF0ZSdzIHBsYXllcnNcbmZvb3RiYWxsX3Jvc3RlcnNfYXogPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiA9PSBcIkFaXCIpXG5cbiMgU3RlcCAyOiBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc19heiA8LSBmb290YmFsbF9yb3N0ZXJzX2F6ICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbF9wbGF5ZXJzID0gbigpKVxuYGBgIn0= -->

```r

# ARIZONA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_az <- football_rosters_usa %>%
  filter(hometown_state_clean == "AZ")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_az <- football_rosters_az %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfYXpfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJBWlwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_az_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "AZ",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzA0JyBmb3Igc3RhdGUgJ0FaJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '04' for state 'AZ'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfYXpfMjAyMSA8LSBjZW5zdXNfZGF0YV9hel8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9hel8yMDIxIDwtIGNlbnN1c19kYXRhX2F6XzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnQXJpem9uYScgfiBcIkFaXCIpKVxuXG4jIFN0ZXAgNjogSm9pbiB0aGUgY2Vuc3VzIGRhdGEgdG8gdGhlIGxpc3Qgb2YgaG9tZXRvd25zLiBBbHNvIGNyZWF0ZSBhIGNvbHVtbiB0aGF0IHRlbGxzIHVzIGhvdyBtYW55IHBlb3BsZSBhcmUgZWxpdGUgY29sbGVnZSBmb290YmFsbCBwbGF5ZXJzIGZvciBldmVyeSAxLDAwMCByZXNpZGVudHMuXG5ob21ldG93bnNfYXpfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX2F6ICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfYXpfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIFN0ZXAgNzogTm90aWNlIHRoZXJlIGFyZSBhIGZldyBOQSB2YWx1ZXMuIFRoaXMgaGFwcGVucyB3aGVuIHRoZSBjZW5zdXMgZGF0YSBkb2VzIG5vdCBqb2luIHdpdGggdGhlIGhvbWV0b3ducyBkYXRhLCBwZXJoYXBzIGJlY2F1c2UgdGhlIGhvbWV0b3duIGlzIG1pc3NwZWxsZWQgb3IgYmVjYXVzZSB0aGVyZSBpcyBubyBjZW5zdXMgZGF0YSBmb3IgdGhhdCB0b3duLiBGaXJzdCwgbGV0J3MgZmluZCB0aGUgTkEgdmFsdWVzLlxuaG9tZXRvd25zX2F6X2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKVxuYGBgIn0= -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_az_2021 <- census_data_az_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_az_2021 <- census_data_az_2021 %>%
  mutate(state = case_when(
    state == 'Arizona' ~ "AZ"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_az_complete <- distinct_hometowns_az %>%
  left_join(census_data_az_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_az_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWkxUU09rMTdFMFg3UUdxSHFCcXBld1F3VFJHd1lBQUs4M2wwMktiYVJwV1lUUE1ONlA1NS9IK3VuMHF0eVZDYUlueVJZYVdPSHdSL3Z4NHExOVFJTUhKVUk2SzBYNkhwRTM0ak00YXpROXNsZmlyMit5VkFHYVNPaGVMQUN4YjZtbnpaV25Qay9UQzZtT2pBbmNYL2V0NkVGeFBUYzl3MCttZWUzMVVoQWwvSWt4eXFtTG84Uy9rUFBYOEtsWjU3YWtrUnRJVHR3NEU5bHlMRnRxSkdkb0EyRW5LRHY5QTFmTldVRVdFWWtFSXNnenpaTXFFTHFJR01kd1MzK25CVWRVR2ZrNm11OWZHQzYzQ2ZJdnhLRGpaVzJZVDhEQ29jUjl0emJwQkhlcm5jYmRUK0hMQTlGL01rdmxQTElWanFUdXU5a0xCQkZqU0haZlJXWVdqVEd0dmpCWEt3eEVEZGMyMElDQk1TeURUYk9qOEM1MnI4ZHlMQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuI05vdCBhcHBsaWNhYmxlIGZvciBBcml6b25hXG5cbiMgU3RlcCA5OiBXZSBub3cgaGF2ZSB0byBhcHBlbmQgdGhlc2Ugc3BlY2lhbCBjYXNlcyB0byBvdXIgc3RhdGUgY2Vuc3VzIGRhdGEsIHJlZG8gdGhlIGpvaW4sIGFuZCBydW4gb25lIG1vcmUgY2hlY2sgZm9yIE5BIHZhbHVlcy5cbiNOb3QgYXBwbGljYWJsZSBmb3IgQXJpem9uYVxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2F6X2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfYXouY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

#Not applicable for Arizona

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
#Not applicable for Arizona

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_az_complete, file = "hometowns_az.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIEFSS0FOU0FTIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX2FyIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJBUlwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfYXIgPC0gZm9vdGJhbGxfcm9zdGVyc19hciAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# ARKANSAS HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ar <- football_rosters_usa %>%
  filter(hometown_state_clean == "AR")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ar <- football_rosters_ar %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfYXJfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJBUlwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ar_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "AR",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzA1JyBmb3Igc3RhdGUgJ0FSJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '05' for state 'AR'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfYXJfMjAyMSA8LSBjZW5zdXNfZGF0YV9hcl8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9hcl8yMDIxIDwtIGNlbnN1c19kYXRhX2FyXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnQXJrYW5zYXMnIH4gXCJBUlwiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX2FyX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19hciAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2FyXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19hcl9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ar_2021 <- census_data_ar_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ar_2021 <- census_data_ar_2021 %>%
  mutate(state = case_when(
    state == 'Arkansas' ~ "AR"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ar_complete <- distinct_hometowns_ar %>%
  left_join(census_data_ar_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ar_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWkxUU09rMTRrMDNQVURWQTFTdGxCMGltTVlvR0JCZ3BibDhXb3lacG1GVk5zTjhNNXAvSG04dnU2ZDZWeU9FbHFoY0ZHaUp3eGZoai9mWDdUTUtKRGdGS2xFMTJhK1F0QW1meVZtaitZRnRNbi8xUDNzamdKbWt6cVVpQU91T2V0cCtXanJ3TEwyeSt0U3F3TjFWLzdZZUJOZXg2Umx1ZWoxd3IwK0tNT0hQaEVsT1ZRbzkvb2FjcDU3ZnhCcXZQWlhFU0hybTFvSEFnV3ZSUVRzcFF4c0FlMG5aOFE5b0J0NEpxb2hRTEFoQmxtR2V4RXpvSW1rUXd5M3h2UjRkVlYzZ2wyeTZlMjI4MENyTXQ1aU9nck85RlRZREQ2T2E5dEZ0V1QrcTQzUmRWTWZ3OVlENXY1b2x5KzlVQ3FkU2Qxd2RoSUlKc0tSN0xwT3pDa2VKYTIrTkZjckRFUU4xYlZ3UUVLWWxrRGdidXZ3QW9GNEpnNHNDQUFBPSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2FyX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfYXIuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ar_complete, file = "hometowns_ar.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfY2FfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJDQVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5cbmBgYCJ9 -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ca_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "CA",
                           output = "wide")

```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzA2JyBmb3Igc3RhdGUgJ0NBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '06' for state 'CA'
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIENPTE9SQURPIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX2NvIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJDT1wiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfY28gPC0gZm9vdGJhbGxfcm9zdGVyc19jbyAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# COLORADO HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_co <- football_rosters_usa %>%
  filter(hometown_state_clean == "CO")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_co <- football_rosters_co %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfY29fMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJDT1wiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_co_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "CO",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzA4JyBmb3Igc3RhdGUgJ0NPJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '08' for state 'CO'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfY29fMjAyMSA8LSBjZW5zdXNfZGF0YV9jb18yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9jb18yMDIxIDwtIGNlbnN1c19kYXRhX2NvXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnQ29sb3JhZG8nIH4gXCJDT1wiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX2NvX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19jbyAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2NvXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19jb19jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_co_2021 <- census_data_co_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_co_2021 <- census_data_co_2021 %>%
  mutate(state = case_when(
    state == 'Colorado' ~ "CO"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_co_complete <- distinct_hometowns_co %>%
  left_join(census_data_co_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_co_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzVTdESUJUSDZWWTBiZEtseVh5Tk5ocHZmQURqQXhoTmRrY1l4WldNQWdHYXVaZWZVZ3JPY2pWdUR1ZDNUczcvZkx5LzdwN0xYUWtBV0lOOGxZRTFkRjhBUHovZW1oZmdpSE15a0lOaXN0OHVhZXMrazFPRCtVVmJKZjdtTnJzUWdJUmpZMEtSQ01zT1c5eCthVHpRSkwzUTh0UUt4ODFWZjFrdkJtdmY5QXkzdlJ5b2xTZUJDTE5uUkRqRklvUWUva0xHWWtzWHNjcEtpemxTSEorcE5sSGdRQ1hyWWpzaFE2b0k5aHlUNHo5UURiUmpXQ0FtaUJPS1dZcFk1RE5qRjBFREthcVI3ZVZvc09nY3Z5VFQzVXRsbVJSdXZ0VjBGSmpzTGRNSnFFY3g3YU5yU0QrS1kvUDBPQzNYeDY4WFRQL0ZySm4vaEZvdzFMcWo0c0JFSEFGeXZLYzhPQnQzRmIvM1Zta21iTHlpbzZiMUc0cUVTQjZKSHc1Y2ZnRUNiTkdIakFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMgTm9uZSBmb3IgQ29sb3JhZG9cblxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2NvX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfY28uY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
# None for Colorado

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_co_complete, file = "hometowns_co.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIEZMT1JJREEgSE9NRVRPV05TXG5cbiMgU3RlcCAxOiBGaWx0ZXIgZm9yIHRoZSBzdGF0ZSdzIHBsYXllcnNcbmZvb3RiYWxsX3Jvc3RlcnNfZmwgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiA9PSBcIkZMXCIpXG5cbiMgU3RlcCAyOiBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc19mbCA8LSBmb290YmFsbF9yb3N0ZXJzX2ZsICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbF9wbGF5ZXJzID0gbigpKVxuYGBgIn0= -->

```r

# FLORIDA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_fl <- football_rosters_usa %>%
  filter(hometown_state_clean == "FL")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_fl <- football_rosters_fl %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfZmxfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJGTFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_fl_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "FL",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzEyJyBmb3Igc3RhdGUgJ0ZMJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '12' for state 'FL'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfZmxfMjAyMSA8LSBjZW5zdXNfZGF0YV9mbF8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuYGBgIn0= -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_fl_2021 <- census_data_fl_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiV2FybmluZzogRXhwZWN0ZWQgMiBwaWVjZXMuIEFkZGl0aW9uYWwgcGllY2VzIGRpc2NhcmRlZCBpbiAxIHJvd3MgWzM3N10uXG4ifQ== -->

```
Warning: Expected 2 pieces. Additional pieces discarded in 1 rows [377].
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDU6IFN0YXRlLXNwZWNpZmljIGNsZWFuaW5nIG9mIGNlbnN1cyBkYXRhIHRvIHByZXBhcmUgZm9yIGpvaW4gd2l0aCBob21ldG93bnMvcm9zdGVyIGRhdGEuIFRoaXMgcGFydCBpcyBkaWZmZXJlbnQgZm9yIGV2ZXJ5IHN0YXRlLiBUaGUgZmlyc3QgbXV0YXRlIGZ1bmN0aW9uIHNob3VsZCBiZSBpbmNsdWRlZCBmb3IgZXZlcnkgc3RhdGUsIGp1c3QgbW9kaWZpZWQgZGVwZW5kaW5nIG9uIHRoZSBzdGF0ZSBuYW1lLiBBZGRpdGlvbmFsIG11dGF0ZSBmdW5jdGlvbnMgbWF5IGJlIG5lZWRlZCBmb3IgaW5zdGFuY2VzIHdoZW4gdGhlIGNlbnN1cyBuYW1lcyBzb21ldGhpbmcgaW4gYSB3ZWlyZCB3YXkgdGhhdCBkb2Vzbid0IGxpbmUgdXAgd2l0aCB0aGUgaG9tZXRvd25zLlxuY2Vuc3VzX2RhdGFfZmxfMjAyMSA8LSBjZW5zdXNfZGF0YV9mbF8yMDIxICU+JVxuICBtdXRhdGUoc3RhdGUgPSBjYXNlX3doZW4oXG4gICAgc3RhdGUgPT0gJ0Zsb3JpZGEnIH4gXCJGTFwiKSkgJT4lXG4gICAgZmlsdGVyKGNpdHkgIT0gXCJQbGFudGF0aW9uXCIgfCB0b3RhbF9wb3AgIT0gNDU2NSkgI1JlbW92aW5nIHRoZSBzZWNvbmQgUGxhbnRhdGlvbiwgRkwgdGhhdCBpcyBhIENEUFxuXG4jIFN0ZXAgNjogSm9pbiB0aGUgY2Vuc3VzIGRhdGEgdG8gdGhlIGxpc3Qgb2YgaG9tZXRvd25zLiBBbHNvIGNyZWF0ZSBhIGNvbHVtbiB0aGF0IHRlbGxzIHVzIGhvdyBtYW55IHBlb3BsZSBhcmUgZWxpdGUgY29sbGVnZSBmb290YmFsbCBwbGF5ZXJzIGZvciBldmVyeSAxLDAwMCByZXNpZGVudHMuXG5ob21ldG93bnNfZmxfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX2ZsICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfZmxfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIFN0ZXAgNzogTm90aWNlIHRoZXJlIGFyZSBhIGZldyBOQSB2YWx1ZXMuIFRoaXMgaGFwcGVucyB3aGVuIHRoZSBjZW5zdXMgZGF0YSBkb2VzIG5vdCBqb2luIHdpdGggdGhlIGhvbWV0b3ducyBkYXRhLCBwZXJoYXBzIGJlY2F1c2UgdGhlIGhvbWV0b3duIGlzIG1pc3NwZWxsZWQgb3IgYmVjYXVzZSB0aGVyZSBpcyBubyBjZW5zdXMgZGF0YSBmb3IgdGhhdCB0b3duLiBGaXJzdCwgbGV0J3MgZmluZCB0aGUgTkEgdmFsdWVzLlxuaG9tZXRvd25zX2ZsX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKVxuYGBgIn0= -->

```r
# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_fl_2021 <- census_data_fl_2021 %>%
  mutate(state = case_when(
    state == 'Florida' ~ "FL")) %>%
    filter(city != "Plantation" | total_pop != 4565) #Removing the second Plantation, FL that is a CDP

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_fl_complete <- distinct_hometowns_fl %>%
  left_join(census_data_fl_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_fl_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjQsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiNCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFs0XSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE4MVQwVXJETUJSTnU5YlJ3VVpsZmtCL1lJWGhpODhpZTVBOXlLYXl0M0tYeGpVc1MwcVRNZmVrMytJWCtnR3ltYlNKdUlMNmFpRzk5NTU3eU0wOXVabmRMQzU3aXg1Q3FJTUMzME9kVUxzb2ZMaWZqSzZRUm5UZ29RQkZ4ajVyMGxBN0pvajFDbXppYkVwVlFjRkc1M2VDSzVJOGtyeUM1Sm9BTG13aW5nTlhrTXlFUE1XanVVcVRXMUZ3MmRyWG4wei84QkRxMTN4eittWjVkc1VXajQ3Nis4VU9ETy9sM1RUZGZmdkovbi9leVVXRm1JRjBZanF3bDRPQzlLbUNEV25SbzByc1VxNXhhZlgwWC9WUHkvUFIzdGVSNG5vSUduQllpQTFSWXNjelROVSt3NHdBdDZtTHI1UlVvTWhKcnErRUFwYVZEUGFra3E3QWlnaWF1Mk5aaGlnZHNHU0ExOStBL29ia0ZIaEdPZGFGSEt2RUtxdVo3aFMyUmxhU0tsT0YyRXJndWNZUHJlNjZvbFJVbUNIMHpaQ0hMZjI4cWdYRVcyNzB5RWU0MlBMMWFEdzJJdHZwUTFaSnowNmg4Nk9tWm5DMGU0WHVCUkcrb3R5MUVESllFbWFEZ2I2ZFd2ZTByQ2hYN2pZMUt0TmFJWWRnd1J4U040Y09uNWZsYURqY0F3QUEifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Lithia","2":"FL","3":"3","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Ponte Vedra Beach","2":"FL","3":"3","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Santa Rosa Beach","2":"FL","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"St. Johns","2":"FL","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[4]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgTGl0aGlhLCBGTCwgdGhlIHppcCBjb2RlICgzMzU0Nykgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMzMzU0Ny0zMzU0Ny9cbmNlbnN1c19kYXRhX2xpdGhpYV9mbF8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgMzM1NDdcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJGTFwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDMzNTQ3XCIgfiBcIkxpdGhpYVwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Lithia, FL, the zip code (33547) seems to be a good substitute: https://censusreporter.org/profiles/86000US33547-33547/
census_data_lithia_fl_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 33547") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "FL") %>%
  mutate(city = case_when(
    city == "ZCTA5 33547" ~ "Lithia")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgUG9udGUgVmVkcmEgQmVhY2gsIEZMLCB0aGUgemlwIGNvZGUgKDMyMDgyKSBzZWVtcyB0byBiZSBhIGdvb2Qgc3Vic3RpdHV0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvODYwMDBVUzMyMDgyLTMyMDgyL1xuY2Vuc3VzX2RhdGFfcG9udGVfZmxfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiemN0YVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIlpDVEE1IDMyMDgyXCIpICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiRkxcIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJaQ1RBNSAzMjA4MlwiIH4gXCJQb250ZSBWZWRyYSBCZWFjaFwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r
# For Ponte Vedra Beach, FL, the zip code (32082) seems to be a good substitute: https://censusreporter.org/profiles/86000US32082-32082/
census_data_ponte_fl_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 32082") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "FL") %>%
  mutate(city = case_when(
    city == "ZCTA5 32082" ~ "Ponte Vedra Beach")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgU2FudGEgUm9zYSBCZWFjaCwgRkwsIHRoZSB6aXAgY29kZSAoMzI0NTkpIHNlZW1zIHRvIGJlIGEgZ29vZCBzdWJzdGl0dXRlOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTMzI0NTktMzI0NTkvXG5jZW5zdXNfZGF0YV9zYW50YV9mbF8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgMzI0NTlcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJGTFwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDMyNDU5XCIgfiBcIlNhbnRhIFJvc2EgQmVhY2hcIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r
# For Santa Rosa Beach, FL, the zip code (32459) seems to be a good substitute: https://censusreporter.org/profiles/86000US32459-32459/
census_data_santa_fl_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 32459") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "FL") %>%
  mutate(city = case_when(
    city == "ZCTA5 32459" ~ "Santa Rosa Beach")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgU3QuIEpvaG5zLCBGTCwgdGhlIHppcCBjb2RlIG9mIHRoZSBoaWdoIHNjaG9vbCAoMzIyNTkpIHNlZW1zIHRvIGJlIGEgZ29vZCBzdWJzdGl0dXRlOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTMzIyNTktMzIyNTkvXG5jZW5zdXNfZGF0YV9zdGpvaG5zX2ZsXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcInpjdGFcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgZmlsdGVyKG5hbWUgPT0gXCJaQ1RBNSAzMjI1OVwiKSAlPiVcbiAgcmVuYW1lKGNpdHkgPSBuYW1lLCB0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpICU+JVxuICBtdXRhdGUoc3RhdGUgPSBcIkZMXCIpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09IFwiWkNUQTUgMzIyNTlcIiB+IFwiU3QuIEpvaG5zXCIpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgdG90YWxfcG9wLCBibGFja19wb3AsIG1lZGlhbl9pbmNvbWUsIHBjdF9ibGFjaylcbmBgYCJ9 -->

```r
# For St. Johns, FL, the zip code of the high school (32259) seems to be a good substitute: https://censusreporter.org/profiles/86000US32259-32259/
census_data_stjohns_fl_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 32259") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "FL") %>%
  mutate(city = case_when(
    city == "ZCTA5 32259" ~ "St. Johns")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfZmxfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfZmxfMjAyMSwgY2Vuc3VzX2RhdGFfbGl0aGlhX2ZsXzIwMjEsIGNlbnN1c19kYXRhX3BvbnRlX2ZsXzIwMjEsIGNlbnN1c19kYXRhX3NhbnRhX2ZsXzIwMjEsIGNlbnN1c19kYXRhX3N0am9obnNfZmxfMjAyMSlcbiBcbmhvbWV0b3duc19mbF9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfZmwgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9mbF8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbmhvbWV0b3duc19mbF9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSkgI0lmIHRoaXMgaXMgbm90IHByb2R1Y2luZyBhbiBlbXB0eSBkYXRhZnJhbWUsIGdvIGJhY2sgYW5kIGNvbnRpbnVlIHRvIHdvcmsgb24gTkEgdmFsdWVzXG5gYGAifQ== -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_fl_2021 <- bind_rows(census_data_fl_2021, census_data_lithia_fl_2021, census_data_ponte_fl_2021, census_data_santa_fl_2021, census_data_stjohns_fl_2021)
 
hometowns_fl_complete <- distinct_hometowns_fl %>%
  left_join(census_data_fl_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_fl_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzV3JESUJUSFRSczNFa2dKZEsrUlFObk5IbURzQWNZR3ZSTnJYQ00xS21ybyt2TGRqTkYxOGFyZUhNL3ZITTcvZkx5LzdwL0xmUWtBV0lOOGxZRTFkRjhBUHovZW1oZmdpSE15a0lOaXN0OHVhZXMrazFPRCtVVmJKZjdtUHJzUWdJUmpZMEtSQ01zT1c5eCthVHpRSkwzUTh0d0t4ODFOZjFrdkJtdmY5QXkzdlJ5b2xXZUJDTE1YUkRqRklvU2Uva0xHWWtzWHNjcEtpemxTSEYrb05sSGdTQ1hyWWpzaFE2b0lEaHlUMHo5UURiUmpXQ0FtaUJPS1dZcFk1RE5qRjBFREthcVI3ZVZvc09nY3Z5YlRQVXBsbVJSdXZ0VjBGSmpzTGRNSnFFY3g3YU5yU0QrS1U3UGJUY3YxOGRzRjAzOHhhK1kvb1JZTXRSNm9PRElSUjRBY0h5Z1B6c1pkeGUrOVZab0pHNi9vcUduOWhpSWhra2ZpaHdQWFh5Qk9qK1NNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2ZsX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfZmwuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_fl_complete, file = "hometowns_fl.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIEdFT1JHSUEgSE9NRVRPV05TXG5cbiMgU3RlcCAxOiBGaWx0ZXIgZm9yIHRoZSBzdGF0ZSdzIHBsYXllcnNcbmZvb3RiYWxsX3Jvc3RlcnNfZ2EgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiA9PSBcIkdBXCIpXG5cbiMgU3RlcCAyOiBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc19nYSA8LSBmb290YmFsbF9yb3N0ZXJzX2dhICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbF9wbGF5ZXJzID0gbigpKVxuYGBgIn0= -->

```r

# GEORGIA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ga <- football_rosters_usa %>%
  filter(hometown_state_clean == "GA")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ga <- football_rosters_ga %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfZ2FfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJHQVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ga_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "GA",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzEzJyBmb3Igc3RhdGUgJ0dBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '13' for state 'GA'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfZ2FfMjAyMSA8LSBjZW5zdXNfZGF0YV9nYV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9nYV8yMDIxIDwtIGNlbnN1c19kYXRhX2dhXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnR2VvcmdpYScgfiBcIkdBXCIpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSAnQXRoZW5zLUNsYXJrZSBDb3VudHkgdW5pZmllZCBnb3Zlcm5tZW50IChiYWxhbmNlKScgfiBcIkF0aGVuc1wiLFxuICAgIGNpdHkgPT0gJ01hY29uLUJpYmIgQ291bnR5JyB+IFwiTWFjb25cIixcbiAgICBjaXR5ID09ICdNY1JhZS1IZWxlbmEnIH4gJ01jUmFlJyxcbiAgICBUUlVFIH4gY2l0eSkpXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cbmhvbWV0b3duc19nYV9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfZ2EgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9nYV8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbiMgU3RlcCA3OiBOb3RpY2UgdGhlcmUgYXJlIGEgZmV3IE5BIHZhbHVlcy4gVGhpcyBoYXBwZW5zIHdoZW4gdGhlIGNlbnN1cyBkYXRhIGRvZXMgbm90IGpvaW4gd2l0aCB0aGUgaG9tZXRvd25zIGRhdGEsIHBlcmhhcHMgYmVjYXVzZSB0aGUgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCBvciBiZWNhdXNlIHRoZXJlIGlzIG5vIGNlbnN1cyBkYXRhIGZvciB0aGF0IHRvd24uIEZpcnN0LCBsZXQncyBmaW5kIHRoZSBOQSB2YWx1ZXMuXG5ob21ldG93bnNfZ2FfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpXG5gYGAifQ== -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ga_2021 <- census_data_ga_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ga_2021 <- census_data_ga_2021 %>%
  mutate(state = case_when(
    state == 'Georgia' ~ "GA")) %>%
  mutate(city = case_when(
    city == 'Athens-Clarke County unified government (balance)' ~ "Athens",
    city == 'Macon-Bibb County' ~ "Macon",
    city == 'McRae-Helena' ~ 'McRae',
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ga_complete <- distinct_hometowns_ga %>%
  left_join(census_data_ga_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ga_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjQsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiNCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFs0XSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE4MVN3VTdETUF4TnU1YlJTWnNxalEvZ0IxWUp1SEJGQW5ZZklPMVd1V25Zb21WSjFhYmFkb0p2NFF2NUFMVGhkTW0wVlFLdVZFcHRQei9aOFlzbjk5T2IzclJIQ09tUXdQZElKMFNYaEMvUGo2TmJnZ2dHSGdsSVpPd2FTVU4wVEJEakNXd2llaENDeVpWU3VRTW1rTlh5Y2d5RkJUb1R0cmJ1K1ZPZENUNlQwQ3JpaisvKzhBanBOL3o5QmJ5akV6dDhoOTh2ZG1CNGI1OW13dTdIVC9iLzgwNWVKYVFDcXNxSzRNQmVEaHFTMXhLV3JFV1BTclZLSk9LVjFkTi94eC9LODlXdTYwaHhJL2dlSE03VmttbTFraW5sZXBOU3dVRGExTVVoVlduUTdDVFgxMHFEU0FzQkcxWldyc0dNS1g3WUdNdFFibU9pVEFCZEhBSDlKY3M1eUpSTGlvMGNxNkE2YlpqdUZyWkhXckF5MVhOVlZ5Qnp4TGV0NmJxcTBGeEpuTTgzR3gyMjlQUEtGaERYMHVpUmoraThsb3ZSMWJVUjJXNGZzVXA2ZGd1ZEgrMTdCanRiSzdTMXpwaWNjZWxHQ0FWa1ROaGdnSy9UNko0VUpaZmF2U2FpVmRJbzVCQ3FoRU9hNGNqMkczS2ZFOC9KQXdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Ellenwood","2":"GA","3":"9","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Rabun Gap","2":"GA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Rex","2":"GA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Subligna","2":"GA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[4]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgRWxsZW53b29kLCBHQSwgdGhlIHppcCBjb2RlICgzMDI5NCkgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMzMDI5NC0zMDI5NC9cbmNlbnN1c19kYXRhX2VsbGVud29vZF9nYV8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgMzAyOTRcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJHQVwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDMwMjk0XCIgfiBcIkVsbGVud29vZFwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Ellenwood, GA, the zip code (30294) seems to be a good substitute: https://censusreporter.org/profiles/86000US30294-30294/
census_data_ellenwood_ga_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 30294") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "GA") %>%
  mutate(city = case_when(
    city == "ZCTA5 30294" ~ "Ellenwood")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgUmFidW4gR2FwLCBHQSwgdGhlIHppcCBjb2RlICgzMDU2OCkgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMzMDU2OC0zMDU2OC9cbmNlbnN1c19kYXRhX3JhYnVuX2dhXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcInpjdGFcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgZmlsdGVyKG5hbWUgPT0gXCJaQ1RBNSAzMDU2OFwiKSAlPiVcbiAgcmVuYW1lKGNpdHkgPSBuYW1lLCB0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpICU+JVxuICBtdXRhdGUoc3RhdGUgPSBcIkdBXCIpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09IFwiWkNUQTUgMzA1NjhcIiB+IFwiUmFidW4gR2FwXCIpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgdG90YWxfcG9wLCBibGFja19wb3AsIG1lZGlhbl9pbmNvbWUsIHBjdF9ibGFjaylcbmBgYCJ9 -->

```r
# For Rabun Gap, GA, the zip code (30568) seems to be a good substitute: https://censusreporter.org/profiles/86000US30568-30568/
census_data_rabun_ga_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 30568") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "GA") %>%
  mutate(city = case_when(
    city == "ZCTA5 30568" ~ "Rabun Gap")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgUmV4LCBHQSwgdGhlIHppcCBjb2RlICgzMDI3Mykgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMzMDI3My0zMDI3My9cbmNlbnN1c19kYXRhX3JleF9nYV8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgMzAyNzNcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJHQVwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDMwMjczXCIgfiBcIlJleFwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r
# For Rex, GA, the zip code (30273) seems to be a good substitute: https://censusreporter.org/profiles/86000US30273-30273/
census_data_rex_ga_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 30273") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "GA") %>%
  mutate(city = case_when(
    city == "ZCTA5 30273" ~ "Rex")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgU3VibGlnbmEsIEdBLCB0aGUgYmxvY2sgZ3JvdXAgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzE1MDAwVVMxMzA1NTAxMDEwMDItYmctMi10cmFjdC0xMDEtY2hhdHRvb2dhLWdhL1xuY2Vuc3VzX2RhdGFfc3VibGlnbmFfZ2FfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiYmxvY2sgZ3JvdXBcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJHQVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIkJsb2NrIEdyb3VwIDIsIENlbnN1cyBUcmFjdCAxMDEsIENoYXR0b29nYSBDb3VudHksIEdlb3JnaWFcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJHQVwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIkJsb2NrIEdyb3VwIDIsIENlbnN1cyBUcmFjdCAxMDEsIENoYXR0b29nYSBDb3VudHksIEdlb3JnaWFcIiB+IFwiU3VibGlnbmFcIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r
# For Subligna, GA, the block group seems to be a good substitute: https://censusreporter.org/profiles/15000US130550101002-bg-2-tract-101-chattooga-ga/
census_data_subligna_ga_2021 <- get_acs(geography = "block group",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "GA",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Block Group 2, Census Tract 101, Chattooga County, Georgia") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "GA") %>%
  mutate(city = case_when(
    city == "Block Group 2, Census Tract 101, Chattooga County, Georgia" ~ "Subligna")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzEzJyBmb3Igc3RhdGUgJ0dBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '13' for state 'GA'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfZ2FfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfZ2FfMjAyMSwgY2Vuc3VzX2RhdGFfZWxsZW53b29kX2dhXzIwMjEsIGNlbnN1c19kYXRhX3JhYnVuX2dhXzIwMjEsIGNlbnN1c19kYXRhX3JleF9nYV8yMDIxLCBjZW5zdXNfZGF0YV9zdWJsaWduYV9nYV8yMDIxKVxuXG5ob21ldG93bnNfZ2FfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX2dhICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfZ2FfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG5ob21ldG93bnNfZ2FfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpICNJZiB0aGlzIGlzIG5vdCBwcm9kdWNpbmcgYW4gZW1wdHkgZGF0YWZyYW1lLCBnbyBiYWNrIGFuZCBjb250aW51ZSB0byB3b3JrIG9uIE5BIHZhbHVlc1xuYGBgIn0= -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_ga_2021 <- bind_rows(census_data_ga_2021, census_data_ellenwood_ga_2021, census_data_rabun_ga_2021, census_data_rex_ga_2021, census_data_subligna_ga_2021)

hometowns_ga_complete <- distinct_hometowns_ga %>%
  left_join(census_data_ga_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_ga_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzVTdESUJUSDZWWTBiZEtseVh5Tk5sRnZmQURqQXhoTmRrY1l4WldNQWdHYXVaZWZVZ3JPY2pWdUR1ZDNUczcvZkx5LzdwN0xYUWtBV0lOOGxZRTFkRjhBUHovZW1oZmdpSE15a0lOaXN0OHVhZXMrazFPRCtVVmJKZjdtTnJzUWdJUmpZMEtSQ01zT1c5eCthVHpRSkwzUTh0UUt4ODFWZjFrdkJtdmY5QXkzdlJ5b2xTZUJDTE5uUkRqRklvUWUva0xHWWtzWHNjcEtpemxTSEorcE5sSGdRQ1hyWWpzaFE2b0k5aHlUNHo5UURiUmpXQ0FtaUJPS1dZcFk1RE5qRjBFREthcVI3ZVZvc09nY3Z5VFQzVXRsbVJSdXZ0VjBGSmpzTGRNSnFFY3g3YU5yU0QrS1kvUDROQzNYeDY4WFRQL0ZySm4vaEZvdzFMcWo0c0JFSEFGeXZLYzhPQnQzRmIvM1Zta21iTHlpbzZiMUc0cUVTQjZKSHc1Y2ZnRkdLRzFCakFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2dhX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfZ2EuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ga_complete, file = "hometowns_ga.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIEhBV0FJSSBIT01FVE9XTlNcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc19oaSA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiSElcIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX2hpIDwtIGZvb3RiYWxsX3Jvc3RlcnNfaGkgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# HAWAII HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_hi <- football_rosters_usa %>%
  filter(hometown_state_clean == "HI")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_hi <- football_rosters_hi %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfaGlfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJISVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_hi_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "HI",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzE1JyBmb3Igc3RhdGUgJ0hJJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '15' for state 'HI'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfaGlfMjAyMSA8LSBjZW5zdXNfZGF0YV9oaV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9oaV8yMDIxIDwtIGNlbnN1c19kYXRhX2hpXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnSGF3YWlpJyB+IFwiSElcIikpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09ICdVcmJhbiBIb25vbHVsdScgfiBcIkhvbm9sdWx1XCIsXG4gICAgY2l0eSA9PSAnS2FpbHVhIChIb25vbHVsdSBDb3VudHkpJyB+IFwiS2FpbHVhXCIsXG4gICAgY2l0eSA9PSAnS2FwYWEnIH4gXCJLYXBhJ2FcIixcbiAgICBjaXR5ID09IFwiTWlsaWxhbmkgVG93blwiIH4gXCJNaWxpbGFuaVwiLFxuICAgIFRSVUUgfiBjaXR5KSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX2hpX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19oaSAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2hpXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19oaV9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_hi_2021 <- census_data_hi_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_hi_2021 <- census_data_hi_2021 %>%
  mutate(state = case_when(
    state == 'Hawaii' ~ "HI")) %>%
  mutate(city = case_when(
    city == 'Urban Honolulu' ~ "Honolulu",
    city == 'Kailua (Honolulu County)' ~ "Kailua",
    city == 'Kapaa' ~ "Kapa'a",
    city == "Mililani Town" ~ "Mililani",
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_hi_complete <- distinct_hometowns_hi %>%
  left_join(census_data_hi_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_hi_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzV3JESUJUSFRSczNFa2dKZEsrUndPak5IbURzQWNZR3ZSTnJYQ00xS21ybyt2TGRqTkYxOGFyZUhNL3ZITTcvZkx5LzduZmx2Z1FBckVHK3lzQWF1aStBbng5dnpRdHd4RGtaeUVFeDJXK1h0SFdmeWFuQi9LS3RFbjl6bjEwSVFNS3hNYUZJaEdXSExXNi9OQjVva2w1b2VXNkY0K2FtdjZ3WGc3VnZlb2JiWGc3VXlyTkFoTmtMSXB4aUVVSlBmeUZqc2FXTFdHV2x4Undwamk5VW15aHdwSkoxc1oyUUlWVUVCNDdKNlIrb0J0b3hMQkFUeEFuRkxFVXM4cG14aTZDQkZOWEk5bkkwV0hTT1g1UHBIcVd5VEFvMzMybzZDa3oybHVrRTFLT1k5dEUxcEIvRnFYbmVUY3YxOGRzRjAzOHhhK1kvb1JZTXRSNm9PRElSUjRBY0h5Z1B6c1pkeGUrOVZab0pHNi9vcUduOWhpSWhra2ZpaHdQWFgyUUtNeUtNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgSGF3YWlpLCB3ZSBmaXhlZCBhbGwgdGhlIE5BIHZhbHVlcyBieSBhZGp1c3RpbmcgdGhlIHdheSB0aGUgY2Vuc3VzIHJlZmVycmVkIHRvIHRoZSB0b3duIChzZWUgU3RlcCA1KSBvciBieSBhZGp1c3RpbmcgdGhlIHBsYXllcidzIGhvbWV0b3duIG5hbWUgaW4gT3BlblJlZmluZSAoZm9yIGV4YW1wbGUsIHBsYXllcnMgd2hvc2UgaG9tZXRvd25zIHdlcmUgbGlzdGVkIGFzIE1hdWkpXG5cbiMgU3RlcCA5OiBXZSBub3cgaGF2ZSB0byBhcHBlbmQgdGhlc2Ugc3BlY2lhbCBjYXNlcyB0byBvdXIgc3RhdGUgY2Vuc3VzIGRhdGEsIHJlZG8gdGhlIGpvaW4sIGFuZCBydW4gb25lIG1vcmUgY2hlY2sgZm9yIE5BIHZhbHVlcy5cblxuIyBOL0EgZm9yIEhhd2FpaVxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2hpX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfaGkuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Hawaii, we fixed all the NA values by adjusting the way the census referred to the town (see Step 5) or by adjusting the player's hometown name in OpenRefine (for example, players whose hometowns were listed as Maui)

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.

# N/A for Hawaii

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_hi_complete, file = "hometowns_hi.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIElMTElOT0lTIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX2lsIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJJTFwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfaWwgPC0gZm9vdGJhbGxfcm9zdGVyc19pbCAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# ILLINOIS HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_il <- football_rosters_usa %>%
  filter(hometown_state_clean == "IL")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_il <- football_rosters_il %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfaWxfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJJTFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_il_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "IL",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzE3JyBmb3Igc3RhdGUgJ0lMJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '17' for state 'IL'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfaWxfMjAyMSA8LSBjZW5zdXNfZGF0YV9pbF8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9pbF8yMDIxIDwtIGNlbnN1c19kYXRhX2lsXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnSWxsaW5vaXMnIH4gXCJJTFwiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX2lsX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19pbCAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2lsXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19pbF9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_il_2021 <- census_data_il_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_il_2021 <- census_data_il_2021 %>%
  mutate(state = case_when(
    state == 'Illinois' ~ "IL"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_il_complete <- distinct_hometowns_il %>%
  left_join(census_data_il_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_il_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzVTdESUJUSDZWWTBiZEtseVh5Tk5qRjY0UU1ZSDhCb3NqdkNLSzVrRkFqUXpMMzhsRkp3bHF0eGN6aS9jM0wrNStQOWRmZFU3a29Bd0Jya3F3eXNvZnNDK1BueDFyd0FSNXlUZ1J3VWsvMTJTVnYzbVp3YXpDL2FLdkUzdDltRkFDUWNHeE9LUkZoMjJPTDJTK09CSnVtRmxxZFdPRzZ1K3N0Nk1WajdwbWU0N2VWQXJUd0pSSmc5SThJcEZpSDA4QmN5Rmx1NmlGVldXc3lSNHZoTXRZa0NCeXBaRjlzSkdWSkZzT2VZSFArQmFxQWR3d0l4UVp4UXpGTEVJcDhadXdnYVNGR05iQzlIZzBYbitDV1o3bDRxeTZSdzg2Mm1vOEJrYjVsT1FEMkthUjlkUS9wUkhKdkg1Mm01UG42OVlQb3ZaczM4SjlTQ29kWWRGUWNtNGdpUTR6M2x3ZG00cS9pOXQwb3pZZU1WSFRXdDMxQWtSUEpJL0hEZzhndkw0dGpSakFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMgTm9uZSBmb3IgSWxsaW5vaXNcblxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuIyBOb25lIGZvciBJbGxpbm9pc1xuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2lsX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfaWwuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
# None for Illinois

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
# None for Illinois

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_il_complete, file = "hometowns_il.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIElORElBTkEgSE9NRVRPV05TXG5cbiMgU3RlcCAxOiBGaWx0ZXIgZm9yIHRoZSBzdGF0ZSdzIHBsYXllcnNcbmZvb3RiYWxsX3Jvc3RlcnNfaW4gPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiA9PSBcIklOXCIpXG5cbiMgU3RlcCAyOiBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc19pbiA8LSBmb290YmFsbF9yb3N0ZXJzX2luICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbF9wbGF5ZXJzID0gbigpKVxuYGBgIn0= -->

```r

# INDIANA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_in <- football_rosters_usa %>%
  filter(hometown_state_clean == "IN")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_in <- football_rosters_in %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfaW5fMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJJTlwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_in_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "IN",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzE4JyBmb3Igc3RhdGUgJ0lOJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '18' for state 'IN'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfaW5fMjAyMSA8LSBjZW5zdXNfZGF0YV9pbl8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9pbl8yMDIxIDwtIGNlbnN1c19kYXRhX2luXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnSW5kaWFuYScgfiBcIklOXCIpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSAnSW5kaWFuYXBvbGlzIChiYWxhbmNlKScgfiBcIkluZGlhbmFwb2xpc1wiLFxuICAgIFRSVUUgfiBjaXR5KSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX2luX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19pbiAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2luXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19pbl9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_in_2021 <- census_data_in_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_in_2021 <- census_data_in_2021 %>%
  mutate(state = case_when(
    state == 'Indiana' ~ "IN")) %>%
  mutate(city = case_when(
    city == 'Indianapolis (balance)' ~ "Indianapolis",
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_in_complete <- distinct_hometowns_in %>%
  left_join(census_data_in_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_in_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjIsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMiDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsyXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE3VlNYV29DTVJET3JtNnRVa1d3QitnRlhDaWwwQU1VU3luMG9iVGdXNGpacU1HWUxFa1c2MU43bHA2d0o5Qk8xb3pvdm5jaG01bHZQdWJubTd3OVR1OTYweDRocEVYYWFVSmFHWmdrKzNpZmpCOElJT0FrcEUyNjRmNEUwZ2lNNEF6aHBERndOVkZtVzdpYkYyMW1MbUtYVDVWVWMyT0xCamQ5ZmoyeENPblhzY05Kamx5b3NZZnY1QjRFL09zM05OZjV3ZnYvOFRNQk1xNlljN0ZKQkhzRjh5eWZXN1lXRFhyWG1rMnVBWGM0NXpmOFlKeGRNeStTaHJXNEIzQzBOR3ZoelVaVEx2MldjaVdZanFIclk4aDU1c1Zack8rTlo0cVdpbTJGeFdWa0MyRmtnVzFGaGlrUm1DbkdWeWRBZnkwS3lUU1Zta01oWkpYYzA1cUpYY1FhdEJTVytxV3BITk5oMjgzcE9xYjAwbWlZTHcyUEoydm9sOWdHTUt4MDBLTVk4MldsVitQYit5QnlmQjBrS3BuRVY0SjI5MUN6dlkrNXNwanJRdWlGMURoQ3B0aE1xT2dNWUR1MTdubHBwZmE0VFVCZFhpdUVDRGNLa1hvNHN2c0RWVVJoOVRRREFBQT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Floyds Knobs","2":"IN","3":"2","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Guilford","2":"IN","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[2]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgRmxveWRzIEtub2JzLCBJTiAoNDcxMTkpIGFuZCBHdWlsZm9yZCwgSU4gKDQ3MDIyKSAgdGhlIHppcCBjb2RlcyBzZWVtcyB0byBiZSBnb29kIHN1YnN0aXR1dGVzOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTNDcxMTktNDcxMTkvIGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVM0NzAyMi00NzAyMi9cbmNlbnN1c19kYXRhX3ppcHNfaW5fMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiemN0YVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIlpDVEE1IDQ3MTE5XCIgfCBuYW1lID09IFwiWkNUQTUgNDcwMjJcIiApICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiSU5cIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJaQ1RBNSA0NzExOVwiIH4gXCJGbG95ZHMgS25vYnNcIixcbiAgICBjaXR5ID09IFwiWkNUQTUgNDcwMjJcIiB+IFwiR3VpbGZvcmRcIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Floyds Knobs, IN (47119) and Guilford, IN (47022)  the zip codes seems to be good substitutes: https://censusreporter.org/profiles/86000US47119-47119/ https://censusreporter.org/profiles/86000US47022-47022/
census_data_zips_in_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 47119" | name == "ZCTA5 47022" ) %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "IN") %>%
  mutate(city = case_when(
    city == "ZCTA5 47119" ~ "Floyds Knobs",
    city == "ZCTA5 47022" ~ "Guilford")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfaW5fMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfaW5fMjAyMSwgY2Vuc3VzX2RhdGFfemlwc19pbl8yMDIxKVxuIFxuaG9tZXRvd25zX2luX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19pbiAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2luXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuaG9tZXRvd25zX2luX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKSAjSWYgdGhpcyBpcyBub3QgcHJvZHVjaW5nIGFuIGVtcHR5IGRhdGFmcmFtZSwgZ28gYmFjayBhbmQgY29udGludWUgdG8gd29yayBvbiBOQSB2YWx1ZXNcbmBgYCJ9 -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_in_2021 <- bind_rows(census_data_in_2021, census_data_zips_in_2021)
 
hometowns_in_complete <- distinct_hometowns_in %>%
  left_join(census_data_in_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_in_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzV3JESUJUSFRSczNFa2dKZEsrUndCaURQY0RZQTR3TmVpZld1RVpxVk5UUTllVzdHYVByNGxXOU9aN2ZPWnovK1hoLzNUMlZ1eElBc0FiNUtnTnI2TDRBZm42OE5TL0FFZWRrSUFmRlpMOWQwdFo5SnFjRzg0dTJTdnpOYlhZaEFBbkh4b1FpRVpZZHRyajkwbmlnU1hxaDVha1ZqcHVyL3JKZUROYSs2Umx1ZXpsUUswOENFV2JQaUhDS1JRZzkvSVdNeFpZdVlwV1ZGbk9rT0Q1VGJhTEFnVXJXeFhaQ2hsUVI3RGtteDMrZ0dtakhzRUJNRUNjVXN4U3h5R2ZHTG9JR1VsUWoyOHZSWU5FNWZrbW11NWZLTWluY2ZLdnBLRERaVzZZVFVJOWkya2ZYa0g0VXgrYnhlVnF1ajE4dm1QNkxXVFAvQ2JWZ3FIVkh4WUdKT0FMa2VFOTVjRGJ1S243dnJkSk0ySGhGUjAzck54UUprVHdTUHh5NC9BTHB3SWF5akFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2luX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfaW4uY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_in_complete, file = "hometowns_in.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIElPV0EgSE9NRVRPV05TXG5cbiMgU3RlcCAxOiBGaWx0ZXIgZm9yIHRoZSBzdGF0ZSdzIHBsYXllcnNcbmZvb3RiYWxsX3Jvc3RlcnNfaWEgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiA9PSBcIklBXCIpXG5cbiMgU3RlcCAyOiBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc19pYSA8LSBmb290YmFsbF9yb3N0ZXJzX2lhICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbF9wbGF5ZXJzID0gbigpKVxuYGBgIn0= -->

```r

# IOWA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ia <- football_rosters_usa %>%
  filter(hometown_state_clean == "IA")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ia <- football_rosters_ia %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfaWFfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJJQVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ia_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "IA",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzE5JyBmb3Igc3RhdGUgJ0lBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '19' for state 'IA'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfaWFfMjAyMSA8LSBjZW5zdXNfZGF0YV9pYV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9pYV8yMDIxIDwtIGNlbnN1c19kYXRhX2lhXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnSW93YScgfiBcIklBXCIpKVxuXG4jIFN0ZXAgNjogSm9pbiB0aGUgY2Vuc3VzIGRhdGEgdG8gdGhlIGxpc3Qgb2YgaG9tZXRvd25zLiBBbHNvIGNyZWF0ZSBhIGNvbHVtbiB0aGF0IHRlbGxzIHVzIGhvdyBtYW55IHBlb3BsZSBhcmUgZWxpdGUgY29sbGVnZSBmb290YmFsbCBwbGF5ZXJzIGZvciBldmVyeSAxLDAwMCByZXNpZGVudHMuXG5ob21ldG93bnNfaWFfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX2lhICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfaWFfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIFN0ZXAgNzogTm90aWNlIHRoZXJlIGFyZSBhIGZldyBOQSB2YWx1ZXMuIFRoaXMgaGFwcGVucyB3aGVuIHRoZSBjZW5zdXMgZGF0YSBkb2VzIG5vdCBqb2luIHdpdGggdGhlIGhvbWV0b3ducyBkYXRhLCBwZXJoYXBzIGJlY2F1c2UgdGhlIGhvbWV0b3duIGlzIG1pc3NwZWxsZWQgb3IgYmVjYXVzZSB0aGVyZSBpcyBubyBjZW5zdXMgZGF0YSBmb3IgdGhhdCB0b3duLiBGaXJzdCwgbGV0J3MgZmluZCB0aGUgTkEgdmFsdWVzLlxuaG9tZXRvd25zX2lhX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKVxuYGBgIn0= -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ia_2021 <- census_data_ia_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ia_2021 <- census_data_ia_2021 %>%
  mutate(state = case_when(
    state == 'Iowa' ~ "IA"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ia_complete <- distinct_hometowns_ia %>%
  left_join(census_data_ia_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ia_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjEsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMSDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsxXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE2VlJ6VW9ETVJCT3QxM0xGbG9YNmdQNEFsMFFRYndLSW5nVFVla3RUTE94RFUyVFpaTlNlOUpuOFFsOWd0YkpiaUxkWEYzWXpNdzNIL1B6emZQOS9IbzBIeEZDK21TUTlFZy9SWmVrcnk4UHMxdUNDQVk5TWlDWnN4OUltcUxqZ3Z3a2NmNGtPUmhROXZJTnBPVDdLSjA4M3VFN2JwRDJ6NzNOanZpaG5iajQ4OGQxSG43L1ArNU1uVElKeGtRampVcXdVTHpYc09FUlBhdjFybENJR3o5ejhvVlBPMmUzYmlEbGpTSXRPRjNwRGJkNnB5Z1RkazhaNnFKODZ1SXZaU3hZM3NtTnJiWWdhU1ZoejJzVEdpeTVGbVVZeXpOMEZZQ0ZCTFkrQWNZYlhncFFWQ2lHalFLcllwWTJ6RENGNzBFclhsTzcwbHM4VzRuNElkcHVxQ3NydE1MOUVuZnhOTkt2VjBkQXZsVk9qM0xHVmx1MW5sM2RPSkg5bFVsMC9lQm5iYy9CMGRkS2ZhMHpycFpDaFJWU0NRc3VmVERCNnpTNkYxVXRsQTNYUk5RVWpVSUJZVm9HcEZtT0hINEJpL3cyQU9rQ0FBQT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Pleasant Valley","2":"IA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[1]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBQbGVhc2FudCBWYWxsZXksIElBIGlzIGEgY291bnR5IHN1YmRpdmlzaW9uOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy8wNjAwMFVTMTkxNjM5MzQyMC1wbGVhc2FudC12YWxsZXktdG93bnNoaXAtc2NvdHQtY291bnR5LWlhL1xuY2Vuc3VzX2RhdGFfcGxlYXNhbnRfaWFfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiY291bnR5IHN1YmRpdmlzaW9uXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBzdGF0ZSA9IFwiSW93YVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgY291bnR5ID0gXCJTY290dCBDb3VudHlcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgZmlsdGVyKG5hbWUgPT0gXCJQbGVhc2FudCBWYWxsZXkgdG93bnNoaXAsIFNjb3R0IENvdW50eSwgSW93YVwiKSAlPiVcbiAgcmVuYW1lKGNpdHkgPSBuYW1lLCB0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpICU+JVxuICBtdXRhdGUoc3RhdGUgPSBcIklBXCIpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09IFwiUGxlYXNhbnQgVmFsbGV5IHRvd25zaGlwLCBTY290dCBDb3VudHksIElvd2FcIiB+IFwiUGxlYXNhbnQgVmFsbGV5XCIpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgdG90YWxfcG9wLCBibGFja19wb3AsIG1lZGlhbl9pbmNvbWUsIHBjdF9ibGFjaylcbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# Pleasant Valley, IA is a county subdivision: https://censusreporter.org/profiles/06000US1916393420-pleasant-valley-township-scott-county-ia/
census_data_pleasant_ia_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "Iowa",
                           county = "Scott County",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Pleasant Valley township, Scott County, Iowa") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "IA") %>%
  mutate(city = case_when(
    city == "Pleasant Valley township, Scott County, Iowa" ~ "Pleasant Valley")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzE5JyBmb3Igc3RhdGUgJ0lvd2EnXG5Vc2luZyBGSVBTIGNvZGUgJzE2MycgZm9yICdTY290dCBDb3VudHknXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '19' for state 'Iowa'
Using FIPS code '163' for 'Scott County'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfaWFfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfaWFfMjAyMSwgY2Vuc3VzX2RhdGFfcGxlYXNhbnRfaWFfMjAyMSlcbiBcbmhvbWV0b3duc19pYV9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfaWEgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9pYV8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbmhvbWV0b3duc19pYV9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSkgI0lmIHRoaXMgaXMgbm90IHByb2R1Y2luZyBhbiBlbXB0eSBkYXRhZnJhbWUsIGdvIGJhY2sgYW5kIGNvbnRpbnVlIHRvIHdvcmsgb24gTkEgdmFsdWVzXG5gYGAifQ== -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_ia_2021 <- bind_rows(census_data_ia_2021, census_data_pleasant_ia_2021)
 
hometowns_ia_complete <- distinct_hometowns_ia %>%
  left_join(census_data_ia_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_ia_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzV3JESUJUSFRSczNFa2dKZEsrUndCaU1QY0RZQTR3TmVpZld1RVpxVk5UUTllVzdHYVByNGxXOU9aN2ZPWnovK1hoLzNUMlZ1eElBc0FiNUtnTnI2TDRBZm42OE5TL0FFZWRrSUFmRlpMOWQwdFo5SnFjRzg0dTJTdnpOYlhZaEFBbkh4b1FpRVpZZHRyajkwbmlnU1hxaDVha1ZqcHVyL3JKZUROYSs2Umx1ZXpsUUswOENFV2JQaUhDS1JRZzkvSVdNeFpZdVlwV1ZGbk9rT0Q1VGJhTEFnVXJXeFhaQ2hsUVI3RGtteDMrZ0dtakhzRUJNRUNjVXN4U3h5R2ZHTG9JR1VsUWoyOHZSWU5FNWZrbW11NWZLTWluY2ZLdnBLRERaVzZZVFVJOWkya2ZYa0g0VXgrYnhlVnF1ajE4dm1QNkxXVFAvQ2JWZ3FIVkh4WUdKT0FMa2VFOTVjRGJ1S243dnJkSk0ySGhGUjAzck54UUprVHdTUHh5NC9BS1BwbVFYakFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2lhX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfaWEuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ia_complete, file = "hometowns_ia.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIEtBTlNBUyBIT01FVE9XTlNcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc19rcyA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiS1NcIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX2tzIDwtIGZvb3RiYWxsX3Jvc3RlcnNfa3MgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# KANSAS HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ks <- football_rosters_usa %>%
  filter(hometown_state_clean == "KS")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ks <- football_rosters_ks %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfa3NfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJLU1wiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ks_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "KS",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzIwJyBmb3Igc3RhdGUgJ0tTJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '20' for state 'KS'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuXG5jZW5zdXNfZGF0YV9rc18yMDIxIDwtIGNlbnN1c19kYXRhX2tzXzIwMjEgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIHNlcGFyYXRlKG5hbWUsIGludG8gPSBjKFwiY2l0eVwiLCBcInN0YXRlXCIpLCBzZXAgPSBcIiwgXCIsIHJlbW92ZSA9IEZBTFNFKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBnc3ViKFwiXFxcXGIodG93bnxjaXR5fENEUHx2aWxsYWdlKVxcXFxiXCIsIFwiXCIsIGNpdHkpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBzdHJfc3F1aXNoKGNpdHkpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgYjAxMDAzXzAwMWUsIGIwMjAwMV8wMDNlLCBiMTkwMTNfMDAxZSkgJT4lXG4gIHJlbmFtZSh0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpXG5cbiMgU3RlcCA1OiBTdGF0ZS1zcGVjaWZpYyBjbGVhbmluZyBvZiBjZW5zdXMgZGF0YSB0byBwcmVwYXJlIGZvciBqb2luIHdpdGggaG9tZXRvd25zL3Jvc3RlciBkYXRhLiBUaGlzIHBhcnQgaXMgZGlmZmVyZW50IGZvciBldmVyeSBzdGF0ZS4gVGhlIGZpcnN0IG11dGF0ZSBmdW5jdGlvbiBzaG91bGQgYmUgaW5jbHVkZWQgZm9yIGV2ZXJ5IHN0YXRlLCBqdXN0IG1vZGlmaWVkIGRlcGVuZGluZyBvbiB0aGUgc3RhdGUgbmFtZS4gQWRkaXRpb25hbCBtdXRhdGUgZnVuY3Rpb25zIG1heSBiZSBuZWVkZWQgZm9yIGluc3RhbmNlcyB3aGVuIHRoZSBjZW5zdXMgbmFtZXMgc29tZXRoaW5nIGluIGEgd2VpcmQgd2F5IHRoYXQgZG9lc24ndCBsaW5lIHVwIHdpdGggdGhlIGhvbWV0b3ducy5cbmNlbnN1c19kYXRhX2tzXzIwMjEgPC0gY2Vuc3VzX2RhdGFfa3NfMjAyMSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gY2FzZV93aGVuKFxuICAgIHN0YXRlID09ICdLYW5zYXMnIH4gXCJLU1wiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX2tzX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19rcyAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2tzXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19rc19jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.

census_data_ks_2021 <- census_data_ks_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ks_2021 <- census_data_ks_2021 %>%
  mutate(state = case_when(
    state == 'Kansas' ~ "KS"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ks_complete <- distinct_hometowns_ks %>%
  left_join(census_data_ks_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ks_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjEsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMSDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsxXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE2VlJRVzdDTUJCMEFpa0ZLU2dTZklOSVZRL3RBNnBlZWl1dHhNMHlqZ3NXeG81c0k4cXBmVXRmMkJkQTE0bU5FbC9yZysyWkhlM083cjQrcmU0bnF3bENhSUNHYVlJR0dYeFI5djcydkhoRXdBQkkwQkNOM2ZzSm9obDhIQ2c2Z2R1bDVlTEloSWo0OUdVSmQ5NHdnSzVSeUhDQkErL1U0YTlmVjNMMDgzL2NzNXRSUVl5SkxFMHFZa241b2NtZVJmS3hWc2RTQW0rODUvUWJydFpuUDI4UUZjMG9XbksyVlh0bTFWRml5dTBKVThHSTlLSDVOV1Fzc2F3WHk2MnlST0Jha0JQVEpoVFlNTVdyWU1zclZCMkl0U0IwMXlIeVBhczRrWmhMQ29XQ3FxWVdOOHJnd3RmQU5kUFlidFhCRUZrQmY0NjZHNm5hY2lXaHY5U3RPb3ZtbCtpSUtBN1N6YU5hME8xQjdoWjNEMjdJZnN1b3MvMms4eCszTlljWG55dnp1VzZZM0hBWldzZ0VXVFBod1JTMjA4eTlyRFdYTm13VFdGTTJFd29NVlNJd1RYUG8vQWR6Tk95djRnSUFBQT09In0= -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Stilwell","2":"KS","3":"2","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[1]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuI0ZvciBTdGlsd2VsbCwgS1MsIHRoZSB6aXAgY29kZSBhcHBlYXJzIHRvIGJlIGEgZ29vZCBzdWJzdGl0dXRlOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTNjYwODUtNjYwODUvXG5jZW5zdXNfZGF0YV96aXBzX2tzXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcInpjdGFcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgZmlsdGVyKG5hbWUgPT0gXCJaQ1RBNSA2NjA4NVwiKSAlPiVcbiAgcmVuYW1lKGNpdHkgPSBuYW1lLCB0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpICU+JVxuICBtdXRhdGUoc3RhdGUgPSBcIktTXCIpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09IFwiWkNUQTUgNjYwODVcIiB+IFwiU3RpbHdlbGxcIikpJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

#For Stilwell, KS, the zip code appears to be a good substitute: https://censusreporter.org/profiles/86000US66085-66085/
census_data_zips_ks_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 66085") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "KS") %>%
  mutate(city = case_when(
    city == "ZCTA5 66085" ~ "Stilwell"))%>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfa3NfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfa3NfMjAyMSwgY2Vuc3VzX2RhdGFfemlwc19rc18yMDIxKVxuXG5ob21ldG93bnNfa3NfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX2tzICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfa3NfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG5ob21ldG93bnNfa3NfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpICNJZiB0aGlzIGlzIG5vdCBwcm9kdWNpbmcgYW4gZW1wdHkgZGF0YWZyYW1lLCBnbyBiYWNrIGFuZCBjb250aW51ZSB0byB3b3JrIG9uIE5BIHZhbHVlc1xuYGBgIn0= -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_ks_2021 <- bind_rows(census_data_ks_2021, census_data_zips_ks_2021)

hometowns_ks_complete <- distinct_hometowns_ks %>%
  left_join(census_data_ks_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_ks_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzVTdESUJUSDZWWTBiZEtseVh5Tk5qRmU2QU1ZSDhCb3NqdkNLSzVrRkFqUXpMMzhsRkp3bHF0eGN6aS9jM0wrNStQOWRmZFU3a29Bd0Jya3F3eXNvZnNDK1BueDFyd0FSNXlUZ1J3VWsvMTJTVnYzbVp3YXpDL2FLdkUzdDltRkFDUWNHeE9LUkZoMjJPTDJTK09CSnVtRmxxZFdPRzZ1K3N0Nk1WajdwbWU0N2VWQXJUd0pSSmc5SThJcEZpSDA4QmN5Rmx1NmlGVldXc3lSNHZoTXRZa0NCeXBaRjlzSkdWSkZzT2VZSFArQmFxQWR3d0l4UVp4UXpGTEVJcDhadXdnYVNGR05iQzlIZzBYbitDV1o3bDRxeTZSdzg2Mm1vOEJrYjVsT1FEMkthUjlkUS9wUkhKdkg1Mm01UG42OVlQb3ZaczM4SjlTQ29kWWRGUWNtNGdpUTR6M2x3ZG00cS9pOXQwb3pZZU1WSFRXdDMxQWtSUEpJL0hEZzhndXRoRHAwakFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2tzX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfa3MuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ks_complete, file = "hometowns_ks.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIEtFTlRVQ0tZIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX2t5IDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJLWVwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfa3kgPC0gZm9vdGJhbGxfcm9zdGVyc19reSAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# KENTUCKY HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ky <- football_rosters_usa %>%
  filter(hometown_state_clean == "KY")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ky <- football_rosters_ky %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfa3lfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJLWVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ky_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "KY",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzIxJyBmb3Igc3RhdGUgJ0tZJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '21' for state 'KY'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfa3lfMjAyMSA8LSBjZW5zdXNfZGF0YV9reV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9reV8yMDIxIDwtIGNlbnN1c19kYXRhX2t5XzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnS2VudHVja3knIH4gXCJLWVwiKSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gJ0xvdWlzdmlsbGUvSmVmZmVyc29uIENvdW50eSBtZXRybyBnb3Zlcm5tZW50IChiYWxhbmNlKScgfiAnTG91aXN2aWxsZScsXG4gICAgY2l0eSA9PSAnTGV4aW5ndG9uLUZheWV0dGUgdXJiYW4gY291bnR5JyB+ICdMZXhpbmd0b24nLFxuICAgIFRSVUUgfiBjaXR5KSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX2t5X2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19reSAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2t5XzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19reV9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ky_2021 <- census_data_ky_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ky_2021 <- census_data_ky_2021 %>%
  mutate(state = case_when(
    state == 'Kentucky' ~ "KY")) %>%
  mutate(city = case_when(
    city == 'Louisville/Jefferson County metro government (balance)' ~ 'Louisville',
    city == 'Lexington-Fayette urban county' ~ 'Lexington',
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ky_complete <- distinct_hometowns_ky %>%
  left_join(census_data_ky_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ky_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzV3JESUJUSFRSczNFa2dKZEsrUndOaE5IMkRzQWNZR3ZSTnJYQ00xS21ybyt2TGRqTkYxOGFyZUhNL3ZITTcvZkx5LzdsL0tmUWtBV0lOOGxZRTFkRjhBUHovZW1oMXd4RGtaeUVFeDJXK1h0SFdmeWFuQi9LS3RFbjl6bjEwSVFNS3hNYUZJaEdXSExXNi9OQjVva2w1b2VXNkY0K2FtdjZ3WGc3VnZlb2JiWGc3VXlyTkFoTmtMSXB4aUVVSlBmeUZqc2FXTFdHV2x4Undwamk5VW15aHdwSkoxc1oyUUlWVUVCNDdKNlIrb0J0b3hMQkFUeEFuRkxFVXM4cG14aTZDQkZOWEk5bkkwV0hTT1g1UHBIcVd5VEFvMzMybzZDa3oybHVrRTFLT1k5dEUxcEIvRnFYbmVUY3YxOGRzRjAzOHhhK1kvb1JZTXRSNm9PRElSUjRBY0h5Z1B6c1pkeGUrOVZab0pHNi9vcUduOWhpSWhra2ZpaHdQWFg1Qnh3aXVNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMgTm90IG5lZWRlZCBmb3IgS2VudHVja3lcblxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuIyBOb3QgbmVlZGVkIGZvciBLZW50dWNreVxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2t5X2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfa3kuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
# Not needed for Kentucky

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
# Not needed for Kentucky

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ky_complete, file = "hometowns_ky.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIExPVUlTSUFOQSBIT01FVE9XTlNcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc19sYSA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiTEFcIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX2xhIDwtIGZvb3RiYWxsX3Jvc3RlcnNfbGEgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# LOUISIANA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_la <- football_rosters_usa %>%
  filter(hometown_state_clean == "LA")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_la <- football_rosters_la %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfbGFfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJMQVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_la_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "LA",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzIyJyBmb3Igc3RhdGUgJ0xBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '22' for state 'LA'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfbGFfMjAyMSA8LSBjZW5zdXNfZGF0YV9sYV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9sYV8yMDIxIDwtIGNlbnN1c19kYXRhX2xhXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnTG91aXNpYW5hJyB+IFwiTEFcIikpXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cbmhvbWV0b3duc19sYV9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfbGEgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9sYV8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbiMgU3RlcCA3OiBOb3RpY2UgdGhlcmUgYXJlIGEgZmV3IE5BIHZhbHVlcy4gVGhpcyBoYXBwZW5zIHdoZW4gdGhlIGNlbnN1cyBkYXRhIGRvZXMgbm90IGpvaW4gd2l0aCB0aGUgaG9tZXRvd25zIGRhdGEsIHBlcmhhcHMgYmVjYXVzZSB0aGUgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCBvciBiZWNhdXNlIHRoZXJlIGlzIG5vIGNlbnN1cyBkYXRhIGZvciB0aGF0IHRvd24uIEZpcnN0LCBsZXQncyBmaW5kIHRoZSBOQSB2YWx1ZXMuXG5ob21ldG93bnNfbGFfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpXG5gYGAifQ== -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_la_2021 <- census_data_la_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_la_2021 <- census_data_la_2021 %>%
  mutate(state = case_when(
    state == 'Louisiana' ~ "LA"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_la_complete <- distinct_hometowns_la %>%
  left_join(census_data_la_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_la_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjMsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMyDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFszXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE4VlNTMDdETUJCMTBvYVFTSzBpbFFOd2dVWkNiR0JaQ2NHR0ZUOTFGMDBkMDFoMTdNaDJWYnFDczNCQ0xrQ0xuZHFGUnQwVHlabVpOODhlei9NODNFd3YwMm1LRU9xaGZoaWdYbVJjRkQwLzNZNnZrRUZNRUtBK1NxeDlNNlNSY1d5UTdYYTBmbnhIcUtwQnVqQjUxUG41cEFhdUhYRDZBcmdpa3BMT3Z2QitjdFJEYU5DeWJPbmZsVGtzMlpydmlCM2EvUHVYdlg3ODJiWC9ueitRTXNJTWxISk5lVEF0UVVQK0txRW1IWG9peFNybkJsZE9tL0REL0V6YjM5MXpQU2xybjJrSGppcFJFeTFXdk1CVXJ3dk1DSENYT3R1bmxBWk5EbklETFRTd29tR3dKbEw1QW5NaWFPbXY1UmlpOGNDTUFWNzhBUVkxS1Nud2duSnNDbmxXZzNYUk12MHRYSTJpSWJMUWxWZ3E0S1hCTjUzdVl0Rm9LcmpwTDdSakdIWDBDMlFIeUpiYzZsR09jYlhraS9IRnRSWFpUUk55U2dadXFyeWY3R3IydCs2c3lKMTFRdmljY3Q5Q3hHQkdtQXVHNW5WYTNmTkcwdjNRcHdaVmVhdVFSN0JnSG1tYlE1c2ZOd0N0RDM0REFBQT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Geismar","2":"LA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"St. Amant","2":"LA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Vacherie","2":"LA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[3]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgR2Vpc21hciwgTEEgKDcwNzM0KSwgU3QuIEFtYW50LCBMQSAoNzA3NzQpLCBhbmQgVmFjaGVyaWUsIExBICg3MDA5MCksIHRoZSB6aXAgY29kZXMgc2VlbXMgdG8gYmUgZ29vZCBzdWJzdGl0dXRlczogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvODYwMDBVUzcwNzM0LTcwNzM0LyBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTNzA3NzQtNzA3NzQvIGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVM3MDA5MC03MDA5MC9cbmNlbnN1c19kYXRhX3ppcHNfbGFfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiemN0YVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIlpDVEE1IDcwNzM0XCIgfCBuYW1lID09IFwiWkNUQTUgNzA3NzRcIiB8IG5hbWUgPT0gXCJaQ1RBNSA3MDA5MFwiKSAlPiVcbiAgcmVuYW1lKGNpdHkgPSBuYW1lLCB0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpICU+JVxuICBtdXRhdGUoc3RhdGUgPSBcIkxBXCIpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09IFwiWkNUQTUgNzA3MzRcIiB+IFwiR2Vpc21hclwiLFxuICAgIGNpdHkgPT0gXCJaQ1RBNSA3MDc3NFwiIH4gXCJTdC4gQW1hbnRcIixcbiAgICBjaXR5ID09IFwiWkNUQTUgNzAwOTBcIiB+IFwiVmFjaGVyaWVcIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Geismar, LA (70734), St. Amant, LA (70774), and Vacherie, LA (70090), the zip codes seems to be good substitutes: https://censusreporter.org/profiles/86000US70734-70734/ https://censusreporter.org/profiles/86000US70774-70774/ https://censusreporter.org/profiles/86000US70090-70090/
census_data_zips_la_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 70734" | name == "ZCTA5 70774" | name == "ZCTA5 70090") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "LA") %>%
  mutate(city = case_when(
    city == "ZCTA5 70734" ~ "Geismar",
    city == "ZCTA5 70774" ~ "St. Amant",
    city == "ZCTA5 70090" ~ "Vacherie")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfbGFfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfbGFfMjAyMSwgY2Vuc3VzX2RhdGFfemlwc19sYV8yMDIxKVxuIFxuaG9tZXRvd25zX2xhX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19sYSAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX2xhXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuaG9tZXRvd25zX2xhX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKSAjSWYgdGhpcyBpcyBub3QgcHJvZHVjaW5nIGFuIGVtcHR5IGRhdGFmcmFtZSwgZ28gYmFjayBhbmQgY29udGludWUgdG8gd29yayBvbiBOQSB2YWx1ZXNcbmBgYCJ9 -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_la_2021 <- bind_rows(census_data_la_2021, census_data_zips_la_2021)
 
hometowns_la_complete <- distinct_hometowns_la %>%
  left_join(census_data_la_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_la_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzVTdESUJUSDZWWTBiZEtseVh5Tk5qSGU2TDN4QVl3bXV5T000a3BHZ1FETjNNdFBLUVZudVJvM2gvTTdKK2QvUHQ1ZmQwL2xyZ1FBckVHK3lzQWF1aStBbng5dnpUTnd4RGtaeUVFeDJXK1h0SFdmeWFuQi9LS3RFbjl6bTEwSVFNS3hNYUZJaEdXSExXNi9OQjVva2w1b2VXcUY0K2FxdjZ3WGc3VnZlb2JiWGc3VXlwTkFoTmt6SXB4aUVVSVBmeUZqc2FXTFdHV2x4UndwanM5VW15aHdvSkoxc1oyUUlWVUVlNDdKOFIrb0J0b3hMQkFUeEFuRkxFVXM4cG14aTZDQkZOWEk5bkkwV0hTT1g1THA3cVd5VEFvMzMybzZDa3oybHVrRTFLT1k5dEUxcEIvRnNYbDhtWmJyNDljTHB2OWkxc3gvUWkwWWF0MVJjV0FpamdBNTNsTWVuSTI3aXQ5N3F6UVRObDdSVWRQNkRVVkNKSS9FRHdjdXY3SlRuRWlNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX2xhX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfbGEuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_la_complete, file = "hometowns_la.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgQ2xhcmtzdmlsbGUsIE1EICgyMTAyOSksIERhdmlkc29udmlsbGUsIE1EICgyMTAzNSksIElqYW1zdmlsbGUsIE1EICgyMTc3MCksIFBob2VuaXgsIE1EICgyMTEzMSkgdGhlIHppcCBjb2RlcyBzZWVtIHRvIGJlIGdvb2Qgc3Vic3RpdHV0ZXM6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMyMTAyOS0yMTAyOS8gaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvODYwMDBVUzIxMDM1LTIxMDM1LyBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTMjE3NzAtMjE3NzAvIGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMyMTEzMS0yMTEzMS9cbmNlbnN1c19kYXRhX3ppcHNfbWRfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiemN0YVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIlpDVEE1IDIxMDI5XCIgfCBuYW1lID09IFwiWkNUQTUgMjEwMzVcIiB8IG5hbWUgPT0gXCJaQ1RBNSAyMTc3MFwiIHwgbmFtZSA9PSBcIlpDVEE1IDIxMTMxXCIpICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiTURcIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJaQ1RBNSAyMTAyOVwiIH4gXCJDbGFya3N2aWxsZVwiLFxuICAgIGNpdHkgPT0gXCJaQ1RBNSAyMTAzNVwiIH4gXCJEYXZpZHNvbnZpbGxlXCIsXG4gICAgY2l0eSA9PSBcIlpDVEE1IDIxNzcwXCIgfiBcIklqYW1zdmlsbGVcIixcbiAgICBjaXR5ID09IFwiWkNUQTUgMjExMzFcIiB+IFwiUGhvZW5peFwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5cbmBgYCJ9 -->

```r
# For Clarksville, MD (21029), Davidsonville, MD (21035), Ijamsville, MD (21770), Phoenix, MD (21131) the zip codes seem to be good substitutes: https://censusreporter.org/profiles/86000US21029-21029/ https://censusreporter.org/profiles/86000US21035-21035/ https://censusreporter.org/profiles/86000US21770-21770/ https://censusreporter.org/profiles/86000US21131-21131/
census_data_zips_md_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 21029" | name == "ZCTA5 21035" | name == "ZCTA5 21770" | name == "ZCTA5 21131") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "MD") %>%
  mutate(city = case_when(
    city == "ZCTA5 21029" ~ "Clarksville",
    city == "ZCTA5 21035" ~ "Davidsonville",
    city == "ZCTA5 21770" ~ "Ijamsville",
    city == "ZCTA5 21131" ~ "Phoenix")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)

```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBJdCB0dXJucyBvdXQgdGhhdCBtYW55IHRvd25zIGluIE1hc3NhY2h1c2V0dHMgYXJlIGNvdW50eSBzdWJkaXZpc2lvbnMsIHNvIHdlIHdpbGwgZ3JhYiBzb21lIG9mIHRob3NlIHdlIG5lZWQsIHRvb1xuY2Vuc3VzX2RhdGFfbWFfc3ViZGl2aXNpb25zXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcImNvdW50eSBzdWJkaXZpc2lvblwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RhdGUgPSBcIk1BXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGZpbHRlcihOQU1FID09IFwiQWN0b24gdG93biwgTWlkZGxlc2V4IENvdW50eSwgTWFzc2FjaHVzZXR0c1wiIHwgTkFNRSA9PSBcIkNhbnRvbiB0b3duLCBOb3Jmb2xrIENvdW50eSwgTWFzc2FjaHVzZXR0c1wiIHwgTkFNRSA9PSBcIkNvbmNvcmQgdG93biwgTWlkZGxlc2V4IENvdW50eSwgTWFzc2FjaHVzZXR0c1wiIHwgIE5BTUUgPT0gXCJIb2xsaXN0b24gdG93biwgTWlkZGxlc2V4IENvdW50eSwgTWFzc2FjaHVzZXR0c1wiIHwgTkFNRSA9PSBcIk1hbnNmaWVsZCB0b3duLCBCcmlzdG9sIENvdW50eSwgTWFzc2FjaHVzZXR0c1wiIHwgTkFNRSA9PSBcIk5ld2J1cnkgdG93biwgRXNzZXggQ291bnR5LCBNYXNzYWNodXNldHRzXCIgfCBOQU1FID09IFwiTm9ydGggQW5kb3ZlciB0b3duLCBFc3NleCBDb3VudHksIE1hc3NhY2h1c2V0dHNcIiB8IE5BTUUgPT0gXCJOb3J3ZWxsIHRvd24sIFBseW1vdXRoIENvdW50eSwgTWFzc2FjaHVzZXR0c1wiIHwgTkFNRSA9PSBcIlBheHRvbiB0b3duLCBXb3JjZXN0ZXIgQ291bnR5LCBNYXNzYWNodXNldHRzXCIgfCBOQU1FID09IFwiUmF5bmhhbSB0b3duLCBCcmlzdG9sIENvdW50eSwgTWFzc2FjaHVzZXR0c1wiIHwgTkFNRSA9PSBcIlN1ZGJ1cnkgdG93biwgTWlkZGxlc2V4IENvdW50eSwgTWFzc2FjaHVzZXR0c1wiIHwgTkFNRSA9PSBcIldlc3Rib3JvdWdoIHRvd24sIFdvcmNlc3RlciBDb3VudHksIE1hc3NhY2h1c2V0dHNcIilcblxuYGBgIn0= -->

```r
# It turns out that many towns in Massachusetts are county subdivisions, so we will grab some of those we need, too
census_data_ma_subdivisions_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "MA",
                           output = "wide") %>%
  filter(NAME == "Acton town, Middlesex County, Massachusetts" | NAME == "Canton town, Norfolk County, Massachusetts" | NAME == "Concord town, Middlesex County, Massachusetts" |  NAME == "Holliston town, Middlesex County, Massachusetts" | NAME == "Mansfield town, Bristol County, Massachusetts" | NAME == "Newbury town, Essex County, Massachusetts" | NAME == "North Andover town, Essex County, Massachusetts" | NAME == "Norwell town, Plymouth County, Massachusetts" | NAME == "Paxton town, Worcester County, Massachusetts" | NAME == "Raynham town, Bristol County, Massachusetts" | NAME == "Sudbury town, Middlesex County, Massachusetts" | NAME == "Westborough town, Worcester County, Massachusetts")

```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzI1JyBmb3Igc3RhdGUgJ01BJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '25' for state 'MA'
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE1JQ0hJR0FOIEhPTUVUT1dOUyAobm90IHRoZSBiZXN0IHRvIHVzZSBhcyBhIHRlbXBsYXRlKVxuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX21pIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJNSVwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfbWkgPC0gZm9vdGJhbGxfcm9zdGVyc19taSAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# MICHIGAN HOMETOWNS (not the best to use as a template)

# Step 1: Filter for the state's players
football_rosters_mi <- football_rosters_usa %>%
  filter(hometown_state_clean == "MI")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_mi <- football_rosters_mi %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfbWlfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJNSVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_mi_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "MI",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzI2JyBmb3Igc3RhdGUgJ01JJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '26' for state 'MI'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBJdCB0dXJucyBvdXQgdGhhdCBtYW55IHRvd25zIGluIE1pY2hpZ2FuIGFyZSBjb3VudHkgc3ViZGl2aXNpb25zLCBzbyB3ZSB3aWxsIGdyYWIgc29tZSBvZiB0aG9zZSB3ZSBuZWVkLCB0b29cbmNlbnN1c19kYXRhX21pX3N1YmRpdmlzaW9uc18yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJjb3VudHkgc3ViZGl2aXNpb25cIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJNSVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBmaWx0ZXIoTkFNRSA9PSBcIkFkYSB0b3duc2hpcCwgS2VudCBDb3VudHksIE1pY2hpZ2FuXCIgfCBOQU1FID09IFwiQnJvd25zdG93biBjaGFydGVyIHRvd25zaGlwLCBXYXluZSBDb3VudHksIE1pY2hpZ2FuXCIgfCBOQU1FID09IFwiQ2FudG9uIGNoYXJ0ZXIgdG93bnNoaXAsIFdheW5lIENvdW50eSwgTWljaGlnYW5cIiB8IE5BTUUgPT0gXCJDbGludG9uIGNoYXJ0ZXIgdG93bnNoaXAsIE1hY29tYiBDb3VudHksIE1pY2hpZ2FuXCIgfCBOQU1FID09IFwiTWFjb21iIHRvd25zaGlwLCBNYWNvbWIgQ291bnR5LCBNaWNoaWdhblwiIHwgTkFNRSA9PSBcIlJlZGZvcmQgY2hhcnRlciB0b3duc2hpcCwgV2F5bmUgQ291bnR5LCBNaWNoaWdhblwiIHwgTkFNRSA9PSBcIldhc2hpbmd0b24gY2hhcnRlciB0b3duc2hpcCwgTWFjb21iIENvdW50eSwgTWljaGlnYW5cIiB8IE5BTUUgPT0gXCJXZXN0IEJsb29tZmllbGQgY2hhcnRlciB0b3duc2hpcCwgT2FrbGFuZCBDb3VudHksIE1pY2hpZ2FuXCIpXG5gYGAifQ== -->

```r
# It turns out that many towns in Michigan are county subdivisions, so we will grab some of those we need, too
census_data_mi_subdivisions_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "MI",
                           output = "wide") %>%
  filter(NAME == "Ada township, Kent County, Michigan" | NAME == "Brownstown charter township, Wayne County, Michigan" | NAME == "Canton charter township, Wayne County, Michigan" | NAME == "Clinton charter township, Macomb County, Michigan" | NAME == "Macomb township, Macomb County, Michigan" | NAME == "Redford charter township, Wayne County, Michigan" | NAME == "Washington charter township, Macomb County, Michigan" | NAME == "West Bloomfield charter township, Oakland County, Michigan")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzI2JyBmb3Igc3RhdGUgJ01JJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '26' for state 'MI'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfbWlfMjAyMSA8LSBjZW5zdXNfZGF0YV9taV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG5jZW5zdXNfZGF0YV9taV9zdWJkaXZpc2lvbnNfMjAyMSA8LSBjZW5zdXNfZGF0YV9taV9zdWJkaXZpc2lvbnNfMjAyMSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgc2VwYXJhdGUobmFtZSwgaW50byA9IGMoXCJjaXR5XCIsIFwiY291bnR5XCIsIFwic3RhdGVcIiksIHNlcCA9IFwiLCBcIiwgcmVtb3ZlID0gRkFMU0UpICU+JVxuICBtdXRhdGUoY2l0eSA9IGdzdWIoXCJcXFxcYih0b3dufGNpdHl8Q0RQfHZpbGxhZ2V8bXVuaWNpcGFsaXR5fHRvd25zaGlwfGJvcm91Z2h8Y2hhcnRlcilcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG5jZW5zdXNfZGF0YV9taV8yMDIxIDwtIGJpbmRfcm93cyhjZW5zdXNfZGF0YV9taV8yMDIxLCBjZW5zdXNfZGF0YV9taV9zdWJkaXZpc2lvbnNfMjAyMSlcblxuIyBTdGVwIDU6IFN0YXRlLXNwZWNpZmljIGNsZWFuaW5nIG9mIGNlbnN1cyBkYXRhIHRvIHByZXBhcmUgZm9yIGpvaW4gd2l0aCBob21ldG93bnMvcm9zdGVyIGRhdGEuIFRoaXMgcGFydCBpcyBkaWZmZXJlbnQgZm9yIGV2ZXJ5IHN0YXRlLiBUaGUgZmlyc3QgbXV0YXRlIGZ1bmN0aW9uIHNob3VsZCBiZSBpbmNsdWRlZCBmb3IgZXZlcnkgc3RhdGUsIGp1c3QgbW9kaWZpZWQgZGVwZW5kaW5nIG9uIHRoZSBzdGF0ZSBuYW1lLiBBZGRpdGlvbmFsIG11dGF0ZSBmdW5jdGlvbnMgbWF5IGJlIG5lZWRlZCBmb3IgaW5zdGFuY2VzIHdoZW4gdGhlIGNlbnN1cyBuYW1lcyBzb21ldGhpbmcgaW4gYSB3ZWlyZCB3YXkgdGhhdCBkb2Vzbid0IGxpbmUgdXAgd2l0aCB0aGUgaG9tZXRvd25zLlxuY2Vuc3VzX2RhdGFfbWlfMjAyMSA8LSBjZW5zdXNfZGF0YV9taV8yMDIxICU+JVxuICBtdXRhdGUoc3RhdGUgPSBjYXNlX3doZW4oXG4gICAgc3RhdGUgPT0gJ01pY2hpZ2FuJyB+IFwiTUlcIikpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09ICdCcm93bnN0b3duJyB+IFwiQnJvd25zdG93biBDaGFydGVyIFRvd25zaGlwXCIsXG4gICAgY2l0eSA9PSAnVmlsbGFnZSBvZiBDbGFya3N0b24nIH4gXCJDbGFya3N0b25cIixcbiAgICBjaXR5ID09ICdNYWNvbWInIH4gXCJNYWNvbWIgVG93bnNoaXBcIixcbiAgICBnZW9pZCA9PSAnMjYwOTkxNjUyMCcgfiBcIkNsaW50b24gVG93bnNoaXBcIixcbiAgICBUUlVFIH4gY2l0eSkpXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cbmhvbWV0b3duc19taV9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfbWkgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9taV8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbiMgU3RlcCA3OiBOb3RpY2UgdGhlcmUgYXJlIGEgZmV3IE5BIHZhbHVlcy4gVGhpcyBoYXBwZW5zIHdoZW4gdGhlIGNlbnN1cyBkYXRhIGRvZXMgbm90IGpvaW4gd2l0aCB0aGUgaG9tZXRvd25zIGRhdGEsIHBlcmhhcHMgYmVjYXVzZSB0aGUgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCBvciBiZWNhdXNlIHRoZXJlIGlzIG5vIGNlbnN1cyBkYXRhIGZvciB0aGF0IHRvd24uIEZpcnN0LCBsZXQncyBmaW5kIHRoZSBOQSB2YWx1ZXMuXG5ob21ldG93bnNfbWlfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpXG5gYGAifQ== -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_mi_2021 <- census_data_mi_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_mi_subdivisions_2021 <- census_data_mi_subdivisions_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "county", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|municipality|township|borough|charter)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_mi_2021 <- bind_rows(census_data_mi_2021, census_data_mi_subdivisions_2021)

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_mi_2021 <- census_data_mi_2021 %>%
  mutate(state = case_when(
    state == 'Michigan' ~ "MI")) %>%
  mutate(city = case_when(
    city == 'Brownstown' ~ "Brownstown Charter Township",
    city == 'Village of Clarkston' ~ "Clarkston",
    city == 'Macomb' ~ "Macomb Township",
    geoid == '2609916520' ~ "Clinton Township",
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_mi_complete <- distinct_hometowns_mi %>%
  left_join(census_data_mi_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_mi_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFVzY2UUdxSHFCcXBld1F3VFJHd1lBQUs4M2wwMklNVGMwcWJJYjVaalQvUE41Zjk4L2x2Z1FBckVHK3lzQWF1aStBbng5dnpRdHd4RGtaeUVFeDJXK1h0SFdmeWFuQi9LS3RFbjl6bjEwSVFNS3hNYUZJaEdXSExXNi9OQjVva2w1b2VXNkY0K2FtdjZ3WGc3VnZlb2JiWGc3VXlyTkFoTmtMSXB4aUVVSlBmeUZqc2FXTFdHV2x4Undwamk5VW15aHdwSkoxc1oyUUlWVUVCNDdKNlIrb0J0b3hMQkFUeEFuRkxFVXM4cG14aTZDQkZOWEk5bkkwV0hTT1g1UHBIcVd5VEFvMzMybzZDa3oybHVrRTFLT1k5dEUxcEIvRnFkbnRwdVg2K08yQzZiK1lOZk9mVUF1R1dnOVVISm1JSTBDT0Q1UUhaK091NHZmZUtzMkVqVmQwMUxSK1E1RVF5U1B4dzRIckwwME9HZVdNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMgTm90IGFwcGxpY2FibGUgZm9yIE1pY2hpZ2FuXG5cbiMgU3RlcCA5OiBXZSBub3cgaGF2ZSB0byBhcHBlbmQgdGhlc2Ugc3BlY2lhbCBjYXNlcyB0byBvdXIgc3RhdGUgY2Vuc3VzIGRhdGEsIHJlZG8gdGhlIGpvaW4sIGFuZCBydW4gb25lIG1vcmUgY2hlY2sgZm9yIE5BIHZhbHVlcy5cbiMgTm90IGFwcGxpY2FibGUgZm9yIE1pY2hpZ2FuXG5cbiMgU3RlcCAxMDogSWYgbmVlZGVkLCB1bmNvbW1lbnQgb3V0IHRvIGNyZWF0ZSBhIENTVlxuI3dyaXRlX2Nzdihob21ldG93bnNfbWlfY29tcGxldGUsIGZpbGUgPSBcImhvbWV0b3duc19taS5jc3ZcIilcblxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
# Not applicable for Michigan

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
# Not applicable for Michigan

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_mi_complete, file = "hometowns_mi.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE1JTk5FU09UQSBIT01FVE9XTlNcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc19tbiA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiTU5cIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX21uIDwtIGZvb3RiYWxsX3Jvc3RlcnNfbW4gJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# MINNESOTA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_mn <- football_rosters_usa %>%
  filter(hometown_state_clean == "MN")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_mn <- football_rosters_mn %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfbW5fMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJNTlwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_mn_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "MN",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzI3JyBmb3Igc3RhdGUgJ01OJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '27' for state 'MN'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfbW5fMjAyMSA8LSBjZW5zdXNfZGF0YV9tbl8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9tbl8yMDIxIDwtIGNlbnN1c19kYXRhX21uXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnTWlubmVzb3RhJyB+IFwiTU5cIikpXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cbmhvbWV0b3duc19tbl9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfbW4gJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9tbl8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbiMgU3RlcCA3OiBOb3RpY2UgdGhlcmUgYXJlIGEgZmV3IE5BIHZhbHVlcy4gVGhpcyBoYXBwZW5zIHdoZW4gdGhlIGNlbnN1cyBkYXRhIGRvZXMgbm90IGpvaW4gd2l0aCB0aGUgaG9tZXRvd25zIGRhdGEsIHBlcmhhcHMgYmVjYXVzZSB0aGUgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCBvciBiZWNhdXNlIHRoZXJlIGlzIG5vIGNlbnN1cyBkYXRhIGZvciB0aGF0IHRvd24uIEZpcnN0LCBsZXQncyBmaW5kIHRoZSBOQSB2YWx1ZXMuXG5ob21ldG93bnNfbW5fY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpXG5gYGAifQ== -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_mn_2021 <- census_data_mn_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_mn_2021 <- census_data_mn_2021 %>%
  mutate(state = case_when(
    state == 'Minnesota' ~ "MN"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_mn_complete <- distinct_hometowns_mn %>%
  left_join(census_data_mn_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_mn_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFV3o2UUdxSHFCcXBld1F3VFJHd1lBQUs4M2wwMklNVGMwcWJJYjVaalQvUE41Zjk3dHlYd0lBMWlCZlpXQU4zUmZBejQrMzVnVTQ0cHdNNUtDWTdMZEwycnJQNU5SZ2Z0RldpYis1enk0RUlPSFltRkFrd3JMREZyZGZHZzgwU1MrMFBMZkNjWFBUWDlhTHdkbzNQY050THdkcTVWa2d3dXdGRVU2eENLR252NUN4Mk5KRnJMTFNZbzRVeHhlcVRSUTRVc202MkU3SWtDcUNBOGZrOUE5VUErMFlGb2dKNG9SaWxpSVcrY3pZUmRCQWltcGtlemthTERySHI4bDBqMUpaSm9XYmJ6VWRCU1o3eTNRQzZsRk0rK2dhMG8vaTFEenZwdVg2K08yQzZiK1lOZk9mVUF1R1dnOVVISm1JSTBDT0Q1UUhaK091NHZmZUtzMkVqVmQwMUxSK1E1RVF5U1B4dzRIckwyOHNSNGFNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMjIE5vdCBuZWVkZWQgZm9yIE1pbm5lb3N0YVxuXG4jIFN0ZXAgOTogV2Ugbm93IGhhdmUgdG8gYXBwZW5kIHRoZXNlIHNwZWNpYWwgY2FzZXMgdG8gb3VyIHN0YXRlIGNlbnN1cyBkYXRhLCByZWRvIHRoZSBqb2luLCBhbmQgcnVuIG9uZSBtb3JlIGNoZWNrIGZvciBOQSB2YWx1ZXMuXG5cbiMgU3RlcCAxMDogSWYgbmVlZGVkLCB1bmNvbW1lbnQgb3V0IHRvIGNyZWF0ZSBhIENTVlxuI3dyaXRlX2Nzdihob21ldG93bnNfbW5fY29tcGxldGUsIGZpbGUgPSBcImhvbWV0b3duc19tbi5jc3ZcIilcblxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
## Not needed for Minneosta

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_mn_complete, file = "hometowns_mn.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE1JU1NJU1NJUFBJIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX21zIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJNU1wiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfbXMgPC0gZm9vdGJhbGxfcm9zdGVyc19tcyAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# MISSISSIPPI HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ms <- football_rosters_usa %>%
  filter(hometown_state_clean == "MS")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ms <- football_rosters_ms %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfbXNfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJNU1wiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ms_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "MS",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzI4JyBmb3Igc3RhdGUgJ01TJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '28' for state 'MS'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfbXNfMjAyMSA8LSBjZW5zdXNfZGF0YV9tc18yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9tc18yMDIxIDwtIGNlbnN1c19kYXRhX21zXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnTWlzc2lzc2lwcGknIH4gXCJNU1wiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX21zX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19tcyAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX21zXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19tc19jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ms_2021 <- census_data_ms_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ms_2021 <- census_data_ms_2021 %>%
  mutate(state = case_when(
    state == 'Mississippi' ~ "MS"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ms_complete <- distinct_hometowns_ms %>%
  left_join(census_data_ms_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ms_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjIsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMiDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsyXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE3VlN6VzdDTUF4T0N4MXFKUmdTZXcxNjJXRjdnSW5iZHRpUHhDMEthVVlqUWxJbFFZelQ5aXg3d2owQnpHbmpDWHBmcGRUMjUwK3gvY1hQRDh2Yllsa1FRZ1prbUNaa2tJRkxzcmZYeGZ5ZUFBSkJRb1lrRC9ZRFNETndRakNGazhaRXNiQlM2TXJWc29uSTFaTndLK2w3dlBUeDVjd2paTnptUW9IdVRHT2NuK0E3czVPQWYvNkV4a2JmYVA4ZnZ4Zys0NG81RjV0RXNLaVlaK1c3WlZ2Um8rZlc3RXNOdU1NNXYrQUg0eHo3OXlKcDJncmJnYlBhYklVM2UwMjU5QWZLbFdBNnBtNytVczR6THk1eVkyODhVN1JSN0NDc3d3SnJZV1NGYlVXR3dZZktWNHJ4elJrdzNvcEtNazJsNWxBSVdRMzN0R1ZpRjdFR2JZU2x2alk3eDNRRmVIKzZrV204TkJybVM4UGlaRDM5RXRzRHJuYzY2RkhOZWIzVG0vbGQwRGd1QjRsQ0puRkowTSs3a3NOVHZDckRGUlI2TFRWT2tDbTJFaW9HRTNpY1Z2YXlzVko3ZkV4QVhka0toQWczQ3BGMk5uTDhCVTh2TE9JdkF3QUEifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Friendship","2":"MS","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Nesbit","2":"MS","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[2]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgTmVzYml0LCBNUywgdGhlIHppcCBjb2RlICgzODY1MSkgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMzODY1MS0zODY1MS9cbmNlbnN1c19kYXRhX25lc2JpdF9tc18yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgMzg2NTFcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJNU1wiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDM4NjUxXCIgfiBcIk5lc2JpdFwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Nesbit, MS, the zip code (38651) seems to be a good substitute: https://censusreporter.org/profiles/86000US38651-38651/
census_data_nesbit_ms_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 38651") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "MS") %>%
  mutate(city = case_when(
    city == "ZCTA5 38651" ~ "Nesbit")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgRnJpZW5kc2hpcCwgTVMgZGF0YSBvYnRhaW5lZCB1c2luZyBwb3B1bGF0aW9uIG9mIG5lYXJieSBDb2xsaW5zLCBNUywgd2hlcmUgdGhlIHBsYXllciB3ZW50IHRvIEhTIGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzE2MDAwVVMyODE1MTQwLWNvbGxpbnMtbXMvXG5jZW5zdXNfZGF0YV9mcmllbmRzaGlwX21zXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcInBsYWNlXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBzdGF0ZSA9IFwiTVNcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgZmlsdGVyKG5hbWUgPT0gXCJDb2xsaW5zIGNpdHksIE1pc3Npc3NpcHBpXCIpICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiTVNcIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJDb2xsaW5zIGNpdHksIE1pc3Npc3NpcHBpXCIgfiBcIkZyaWVuZHNoaXBcIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r
# For Friendship, MS data obtained using population of nearby Collins, MS, where the player went to HS https://censusreporter.org/profiles/16000US2815140-collins-ms/
census_data_friendship_ms_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "MS",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Collins city, Mississippi") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "MS") %>%
  mutate(city = case_when(
    city == "Collins city, Mississippi" ~ "Friendship")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzI4JyBmb3Igc3RhdGUgJ01TJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '28' for state 'MS'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfbXNfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfbXNfMjAyMSwgY2Vuc3VzX2RhdGFfbmVzYml0X21zXzIwMjEsIGNlbnN1c19kYXRhX2ZyaWVuZHNoaXBfbXNfMjAyMSlcbiBcbmhvbWV0b3duc19tc19jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfbXMgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9tc18yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbmhvbWV0b3duc19tc19jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSkgI0lmIHRoaXMgaXMgbm90IHByb2R1Y2luZyBhbiBlbXB0eSBkYXRhZnJhbWUsIGdvIGJhY2sgYW5kIGNvbnRpbnVlIHRvIHdvcmsgb24gTkEgdmFsdWVzXG5gYGAifQ== -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_ms_2021 <- bind_rows(census_data_ms_2021, census_data_nesbit_ms_2021, census_data_friendship_ms_2021)
 
hometowns_ms_complete <- distinct_hometowns_ms %>%
  left_join(census_data_ms_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_ms_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWkxUU09rMTdFMFg3UUdxSHFCcXBld1F3VFJHd1lBQUs4M2wwMktiYVJwV1lUUE1ONlA1NS9IK3VuMHF0eVZDYUlueVJZYVdPSHdSL3Z4NHExOVFJTUhKVUk2SzBYNkhwRTM0ak00YXpROXNsZmlyMit5VkFHYVNPaGVMQUN4YjZtbnpaV25Qay9UQzZtT2pBbmNYL2V0NkVGeFBUYzl3MCttZWUzMVVoQWwvSWt4eXFtTG84Uy9rUFBYOEtsWjU3YWtrUnRJVHR3NEU5bHlMRnRxSkdkb0EyRW5LRHY5QTFmTldVRVdFWWtFSXNnenpaTXFFTHFJR01kd1MzK25CVWRVR2ZrNm11OWZHQzYzQ2ZJdnhLRGpaVzJZVDhEQ29jUjl0emJwQkhlcm5jYmRUK0hMQTlGL01rdmxQTElWanFUdXU5a0xCQkZqU0haZlJXWVdqVEd0dmpCWEt3eEVEZGMyMElDQk1TeURUYk9qOEM1MnI4ZHlMQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX21zX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfbXMuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ms_complete, file = "hometowns_ms.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE1JU1NPVVJJIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX21vIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJNT1wiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfbW8gPC0gZm9vdGJhbGxfcm9zdGVyc19tbyAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# MISSOURI HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_mo <- football_rosters_usa %>%
  filter(hometown_state_clean == "MO")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_mo <- football_rosters_mo %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfbW9fMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJNT1wiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_mo_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "MO",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzI5JyBmb3Igc3RhdGUgJ01PJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '29' for state 'MO'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfbW9fMjAyMSA8LSBjZW5zdXNfZGF0YV9tb18yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9tb18yMDIxIDwtIGNlbnN1c19kYXRhX21vXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnTWlzc291cmknIH4gXCJNT1wiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX21vX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19tbyAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX21vXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19tb19jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_mo_2021 <- census_data_mo_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_mo_2021 <- census_data_mo_2021 %>%
  mutate(state = case_when(
    state == 'Missouri' ~ "MO"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_mo_complete <- distinct_hometowns_mo %>%
  left_join(census_data_mo_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_mo_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzVTdESUJUSDZWWTBiZEtseVh5TjlrSmo0Z01ZSDhCb3NqdkNLSzVrRkFqUXpMMzhsRkp3bHF0eGN6aS9jM0wrNStQOWRmZFU3a29Bd0Jya3F3eXNvZnNDK1BueDFyd0FSNXlUZ1J3VWsvMTJTVnYzbVp3YXpDL2FLdkUzdDltRkFDUWNHeE9LUkZoMjJPTDJTK09CSnVtRmxxZFdPRzZ1K3N0Nk1WajdwbWU0N2VWQXJUd0pSSmc5SThJcEZpSDA4QmN5Rmx1NmlGVldXc3lSNHZoTXRZa0NCeXBaRjlzSkdWSkZzT2VZSFArQmFxQWR3d0l4UVp4UXpGTEVJcDhadXdnYVNGR05iQzlIZzBYbitDV1o3bDRxeTZSdzg2Mm1vOEJrYjVsT1FEMkthUjlkUS9wUkhKdkg1Mm01UG42OVlQb3ZaczM4SjlTQ29kWWRGUWNtNGdpUTR6M2x3ZG00cS9pOXQwb3pZZU1WSFRXdDMxQWtSUEpJL0hEZzhndmk1dklXakFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMgTm90IGFwcGxpY2FibGUgZm9yIE1pc3NvdXJpXG5cbiMgU3RlcCA5OiBXZSBub3cgaGF2ZSB0byBhcHBlbmQgdGhlc2Ugc3BlY2lhbCBjYXNlcyB0byBvdXIgc3RhdGUgY2Vuc3VzIGRhdGEsIHJlZG8gdGhlIGpvaW4sIGFuZCBydW4gb25lIG1vcmUgY2hlY2sgZm9yIE5BIHZhbHVlcy5cbiMgTm90IGFwcGxpY2FibGUgZm9yIE1pc3NvdXJpXG5cbiMgU3RlcCAxMDogSWYgbmVlZGVkLCB1bmNvbW1lbnQgb3V0IHRvIGNyZWF0ZSBhIENTVlxuI3dyaXRlX2Nzdihob21ldG93bnNfbW9fY29tcGxldGUsIGZpbGUgPSBcImhvbWV0b3duc19tby5jc3ZcIilcblxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
# Not applicable for Missouri

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
# Not applicable for Missouri

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_mo_complete, file = "hometowns_mo.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE5FQlJBU0tBIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX25lIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJORVwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfbmUgPC0gZm9vdGJhbGxfcm9zdGVyc19uZSAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# NEBRASKA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ne <- football_rosters_usa %>%
  filter(hometown_state_clean == "NE")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ne <- football_rosters_ne %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfbmVfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJORVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ne_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "NE",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzMxJyBmb3Igc3RhdGUgJ05FJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '31' for state 'NE'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfbmVfMjAyMSA8LSBjZW5zdXNfZGF0YV9uZV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9uZV8yMDIxIDwtIGNlbnN1c19kYXRhX25lXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnTmVicmFza2EnIH4gXCJORVwiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX25lX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19uZSAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX25lXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19uZV9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ne_2021 <- census_data_ne_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ne_2021 <- census_data_ne_2021 %>%
  mutate(state = case_when(
    state == 'Nebraska' ~ "NE"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ne_complete <- distinct_hometowns_ne %>%
  left_join(census_data_ne_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ne_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzVTdESUJUSDZWWTBiZEtseVh5TjlrSVQ0d01ZSDhCb3NqdkNLSzVrRkFqUXpMMzhsRkp3bHF0eGN6aS9jM0wrNStQOWRmZFU3a29Bd0Jya3F3eXNvZnNDK1BueDFyd0FSNXlUZ1J3VWsvMTJTVnYzbVp3YXpDL2FLdkUzdDltRkFDUWNHeE9LUkZoMjJPTDJTK09CSnVtRmxxZFdPRzZ1K3N0Nk1WajdwbWU0N2VWQXJUd0pSSmc5SThJcEZpSDA4QmN5Rmx1NmlGVldXc3lSNHZoTXRZa0NCeXBaRjlzSkdWSkZzT2VZSFArQmFxQWR3d0l4UVp4UXpGTEVJcDhadXdnYVNGR05iQzlIZzBYbitDV1o3bDRxeTZSdzg2Mm1vOEJrYjVsT1FEMkthUjlkUS9wUkhKdkg1Mm01UG42OVlQb3ZaczM4SjlTQ29kWWRGUWNtNGdpUTR6M2x3ZG00cS9pOXQwb3pZZU1WSFRXdDMxQWtSUEpJL0hEZzhndUVnQkN6akFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMgTm90IGFwcGxpY2FibGUgYmVjYXVzZSBubyBOQSB2YWx1ZXMgZm9yIE5lYnJhc2thXG5cbiMgU3RlcCA5OiBXZSBub3cgaGF2ZSB0byBhcHBlbmQgdGhlc2Ugc3BlY2lhbCBjYXNlcyB0byBvdXIgc3RhdGUgY2Vuc3VzIGRhdGEsIHJlZG8gdGhlIGpvaW4sIGFuZCBydW4gb25lIG1vcmUgY2hlY2sgZm9yIE5BIHZhbHVlcy5cbiMgTm90IGFwcGxpY2FibGUgYmVjYXVzZSBubyBOQSB2YWx1ZXMgZm9yIE5lYnJhc2thXG5cbiMgU3RlcCAxMDogSWYgbmVlZGVkLCB1bmNvbW1lbnQgb3V0IHRvIGNyZWF0ZSBhIENTVlxuI3dyaXRlX2Nzdihob21ldG93bnNfbmVfY29tcGxldGUsIGZpbGUgPSBcImhvbWV0b3duc19uZS5jc3ZcIilcblxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
# Not applicable because no NA values for Nebraska

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
# Not applicable because no NA values for Nebraska

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ne_complete, file = "hometowns_ne.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE5FVyBKRVJTRVkgSE9NRVRPV05TIC0gbm90IGEgZ29vZCBvbmUgdG8gdXNlIGFzIGEgdGVtcGxhdGVcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc19uaiA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiTkpcIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX25qIDwtIGZvb3RiYWxsX3Jvc3RlcnNfbmogJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# NEW JERSEY HOMETOWNS - not a good one to use as a template

# Step 1: Filter for the state's players
football_rosters_nj <- football_rosters_usa %>%
  filter(hometown_state_clean == "NJ")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_nj <- football_rosters_nj %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfbmpfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJOSlwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_nj_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "NJ",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzM0JyBmb3Igc3RhdGUgJ05KJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '34' for state 'NJ'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBJdCB0dXJucyBvdXQgdGhhdCBtYW55IHRvd25zIGluIE5ldyBKZXJzZXkgYXJlIGNvdW50eSBzdWJkaXZpc2lvbnMsIHNvIHdlIHdpbGwgZ3JhYiB0aGUgcmVsZXZhbnQgb25lcyBvZiB0aG9zZSwgdG9vXG5jZW5zdXNfZGF0YV9ual9zdWJkaXZpc2lvbnNfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiY291bnR5IHN1YmRpdmlzaW9uXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBzdGF0ZSA9IFwiTkpcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgZmlsdGVyKE5BTUUgPT0gXCJBYmVyZGVlbiB0b3duc2hpcCwgTW9ubW91dGggQ291bnR5LCBOZXcgSmVyc2V5XCIgfCBOQU1FID09IFwiQnJpZGdld2F0ZXIgdG93bnNoaXAsIFNvbWVyc2V0IENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIkNpbm5hbWluc29uIHRvd25zaGlwLCBCdXJsaW5ndG9uIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIkNvbHRzIE5lY2sgdG93bnNoaXAsIE1vbm1vdXRoIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIkRlbHJhbiB0b3duc2hpcCwgQnVybGluZ3RvbiBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJFZ2cgSGFyYm9yIHRvd25zaGlwLCBBdGxhbnRpYyBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJGcmVkb24gdG93bnNoaXAsIFN1c3NleCBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJHYWxsb3dheSB0b3duc2hpcCwgQXRsYW50aWMgQ291bnR5LCBOZXcgSmVyc2V5XCIgfCBOQU1FID09IFwiR2xvdWNlc3RlciB0b3duc2hpcCwgQ2FtZGVuIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIkhhaW5lc3BvcnQgdG93bnNoaXAsIEJ1cmxpbmd0b24gQ291bnR5LCBOZXcgSmVyc2V5XCIgfCBOQU1FID09IFwiSGlsbHNpZGUgdG93bnNoaXAsIFVuaW9uIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIkhvbGxhbmQgdG93bnNoaXAsIEh1bnRlcmRvbiBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJIb2xtZGVsIHRvd25zaGlwLCBNb25tb3V0aCBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJJcnZpbmd0b24gdG93bnNoaXAsIEVzc2V4IENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIkphY2tzb24gdG93bnNoaXAsIE9jZWFuIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIkplZmZlcnNvbiB0b3duc2hpcCwgTW9ycmlzIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIk1lZGZvcmQgdG93bnNoaXAsIEJ1cmxpbmd0b24gQ291bnR5LCBOZXcgSmVyc2V5XCIgfCBOQU1FID09IFwiTWlkZGxldG93biB0b3duc2hpcCwgTW9ubW91dGggQ291bnR5LCBOZXcgSmVyc2V5XCIgfCBOQU1FID09IFwiTW9udGNsYWlyIHRvd25zaGlwLCBFc3NleCBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJNb29yZXN0b3duIHRvd25zaGlwLCBCdXJsaW5ndG9uIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIk1vdW50IExhdXJlbCB0b3duc2hpcCwgQnVybGluZ3RvbiBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJPY2VhbiB0b3duc2hpcCwgTW9ubW91dGggQ291bnR5LCBOZXcgSmVyc2V5XCIgfCBOQU1FID09IFwiUGVubnNhdWtlbiB0b3duc2hpcCwgQ2FtZGVuIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIlBsYWluc2Jvcm8gdG93bnNoaXAsIE1pZGRsZXNleCBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJSb2JiaW5zdmlsbGUgdG93bnNoaXAsIE1lcmNlciBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJTb3V0aCBCcnVuc3dpY2sgdG93bnNoaXAsIE1pZGRsZXNleCBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJUZWFuZWNrIHRvd25zaGlwLCBCZXJnZW4gQ291bnR5LCBOZXcgSmVyc2V5XCIgfCBOQU1FID09IFwiVW5pb24gdG93bnNoaXAsIFVuaW9uIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIlZlcm9uYSB0b3duc2hpcCwgRXNzZXggQ291bnR5LCBOZXcgSmVyc2V5XCIgfCBOQU1FID09IFwiV2FycmVuIHRvd25zaGlwLCBTb21lcnNldCBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJXYXluZSB0b3duc2hpcCwgUGFzc2FpYyBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJXZXN0IERlcHRmb3JkIHRvd25zaGlwLCBHbG91Y2VzdGVyIENvdW50eSwgTmV3IEplcnNleVwiIHwgTkFNRSA9PSBcIldlc3QgT3JhbmdlIHRvd25zaGlwLCBFc3NleCBDb3VudHksIE5ldyBKZXJzZXlcIiB8IE5BTUUgPT0gXCJXaWxsaW5nYm9ybyB0b3duc2hpcCwgQnVybGluZ3RvbiBDb3VudHksIE5ldyBKZXJzZXlcIilcbmBgYCJ9 -->

```r
# It turns out that many towns in New Jersey are county subdivisions, so we will grab the relevant ones of those, too
census_data_nj_subdivisions_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "NJ",
                           output = "wide") %>%
  filter(NAME == "Aberdeen township, Monmouth County, New Jersey" | NAME == "Bridgewater township, Somerset County, New Jersey" | NAME == "Cinnaminson township, Burlington County, New Jersey" | NAME == "Colts Neck township, Monmouth County, New Jersey" | NAME == "Delran township, Burlington County, New Jersey" | NAME == "Egg Harbor township, Atlantic County, New Jersey" | NAME == "Fredon township, Sussex County, New Jersey" | NAME == "Galloway township, Atlantic County, New Jersey" | NAME == "Gloucester township, Camden County, New Jersey" | NAME == "Hainesport township, Burlington County, New Jersey" | NAME == "Hillside township, Union County, New Jersey" | NAME == "Holland township, Hunterdon County, New Jersey" | NAME == "Holmdel township, Monmouth County, New Jersey" | NAME == "Irvington township, Essex County, New Jersey" | NAME == "Jackson township, Ocean County, New Jersey" | NAME == "Jefferson township, Morris County, New Jersey" | NAME == "Medford township, Burlington County, New Jersey" | NAME == "Middletown township, Monmouth County, New Jersey" | NAME == "Montclair township, Essex County, New Jersey" | NAME == "Moorestown township, Burlington County, New Jersey" | NAME == "Mount Laurel township, Burlington County, New Jersey" | NAME == "Ocean township, Monmouth County, New Jersey" | NAME == "Pennsauken township, Camden County, New Jersey" | NAME == "Plainsboro township, Middlesex County, New Jersey" | NAME == "Robbinsville township, Mercer County, New Jersey" | NAME == "South Brunswick township, Middlesex County, New Jersey" | NAME == "Teaneck township, Bergen County, New Jersey" | NAME == "Union township, Union County, New Jersey" | NAME == "Verona township, Essex County, New Jersey" | NAME == "Warren township, Somerset County, New Jersey" | NAME == "Wayne township, Passaic County, New Jersey" | NAME == "West Deptford township, Gloucester County, New Jersey" | NAME == "West Orange township, Essex County, New Jersey" | NAME == "Willingboro township, Burlington County, New Jersey")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzM0JyBmb3Igc3RhdGUgJ05KJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '34' for state 'NJ'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfbmpfMjAyMSA8LSBjZW5zdXNfZGF0YV9ual8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZXxib3JvdWdoKVxcXFxiXCIsIFwiXCIsIGNpdHkpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBzdHJfc3F1aXNoKGNpdHkpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgYjAxMDAzXzAwMWUsIGIwMjAwMV8wMDNlLCBiMTkwMTNfMDAxZSkgJT4lXG4gIHJlbmFtZSh0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpXG5cbmNlbnN1c19kYXRhX25qX3N1YmRpdmlzaW9uc18yMDIxIDwtIGNlbnN1c19kYXRhX25qX3N1YmRpdmlzaW9uc18yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJjb3VudHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZXxtdW5pY2lwYWxpdHl8dG93bnNoaXB8Ym9yb3VnaClcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG5jZW5zdXNfZGF0YV9ual8yMDIxIDwtIGJpbmRfcm93cyhjZW5zdXNfZGF0YV9ual8yMDIxLCBjZW5zdXNfZGF0YV9ual9zdWJkaXZpc2lvbnNfMjAyMSkgJT4lXG4gIGZpbHRlcihjaXR5ICE9IFwiVW5pb25cIiB8IGdlb2lkICE9IDM0NzQ0NzgpICNSZW1vdmluZyBhIFVuaW9uLCBOSiB0aGF0IGlzIGEgQ0RQXG5cbiMgU3RlcCA1OiBTdGF0ZS1zcGVjaWZpYyBjbGVhbmluZyBvZiBjZW5zdXMgZGF0YSB0byBwcmVwYXJlIGZvciBqb2luIHdpdGggaG9tZXRvd25zL3Jvc3RlciBkYXRhLiBUaGlzIHBhcnQgaXMgZGlmZmVyZW50IGZvciBldmVyeSBzdGF0ZS4gVGhlIGZpcnN0IG11dGF0ZSBmdW5jdGlvbiBzaG91bGQgYmUgaW5jbHVkZWQgZm9yIGV2ZXJ5IHN0YXRlLCBqdXN0IG1vZGlmaWVkIGRlcGVuZGluZyBvbiB0aGUgc3RhdGUgbmFtZS4gQWRkaXRpb25hbCBtdXRhdGUgZnVuY3Rpb25zIG1heSBiZSBuZWVkZWQgZm9yIGluc3RhbmNlcyB3aGVuIHRoZSBjZW5zdXMgbmFtZXMgc29tZXRoaW5nIGluIGEgd2VpcmQgd2F5IHRoYXQgZG9lc24ndCBsaW5lIHVwIHdpdGggdGhlIGhvbWV0b3ducy5cbmNlbnN1c19kYXRhX25qXzIwMjEgPC0gY2Vuc3VzX2RhdGFfbmpfMjAyMSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gY2FzZV93aGVuKFxuICAgIHN0YXRlID09ICdOZXcgSmVyc2V5JyB+IFwiTkpcIikpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09ICdFZ2cgSGFyYm9yJyB+IFwiRWdnIEhhcmJvciBUb3duc2hpcFwiLFxuICAgIGNpdHkgPT0gJ0plZmZlcnNvbicgfiBcIkplZmZlcnNvbiBUb3duc2hpcFwiLFxuICAgIGNpdHkgPT0gJ09jZWFuJyB+IFwiT2NlYW4gVG93bnNoaXBcIixcbiAgICBjaXR5ID09IFwiVW5pb25cIiB+IFwiVW5pb24gVG93bnNoaXBcIixcbiAgICBUUlVFIH4gY2l0eSkpXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cbmhvbWV0b3duc19ual9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfbmogJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9ual8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbiMgU3RlcCA3OiBOb3RpY2UgdGhlcmUgYXJlIGEgZmV3IE5BIHZhbHVlcy4gVGhpcyBoYXBwZW5zIHdoZW4gdGhlIGNlbnN1cyBkYXRhIGRvZXMgbm90IGpvaW4gd2l0aCB0aGUgaG9tZXRvd25zIGRhdGEsIHBlcmhhcHMgYmVjYXVzZSB0aGUgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCBvciBiZWNhdXNlIHRoZXJlIGlzIG5vIGNlbnN1cyBkYXRhIGZvciB0aGF0IHRvd24uIEZpcnN0LCBsZXQncyBmaW5kIHRoZSBOQSB2YWx1ZXMuXG5ob21ldG93bnNfbmpfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpXG5gYGAifQ== -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_nj_2021 <- census_data_nj_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|borough)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_nj_subdivisions_2021 <- census_data_nj_subdivisions_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "county", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|municipality|township|borough)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_nj_2021 <- bind_rows(census_data_nj_2021, census_data_nj_subdivisions_2021) %>%
  filter(city != "Union" | geoid != 3474478) #Removing a Union, NJ that is a CDP

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_nj_2021 <- census_data_nj_2021 %>%
  mutate(state = case_when(
    state == 'New Jersey' ~ "NJ")) %>%
  mutate(city = case_when(
    city == 'Egg Harbor' ~ "Egg Harbor Township",
    city == 'Jefferson' ~ "Jefferson Township",
    city == 'Ocean' ~ "Ocean Township",
    city == "Union" ~ "Union Township",
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_nj_complete <- distinct_hometowns_nj %>%
  left_join(census_data_nj_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_nj_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFVzdhQTlROVFCVksyV0hDS1l4Q2dZRVdHa3VueFpqYUdwV1lUUE1ONlA1NS9IK3Vuc3FkeVVBWUEzeVZRYlcwSDBCL1B4NGExNkFJODdKUUE2S3lYNjdwSzM3VEU0TjVoZHRsZmliMit4Q0FCS09qUWxGSWl3N2JISDdwZkZBay9SQ3kxTXJIRGRYL1dXOUdLeDkwelBjOW5LZ1ZwNEVJc3llRWVFVWl4QjYrQXNaaXkxZHhDb3JMZVpJY1h5bTJrU0JBNVdzaSsyRURLa2kySE5NanY5QU5kQ09ZWUdZSUU0b1ppbGlrYytNWFFRTnBLaEd0cGVqd2FKei9KSk1keStWWlZLNCtWYlRVV0N5dDB3bm9CN0Z0SSt1SWYwb2pzM2o4N1JjSDc5ZU1QMFhzMmIrRTJyQlVPdU9pZ01UY1FUSThaN3k0R3pjVmZ6ZVc2V1pzUEdLanByV2J5Z1NJbmtrZmpodytRV21vazdRakFJQUFBPT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiNOb3QgbmVlZGVkIGZvciBOSlxuXG4jIFN0ZXAgOTogV2Ugbm93IGhhdmUgdG8gYXBwZW5kIHRoZXNlIHNwZWNpYWwgY2FzZXMgdG8gb3VyIHN0YXRlIGNlbnN1cyBkYXRhLCByZWRvIHRoZSBqb2luLCBhbmQgcnVuIG9uZSBtb3JlIGNoZWNrIGZvciBOQSB2YWx1ZXMuXG4jTm90IG5lZWRlZCBmb3IgTkpcblxuIyBTdGVwIDEwOiBJZiBuZWVkZWQsIHVuY29tbWVudCBvdXQgdG8gY3JlYXRlIGEgQ1NWXG4jd3JpdGVfY3N2KGhvbWV0b3duc19ual9jb21wbGV0ZSwgZmlsZSA9IFwiaG9tZXRvd25zX25qLmNzdlwiKVxuXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
#Not needed for NJ

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
#Not needed for NJ

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_nj_complete, file = "hometowns_nj.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE5FVyBZT1JLIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX255IDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJOWVwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfbnkgPC0gZm9vdGJhbGxfcm9zdGVyc19ueSAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# NEW YORK HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ny <- football_rosters_usa %>%
  filter(hometown_state_clean == "NY")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ny <- football_rosters_ny %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfbnlfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJOWVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ny_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "NY",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzM2JyBmb3Igc3RhdGUgJ05ZJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '36' for state 'NY'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuY2Vuc3VzX2RhdGFfbnlfc3ViZGl2aXNpb25zXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcImNvdW50eSBzdWJkaXZpc2lvblwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RhdGUgPSBcIk5ZXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGZpbHRlcihOQU1FID09IFwiQmFsbHN0b24gdG93biwgU2FyYXRvZ2EgQ291bnR5LCBOZXcgWW9ya1wiIHwgTkFNRSA9PSBcIlNvbWVycyB0b3duLCBXZXN0Y2hlc3RlciBDb3VudHksIE5ldyBZb3JrXCIpXG5gYGAifQ== -->

```r
census_data_ny_subdivisions_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "NY",
                           output = "wide") %>%
  filter(NAME == "Ballston town, Saratoga County, New York" | NAME == "Somers town, Westchester County, New York")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzM2JyBmb3Igc3RhdGUgJ05ZJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '36' for state 'NY'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfbnlfMjAyMSA8LSBjZW5zdXNfZGF0YV9ueV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG5jZW5zdXNfZGF0YV9ueV9zdWJkaXZpc2lvbnNfMjAyMSA8LSBjZW5zdXNfZGF0YV9ueV9zdWJkaXZpc2lvbnNfMjAyMSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgc2VwYXJhdGUobmFtZSwgaW50byA9IGMoXCJjaXR5XCIsIFwiY291bnR5XCIsIFwic3RhdGVcIiksIHNlcCA9IFwiLCBcIiwgcmVtb3ZlID0gRkFMU0UpICU+JVxuICBtdXRhdGUoY2l0eSA9IGdzdWIoXCJcXFxcYih0b3dufGNpdHl8Q0RQfHZpbGxhZ2V8bXVuaWNpcGFsaXR5fHRvd25zaGlwfGJvcm91Z2gpXFxcXGJcIiwgXCJcIiwgY2l0eSkpICU+JVxuICBtdXRhdGUoY2l0eSA9IHN0cl9zcXVpc2goY2l0eSkpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCBiMDEwMDNfMDAxZSwgYjAyMDAxXzAwM2UsIGIxOTAxM18wMDFlKSAlPiVcbiAgcmVuYW1lKHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSlcblxuY2Vuc3VzX2RhdGFfbnlfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfbnlfMjAyMSwgY2Vuc3VzX2RhdGFfbnlfc3ViZGl2aXNpb25zXzIwMjEpXG5cbiMgU3RlcCA1OiBTdGF0ZS1zcGVjaWZpYyBjbGVhbmluZyBvZiBjZW5zdXMgZGF0YSB0byBwcmVwYXJlIGZvciBqb2luIHdpdGggaG9tZXRvd25zL3Jvc3RlciBkYXRhLiBUaGlzIHBhcnQgaXMgZGlmZmVyZW50IGZvciBldmVyeSBzdGF0ZS4gVGhlIGZpcnN0IG11dGF0ZSBmdW5jdGlvbiBzaG91bGQgYmUgaW5jbHVkZWQgZm9yIGV2ZXJ5IHN0YXRlLCBqdXN0IG1vZGlmaWVkIGRlcGVuZGluZyBvbiB0aGUgc3RhdGUgbmFtZS4gQWRkaXRpb25hbCBtdXRhdGUgZnVuY3Rpb25zIG1heSBiZSBuZWVkZWQgZm9yIGluc3RhbmNlcyB3aGVuIHRoZSBjZW5zdXMgbmFtZXMgc29tZXRoaW5nIGluIGEgd2VpcmQgd2F5IHRoYXQgZG9lc24ndCBsaW5lIHVwIHdpdGggdGhlIGhvbWV0b3ducy5cbmNlbnN1c19kYXRhX255XzIwMjEgPC0gY2Vuc3VzX2RhdGFfbnlfMjAyMSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gY2FzZV93aGVuKFxuICAgIHN0YXRlID09ICdOZXcgWW9yaycgfiBcIk5ZXCIpKSBcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX255X2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19ueSAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX255XzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19ueV9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ny_2021 <- census_data_ny_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_ny_subdivisions_2021 <- census_data_ny_subdivisions_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "county", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|municipality|township|borough)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_ny_2021 <- bind_rows(census_data_ny_2021, census_data_ny_subdivisions_2021)

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ny_2021 <- census_data_ny_2021 %>%
  mutate(state = case_when(
    state == 'New York' ~ "NY")) 

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ny_complete <- distinct_hometowns_ny %>%
  left_join(census_data_ny_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ny_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjEsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMSDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsxXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE2VlJ3VTdETUF4TnU1YXBsVHBWR3IreEh1Q3lEMEFjT0hCQUlJMVRsS1ZoaTVZbVZaTXlkb0p2NFF2NWdnMm5UZENXSzVVYTI4OVA5clA5ZExlNnpWYzVRbWlDa2poQ2t4UmNsTDQ4M3krV0NCQUlJcFNnek5vUElNM0JzVUY1bHNnZlNNUDBPeGVDQlpuNDhSWGVZa0RHdjNRMk84RUhkbWJqengvYmRQcjkvL2hDY0VvRjBUb1VXeE5EcXJjT0pBZjByRlA3U3RwUm5PYjRDNTVSNTJWZFR5cUhaWXpnZktzYVp0UmVZc3JOQVZQQmlIU3A2NytVTnNTd2kxeGhsQ0VDdDRJY1dLZDlndzFUdlBheUhFTzFIbGdMUW5kblFOR3dtaE9KdWFUUXlMTmFhdkRBOUNwY0Q5eXlEcHV0NmpXUk5lREhZTHFwYWcxWEV1YUw3YkhUWUg5UkZ3QmxMKzArNmdYZDluSzN1Rm5hSmJzcm8rRDYzcy9HbnNuSjFVcGRyU3NtTjF6NkVWSkIxa3k0WUFiWEdmWmV0UjJYeGw4VFVGME5HL0lJVmNJanczRG8rQXZ2ZFBQbTVBSUFBQT09In0= -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Jamesville","2":"NY","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[1]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgSmFtZXN2aWxsZSwgdGhlIHppcCBjb2RlICgxMzA3OCkgYXBwZWFycyB0byBiZSBhIGdvb2Qgc3Vic3RpdHV0ZSBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTMTMwNzgtMTMwNzgvXG5jZW5zdXNfZGF0YV96aXBzX255XzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcInpjdGFcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgZmlsdGVyKG5hbWUgPT0gXCJaQ1RBNSAxMzA3OFwiKSAlPiUgXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJOWVwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDEzMDc4XCIgfiBcIkphbWVzdmlsbGVcIikpJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Jamesville, the zip code (13078) appears to be a good substitute https://censusreporter.org/profiles/86000US13078-13078/
census_data_zips_ny_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 13078") %>% 
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "NY") %>%
  mutate(city = case_when(
    city == "ZCTA5 13078" ~ "Jamesville"))%>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuXG5jZW5zdXNfZGF0YV9ueV8yMDIxIDwtIGJpbmRfcm93cyhjZW5zdXNfZGF0YV9ueV8yMDIxLCBjZW5zdXNfZGF0YV96aXBzX255XzIwMjEpXG4gXG5ob21ldG93bnNfbnlfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX255ICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfbnlfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG5ob21ldG93bnNfbnlfY29tcGxldGUgJT4lIFxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKVxuYGBgIn0= -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.

census_data_ny_2021 <- bind_rows(census_data_ny_2021, census_data_zips_ny_2021)
 
hometowns_ny_complete <- distinct_hometowns_ny %>%
  left_join(census_data_ny_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_ny_complete %>% 
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFVzd5UUdxSHFCcXBld1F3VFJHd1lBQUs4M2wwMklNVGMwcWJJYjVaalQvUE41Zjl5L2x2Z1FBckVHK3lzQWF1aStBbng5dnpRNDQ0cHdNNUtDWTdMZEwycnJQNU5SZ2Z0RldpYis1enk0RUlPSFltRkFrd3JMREZyZGZHZzgwU1MrMFBMZkNjWFBUWDlhTHdkbzNQY050THdkcTVWa2d3dXdGRVU2eENLR252NUN4Mk5KRnJMTFNZbzRVeHhlcVRSUTRVc202MkU3SWtDcUNBOGZrOUE5VUErMFlGb2dKNG9SaWxpSVcrY3pZUmRCQWltcGtlemthTERySHI4bDBqMUpaSm9XYmJ6VWRCU1o3eTNRQzZsRk0rK2dhMG8vaTFEenZwdVg2K08yQzZiK1lOZk9mVUF1R1dnOVVISm1JSTBDT0Q1UUhaK091NHZmZUtzMkVqVmQwMUxSK1E1RVF5U1B4dzRIckw1dFh0bytNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX255X2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfbnkuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ny_complete, file = "hometowns_ny.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgQXJkZW4sIE5DICgyODcwNCksIHRoZSB6aXAgY29kZSBzZWVtcyB0byBiZSBnb29kIHN1YnN0aXR1dGVzOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTMjg3MDQtMjg3MDQvXG5jZW5zdXNfZGF0YV9hcmRlbl9uY18yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgMjg3MDRcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJOQ1wiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDI4NzA0XCIgfiBcIkFyZGVuXCIpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgdG90YWxfcG9wLCBibGFja19wb3AsIG1lZGlhbl9pbmNvbWUsIHBjdF9ibGFjaylcblxuYGBgIn0= -->

```r
# For Arden, NC (28704), the zip code seems to be good substitutes: https://censusreporter.org/profiles/86000US28704-28704/
census_data_arden_nc_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 28704") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "NC") %>%
  mutate(city = case_when(
    city == "ZCTA5 28704" ~ "Arden")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)

```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE9ISU8gSE9NRVRPV05TIChub3QgdGhlIGJlc3Qgb25lIHRvIHVzZSBhcyBhIHRlbXBsYXRlKVxuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX29oIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJPSFwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfb2ggPC0gZm9vdGJhbGxfcm9zdGVyc19vaCAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# OHIO HOMETOWNS (not the best one to use as a template)

# Step 1: Filter for the state's players
football_rosters_oh <- football_rosters_usa %>%
  filter(hometown_state_clean == "OH")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_oh <- football_rosters_oh %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfb2hfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJPSFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_oh_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "OH",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzM5JyBmb3Igc3RhdGUgJ09IJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '39' for state 'OH'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBJdCB0dXJucyBvdXQgdGhhdCBtYW55IHRvd25zIGluIE9oaW8gYXJlIGNvdW50eSBzdWJkaXZpc2lvbnMsIHNvIHdlIHdpbGwgZ3JhYiBzb21lIG9mIHRob3NlIHdlIG5lZWQsIHRvb1xuY2Vuc3VzX2RhdGFfb2hfc3ViZGl2aXNpb25zXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcImNvdW50eSBzdWJkaXZpc2lvblwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RhdGUgPSBcIk9IXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGZpbHRlcihOQU1FID09IFwiQnJhY2V2aWxsZSB0b3duc2hpcCwgVHJ1bWJ1bGwgQ291bnR5LCBPaGlvXCIgfCBOQU1FID09IFwiQ29sZXJhaW4gdG93bnNoaXAsIEhhbWlsdG9uIENvdW50eSwgT2hpb1wiIHwgTkFNRSA9PSBcIkNvbmNvcmQgdG93bnNoaXAsIExha2UgQ291bnR5LCBPaGlvXCIgfCBOQU1FID09IFwiTGliZXJ0eSB0b3duc2hpcCwgQnV0bGVyIENvdW50eSwgT2hpb1wiIHwgTkFNRSA9PSBcIldlc3QgQ2hlc3RlciB0b3duc2hpcCwgQnV0bGVyIENvdW50eSwgT2hpb1wiKVxuYGBgIn0= -->

```r
# It turns out that many towns in Ohio are county subdivisions, so we will grab some of those we need, too
census_data_oh_subdivisions_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "OH",
                           output = "wide") %>%
  filter(NAME == "Braceville township, Trumbull County, Ohio" | NAME == "Colerain township, Hamilton County, Ohio" | NAME == "Concord township, Lake County, Ohio" | NAME == "Liberty township, Butler County, Ohio" | NAME == "West Chester township, Butler County, Ohio")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzM5JyBmb3Igc3RhdGUgJ09IJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '39' for state 'OH'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfb2hfMjAyMSA8LSBjZW5zdXNfZGF0YV9vaF8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG5jZW5zdXNfZGF0YV9vaF9zdWJkaXZpc2lvbnNfMjAyMSA8LSBjZW5zdXNfZGF0YV9vaF9zdWJkaXZpc2lvbnNfMjAyMSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgc2VwYXJhdGUobmFtZSwgaW50byA9IGMoXCJjaXR5XCIsIFwiY291bnR5XCIsIFwic3RhdGVcIiksIHNlcCA9IFwiLCBcIiwgcmVtb3ZlID0gRkFMU0UpICU+JVxuICBtdXRhdGUoY2l0eSA9IGdzdWIoXCJcXFxcYih0b3dufGNpdHl8Q0RQfHZpbGxhZ2V8bXVuaWNpcGFsaXR5fHRvd25zaGlwKVxcXFxiXCIsIFwiXCIsIGNpdHkpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBzdHJfc3F1aXNoKGNpdHkpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgYjAxMDAzXzAwMWUsIGIwMjAwMV8wMDNlLCBiMTkwMTNfMDAxZSkgJT4lXG4gIHJlbmFtZSh0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpXG5cbmNlbnN1c19kYXRhX29oXzIwMjEgPC0gYmluZF9yb3dzKGNlbnN1c19kYXRhX29oXzIwMjEsIGNlbnN1c19kYXRhX29oX3N1YmRpdmlzaW9uc18yMDIxKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9vaF8yMDIxIDwtIGNlbnN1c19kYXRhX29oXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnT2hpbycgfiBcIk9IXCIpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIkxpYmVydHlcIiB+IFwiTGliZXJ0eSBUb3duc2hpcFwiLFxuICAgIFRSVUUgfiBjaXR5KSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX29oX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19vaCAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX29oXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19vaF9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_oh_2021 <- census_data_oh_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_oh_subdivisions_2021 <- census_data_oh_subdivisions_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "county", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|municipality|township)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_oh_2021 <- bind_rows(census_data_oh_2021, census_data_oh_subdivisions_2021)

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_oh_2021 <- census_data_oh_2021 %>%
  mutate(state = case_when(
    state == 'Ohio' ~ "OH")) %>%
  mutate(city = case_when(
    city == "Liberty" ~ "Liberty Township",
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_oh_complete <- distinct_hometowns_oh %>%
  left_join(census_data_oh_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_oh_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjIsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMiDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsyXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE3V1MwV3JDTUJTRzAyb255aFRCUFlBdllCbDRzL3VOTWNiWVlHemdYWWhwWm9NeEtVbkVlYlU5eTU1d1Q2QTdxVG1pdlYraHpjbDMvdWJrL01ucjNXemFtL1VJSVMzU1RoUFN5aUFrMmZ2Yi9lU0dBSUZKUXRxa0c4WlBFSTBnQ0pNaHZHbE1YRDZKalhUalc2RzlzSkgxbjQzMTVmaVI4YVV6dXZGRCt2SndFb0c0emgzZTVLaUZRbnQ0VHNaQjRGKy9ZWWVkSHh6L241KzVrSEhGbkl1YlJOZ3JtR2Y1aDJVcjBaQjNyZG5rR3JqRFByL2hBKzNzbXV1aWFGZzdmSUNqMHF5RU54dE51ZlJieXBWZ09xYXVqaW5ubVJkbnViNDNuaWxhS2JZVjFtR0JoVEN5d0cxRmhha1F6QlVjMVFub3IwUWhtYVpTY3lpRXFvcDdXaXR4RjdFR3JZU2x2alJyeDNRQnZObGR4MVJlR2czOXBlRUdaUTMvRXRzQXc3VU9maFFUWHE3MWNqSzlEaWJIMjBHaWswbThKUmgzRHpYYis3aFdGdGU2RUhvaE5iYVFLVFlYS2s0R2NEcTE3M2xscGZaNG1rQmRYanVFaEJ1RnBHNk83UDRBaXZZOS9Ua0RBQUE9In0= -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Lewis Center","2":"OH","3":"2","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"North Jackson","2":"OH","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[2]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgTGV3aXMgQ2VudGVyLCBPSCAoNDMwMzUpIGFuZCBOb3J0aCBKYWNrc29uLCBPSCAoNDQ0NTEpLCB0aGUgemlwIGNvZGVzIHNlZW1zIHRvIGJlIGdvb2Qgc3Vic3RpdHV0ZXM6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVM0MzAzNS00MzAzNS8gaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvODYwMDBVUzQ0NDUxLTQ0NDUxL1xuY2Vuc3VzX2RhdGFfemlwc19vaF8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgNDMwMzVcIiB8IG5hbWUgPT0gXCJaQ1RBNSA0NDQ1MVwiKSAlPiVcbiAgcmVuYW1lKGNpdHkgPSBuYW1lLCB0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpICU+JVxuICBtdXRhdGUoc3RhdGUgPSBcIk9IXCIpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09IFwiWkNUQTUgNDMwMzVcIiB+IFwiTGV3aXMgQ2VudGVyXCIsXG4gICAgY2l0eSA9PSBcIlpDVEE1IDQ0NDUxXCIgfiBcIk5vcnRoIEphY2tzb25cIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Lewis Center, OH (43035) and North Jackson, OH (44451), the zip codes seems to be good substitutes: https://censusreporter.org/profiles/86000US43035-43035/ https://censusreporter.org/profiles/86000US44451-44451/
census_data_zips_oh_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 43035" | name == "ZCTA5 44451") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "OH") %>%
  mutate(city = case_when(
    city == "ZCTA5 43035" ~ "Lewis Center",
    city == "ZCTA5 44451" ~ "North Jackson")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfb2hfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfb2hfMjAyMSwgY2Vuc3VzX2RhdGFfemlwc19vaF8yMDIxKVxuIFxuaG9tZXRvd25zX29oX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19vaCAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX29oXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuaG9tZXRvd25zX29oX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKSAjSWYgdGhpcyBpcyBub3QgcHJvZHVjaW5nIGFuIGVtcHR5IGRhdGFmcmFtZSwgZ28gYmFjayBhbmQgY29udGludWUgdG8gd29yayBvbiBOQSB2YWx1ZXNcbmBgYCJ9 -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_oh_2021 <- bind_rows(census_data_oh_2021, census_data_zips_oh_2021)
 
hometowns_oh_complete <- distinct_hometowns_oh %>%
  left_join(census_data_oh_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_oh_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzV3JESUJUSFRSczNFa2dKZEsrUk1Pak5IbURzQWNZR3ZSTnJYQ00xS21ybyt2TGRqTkYxOGFyZUhNL3ZITTcvZkx5LzduZmx2Z1FBckVHK3lzQWF1aStBbng5dnpRdHd4RGtaeUVFeDJXK1h0SFdmeWFuQi9LS3RFbjl6bjEwSVFNS3hNYUZJaEdXSExXNi9OQjVva2w1b2VXNkY0K2FtdjZ3WGc3VnZlb2JiWGc3VXlyTkFoTmtMSXB4aUVVSlBmeUZqc2FXTFdHV2x4Undwamk5VW15aHdwSkoxc1oyUUlWVUVCNDdKNlIrb0J0b3hMQkFUeEFuRkxFVXM4cG14aTZDQkZOWEk5bkkwV0hTT1g1UHBIcVd5VEFvMzMybzZDa3oybHVrRTFLT1k5dEUxcEIvRnFkazlUOHYxOGRzRjAzOHhhK1kvb1JZTXRSNm9PRElSUjRBY0h5Z1B6c1pkeGUrOVZab0pHNi9vcUduOWhpSWhra2ZpaHdQWFg4OVZwdmFNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX29oX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfb2guY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_oh_complete, file = "hometowns_oh.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE9LTEFIT01BIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX29rIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJPS1wiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfb2sgPC0gZm9vdGJhbGxfcm9zdGVyc19vayAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# OKLAHOMA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ok <- football_rosters_usa %>%
  filter(hometown_state_clean == "OK")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ok <- football_rosters_ok %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfb2tfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJPS1wiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ok_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "OK",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQwJyBmb3Igc3RhdGUgJ09LJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '40' for state 'OK'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfb2tfMjAyMSA8LSBjZW5zdXNfZGF0YV9va18yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9va18yMDIxIDwtIGNlbnN1c19kYXRhX29rXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnT2tsYWhvbWEnIH4gXCJPS1wiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX29rX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19vayAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX29rXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19va19jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ok_2021 <- census_data_ok_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ok_2021 <- census_data_ok_2021 %>%
  mutate(state = case_when(
    state == 'Oklahoma' ~ "OK"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ok_complete <- distinct_hometowns_ok %>%
  left_join(census_data_ok_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ok_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjEsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMSDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsxXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE2VlJTMnJETUJCVm5MakJoZ1JEZW8wWVNqWmRsOUpORjRYU1FuWkNrZFZZUkphTXBKQm0xWjZsSit3SmtvNXNLY1RhMW1ETnpKdkhmTjY4UHE1WCtUcEhDSTNSSkJtaGNRb3VTdC9mbnBiM0NCQUlSbWlDTW1jL2diUUF4d1hGVlNKN1lGb2ZheTVFbEVoZW51R2RkVWovRjk1bVovakF6bDM4OWV0NlRuLytIdy9tVGFrZ3hrUWo1Uld4cFB6UXBHRVJQZFBxVUVyQWpaODUrWWFubjNOWU41Q0tUb3NlWE5TcVlWWWRKS2JjSGpFVmpFaWZ1cjJrakNXV0RYSXpxeXdSdUJYa3lMUUpEYlpNOFNxTTVSbXFEY0JHRUxxN0FtWU5xemlSbUVzS2pRS3JwUlozekRDRjc0RmJwckd0MWQ0UVdRRitpcmFicXRaeUpXRy94TjA2amZRYjZRZ285dExwVVMxcHZaZTc1ZXJPaWV5dmpLTHJCei9yZTA3T3ZsYnFhOTB3dWVVeXJKQUtzbUhDQjNPNFRxZDcyV291YmJnbW9LYnNGQW9JVlNJZzNYTG85QWRxa1FQZTR3SUFBQT09In0= -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Berryhill","2":"OK","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[1]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMgRm9yIEJlcnJ5aGlsbCwgT0ssIHdlIHVzZWQgdGhlIHNjaG9vbCBkaXN0cmljdCBiZWNhdXNlIGl0IGRpZG4ndCBzZWVtIGxpa2UgdGhlcmUgd2FzIGEgYmV0dGVyIG9wdGlvbjogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvOTcwMDBVUzQwMDQwMjAtYmVycnloaWxsLXB1YmxpYy1zY2hvb2xzLW9rL1xuY2Vuc3VzX2RhdGFfc2Rfb2tfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwic2Nob29sIGRpc3RyaWN0ICh1bmlmaWVkKVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RhdGUgPSBcIk9LXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiQmVycnloaWxsIFB1YmxpYyBTY2hvb2xzLCBPa2xhaG9tYVwiKSAlPiVcbiAgcmVuYW1lKGNpdHkgPSBuYW1lLCB0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpICU+JVxuICBtdXRhdGUoc3RhdGUgPSBcIk9LXCIpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09IFwiQmVycnloaWxsIFB1YmxpYyBTY2hvb2xzLCBPa2xhaG9tYVwiIH4gXCJCZXJyeWhpbGxcIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
# For Berryhill, OK, we used the school district because it didn't seem like there was a better option: https://censusreporter.org/profiles/97000US4004020-berryhill-public-schools-ok/
census_data_sd_ok_2021 <- get_acs(geography = "school district (unified)",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "OK",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Berryhill Public Schools, Oklahoma") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "OK") %>%
  mutate(city = case_when(
    city == "Berryhill Public Schools, Oklahoma" ~ "Berryhill")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQwJyBmb3Igc3RhdGUgJ09LJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '40' for state 'OK'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfb2tfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfb2tfMjAyMSwgY2Vuc3VzX2RhdGFfc2Rfb2tfMjAyMSlcblxuaG9tZXRvd25zX29rX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19vayAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX29rXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuaG9tZXRvd25zX29rX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKSAjSWYgdGhpcyBpcyBub3QgcHJvZHVjaW5nIGFuIGVtcHR5IGRhdGFmcmFtZSwgZ28gYmFjayBhbmQgY29udGludWUgdG8gd29yayBvbiBOQSB2YWx1ZXNcbmBgYCJ9 -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_ok_2021 <- bind_rows(census_data_ok_2021, census_data_sd_ok_2021)

hometowns_ok_complete <- distinct_hometowns_ok %>%
  left_join(census_data_ok_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_ok_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzV3JESUJUSFRSczNFa2dKZEsrUndPak5IbURzQWNZR3ZSTnJYQ00xS21ybyt2TGRqTkYxOGFyZUhNL3ZITTcvZkx5LzduZmx2Z1FBckVHK3lzQWF1aStBbng5dnpRdHd4RGtaeUVFeDJXK1h0SFdmeWFuQi9LS3RFbjl6bjEwSVFNS3hNYUZJaEdXSExXNi9OQjVva2w1b2VXNkY0K2FtdjZ3WGc3VnZlb2JiWGc3VXlyTkFoTmtMSXB4aUVVSlBmeUZqc2FXTFdHV2x4Undwamk5VW15aHdwSkoxc1oyUUlWVUVCNDdKNlIrb0J0b3hMQkFUeEFuRkxFVXM4cG14aTZDQkZOWEk5bkkwV0hTT1g1UHBIcVd5VEFvMzMybzZDa3oybHVrRTFLT1k5dEUxcEIvRnFkazlUOHYxOGRzRjAzOHhhK1kvb1JZTXRSNm9PRElSUjRBY0h5Z1B6c1pkeGUrOVZab0pHNi9vcUduOWhpSWhra2ZpaHdQWFgrMTMrSldNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX29rX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfb2suY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ok_complete, file = "hometowns_ok.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE9SRUdPTiBIT01FVE9XTlNcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc19vciA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiT1JcIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX29yIDwtIGZvb3RiYWxsX3Jvc3RlcnNfb3IgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# OREGON HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_or <- football_rosters_usa %>%
  filter(hometown_state_clean == "OR")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_or <- football_rosters_or %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfb3JfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJPUlwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_or_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "OR",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQxJyBmb3Igc3RhdGUgJ09SJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '41' for state 'OR'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfb3JfMjAyMSA8LSBjZW5zdXNfZGF0YV9vcl8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9vcl8yMDIxIDwtIGNlbnN1c19kYXRhX29yXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnT3JlZ29uJyB+IFwiT1JcIikpIFxuXG4jIFN0ZXAgNjogSm9pbiB0aGUgY2Vuc3VzIGRhdGEgdG8gdGhlIGxpc3Qgb2YgaG9tZXRvd25zLiBBbHNvIGNyZWF0ZSBhIGNvbHVtbiB0aGF0IHRlbGxzIHVzIGhvdyBtYW55IHBlb3BsZSBhcmUgZWxpdGUgY29sbGVnZSBmb290YmFsbCBwbGF5ZXJzIGZvciBldmVyeSAxLDAwMCByZXNpZGVudHMuXG5ob21ldG93bnNfb3JfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX29yICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfb3JfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIFN0ZXAgNzogTm90aWNlIHRoZXJlIGFyZSBhIGZldyBOQSB2YWx1ZXMuIFRoaXMgaGFwcGVucyB3aGVuIHRoZSBjZW5zdXMgZGF0YSBkb2VzIG5vdCBqb2luIHdpdGggdGhlIGhvbWV0b3ducyBkYXRhLCBwZXJoYXBzIGJlY2F1c2UgdGhlIGhvbWV0b3duIGlzIG1pc3NwZWxsZWQgb3IgYmVjYXVzZSB0aGVyZSBpcyBubyBjZW5zdXMgZGF0YSBmb3IgdGhhdCB0b3duLiBGaXJzdCwgbGV0J3MgZmluZCB0aGUgTkEgdmFsdWVzLlxuaG9tZXRvd25zX29yX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKVxuYGBgIn0= -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_or_2021 <- census_data_or_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_or_2021 <- census_data_or_2021 %>%
  mutate(state = case_when(
    state == 'Oregon' ~ "OR")) 

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_or_complete <- distinct_hometowns_or %>%
  left_join(census_data_or_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_or_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFV3o2UUdxSHFCcXBld1F3VFJHd1lBQUs4M2wwMklNVGMwcWJJYjVaalQvUE41Zjk3dHlYd0lBMWlCZlpXQU4zUmZBejQrMzVnVTQ0cHdNNUtDWTdMZEwycnJQNU5SZ2Z0RldpYis1enk0RUlPSFltRkFrd3JMREZyZGZHZzgwU1MrMFBMZkNjWFBUWDlhTHdkbzNQY050THdkcTVWa2d3dXdGRVU2eENLR252NUN4Mk5KRnJMTFNZbzRVeHhlcVRSUTRVc202MkU3SWtDcUNBOGZrOUE5VUErMFlGb2dKNG9SaWxpSVcrY3pZUmRCQWltcGtlemthTERySHI4bDBqMUpaSm9XYmJ6VWRCU1o3eTNRQzZsRk0rK2dhMG8vaTFPeWVwK1g2K08yQzZiK1lOZk9mVUF1R1dnOVVISm1JSTBDT0Q1UUhaK091NHZmZUtzMkVqVmQwMUxSK1E1RVF5U1B4dzRIckw0c1JHakNNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX29yX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfb3IuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_or_complete, file = "hometowns_or.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFBFTk5TWUxWQU5JQSBIT01FVE9XTlNcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc19wYSA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiUEFcIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX3BhIDwtIGZvb3RiYWxsX3Jvc3RlcnNfcGEgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# PENNSYLVANIA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_pa <- football_rosters_usa %>%
  filter(hometown_state_clean == "PA")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_pa <- football_rosters_pa %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfcGFfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJQQVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_pa_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "PA",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQyJyBmb3Igc3RhdGUgJ1BBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '42' for state 'PA'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBJdCB0dXJucyBvdXQgdGhhdCBtYW55IHRvd25zIGluIFBlbm5zeWx2YW5pYSBhcmUgY291bnR5IHN1YmRpdmlzaW9ucywgc28gd2Ugd2lsbCBncmFiIHNvbWUgb2YgdGhvc2Ugd2UgbmVlZCwgdG9vXG5jZW5zdXNfZGF0YV9wYV9zdWJkaXZpc2lvbnNfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiY291bnR5IHN1YmRpdmlzaW9uXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBzdGF0ZSA9IFwiUEFcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgZmlsdGVyKE5BTUUgPT0gXCJBYmluZ3RvbiB0b3duc2hpcCwgTW9udGdvbWVyeSBDb3VudHksIFBlbm5zeWx2YW5pYVwiIHwgTkFNRSA9PSBcIkNyYW5iZXJyeSB0b3duc2hpcCwgQnV0bGVyIENvdW50eSwgUGVubnN5bHZhbmlhXCIgfCBOQU1FID09IFwiSGFub3ZlciB0b3duc2hpcCwgTHV6ZXJuZSBDb3VudHksIFBlbm5zeWx2YW5pYVwiIHwgTkFNRSA9PSBcIk11cnJ5c3ZpbGxlIG11bmljaXBhbGl0eSwgV2VzdG1vcmVsYW5kIENvdW50eSwgUGVubnN5bHZhbmlhXCIgfCBOQU1FID09IFwiTmV3dG9uIHRvd25zaGlwLCBMYWNrYXdhbm5hIENvdW50eSwgUGVubnN5bHZhbmlhXCIgfCBOQU1FID09IFwiTG93ZXIgR3d5bmVkZCB0b3duc2hpcCwgTW9udGdvbWVyeSBDb3VudHksIFBlbm5zeWx2YW5pYVwiIHwgTkFNRSA9PSBcIk5vcnRoYW1wdG9uIHRvd25zaGlwLCBCdWNrcyBDb3VudHksIFBlbm5zeWx2YW5pYVwiIHwgTkFNRSA9PSBcIk5ldyBHYXJkZW4gdG93bnNoaXAsIENoZXN0ZXIgQ291bnR5LCBQZW5uc3lsdmFuaWFcIiB8IE5BTUUgPT0gXCJOb3J0aCBXaGl0ZWhhbGwgdG93bnNoaXAsIExlaGlnaCBDb3VudHksIFBlbm5zeWx2YW5pYVwiIHwgTkFNRSA9PSBcIlBpbmUgdG93bnNoaXAsIEFsbGVnaGVueSBDb3VudHksIFBlbm5zeWx2YW5pYVwiIHwgTkFNRSA9PSBcIlRob3JuYnVyeSB0b3duc2hpcCwgRGVsYXdhcmUgQ291bnR5LCBQZW5uc3lsdmFuaWFcIilcbmBgYCJ9 -->

```r
# It turns out that many towns in Pennsylvania are county subdivisions, so we will grab some of those we need, too
census_data_pa_subdivisions_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "PA",
                           output = "wide") %>%
  filter(NAME == "Abington township, Montgomery County, Pennsylvania" | NAME == "Cranberry township, Butler County, Pennsylvania" | NAME == "Hanover township, Luzerne County, Pennsylvania" | NAME == "Murrysville municipality, Westmoreland County, Pennsylvania" | NAME == "Newton township, Lackawanna County, Pennsylvania" | NAME == "Lower Gwynedd township, Montgomery County, Pennsylvania" | NAME == "Northampton township, Bucks County, Pennsylvania" | NAME == "New Garden township, Chester County, Pennsylvania" | NAME == "North Whitehall township, Lehigh County, Pennsylvania" | NAME == "Pine township, Allegheny County, Pennsylvania" | NAME == "Thornbury township, Delaware County, Pennsylvania")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQyJyBmb3Igc3RhdGUgJ1BBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '42' for state 'PA'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfcGFfMjAyMSA8LSBjZW5zdXNfZGF0YV9wYV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZXxib3JvdWdoKVxcXFxiXCIsIFwiXCIsIGNpdHkpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBzdHJfc3F1aXNoKGNpdHkpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgYjAxMDAzXzAwMWUsIGIwMjAwMV8wMDNlLCBiMTkwMTNfMDAxZSkgJT4lXG4gIHJlbmFtZSh0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpXG5cbmNlbnN1c19kYXRhX3BhX3N1YmRpdmlzaW9uc18yMDIxIDwtIGNlbnN1c19kYXRhX3BhX3N1YmRpdmlzaW9uc18yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJjb3VudHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZXxtdW5pY2lwYWxpdHl8dG93bnNoaXApXFxcXGJcIiwgXCJcIiwgY2l0eSkpICU+JVxuICBtdXRhdGUoY2l0eSA9IHN0cl9zcXVpc2goY2l0eSkpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCBiMDEwMDNfMDAxZSwgYjAyMDAxXzAwM2UsIGIxOTAxM18wMDFlKSAlPiVcbiAgcmVuYW1lKHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSlcblxuY2Vuc3VzX2RhdGFfcGFfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfcGFfMjAyMSwgY2Vuc3VzX2RhdGFfcGFfc3ViZGl2aXNpb25zXzIwMjEpXG5cbiMgU3RlcCA1OiBTdGF0ZS1zcGVjaWZpYyBjbGVhbmluZyBvZiBjZW5zdXMgZGF0YSB0byBwcmVwYXJlIGZvciBqb2luIHdpdGggaG9tZXRvd25zL3Jvc3RlciBkYXRhLiBUaGlzIHBhcnQgaXMgZGlmZmVyZW50IGZvciBldmVyeSBzdGF0ZS4gVGhlIGZpcnN0IG11dGF0ZSBmdW5jdGlvbiBzaG91bGQgYmUgaW5jbHVkZWQgZm9yIGV2ZXJ5IHN0YXRlLCBqdXN0IG1vZGlmaWVkIGRlcGVuZGluZyBvbiB0aGUgc3RhdGUgbmFtZS4gQWRkaXRpb25hbCBtdXRhdGUgZnVuY3Rpb25zIG1heSBiZSBuZWVkZWQgZm9yIGluc3RhbmNlcyB3aGVuIHRoZSBjZW5zdXMgbmFtZXMgc29tZXRoaW5nIGluIGEgd2VpcmQgd2F5IHRoYXQgZG9lc24ndCBsaW5lIHVwIHdpdGggdGhlIGhvbWV0b3ducy5cbmNlbnN1c19kYXRhX3BhXzIwMjEgPC0gY2Vuc3VzX2RhdGFfcGFfMjAyMSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gY2FzZV93aGVuKFxuICAgIHN0YXRlID09ICdQZW5uc3lsdmFuaWEnIH4gXCJQQVwiKSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gJ0NyYW5iZXJyeScgfiBcIkNyYW5iZXJyeSBUb3duc2hpcFwiLFxuICAgIGdlb2lkID09ICc0MjA3OTMyNDE2JyB+IFwiSGFub3ZlciBUb3duc2hpcFwiLFxuICAgIGNpdHkgPT0gJ0xvd2VyIEd3eW5lZGQnIH4gXCJMb3dlciBHd3luZWRkIFRvd25zaGlwXCIsXG4gICAgZ2VvaWQgPT0gJzQyMDE3NTQ2ODgnIH4gXCJOb3J0aGFtcHRvbiBUb3duc2hpcFwiLFxuICAgIGNpdHkgPT0gJ05ldyBHYXJkZW4nIH4gXCJOZXcgR2FyZGVuIFRvd25zaGlwXCIsXG4gICAgY2l0eSA9PSAnTm9ydGggV2hpdGVoYWxsJyB+IFwiTm9ydGggV2hpdGVoYWxsIFRvd25zaGlwXCIsXG4gICAgY2l0eSA9PSAnUGluZScgfiBcIlBpbmUgVG93bnNoaXBcIixcbiAgICBjaXR5ID09ICdUaG9ybmJ1cnknIH4gXCJUaG9ybmJ1cnkgVG93bnNoaXBcIixcbiAgICBUUlVFIH4gY2l0eSkpXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cbmhvbWV0b3duc19wYV9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfcGEgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9wYV8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbiMgU3RlcCA3OiBOb3RpY2UgdGhlcmUgYXJlIGEgZmV3IE5BIHZhbHVlcy4gVGhpcyBoYXBwZW5zIHdoZW4gdGhlIGNlbnN1cyBkYXRhIGRvZXMgbm90IGpvaW4gd2l0aCB0aGUgaG9tZXRvd25zIGRhdGEsIHBlcmhhcHMgYmVjYXVzZSB0aGUgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCBvciBiZWNhdXNlIHRoZXJlIGlzIG5vIGNlbnN1cyBkYXRhIGZvciB0aGF0IHRvd24uIEZpcnN0LCBsZXQncyBmaW5kIHRoZSBOQSB2YWx1ZXMuXG5ob21ldG93bnNfcGFfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpXG5gYGAifQ== -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_pa_2021 <- census_data_pa_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|borough)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_pa_subdivisions_2021 <- census_data_pa_subdivisions_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "county", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|municipality|township)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_pa_2021 <- bind_rows(census_data_pa_2021, census_data_pa_subdivisions_2021)

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_pa_2021 <- census_data_pa_2021 %>%
  mutate(state = case_when(
    state == 'Pennsylvania' ~ "PA")) %>%
  mutate(city = case_when(
    city == 'Cranberry' ~ "Cranberry Township",
    geoid == '4207932416' ~ "Hanover Township",
    city == 'Lower Gwynedd' ~ "Lower Gwynedd Township",
    geoid == '4201754688' ~ "Northampton Township",
    city == 'New Garden' ~ "New Garden Township",
    city == 'North Whitehall' ~ "North Whitehall Township",
    city == 'Pine' ~ "Pine Township",
    city == 'Thornbury' ~ "Thornbury Township",
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_pa_complete <- distinct_hometowns_pa %>%
  left_join(census_data_pa_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_pa_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjEsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMSDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsxXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE2VlJTMjdDTUJBMUlTa05FaWdTdlFiWnNPbTJVdFZ1cTZxVjJGbkdjY0hDR1VleEVXWFZucVVuN0FtZzQ4Ukc0RzBqeFRQejVtaytiMTRmbDR2eGNrd0lHWkkwR1pCaGhpN0ozdCtlNXZjRUVRd0dKQ1c1czU5SW1xSGpndUlpY2Z1c1dMVS9nSWp3NU9VQjMwbUg5SC9oYlg3Q0QrM1V4VisvcnVYbzUvL3gxYmdaVjh5WWFLUnh4U3dyUDFwV2k0aWV0M3BmQXVMR3o1eDg0OVBQZVYwM2tJcE9paDZjYlhRdHJONEQ1ZEllS0ZlQ2dVL2RuVlBHTWl1dWNoT3JMVk8wVWV3Z1doTWFySVdXVlJqTE0zUVRnSlZpZkhzQlRHcFJTUVpVQXNkR2dkVndTenRtbU1MM29JMW9xZDNvbldGUUlYNk10aHZweGtvTnVGL2lUcDFGK2czYUNDaDI0UFNvNW55emcrMThzWEFpK3l1VDZQckJ6L3VlNmNuWHlueXRHd0ZyQ1dHRlRMR1ZVRDZZNG5VNjNjdW1sV0RETlJFMVphZFFRTGhXQWVtV0k4Yy85Z3lUck9JQ0FBQT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Gladwyne","2":"PA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[1]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgR2xhZHd5bmUsIFBBICgxOTAzNSksIHRoZSB6aXAgY29kZXMgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMxOTAzNS0xOTAzNS9cbmNlbnN1c19kYXRhX3ppcHNfcGFfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiemN0YVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIlpDVEE1IDE5MDM1XCIpICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiUEFcIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJaQ1RBNSAxOTAzNVwiIH4gXCJHbGFkd3luZVwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Gladwyne, PA (19035), the zip codes seems to be a good substitute: https://censusreporter.org/profiles/86000US19035-19035/
census_data_zips_pa_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 19035") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "PA") %>%
  mutate(city = case_when(
    city == "ZCTA5 19035" ~ "Gladwyne")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuXG5jZW5zdXNfZGF0YV9wYV8yMDIxIDwtIGJpbmRfcm93cyhjZW5zdXNfZGF0YV9wYV8yMDIxLCBjZW5zdXNfZGF0YV96aXBzX3BhXzIwMjEpXG4gXG5ob21ldG93bnNfcGFfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX3BhICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfcGFfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX3BhX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfcGEuY3N2XCIpXG5cbmBgYCJ9 -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.

census_data_pa_2021 <- bind_rows(census_data_pa_2021, census_data_zips_pa_2021)
 
hometowns_pa_complete <- distinct_hometowns_pa %>%
  left_join(census_data_pa_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_pa_complete, file = "hometowns_pa.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFNPVVRIIENBUk9MSU5BIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX3NjIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJTQ1wiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfc2MgPC0gZm9vdGJhbGxfcm9zdGVyc19zYyAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# SOUTH CAROLINA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_sc <- football_rosters_usa %>%
  filter(hometown_state_clean == "SC")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_sc <- football_rosters_sc %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfc2NfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJTQ1wiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_sc_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "SC",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQ1JyBmb3Igc3RhdGUgJ1NDJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '45' for state 'SC'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfc2NfMjAyMSA8LSBjZW5zdXNfZGF0YV9zY18yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV9zY18yMDIxIDwtIGNlbnN1c19kYXRhX3NjXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnU291dGggQ2Fyb2xpbmEnIH4gXCJTQ1wiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX3NjX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19zYyAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX3NjXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc19zY19jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_sc_2021 <- census_data_sc_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_sc_2021 <- census_data_sc_2021 %>%
  mutate(state = case_when(
    state == 'South Carolina' ~ "SC"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_sc_complete <- distinct_hometowns_sc %>%
  left_join(census_data_sc_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_sc_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjEsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMSDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsxXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE2VlJTMjdDTUJBMWdSUUZGUlNwdlFiWjBFWDNWRDFBUHhJN3l6Z3VXSmh4Wkp0U1Z1MVplc0tlQURwTzdBcThiYVI0WnQ0OHplZk4wOE5pTmxxTUNDRjlNc2g2cEoralMvTFhsOGZwUFVFRWd4NFprTUxiRHlUZG9PT0Q4aXh4UFRmczREUzhTNlZFa3N1ZTUvaU9XNlQ3eTJDTEUzNW9KejcrL1BGdGg5Ly9qeTlHenJsaTFpWWpqV3JtV1BWbTJGWWs5TUxvZlFXSTJ6Qno5b1ZQTitkbDNVZ3FXems2OEdhdHQ4THBQVkF1M1lGeUpSaUUxTzFmeWpybXhFVnU3TFJqaWphS0hZU3hzY0ZLYUZuSHNRSkROeEZZS3NZM1o4QjRLMnJKZ0VyZzJDaXlHdTVveTR4VGhCNjBFWWE2dGQ1WkJqWGl4MlM3b1c2YzFJRDdaZjdjZWFKZnp5UkF1UU92UnozbDZ4MXNwck03TDNLNE1rbXVILzJpNnprNGhWcDVxSFVsWUNVaHJwQXJ0aFFxQkJPOFRxdDcxUmdKTGw0VFVWdTFDa1dFYXhXUmRqbHkvQVhDRHdQaTVnSUFBQT09In0= -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Craytonville","2":"SC","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[1]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgQ3JheXRvbnZpbGxlLCBTQywgdGhlIGJsb2NrIGdyb3VwIHNlZW1zIHRvIGJlIGEgZ29vZCBzdWJzdGl0dXRlOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy8xNTAwMFVTNDUwMDcwMTE1MDEzLWJnLTMtdHJhY3QtMTE1MDEtYW5kZXJzb24tc2MvXG5jZW5zdXNfZGF0YV9jcmF5dG9udmlsbGVfc2NfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiYmxvY2sgZ3JvdXBcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJTQ1wiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIkJsb2NrIEdyb3VwIDMsIENlbnN1cyBUcmFjdCAxMTUuMDEsIEFuZGVyc29uIENvdW50eSwgU291dGggQ2Fyb2xpbmFcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJTQ1wiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIkJsb2NrIEdyb3VwIDMsIENlbnN1cyBUcmFjdCAxMTUuMDEsIEFuZGVyc29uIENvdW50eSwgU291dGggQ2Fyb2xpbmFcIiB+IFwiQ3JheXRvbnZpbGxlXCIpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgdG90YWxfcG9wLCBibGFja19wb3AsIG1lZGlhbl9pbmNvbWUsIHBjdF9ibGFjaylcbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Craytonville, SC, the block group seems to be a good substitute: https://censusreporter.org/profiles/15000US450070115013-bg-3-tract-11501-anderson-sc/
census_data_craytonville_sc_2021 <- get_acs(geography = "block group",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "SC",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Block Group 3, Census Tract 115.01, Anderson County, South Carolina") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "SC") %>%
  mutate(city = case_when(
    city == "Block Group 3, Census Tract 115.01, Anderson County, South Carolina" ~ "Craytonville")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQ1JyBmb3Igc3RhdGUgJ1NDJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '45' for state 'SC'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfc2NfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfc2NfMjAyMSwgY2Vuc3VzX2RhdGFfY3JheXRvbnZpbGxlX3NjXzIwMjEpXG4gXG5ob21ldG93bnNfc2NfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX3NjICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfc2NfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG5ob21ldG93bnNfc2NfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpICNJZiB0aGlzIGlzIG5vdCBwcm9kdWNpbmcgYW4gZW1wdHkgZGF0YWZyYW1lLCBnbyBiYWNrIGFuZCBjb250aW51ZSB0byB3b3JrIG9uIE5BIHZhbHVlc1xuYGBgIn0= -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_sc_2021 <- bind_rows(census_data_sc_2021, census_data_craytonville_sc_2021)
 
hometowns_sc_complete <- distinct_hometowns_sc %>%
  left_join(census_data_sc_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_sc_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFMjY2QUdxSHFCcXBld1F3VFJHd1lBQUs4M2wwMklNVGMwcWJJYjVaalQvUE41Zjk3dHlYd0lBMWlCZlpXQU4zUmZBejQrMzVnVTQ0cHdNNUtDWTdMZEwycnJQNU5SZ2Z0RldpYis1enk0RUlPSFltRkFrd3JMREZyZGZHZzgwU1MrMFBMZkNjWFBUWDlhTHdkbzNQY050THdkcTVWa2d3dXdGRVU2eENLR252NUN4Mk5KRnJMTFNZbzRVeHhlcVRSUTRVc202MkU3SWtDcUNBOGZrOUE5VUErMFlGb2dKNG9SaWxpSVcrY3pZUmRCQWltcGtlemthTERySHI4bDBqMUpaSm9XYmJ6VWRCU1o3eTNRQzZsRk0rK2dhMG8vaTFPeWVwK1g2K08yQzZiK1lOZk9mVUF1R1dnOVVISm1JSTBDT0Q1UUhaK091NHZmZUtzMkVqVmQwMUxSK1E1RVF5U1B4dzRIckx3YmJyNkNNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX3NjX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfc2MuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_sc_complete, file = "hometowns_sc.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFRFTk5FU1NFRSBIT01FVE9XTlNcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc190biA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiVE5cIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX3RuIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdG4gJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# TENNESSEE HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_tn <- football_rosters_usa %>%
  filter(hometown_state_clean == "TN")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_tn <- football_rosters_tn %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfdG5fMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJUTlwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_tn_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "TN",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQ3JyBmb3Igc3RhdGUgJ1ROJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '47' for state 'TN'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfdG5fMjAyMSA8LSBjZW5zdXNfZGF0YV90bl8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuYGBgIn0= -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_tn_2021 <- census_data_tn_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiV2FybmluZzogRXhwZWN0ZWQgMiBwaWVjZXMuIEFkZGl0aW9uYWwgcGllY2VzIGRpc2NhcmRlZCBpbiAxIHJvd3MgWzI3NF0uXG4ifQ== -->

```
Warning: Expected 2 pieces. Additional pieces discarded in 1 rows [274].
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDU6IFN0YXRlLXNwZWNpZmljIGNsZWFuaW5nIG9mIGNlbnN1cyBkYXRhIHRvIHByZXBhcmUgZm9yIGpvaW4gd2l0aCBob21ldG93bnMvcm9zdGVyIGRhdGEuIFRoaXMgcGFydCBpcyBkaWZmZXJlbnQgZm9yIGV2ZXJ5IHN0YXRlLiBUaGUgZmlyc3QgbXV0YXRlIGZ1bmN0aW9uIHNob3VsZCBiZSBpbmNsdWRlZCBmb3IgZXZlcnkgc3RhdGUsIGp1c3QgbW9kaWZpZWQgZGVwZW5kaW5nIG9uIHRoZSBzdGF0ZSBuYW1lLiBBZGRpdGlvbmFsIG11dGF0ZSBmdW5jdGlvbnMgbWF5IGJlIG5lZWRlZCBmb3IgaW5zdGFuY2VzIHdoZW4gdGhlIGNlbnN1cyBuYW1lcyBzb21ldGhpbmcgaW4gYSB3ZWlyZCB3YXkgdGhhdCBkb2Vzbid0IGxpbmUgdXAgd2l0aCB0aGUgaG9tZXRvd25zLlxuY2Vuc3VzX2RhdGFfdG5fMjAyMSA8LSBjZW5zdXNfZGF0YV90bl8yMDIxICU+JVxuICBtdXRhdGUoc3RhdGUgPSBjYXNlX3doZW4oXG4gICAgc3RhdGUgPT0gJ1Rlbm5lc3NlZScgfiBcIlROXCIpKSAlPiUgXG4gICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09ICdOYXNodmlsbGUtRGF2aWRzb24gbWV0cm9wb2xpdGFuIGdvdmVybm1lbnQgKGJhbGFuY2UpJ34gXCJOYXNodmlsbGVcIixcbiAgICBUUlVFIH4gY2l0eSkpXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cbmhvbWV0b3duc190bl9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfdG4gJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV90bl8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbiMgU3RlcCA3OiBOb3RpY2UgdGhlcmUgYXJlIGEgZmV3IE5BIHZhbHVlcy4gVGhpcyBoYXBwZW5zIHdoZW4gdGhlIGNlbnN1cyBkYXRhIGRvZXMgbm90IGpvaW4gd2l0aCB0aGUgaG9tZXRvd25zIGRhdGEsIHBlcmhhcHMgYmVjYXVzZSB0aGUgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCBvciBiZWNhdXNlIHRoZXJlIGlzIG5vIGNlbnN1cyBkYXRhIGZvciB0aGF0IHRvd24uIEZpcnN0LCBsZXQncyBmaW5kIHRoZSBOQSB2YWx1ZXMuXG5ob21ldG93bnNfdG5fY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpXG5gYGAifQ== -->

```r
# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_tn_2021 <- census_data_tn_2021 %>%
  mutate(state = case_when(
    state == 'Tennessee' ~ "TN")) %>% 
   mutate(city = case_when(
    city == 'Nashville-Davidson metropolitan government (balance)'~ "Nashville",
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_tn_complete <- distinct_hometowns_tn %>%
  left_join(census_data_tn_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_tn_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjIsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMiDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsyXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE3VlN5MjdDTUJCMFFsSWFKRkFrK2h2a2dpcjEzc2V4aDRwSzNDemp1R0JoN01nMm9wemFiK2tYOWd1ZzYrQkZrSHNqT2Q2ZEhlMTZ4bjU3bWs4SDh3RWhwRWV5TkNHOUhFS1N2ODllSmc4RUVFZ1NrcEVpN0o5QUdrTVFraEpXR2d1M2o4YmF2VGM2NXRrenExMkhrODVlTHlKQ2htMHRORCt0TXViRkViNkxmUlR3cjk5d3FQNFA3ditQWHduUHVXSU9CU0U0cUpsbjFZZGxHOUdoRjlic0tnMjRRNTNmOEFNNWgyNWZKSld0cVNkd3ZESWI0YzFPVXk3OW5uSWxHUHA2ZHk0NXo3eTRxZzI5OFV6UlJyRzlzQTRITElXUk5SNHJNa3lEd0VJeHZyNEFoaHRSUzZhcDFCd0dJYXZobnJaTVBFV2NRUnRocVYrWnJXTzZCcnlycm04YUw0MEdmV2w0TkhuSHY4UjJnSEtyZ3gvMWhLKzJlajJaM2dlVDQrc2cwY2trdmhLTWk5UE03Qmg3NWJIWGpkQkxxVkZDcnRoQ3FKaU00SFphMzZ2R1N1M3hOZ0YxVmVzUUl0d29SRnB4NVBBSExyQVpMeXdEQUFBPSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Corryton","2":"TN","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Eads","2":"TN","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[2]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgQ29ycnl0b24sIFROICgzNzcyMSkgYW5kIEVhZHMsIFROICgzODAyOCksIHRoZSB6aXAgY29kZXMgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMzNzcyMS0zNzcyMS9cbmNlbnN1c19kYXRhX3ppcHNfdG5fMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiemN0YVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIlpDVEE1IDM3NzIxXCIgfCBuYW1lID09IFwiWkNUQTUgMzgwMjhcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJUTlwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDM3NzIxXCIgfiBcIkNvcnJ5dG9uXCIsXG4gICAgY2l0eSA9PSBcIlpDVEE1IDM4MDI4XCIgfiBcIkVhZHNcIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Corryton, TN (37721) and Eads, TN (38028), the zip codes seems to be a good substitute: https://censusreporter.org/profiles/86000US37721-37721/
census_data_zips_tn_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 37721" | name == "ZCTA5 38028") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "TN") %>%
  mutate(city = case_when(
    city == "ZCTA5 37721" ~ "Corryton",
    city == "ZCTA5 38028" ~ "Eads")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfdG5fMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfdG5fMjAyMSwgY2Vuc3VzX2RhdGFfemlwc190bl8yMDIxKVxuIFxuaG9tZXRvd25zX3RuX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc190biAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX3RuXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDEwOiBJZiBuZWVkZWQsIHVuY29tbWVudCBvdXQgdG8gY3JlYXRlIGEgQ1NWXG4jd3JpdGVfY3N2KGhvbWV0b3duc190bl9jb21wbGV0ZSwgZmlsZSA9IFwiaG9tZXRvd25zX3RuLmNzdlwiKVxuXG5gYGAifQ== -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_tn_2021 <- bind_rows(census_data_tn_2021, census_data_zips_tn_2021)
 
hometowns_tn_complete <- distinct_hometowns_tn %>%
  left_join(census_data_tn_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_tn_complete, file = "hometowns_tn.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFRFWEFTIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX3R4IDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJUWFwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfdHggPC0gZm9vdGJhbGxfcm9zdGVyc190eCAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# TEXAS HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_tx <- football_rosters_usa %>%
  filter(hometown_state_clean == "TX")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_tx <- football_rosters_tx %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfdHhfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJUWFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_tx_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "TX",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQ4JyBmb3Igc3RhdGUgJ1RYJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '48' for state 'TX'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfdHhfMjAyMSA8LSBjZW5zdXNfZGF0YV90eF8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV90eF8yMDIxIDwtIGNlbnN1c19kYXRhX3R4XzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnVGV4YXMnIH4gXCJUWFwiKSkgJT4lXG4gIGZpbHRlcihjaXR5ICE9IFwiTWVzcXVpdGVcIiB8IHRvdGFsX3BvcCAhPSAxODEpICNSZW1vdmluZyB0aGUgc2Vjb25kIE1lc3F1aXRlLCBUWCB0aGF0IGlzIGEgQ0RQXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cbmhvbWV0b3duc190eF9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfdHggJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV90eF8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbiMgU3RlcCA3OiBOb3RpY2UgdGhlcmUgYXJlIGEgZmV3IE5BIHZhbHVlcy4gVGhpcyBoYXBwZW5zIHdoZW4gdGhlIGNlbnN1cyBkYXRhIGRvZXMgbm90IGpvaW4gd2l0aCB0aGUgaG9tZXRvd25zIGRhdGEsIHBlcmhhcHMgYmVjYXVzZSB0aGUgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCBvciBiZWNhdXNlIHRoZXJlIGlzIG5vIGNlbnN1cyBkYXRhIGZvciB0aGF0IHRvd24uIEZpcnN0LCBsZXQncyBmaW5kIHRoZSBOQSB2YWx1ZXMuXG5ob21ldG93bnNfdHhfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpXG5gYGAifQ== -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_tx_2021 <- census_data_tx_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_tx_2021 <- census_data_tx_2021 %>%
  mutate(state = case_when(
    state == 'Texas' ~ "TX")) %>%
  filter(city != "Mesquite" | total_pop != 181) #Removing the second Mesquite, TX that is a CDP

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_tx_complete <- distinct_hometowns_tx %>%
  left_join(census_data_tx_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_tx_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjUsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiNSDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFs1XSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE5VlRzVzdDTUJDOVFGSVVKQkFTN2Q0ZklBdFMxYmxVWFNwMXFLaktGaG5IQlF0alI0NFJ6ZFIrUzcrd2V5WG9PYkVSWkNsckl6bStlL2R5OXIyN1BOL1B4dDFaRndEYUVMWUNhRWRvUXZReWZSamRBaUxvQkJCQ2JQZDNKQTNSc003QXNsd2d1dE9LcnB6VG1aUzVaa1hoWTQrQ2NlbWMrSWx0cnlkRXN0SUI0U3NSb3BHdE5aMmRiUUgwcWk4eEU2NHJpMVlYcnRmQXhlSTlQbWZzZmN2LytMWUNkTDcrMnY4Ly82UzVFUlVFbTFhTDVzRnVSZ3hKM2pSWnN3WTkxbXFiU01RTDE0UFdKNzVReHA5bVhrK3llV01IRHBkcXpZemF5cFJ5VTZaVU1PSkg1UElRS2d3eDdDVFdNOG9Ra2VhQ2xFd2ZCbXpCRk0vOHRSeEQ1UjZZQzBKWFIwQnZ6VEpPWk1vbHhZTThLNmNtclpqK0Z1Nk1OR2M2TlV1MUtZak1FTjgxcXV1bzNIQWxzYjdXMEEzYnNYNkJiZ0NEamJSNlpDTzYzTWpWYUh4alJZWjZXc0VwR2JoRTNvN3JNOE05blA0bkYwd3V1UFFsUklMTW1YQk9IN3RUNlo3a21rdmp1NGxva1ZRS2VZUXE0WkdxT05qOUFnMnBZN0lRQkFBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Brock","2":"TX","3":"4","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Cypress","2":"TX","3":"21","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Klein","2":"TX","3":"2","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"New Caney","2":"TX","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Wall","2":"TX","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[5]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgQ3lwcmVzcywgVFggKDc3NDI5KSwgTmV3IENhbmV5LCBUWCAoNzczNTcpLCBhbmQgV2FsbCwgVFggKDc2OTU3KSwgdGhlIHppcCBjb2RlcyBzZWVtcyB0byBiZSBnb29kIHN1YnN0aXR1dGVzOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTNzc0MjktNzc0MjkvIGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVM3NzM1Ny03NzM1Ny8gaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvODYwMDBVUzc2OTU3LTc2OTU3L1xuY2Vuc3VzX2RhdGFfemlwc190eF8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgNzc0MjlcIiB8IG5hbWUgPT0gXCJaQ1RBNSA3NzM1N1wiIHwgbmFtZSA9PSBcIlpDVEE1IDc2OTU3XCIpICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiVFhcIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJaQ1RBNSA3NzQyOVwiIH4gXCJDeXByZXNzXCIsXG4gICAgY2l0eSA9PSBcIlpDVEE1IDc3MzU3XCIgfiBcIk5ldyBDYW5leVwiLFxuICAgIGNpdHkgPT0gXCJaQ1RBNSA3Njk1N1wiIH4gXCJXYWxsXCIpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgdG90YWxfcG9wLCBibGFja19wb3AsIG1lZGlhbl9pbmNvbWUsIHBjdF9ibGFjaylcbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Cypress, TX (77429), New Caney, TX (77357), and Wall, TX (76957), the zip codes seems to be good substitutes: https://censusreporter.org/profiles/86000US77429-77429/ https://censusreporter.org/profiles/86000US77357-77357/ https://censusreporter.org/profiles/86000US76957-76957/
census_data_zips_tx_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 77429" | name == "ZCTA5 77357" | name == "ZCTA5 76957") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "TX") %>%
  mutate(city = case_when(
    city == "ZCTA5 77429" ~ "Cypress",
    city == "ZCTA5 77357" ~ "New Caney",
    city == "ZCTA5 76957" ~ "Wall")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBGb3IgQnJvY2ssIFRYLCBhbmQgS2xlaW4sIFRYLCB1c2VkIHRoZSBzY2hvb2wgZGlzdHJpY3RzIGJlY2F1c2UgYWxsIHBsYXllcnMgd2VudCB0byB0aGUgc2FtZSBoaWdoIHNjaG9vbDogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvOTcwMDBVUzQ4MTE0NjAtYnJvY2staW5kZXBlbmRlbnQtc2Nob29sLWRpc3RyaWN0LXR4LyBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy85NzAwMFVTNDgyNTc0MC1rbGVpbi1pbmRlcGVuZGVudC1zY2hvb2wtZGlzdHJpY3QtdHgvIFxuY2Vuc3VzX2RhdGFfc2RfdHhfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwic2Nob29sIGRpc3RyaWN0ICh1bmlmaWVkKVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RhdGUgPSBcIlRYXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiQnJvY2sgSW5kZXBlbmRlbnQgU2Nob29sIERpc3RyaWN0LCBUZXhhc1wiIHwgbmFtZSA9PSBcIktsZWluIEluZGVwZW5kZW50IFNjaG9vbCBEaXN0cmljdCwgVGV4YXNcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJUWFwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIkJyb2NrIEluZGVwZW5kZW50IFNjaG9vbCBEaXN0cmljdCwgVGV4YXNcIiB+IFwiQnJvY2tcIixcbiAgICBjaXR5ID09IFwiS2xlaW4gSW5kZXBlbmRlbnQgU2Nob29sIERpc3RyaWN0LCBUZXhhc1wiIH4gXCJLbGVpblwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r
# For Brock, TX, and Klein, TX, used the school districts because all players went to the same high school: https://censusreporter.org/profiles/97000US4811460-brock-independent-school-district-tx/ https://censusreporter.org/profiles/97000US4825740-klein-independent-school-district-tx/ 
census_data_sd_tx_2021 <- get_acs(geography = "school district (unified)",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "TX",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Brock Independent School District, Texas" | name == "Klein Independent School District, Texas") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "TX") %>%
  mutate(city = case_when(
    city == "Brock Independent School District, Texas" ~ "Brock",
    city == "Klein Independent School District, Texas" ~ "Klein")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQ4JyBmb3Igc3RhdGUgJ1RYJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '48' for state 'TX'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfdHhfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfdHhfMjAyMSwgY2Vuc3VzX2RhdGFfemlwc190eF8yMDIxLCBjZW5zdXNfZGF0YV9zZF90eF8yMDIxKVxuIFxuaG9tZXRvd25zX3R4X2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc190eCAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX3R4XzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuaG9tZXRvd25zX3R4X2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKSAjSWYgdGhpcyBpcyBub3QgcHJvZHVjaW5nIGFuIGVtcHR5IGRhdGFmcmFtZSwgZ28gYmFjayBhbmQgY29udGludWUgdG8gd29yayBvbiBOQSB2YWx1ZXNcbmBgYCJ9 -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_tx_2021 <- bind_rows(census_data_tx_2021, census_data_zips_tx_2021, census_data_sd_tx_2021)
 
hometowns_tx_complete <- distinct_hometowns_tx %>%
  left_join(census_data_tx_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_tx_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlIzV3JESUJUSFRSczNFa2dKZEsrUjNCVEdIbURzQWNZR3ZSTnJYQ00xS21ybyt2TGRqTkYxOGFyZUhNL3ZITTcvZkx5LzduZmx2Z1FBckVHK3lzQWF1aStBbng5dnpRdHd4RGtaeUVFeDJXK1h0SFdmeWFuQi9LS3RFbjl6bjEwSVFNS3hNYUZJaEdXSExXNi9OQjVva2w1b2VXNkY0K2FtdjZ3WGc3VnZlb2JiWGc3VXlyTkFoTmtMSXB4aUVVSlBmeUZqc2FXTFdHV2x4Undwamk5VW15aHdwSkoxc1oyUUlWVUVCNDdKNlIrb0J0b3hMQkFUeEFuRkxFVXM4cG14aTZDQkZOWEk5bkkwV0hTT1g1UHBIcVd5VEFvMzMybzZDa3oybHVrRTFLT1k5dEUxcEIvRnFkazlUOHYxOGRzRjAzOHhhK1kvb1JZTXRSNm9PRElSUjRBY0h5Z1B6c1pkeGUrOVZab0pHNi9vcUduOWhpSWhra2ZpaHdQWFgwS2ZFMmFNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX3R4X2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfdHguY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_tx_complete, file = "hometowns_tx.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFVUQUggSE9NRVRPV05TXG5cbiMgU3RlcCAxOiBGaWx0ZXIgZm9yIHRoZSBzdGF0ZSdzIHBsYXllcnNcbmZvb3RiYWxsX3Jvc3RlcnNfdXQgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiA9PSBcIlVUXCIpXG5cbiMgU3RlcCAyOiBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc191dCA8LSBmb290YmFsbF9yb3N0ZXJzX3V0ICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbF9wbGF5ZXJzID0gbigpKVxuYGBgIn0= -->

```r

# UTAH HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_ut <- football_rosters_usa %>%
  filter(hometown_state_clean == "UT")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_ut <- football_rosters_ut %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfdXRfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJVVFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_ut_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "UT",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQ5JyBmb3Igc3RhdGUgJ1VUJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '49' for state 'UT'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfdXRfMjAyMSA8LSBjZW5zdXNfZGF0YV91dF8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV91dF8yMDIxIDwtIGNlbnN1c19kYXRhX3V0XzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnVXRhaCcgfiBcIlVUXCIpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSAnSGViZXInIH4gXCJIZWJlciBDaXR5XCIsXG4gICAgVFJVRSB+IGNpdHkpKVxuXG4jIFN0ZXAgNjogSm9pbiB0aGUgY2Vuc3VzIGRhdGEgdG8gdGhlIGxpc3Qgb2YgaG9tZXRvd25zLiBBbHNvIGNyZWF0ZSBhIGNvbHVtbiB0aGF0IHRlbGxzIHVzIGhvdyBtYW55IHBlb3BsZSBhcmUgZWxpdGUgY29sbGVnZSBmb290YmFsbCBwbGF5ZXJzIGZvciBldmVyeSAxLDAwMCByZXNpZGVudHMuXG5ob21ldG93bnNfdXRfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX3V0ICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfdXRfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIFN0ZXAgNzogTm90aWNlIHRoZXJlIGFyZSBhIGZldyBOQSB2YWx1ZXMuIFRoaXMgaGFwcGVucyB3aGVuIHRoZSBjZW5zdXMgZGF0YSBkb2VzIG5vdCBqb2luIHdpdGggdGhlIGhvbWV0b3ducyBkYXRhLCBwZXJoYXBzIGJlY2F1c2UgdGhlIGhvbWV0b3duIGlzIG1pc3NwZWxsZWQgb3IgYmVjYXVzZSB0aGVyZSBpcyBubyBjZW5zdXMgZGF0YSBmb3IgdGhhdCB0b3duLiBGaXJzdCwgbGV0J3MgZmluZCB0aGUgTkEgdmFsdWVzLlxuaG9tZXRvd25zX3V0X2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKVxuYGBgIn0= -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_ut_2021 <- census_data_ut_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_ut_2021 <- census_data_ut_2021 %>%
  mutate(state = case_when(
    state == 'Utah' ~ "UT")) %>%
  mutate(city = case_when(
    city == 'Heber' ~ "Heber City",
    TRUE ~ city))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_ut_complete <- distinct_hometowns_ut %>%
  left_join(census_data_ut_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_ut_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFMFc3UUdxSHFCcXBld1F3VFJHd1lBQUs4M2wwMklNVGMwcWJJYjVaalQvUE41Zjk3dHlYd0lBMWlCZlpXQU4zUmZBejQrMzVnVTQ0cHdNNUtDWTdMZEwycnJQNU5SZ2Z0RldpYis1enk0RUlPSFltRkFrd3JMREZyZGZHZzgwU1MrMFBMZkNjWFBUWDlhTHdkbzNQY050THdkcTVWa2d3dXdGRVU2eENLR252NUN4Mk5KRnJMTFNZbzRVeHhlcVRSUTRVc202MkU3SWtDcUNBOGZrOUE5VUErMFlGb2dKNG9SaWxpSVcrY3pZUmRCQWltcGtlemthTERySHI4bDBqMUpaSm9XYmJ6VWRCU1o3eTNRQzZsRk0rK2dhMG8vaTFPeWVwK1g2K08yQzZiK1lOZk9mVUF1R1dnOVVISm1JSTBDT0Q1UUhaK091NHZmZUtzMkVqVmQwMUxSK1E1RVF5U1B4dzRIckwyQzlUUVdNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cbiMgSW4gdGhpcyBjYXNlLCB0aGVyZSB3YXMgYSBkaXNjcmVwYW5jeSBiZXR3ZWVuIG91ciBob21ldG93biBkYXRhLCB3aGljaCBoYWQgYSBjaXR5IG5hbWVkIEhlYmVyIENpdHksIGFuZCB0aGUgY2Vuc3VzIGRhdGEsIHdoaWNoIHJlZmVycmVkIHRvIHRoYXQgdG93biBhcyBIZWJlci4gV2UgZml4ZWQgaXQgYnkgZ29pbmcgYmFjayB0byBTdGVwICM1IGFuZCBhZGRpbmcgaW4gYSBjYXNlX3doZW4gc3RhdGVtZW50IGZvciBIZWJlci5cblxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuIyBOb3QgYXBwbGljYWJsZSBmb3IgVXRhaFxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX3V0X2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfdXQuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.
# In this case, there was a discrepancy between our hometown data, which had a city named Heber City, and the census data, which referred to that town as Heber. We fixed it by going back to Step #5 and adding in a case_when statement for Heber.

# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
# Not applicable for Utah

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_ut_complete, file = "hometowns_ut.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFZJUkdJTklBIEhPTUVUT1dOU1xuXG4jIFN0ZXAgMTogRmlsdGVyIGZvciB0aGUgc3RhdGUncyBwbGF5ZXJzXG5mb290YmFsbF9yb3N0ZXJzX3ZhIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhICU+JVxuICBmaWx0ZXIoaG9tZXRvd25fc3RhdGVfY2xlYW4gPT0gXCJWQVwiKVxuXG4jIFN0ZXAgMjogR2V0IGEgbGlzdCBvZiBhbGwgdGhlIHVuaXF1ZSBob21ldG93bnMgaW4gdGhlIHN0YXRlXG5kaXN0aW5jdF9ob21ldG93bnNfdmEgPC0gZm9vdGJhbGxfcm9zdGVyc192YSAlPiVcbiAgZ3JvdXBfYnkoaG9tZXRvd25fY2l0eV9jbGVhbiwgaG9tZXRvd25fc3RhdGVfY2xlYW4pICU+JVxuICBzdW1tYXJpc2UodG90YWxfcGxheWVycyA9IG4oKSlcbmBgYCJ9 -->

```r

# VIRGINIA HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_va <- football_rosters_usa %>%
  filter(hometown_state_clean == "VA")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_va <- football_rosters_va %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfdmFfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJWQVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_va_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "VA",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzUxJyBmb3Igc3RhdGUgJ1ZBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '51' for state 'VA'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfdmFfMjAyMSA8LSBjZW5zdXNfZGF0YV92YV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV92YV8yMDIxIDwtIGNlbnN1c19kYXRhX3ZhXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnVmlyZ2luaWEnIH4gXCJWQVwiKSlcblxuIyBTdGVwIDY6IEpvaW4gdGhlIGNlbnN1cyBkYXRhIHRvIHRoZSBsaXN0IG9mIGhvbWV0b3ducy4gQWxzbyBjcmVhdGUgYSBjb2x1bW4gdGhhdCB0ZWxscyB1cyBob3cgbWFueSBwZW9wbGUgYXJlIGVsaXRlIGNvbGxlZ2UgZm9vdGJhbGwgcGxheWVycyBmb3IgZXZlcnkgMSwwMDAgcmVzaWRlbnRzLlxuaG9tZXRvd25zX3ZhX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc192YSAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX3ZhXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc192YV9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_va_2021 <- census_data_va_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_va_2021 <- census_data_va_2021 %>%
  mutate(state = case_when(
    state == 'Virginia' ~ "VA"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_va_complete <- distinct_hometowns_va %>%
  left_join(census_data_va_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_va_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjYsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiNiDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFs2XSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE5MVR6VzdDTUF4T1N3dHJOUkFTZXdCZWdGNjRjSVZORTdkSit4TzNLbXNEalFoSmxRUXhUdHV6N0FsMzNnSG1sQVJCVDl1T3E5VGEvdXpZOVJmNy9tWTJqR2N4UXFpQkF0OURqUkJVRkQ0OTNnNUdDQkF3UEJTZ3lNaFhDT3FCWW93dXZFM3JhSTYzakdodHJkWkVVcVhGeHBxWEV5azJYUFVmdEpERVlkY0ZVWnJJT1NVc3QxZzR4VnVpckhGeGg1ZjlLV1dzVnNsL0h2OUJRNmhkNVRDdEFHSmxZS1YzckFHZDdlSDVoZXlZYzIrZmhyTFd4MC9sL3o5M05qWmh4ckJTbG1RSHhqbldPSmxMdkNLMThBakdKZUdBSzN0di9qdDhnTzZ2ZWw0WFpQSkdGdXdWWWtWZytIaWFVYjFOTTBZd3Q2NnJvMHRwck1tWnI2MkZ4aXd0R2N5Z2RFTVlMb2lnYmp3akd5RktCN3d3bkMxUGdQYUs1QlR6bFBJTUNybW9NdE5wRmVuK3d0WklTeUpUWFlpMXdqd0hmRmZycmlWS1RRV0gvbnl6Y21HTlAwL1dnTzZhR3o3eVFWYXMrWEl3SEJtUzBXRzZrV1hTNk0wVFBUclVEUFkyVitqMm1mQUY1YTZGa09FWHdxelJNY3RzZUU5S1NibGIrUmhRbFZRTU9TUVR6Q0ZWYzJqM0RSZGs4UnBxQkFBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Aylett","2":"VA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Bristow","2":"VA","3":"2","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Browns Store","2":"VA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Chesterfield","2":"VA","3":"4","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Hayes","2":"VA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Oak Hill","2":"VA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[6]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgQXlsZXR0LCBWQSAoMjMwMDkpLCBCcmlzdG93LCBWQSAoMjAxMzYpLCBIYXllcywgVkEgKDIzMDcyKSwgT2FrIEhpbGwsIFZBICgyMjAzMCksIGFuZCBDaGVzdGVyZmllbGQsIFZBICgyMzgzMikgdGhlIHppcCBjb2RlcyBzZWVtcyB0byBiZSBnb29kIHN1YnN0aXR1dGVzOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTMjMwMDktMjMwMDkvIGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMyMDEzNi0yMDEzNi8gaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvODYwMDBVUzIzMDcyLTIzMDcyLyBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy84NjAwMFVTMjIwMzAtMjIwMzAvIGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMyMzgzMi0yMzgzMi9cbmNlbnN1c19kYXRhX3ppcHNfdmFfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiemN0YVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBmaWx0ZXIobmFtZSA9PSBcIlpDVEE1IDIzMDA5XCIgfCBuYW1lID09IFwiWkNUQTUgMjAxMzZcIiB8IG5hbWUgPT0gXCJaQ1RBNSAyMzA3MlwiIHwgbmFtZSA9PSBcIlpDVEE1IDIyMDMwXCIgfCBuYW1lID09IFwiWkNUQTUgMjM4MzJcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJWQVwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDIzMDA5XCIgfiBcIkF5bGV0dFwiLFxuICAgIGNpdHkgPT0gXCJaQ1RBNSAyMDEzNlwiIH4gXCJCcmlzdG93XCIsXG4gICAgY2l0eSA9PSBcIlpDVEE1IDIzMDcyXCIgfiBcIkhheWVzXCIsXG4gICAgY2l0eSA9PSBcIlpDVEE1IDIyMDMwXCIgfiBcIk9hayBIaWxsXCIsXG4gICAgY2l0eSA9PSBcIlpDVEE1IDIzODMyXCIgfiBcIkNoZXN0ZXJmaWVsZFwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Aylett, VA (23009), Bristow, VA (20136), Hayes, VA (23072), Oak Hill, VA (22030), and Chesterfield, VA (23832) the zip codes seems to be good substitutes: https://censusreporter.org/profiles/86000US23009-23009/ https://censusreporter.org/profiles/86000US20136-20136/ https://censusreporter.org/profiles/86000US23072-23072/ https://censusreporter.org/profiles/86000US22030-22030/ https://censusreporter.org/profiles/86000US23832-23832/
census_data_zips_va_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 23009" | name == "ZCTA5 20136" | name == "ZCTA5 23072" | name == "ZCTA5 22030" | name == "ZCTA5 23832") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "VA") %>%
  mutate(city = case_when(
    city == "ZCTA5 23009" ~ "Aylett",
    city == "ZCTA5 20136" ~ "Bristow",
    city == "ZCTA5 23072" ~ "Hayes",
    city == "ZCTA5 22030" ~ "Oak Hill",
    city == "ZCTA5 23832" ~ "Chesterfield")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBCcm93bnMgU3RvcmUsIFZBIGlzIGEgY291bnR5IHN1YmRpdmlzaW9uOiBodHRwczovL2NlbnN1c3JlcG9ydGVyLm9yZy9wcm9maWxlcy8wNjAwMFVTMTkxNjM5MzQyMC1wbGVhc2FudC12YWxsZXktdG93bnNoaXAtc2NvdHQtY291bnR5LWlhL1xuY2Vuc3VzX2RhdGFfYnJvd25zX3ZhXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcImNvdW50eSBzdWJkaXZpc2lvblwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RhdGUgPSBcIlZpcmdpbmlhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBjb3VudHkgPSBcIkx1bmVuYnVyZyBDb3VudHlcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgZmlsdGVyKG5hbWUgPT0gXCJCcm93bnMgU3RvcmUgZGlzdHJpY3QsIEx1bmVuYnVyZyBDb3VudHksIFZpcmdpbmlhXCIpICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiVkFcIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJCcm93bnMgU3RvcmUgZGlzdHJpY3QsIEx1bmVuYnVyZyBDb3VudHksIFZpcmdpbmlhXCIgfiBcIkJyb3ducyBTdG9yZVwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r
# Browns Store, VA is a county subdivision: https://censusreporter.org/profiles/06000US1916393420-pleasant-valley-township-scott-county-ia/
census_data_browns_va_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "Virginia",
                           county = "Lunenburg County",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Browns Store district, Lunenburg County, Virginia") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "VA") %>%
  mutate(city = case_when(
    city == "Browns Store district, Lunenburg County, Virginia" ~ "Browns Store")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzUxJyBmb3Igc3RhdGUgJ1ZpcmdpbmlhJ1xuVXNpbmcgRklQUyBjb2RlICcxMTEnIGZvciAnTHVuZW5idXJnIENvdW50eSdcbiJ9 -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '51' for state 'Virginia'
Using FIPS code '111' for 'Lunenburg County'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfdmFfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfdmFfMjAyMSwgY2Vuc3VzX2RhdGFfemlwc192YV8yMDIxLCBjZW5zdXNfZGF0YV9icm93bnNfdmFfMjAyMSlcbiBcbmhvbWV0b3duc192YV9jb21wbGV0ZSA8LSBkaXN0aW5jdF9ob21ldG93bnNfdmEgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV92YV8yMDIxLCBieSA9IGMoXCJob21ldG93bl9jaXR5X2NsZWFuXCIgPSBcImNpdHlcIiwgXCJob21ldG93bl9zdGF0ZV9jbGVhblwiID0gXCJzdGF0ZVwiKSkgJT4lXG4gIG11dGF0ZShwbGF5ZXJzX3Blcl90aG91c2FuZCA9IHJvdW5kKCh0b3RhbF9wbGF5ZXJzKjEwMDApL3RvdGFsX3BvcCwxKSkgJT4lXG4gIGFycmFuZ2UoZGVzYyhwbGF5ZXJzX3Blcl90aG91c2FuZCkpXG5cbmhvbWV0b3duc192YV9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSkgI0lmIHRoaXMgaXMgbm90IHByb2R1Y2luZyBhbiBlbXB0eSBkYXRhZnJhbWUsIGdvIGJhY2sgYW5kIGNvbnRpbnVlIHRvIHdvcmsgb24gTkEgdmFsdWVzXG5gYGAifQ== -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_va_2021 <- bind_rows(census_data_va_2021, census_data_zips_va_2021, census_data_browns_va_2021)
 
hometowns_va_complete <- distinct_hometowns_va %>%
  left_join(census_data_va_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_va_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFMDJPVURWQTFTdGxCMGltTVFvR0JCZ3BibDhXb3locVZtVnpURGZqT2FmeC92cllWY2VTZ0RBR3VTckRLeWgrd0w0K2ZIVzdJRWp6c2xBRG9ySmZybWtyZnRNVGczbUYyMlYrSnYvMllVQUpCd2JFNHBFV0hiWTR2YWs4VUNUOUVMTGF5c2NOdy85WmIwWXJIM1RNOXoyY3FCV1hnVWl6TjRRNFJTTEVIcjVEUm1MTFYzRUtpc3Q1a2h4ZktQYVJJRXpsYXlMN1lRTXFTSTRja3d1ZjBBMTBJNWhnWmdnVGlobUtXS1J6NHhkQkEya3FFYTJsNlBCb25QOG5rejNMSlZsVXJqNVZ0TlJZTEszVENlZ0hzVzBqNjRoL1NndXpXNC9MZGZISHhkTS84V3NtWCtIV2pEVWVxTGl6RVFjQVhKOHBEdzRHM2NWdi9kV2FTWnN2S0tqcHZVYmlvUklIb2tmRHR4L0FGMUl0VnFNQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX3ZhX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfdmEuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_va_complete, file = "hometowns_va.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFdBU0hJTkdUT04gSE9NRVRPV05TXG5cbiMgU3RlcCAxOiBGaWx0ZXIgZm9yIHRoZSBzdGF0ZSdzIHBsYXllcnNcbmZvb3RiYWxsX3Jvc3RlcnNfd2EgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiA9PSBcIldBXCIpXG5cbiMgU3RlcCAyOiBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc193YSA8LSBmb290YmFsbF9yb3N0ZXJzX3dhICU+JVxuICBncm91cF9ieShob21ldG93bl9jaXR5X2NsZWFuLCBob21ldG93bl9zdGF0ZV9jbGVhbikgJT4lXG4gIHN1bW1hcmlzZSh0b3RhbF9wbGF5ZXJzID0gbigpKVxuYGBgIn0= -->

```r

# WASHINGTON HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_wa <- football_rosters_usa %>%
  filter(hometown_state_clean == "WA")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_wa <- football_rosters_wa %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfd2FfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJXQVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_wa_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "WA",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzUzJyBmb3Igc3RhdGUgJ1dBJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '53' for state 'WA'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfd2FfMjAyMSA8LSBjZW5zdXNfZGF0YV93YV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG4jIFN0ZXAgNTogU3RhdGUtc3BlY2lmaWMgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIGRpZmZlcmVudCBmb3IgZXZlcnkgc3RhdGUuIFRoZSBmaXJzdCBtdXRhdGUgZnVuY3Rpb24gc2hvdWxkIGJlIGluY2x1ZGVkIGZvciBldmVyeSBzdGF0ZSwganVzdCBtb2RpZmllZCBkZXBlbmRpbmcgb24gdGhlIHN0YXRlIG5hbWUuIEFkZGl0aW9uYWwgbXV0YXRlIGZ1bmN0aW9ucyBtYXkgYmUgbmVlZGVkIGZvciBpbnN0YW5jZXMgd2hlbiB0aGUgY2Vuc3VzIG5hbWVzIHNvbWV0aGluZyBpbiBhIHdlaXJkIHdheSB0aGF0IGRvZXNuJ3QgbGluZSB1cCB3aXRoIHRoZSBob21ldG93bnMuXG5jZW5zdXNfZGF0YV93YV8yMDIxIDwtIGNlbnN1c19kYXRhX3dhXzIwMjEgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNhc2Vfd2hlbihcbiAgICBzdGF0ZSA9PSAnV2FzaGluZ3RvbicgfiBcIldBXCIpKVxuXG4jIFN0ZXAgNjogSm9pbiB0aGUgY2Vuc3VzIGRhdGEgdG8gdGhlIGxpc3Qgb2YgaG9tZXRvd25zLiBBbHNvIGNyZWF0ZSBhIGNvbHVtbiB0aGF0IHRlbGxzIHVzIGhvdyBtYW55IHBlb3BsZSBhcmUgZWxpdGUgY29sbGVnZSBmb290YmFsbCBwbGF5ZXJzIGZvciBldmVyeSAxLDAwMCByZXNpZGVudHMuXG5ob21ldG93bnNfd2FfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX3dhICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfd2FfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIFN0ZXAgNzogTm90aWNlIHRoZXJlIGFyZSBhIGZldyBOQSB2YWx1ZXMuIFRoaXMgaGFwcGVucyB3aGVuIHRoZSBjZW5zdXMgZGF0YSBkb2VzIG5vdCBqb2luIHdpdGggdGhlIGhvbWV0b3ducyBkYXRhLCBwZXJoYXBzIGJlY2F1c2UgdGhlIGhvbWV0b3duIGlzIG1pc3NwZWxsZWQgb3IgYmVjYXVzZSB0aGVyZSBpcyBubyBjZW5zdXMgZGF0YSBmb3IgdGhhdCB0b3duLiBGaXJzdCwgbGV0J3MgZmluZCB0aGUgTkEgdmFsdWVzLlxuaG9tZXRvd25zX3dhX2NvbXBsZXRlICU+JVxuICBmaWx0ZXIoaXMubmEoZ2VvaWQpKVxuYGBgIn0= -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_wa_2021 <- census_data_wa_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_wa_2021 <- census_data_wa_2021 %>%
  mutate(state = case_when(
    state == 'Washington' ~ "WA"))

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.
hometowns_wa_complete <- distinct_hometowns_wa %>%
  left_join(census_data_wa_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_wa_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjIsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMiDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsyXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE3VlN5MjdDTUJBMGdaUUdDUlFKZm9OY3VMVEhTbFY3ci9yZ1ppMk9DeEhHam13anlxbjlsbjVodndDNkR0NEtjbThrWjllekkrL08yRS8zODlsZ1BtQ01kVmt2NmJCdWlpbExYNTRmcGpjTUVkeDBXSTlsSVg0Z2FZeEoyT1M0a2xqSUhxMlVlZ0Y2SFlIclYybWhCQ1ZieE9UdDdpeGpiTmpVUW9kVHpHUE1qdmlkeFZIQVAzL0NaUDF2aXYrUFg2aFBoUUxuNHBBRURrcndVTHhiMk1nV1BiTm1WMmpFSGVuOHdoL0tPYlRQSlZMZU9Ic0N4eXV6a2Q3c05CZVYzM09oSk9oWW12eVZuQWN2TDJwRGJ6d29YaXZZUyt1b3dWS2FxcVN4SXNQVUJDd1VpUFVaTU56SXNnTE5LeTJ3RWJGcTRYbkRwQ2xpRDE1THkvM0tiQjNvRXZHMnVyNnBmV1UwNmt2Q3kwbGIvblZzQzhpM092aFJUc1ZxcTlmVDJXMHdPYjRRRnAyazEwSjVkdXJaTzhhejBualdsZFRMU3BPRVZNRkNxcmdaNGUwMHZoZTFyYlNuMjBUVUZZMURoQWlqQ0duRXNjTXZXOUF5S2pFREFBQT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Greenbank","2":"WA","3":"1","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"},{"1":"Veradale","2":"WA","3":"2","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[2]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuIyBGb3IgR3JlZW5iYW5rICg5ODI1MykgYW5kIFZlcmFkYWxlICg5OTAzNyk6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVM5ODI1My05ODI1My9cbiMgaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvcHJvZmlsZXMvODYwMDBVUzk5MDM3LTk5MDM3L1xuY2Vuc3VzX2RhdGFfemlwc193YV8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgOTgyNTNcIiB8IG5hbWUgPT0gXCJaQ1RBNSA5OTAzN1wiKSAlPiVcbiAgcmVuYW1lKGNpdHkgPSBuYW1lLCB0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpICU+JVxuICBtdXRhdGUoc3RhdGUgPSBcIldBXCIpICU+JVxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09IFwiWkNUQTUgOTgyNTNcIiB+IFwiR3JlZW5iYW5rXCIsXG4gICAgY2l0eSA9PSBcIlpDVEE1IDk5MDM3XCIgfiBcIlZlcmFkYWxlXCIpKSU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

# For Greenbank (98253) and Veradale (99037): https://censusreporter.org/profiles/86000US98253-98253/
# https://censusreporter.org/profiles/86000US99037-99037/
census_data_zips_wa_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 98253" | name == "ZCTA5 99037") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "WA") %>%
  mutate(city = case_when(
    city == "ZCTA5 98253" ~ "Greenbank",
    city == "ZCTA5 99037" ~ "Veradale"))%>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfd2FfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfd2FfMjAyMSwgY2Vuc3VzX2RhdGFfemlwc193YV8yMDIxKVxuXG5ob21ldG93bnNfd2FfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX3dhICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfd2FfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG5ob21ldG93bnNfd2FfY29tcGxldGUgJT4lXG4gIGZpbHRlcihpcy5uYShnZW9pZCkpICNJZiB0aGlzIGlzIG5vdCBwcm9kdWNpbmcgYW4gZW1wdHkgZGF0YWZyYW1lLCBnbyBiYWNrIGFuZCBjb250aW51ZSB0byB3b3JrIG9uIE5BIHZhbHVlc1xuYGBgIn0= -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_wa_2021 <- bind_rows(census_data_wa_2021, census_data_zips_wa_2021)

hometowns_wa_complete <- distinct_hometowns_wa %>%
  left_join(census_data_wa_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

hometowns_wa_complete %>%
  filter(is.na(geoid)) #If this is not producing an empty dataframe, go back and continue to work on NA values
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjAsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMCDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFswXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE0MlJTMjdESUJDR2NXSmEyWklqUytrMTdFMDI3YjdxQWFwV3lnNFJUR01VREFpdzBsdytMY2JRMUt6Q1pwaHZSdlBQNC8xMXZ5djNKUUJnRGZKVkJ0YlFmUUg4L0hocm5vRWp6c2xBRG9ySmZydWtyZnRNVGczbUYyMlYrSnY3N0VJQUVvNk5DVVVpTER0c2NmdWw4VUNUOUVMTGN5c2NOemY5WmIwWXJIM1RNOXoyY3FCV25nVWl6RjRRNFJTTEVIcjZDeG1MTFYzRUtpc3Q1a2h4ZktIYVJJRWpsYXlMN1lRTXFTSTRjRXhPLzBBMTBJNWhnWmdnVGlobUtXS1J6NHhkQkEya3FFYTJsNlBCb25QOG1rejNLSlZsVXJqNVZ0TlJZTEszVENlZ0hzVzBqNjRoL1NoT3plNWxXcTZQM3k2WS9vdFpNLzhKdFdDbzlVREZrWWs0QXVUNFFIbHdOdTRxZnUrdDBrelllRVZIVGVzM0ZBbVJQQkkvSExqK0FuOXE2em1NQWdBQSJ9 -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[0]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgMTA6IElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX3dhX2NvbXBsZXRlLCBmaWxlID0gXCJob21ldG93bnNfd2EuY3N2XCIpXG5cbmBgYCJ9 -->

```r

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_wa_complete, file = "hometowns_wa.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFdJU0NPTlNJTiBIT01FVE9XTlNcblxuIyBTdGVwIDE6IEZpbHRlciBmb3IgdGhlIHN0YXRlJ3MgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc193aSA8LSBmb290YmFsbF9yb3N0ZXJzX3VzYSAlPiVcbiAgZmlsdGVyKGhvbWV0b3duX3N0YXRlX2NsZWFuID09IFwiV0lcIilcblxuIyBTdGVwIDI6IEdldCBhIGxpc3Qgb2YgYWxsIHRoZSB1bmlxdWUgaG9tZXRvd25zIGluIHRoZSBzdGF0ZVxuZGlzdGluY3RfaG9tZXRvd25zX3dpIDwtIGZvb3RiYWxsX3Jvc3RlcnNfd2kgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# WISCONSIN HOMETOWNS

# Step 1: Filter for the state's players
football_rosters_wi <- football_rosters_usa %>%
  filter(hometown_state_clean == "WI")

# Step 2: Get a list of all the unique hometowns in the state
distinct_hometowns_wi <- football_rosters_wi %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDM6IEdyYWIgdGhlIHJlbGV2YW50IGNlbnN1cyBkYXRhIGZvciB0aGF0IHN0YXRlLiBOb3RlOiBCMDEwMDMgPSB0b3RhbCBwb3B1bGF0aW9uLCBCMDIwMDEgPSB0b3RhbCBCbGFjayBwb3B1bGF0aW9uLCBCMTkwMTMgPSBtZWRpYW4gaG91c2Vob2xkIGluY29tZS4gV2UgZ2V0IHRoZXNlIGNvZGVzIHVzaW5nIHRoZSBBQ1MgY3Jvc3N3YWxrIHdlIGxvYWRlZCBlYXJsaWVyIChBQ1NfMjAwMSkgYW5kIHRoaXMgd2Vic2l0ZTogaHR0cHM6Ly9jZW5zdXNyZXBvcnRlci5vcmcvdG9waWNzL3RhYmxlLWNvZGVzL1xuY2Vuc3VzX2RhdGFfd2lfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwicGxhY2VcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB5ZWFyID0gMjAyMSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0YXRlID0gXCJXSVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgb3V0cHV0ID0gXCJ3aWRlXCIpXG5gYGAifQ== -->

```r
# Step 3: Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_wi_2021 <- get_acs(geography = "place",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "WI",
                           output = "wide")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzU1JyBmb3Igc3RhdGUgJ1dJJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '55' for state 'WI'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuY2Vuc3VzX2RhdGFfd2lfc3ViZGl2aXNpb25zXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcImNvdW50eSBzdWJkaXZpc2lvblwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFyaWFibGVzID0gYyhcIkIwMTAwM18wMDFcIiwgXCJCMDIwMDFfMDAzXCIsIFwiQjE5MDEzXzAwMVwiKSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIHllYXIgPSAyMDIxLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgc3RhdGUgPSBcIldJXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGZpbHRlcihOQU1FID09IFwiRXJpbiB0b3duLCBXYXNoaW5ndG9uIENvdW50eSwgV2lzY29uc2luXCIgfCBOQU1FID09IFwiR2FyZG5lciB0b3duLCBEb29yIENvdW50eSwgV2lzY29uc2luXCIpXG5gYGAifQ== -->

```r
census_data_wi_subdivisions_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "WI",
                           output = "wide") %>%
  filter(NAME == "Erin town, Washington County, Wisconsin" | NAME == "Gardner town, Door County, Wisconsin")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzU1JyBmb3Igc3RhdGUgJ1dJJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '55' for state 'WI'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDQ6IEdlbmVyYWwgY2xlYW5pbmcgb2YgY2Vuc3VzIGRhdGEgdG8gcHJlcGFyZSBmb3Igam9pbiB3aXRoIGhvbWV0b3ducy9yb3N0ZXIgZGF0YS4gVGhpcyBwYXJ0IGlzIHRoZSBzYW1lIGZvciBldmVyeSBzdGF0ZSBhbmQgKGV4Y2VwdCBmb3IgdGhlIGRhdGFmcmFtZSBuYW1lKSBjYW4gbW9yZSBvciBsZXNzIGJlIGNvcGllZCBhbmQgcGFzdGVkLlxuY2Vuc3VzX2RhdGFfd2lfMjAyMSA8LSBjZW5zdXNfZGF0YV93aV8yMDIxICU+JVxuICBjbGVhbl9uYW1lcygpICU+JVxuICBzZXBhcmF0ZShuYW1lLCBpbnRvID0gYyhcImNpdHlcIiwgXCJzdGF0ZVwiKSwgc2VwID0gXCIsIFwiLCByZW1vdmUgPSBGQUxTRSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gZ3N1YihcIlxcXFxiKHRvd258Y2l0eXxDRFB8dmlsbGFnZSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG5jZW5zdXNfZGF0YV93aV9zdWJkaXZpc2lvbnNfMjAyMSA8LSBjZW5zdXNfZGF0YV93aV9zdWJkaXZpc2lvbnNfMjAyMSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgc2VwYXJhdGUobmFtZSwgaW50byA9IGMoXCJjaXR5XCIsIFwiY291bnR5XCIsIFwic3RhdGVcIiksIHNlcCA9IFwiLCBcIiwgcmVtb3ZlID0gRkFMU0UpICU+JVxuICBtdXRhdGUoY2l0eSA9IGdzdWIoXCJcXFxcYih0b3dufGNpdHl8Q0RQfHZpbGxhZ2V8bXVuaWNpcGFsaXR5fHRvd25zaGlwfGJvcm91Z2gpXFxcXGJcIiwgXCJcIiwgY2l0eSkpICU+JVxuICBtdXRhdGUoY2l0eSA9IHN0cl9zcXVpc2goY2l0eSkpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCBiMDEwMDNfMDAxZSwgYjAyMDAxXzAwM2UsIGIxOTAxM18wMDFlKSAlPiVcbiAgcmVuYW1lKHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSlcblxuY2Vuc3VzX2RhdGFfd2lfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfd2lfMjAyMSwgY2Vuc3VzX2RhdGFfd2lfc3ViZGl2aXNpb25zXzIwMjEpXG5cbiMgU3RlcCA1OiBTdGF0ZS1zcGVjaWZpYyBjbGVhbmluZyBvZiBjZW5zdXMgZGF0YSB0byBwcmVwYXJlIGZvciBqb2luIHdpdGggaG9tZXRvd25zL3Jvc3RlciBkYXRhLiBUaGlzIHBhcnQgaXMgZGlmZmVyZW50IGZvciBldmVyeSBzdGF0ZS4gVGhlIGZpcnN0IG11dGF0ZSBmdW5jdGlvbiBzaG91bGQgYmUgaW5jbHVkZWQgZm9yIGV2ZXJ5IHN0YXRlLCBqdXN0IG1vZGlmaWVkIGRlcGVuZGluZyBvbiB0aGUgc3RhdGUgbmFtZS4gQWRkaXRpb25hbCBtdXRhdGUgZnVuY3Rpb25zIG1heSBiZSBuZWVkZWQgZm9yIGluc3RhbmNlcyB3aGVuIHRoZSBjZW5zdXMgbmFtZXMgc29tZXRoaW5nIGluIGEgd2VpcmQgd2F5IHRoYXQgZG9lc24ndCBsaW5lIHVwIHdpdGggdGhlIGhvbWV0b3ducy5cbmNlbnN1c19kYXRhX3dpXzIwMjEgPC0gY2Vuc3VzX2RhdGFfd2lfMjAyMSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gY2FzZV93aGVuKFxuICAgIHN0YXRlID09ICdXaXNjb25zaW4nIH4gXCJXSVwiKSkgJT4lXG4gIGZpbHRlcihnZW9pZCAhPSBcIjU1MzU5MDBcIiAmIGdlb2lkICE9IFwiNTU4NDI3NVwiKSAjcmVtb3ZpbmcgSG91bHRvbiBDRFAsIHBvcHVsYXRpb24gMzkgYW5kIFdhdWtlc2hhIFZpbGxhZ2UsIFdJXG5cbiMgU3RlcCA2OiBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuIEFsc28gY3JlYXRlIGEgY29sdW1uIHRoYXQgdGVsbHMgdXMgaG93IG1hbnkgcGVvcGxlIGFyZSBlbGl0ZSBjb2xsZWdlIGZvb3RiYWxsIHBsYXllcnMgZm9yIGV2ZXJ5IDEsMDAwIHJlc2lkZW50cy5cblxuaG9tZXRvd25zX3dpX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc193aSAlPiVcbiAgbGVmdF9qb2luKGNlbnN1c19kYXRhX3dpXzIwMjEsIGJ5ID0gYyhcImhvbWV0b3duX2NpdHlfY2xlYW5cIiA9IFwiY2l0eVwiLCBcImhvbWV0b3duX3N0YXRlX2NsZWFuXCIgPSBcInN0YXRlXCIpKSAlPiVcbiAgbXV0YXRlKHBsYXllcnNfcGVyX3Rob3VzYW5kID0gcm91bmQoKHRvdGFsX3BsYXllcnMqMTAwMCkvdG90YWxfcG9wLDEpKSAlPiVcbiAgYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuIyBTdGVwIDc6IE5vdGljZSB0aGVyZSBhcmUgYSBmZXcgTkEgdmFsdWVzLiBUaGlzIGhhcHBlbnMgd2hlbiB0aGUgY2Vuc3VzIGRhdGEgZG9lcyBub3Qgam9pbiB3aXRoIHRoZSBob21ldG93bnMgZGF0YSwgcGVyaGFwcyBiZWNhdXNlIHRoZSBob21ldG93biBpcyBtaXNzcGVsbGVkIG9yIGJlY2F1c2UgdGhlcmUgaXMgbm8gY2Vuc3VzIGRhdGEgZm9yIHRoYXQgdG93bi4gRmlyc3QsIGxldCdzIGZpbmQgdGhlIE5BIHZhbHVlcy5cbmhvbWV0b3duc193aV9jb21wbGV0ZSAlPiVcbiAgZmlsdGVyKGlzLm5hKGdlb2lkKSlcbmBgYCJ9 -->

```r
# Step 4: General cleaning of census data to prepare for join with hometowns/roster data. This part is the same for every state and (except for the dataframe name) can more or less be copied and pasted.
census_data_wi_2021 <- census_data_wi_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_wi_subdivisions_2021 <- census_data_wi_subdivisions_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "county", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|municipality|township|borough)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_wi_2021 <- bind_rows(census_data_wi_2021, census_data_wi_subdivisions_2021)

# Step 5: State-specific cleaning of census data to prepare for join with hometowns/roster data. This part is different for every state. The first mutate function should be included for every state, just modified depending on the state name. Additional mutate functions may be needed for instances when the census names something in a weird way that doesn't line up with the hometowns.
census_data_wi_2021 <- census_data_wi_2021 %>%
  mutate(state = case_when(
    state == 'Wisconsin' ~ "WI")) %>%
  filter(geoid != "5535900" & geoid != "5584275") #removing Houlton CDP, population 39 and Waukesha Village, WI

# Step 6: Join the census data to the list of hometowns. Also create a column that tells us how many people are elite college football players for every 1,000 residents.

hometowns_wi_complete <- distinct_hometowns_wi %>%
  left_join(census_data_wi_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Step 7: Notice there are a few NA values. This happens when the census data does not join with the hometowns data, perhaps because the hometown is misspelled or because there is no census data for that town. First, let's find the NA values.
hometowns_wi_complete %>%
  filter(is.na(geoid))
```

<!-- rnb-source-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjpbImdyb3VwZWRfZGYiLCJ0YmxfZGYiLCJ0YmwiLCJkYXRhLmZyYW1lIl0sIm5yb3ciOjEsIm5jb2wiOjksInN1bW1hcnkiOnsiQSB0aWJibGUiOlsiMSDDlyA5Il0sIkdyb3VwcyI6WyJob21ldG93bl9jaXR5X2NsZWFuIFsxXSJdfX0sInJkZiI6Ikg0c0lBQUFBQUFBQUE2VlJRVTdETUJCMDBvYXFsVnBWS3Q5b2hBUUhIb0FRWEJHSTNpelhNYTFWZHgzRmprcFA4QlpleUF0YTFvbGRKYjdpZysyWkhlM083cjQ4ckc0bnF3a2haRUNHYVVJR0dYNUo5dmI2dUx3bnlDQkl5SkNNM2Z1Sm9nVitISmgzQXFNblhTdXJJYUxUOTJlOHB3MkQ2QkxGQkdjOCtNNGMvdnAxRlVjLy84Yzl0eGxYekpqSTBxUmdsdVVmRmR1TFNENnU5Q0VINUkzM25IN2oxZnJzNXcyaWVUT0psbHhzOVY1WWZRREtwVDFTcmdRREg3cStoSXhsVnZSaVU2c3RVN1JVN0NncUV3cHNoSlpGc09VVnVnekVXakcrNnhEVHZTZ2tBeXFCWTZHZ0tybWxqVEs0OERWb0tTcHF0N28yREFya1QxRjNJMTFhcVFIN1M5Mm1zMmgrU1JVUjh4cmNQSW9sMzlhd1c5N2R1Q0g3TFpQTzlwUE9mOXpXSEo1OXJzem51aEt3a1JCYXlCUmJDK1hCRExmVHpEMHZLd2syYkJOWmt6Y1RDZ3pYS2pCTmMrVDBCNE9wTGZMaEFnQUEifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":["hometown_city_clean"],"name":[1],"type":["chr"],"align":["left"]},{"label":["hometown_state_clean"],"name":[2],"type":["chr"],"align":["left"]},{"label":["total_players"],"name":[3],"type":["int"],"align":["right"]},{"label":["geoid"],"name":[4],"type":["chr"],"align":["left"]},{"label":["total_pop"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["black_pop"],"name":[6],"type":["dbl"],"align":["right"]},{"label":["median_income"],"name":[7],"type":["dbl"],"align":["right"]},{"label":["pct_black"],"name":[8],"type":["dbl"],"align":["right"]},{"label":["players_per_thousand"],"name":[9],"type":["dbl"],"align":["right"]}],"data":[{"1":"Houlton","2":"WI","3":"2","4":"NA","5":"NA","6":"NA","7":"NA","8":"NA","9":"NA"}],"options":{"columns":{"min":{},"max":[10],"total":[9]},"rows":{"min":[10],"max":[10],"total":[1]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFN0ZXAgODogTm93IHdlIGhhdmUgdG8gZmlndXJlIG91dCBob3cgdG8gYWRkcmVzcyBlYWNoIG9mIHRoZSBOQSB2YWx1ZXMuIFRoaXMgaXMgYSBqdWRnbWVudCBjYWxsLCBhbmQgd2Ugc2hvdWxkIGJlIGNhcmVmdWwgYWJvdXQgZG9jdW1lbnRpbmcgaG93IGFuZCB3aHkgd2UgbWFkZSB0aGF0IGRlY2lzaW9uLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIGEgaG9tZXRvd24gaXMgbWlzc3BlbGxlZCwgdGVsbCBTYXBuYSwgYW5kIHNoZSB3aWxsIG1ha2UgdGhhdCBjb3JyZWN0aW9uIGluIE9wZW4gUmVmaW5lLiBJZiB0aGVyZSBpcyBhbiBOQSB2YWx1ZSBiZWNhdXNlIHRoZSBjZW5zdXMgZG9lcyBub3QgcmVjb2duaXplIHRoZSBob21ldG93biwgd2UgbmVlZCB0byBmaW5kIHNvbWUgc3Vic3RpdHV0ZSBmb3IgdGhhdCBob21ldG93bi5cblxuY2Vuc3VzX2RhdGFfd2lfYmxvY2tzXzIwMjEgPC0gZ2V0X2FjcyhnZW9ncmFwaHkgPSBcImJsb2NrIGdyb3VwXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBzdGF0ZSA9IFwiV0lcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgIG91dHB1dCA9IFwid2lkZVwiKSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgZmlsdGVyKG5hbWUgPT0gXCJCbG9jayBHcm91cCAyLCBDZW5zdXMgVHJhY3QgMTIwNC4wMiwgU3QuIENyb2l4IENvdW50eSwgV2lzY29uc2luXCIpICU+JVxuICByZW5hbWUoY2l0eSA9IG5hbWUsIHRvdGFsX3BvcCA9IGIwMTAwM18wMDFlLCBibGFja19wb3AgPSBiMDIwMDFfMDAzZSwgbWVkaWFuX2luY29tZSA9IGIxOTAxM18wMDFlKSAlPiVcbiAgbXV0YXRlKHBjdF9ibGFjayA9IHJvdW5kKGJsYWNrX3BvcC90b3RhbF9wb3AqMTAwLCAxKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IFwiV0lcIikgJT4lXG4gIG11dGF0ZShjaXR5ID0gY2FzZV93aGVuKFxuICAgIGNpdHkgPT0gXCJCbG9jayBHcm91cCAyLCBDZW5zdXMgVHJhY3QgMTIwNC4wMiwgU3QuIENyb2l4IENvdW50eSwgV2lzY29uc2luXCIgfiBcIkhvdWx0b25cIikpICU+JVxuICBzZWxlY3QoZ2VvaWQsIGNpdHksIHN0YXRlLCB0b3RhbF9wb3AsIGJsYWNrX3BvcCwgbWVkaWFuX2luY29tZSwgcGN0X2JsYWNrKVxuYGBgIn0= -->

```r

# Step 8: Now we have to figure out how to address each of the NA values. This is a judgment call, and we should be careful about documenting how and why we made that decision. If there is an NA value because a hometown is misspelled, tell Sapna, and she will make that correction in Open Refine. If there is an NA value because the census does not recognize the hometown, we need to find some substitute for that hometown.

census_data_wi_blocks_2021 <- get_acs(geography = "block group",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = "WI",
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "Block Group 2, Census Tract 1204.02, St. Croix County, Wisconsin") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "WI") %>%
  mutate(city = case_when(
    city == "Block Group 2, Census Tract 1204.02, St. Croix County, Wisconsin" ~ "Houlton")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzU1JyBmb3Igc3RhdGUgJ1dJJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '55' for state 'WI'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBTdGVwIDk6IFdlIG5vdyBoYXZlIHRvIGFwcGVuZCB0aGVzZSBzcGVjaWFsIGNhc2VzIHRvIG91ciBzdGF0ZSBjZW5zdXMgZGF0YSwgcmVkbyB0aGUgam9pbiwgYW5kIHJ1biBvbmUgbW9yZSBjaGVjayBmb3IgTkEgdmFsdWVzLlxuY2Vuc3VzX2RhdGFfd2lfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfd2lfMjAyMSwgY2Vuc3VzX2RhdGFfd2lfYmxvY2tzXzIwMjEpXG4gXG5ob21ldG93bnNfd2lfY29tcGxldGUgPC0gZGlzdGluY3RfaG9tZXRvd25zX3dpICU+JVxuICBsZWZ0X2pvaW4oY2Vuc3VzX2RhdGFfd2lfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4gI0lmIHRoaXMgaXMgbm90IHByb2R1Y2luZyBhbiBlbXB0eSBkYXRhZnJhbWUsIGdvIGJhY2sgYW5kIGNvbnRpbnVlIHRvIHdvcmsgb24gTkEgdmFsdWVzXG5cbiMgU3RlcCAxMDogSWYgbmVlZGVkLCB1bmNvbW1lbnQgb3V0IHRvIGNyZWF0ZSBhIENTVlxuI3dyaXRlX2Nzdihob21ldG93bnNfd2lfY29tcGxldGUsIGZpbGUgPSBcImhvbWV0b3duc193aS5jc3ZcIilcblxuYGBgIn0= -->

```r
# Step 9: We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_wi_2021 <- bind_rows(census_data_wi_2021, census_data_wi_blocks_2021)
 
hometowns_wi_complete <- distinct_hometowns_wi %>%
  left_join(census_data_wi_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

 #If this is not producing an empty dataframe, go back and continue to work on NA values

# Step 10: If needed, uncomment out to create a CSV
#write_csv(hometowns_wi_complete, file = "hometowns_wi.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIFNNQUxMRVIgU1RBVEUgSE9NRVRPV05TIC0gdXNlZCBmb3IgYWxsIHN0YXRlcyB3aXRoIGxlc3MgdGhhbiA1MCBQb3dlciBGaXZlIHBsYXllcnMgKFdZLCBBSywgUkksIE5ELCBOSCwgTVQsIE5NLCBTRCwgREUsIElELCBEQywgV1YsIENULCBOVik7ICpkbyBub3QgdXNlIHRoaXMgYXMgYSB0ZW1wbGF0ZSpcblxuIyBWZWN0b3Igb2YgYWxsIHN0YXRlcyB3aXRoIGZld2VyIHRoYW4gNTAgcGxheWVyc1xuc3RhdGVzX3VuZGVyXzUwIDwtIGZvb3RiYWxsX3Jvc3RlcnNfdXNhX3N0YXRlcyRob21ldG93bl9zdGF0ZV9jbGVhbltmb290YmFsbF9yb3N0ZXJzX3VzYV9zdGF0ZXMkdG90YWxfcGxheWVycyA8IDUwXVxuXG4jIEZpbHRlciBmb3IgdGhlIHN0YXRlcycgcGxheWVyc1xuZm9vdGJhbGxfcm9zdGVyc19zbWFsbF9zdGF0ZXMgPC0gZm9vdGJhbGxfcm9zdGVyc191c2EgJT4lXG4gIGZpbHRlcihob21ldG93bl9zdGF0ZV9jbGVhbiAlaW4lIHN0YXRlc191bmRlcl81MClcblxuIyBHZXQgYSBsaXN0IG9mIGFsbCB0aGUgdW5pcXVlIGhvbWV0b3ducyBpbiB0aGUgc3RhdGVcbmRpc3RpbmN0X2hvbWV0b3duc19zbWFsbF9zdGF0ZXMgPC0gZm9vdGJhbGxfcm9zdGVyc19zbWFsbF9zdGF0ZXMgJT4lXG4gIGdyb3VwX2J5KGhvbWV0b3duX2NpdHlfY2xlYW4sIGhvbWV0b3duX3N0YXRlX2NsZWFuKSAlPiVcbiAgc3VtbWFyaXNlKHRvdGFsX3BsYXllcnMgPSBuKCkpXG5gYGAifQ== -->

```r

# SMALLER STATE HOMETOWNS - used for all states with less than 50 Power Five players (WY, AK, RI, ND, NH, MT, NM, SD, DE, ID, DC, WV, CT, NV); *do not use this as a template*

# Vector of all states with fewer than 50 players
states_under_50 <- football_rosters_usa_states$hometown_state_clean[football_rosters_usa_states$total_players < 50]

# Filter for the states' players
football_rosters_small_states <- football_rosters_usa %>%
  filter(hometown_state_clean %in% states_under_50)

# Get a list of all the unique hometowns in the state
distinct_hometowns_small_states <- football_rosters_small_states %>%
  group_by(hometown_city_clean, hometown_state_clean) %>%
  summarise(total_players = n())
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiYHN1bW1hcmlzZSgpYCBoYXMgZ3JvdXBlZCBvdXRwdXQgYnkgJ2hvbWV0b3duX2NpdHlfY2xlYW4nLiBZb3UgY2FuIG92ZXJyaWRlIHVzaW5nIHRoZSBgLmdyb3Vwc2AgYXJndW1lbnQuXG4ifQ== -->

```
`summarise()` has grouped output by 'hometown_city_clean'. You can override using the `.groups` argument.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBHcmFiIHRoZSByZWxldmFudCBjZW5zdXMgZGF0YSBmb3IgdGhhdCBzdGF0ZS4gTm90ZTogQjAxMDAzID0gdG90YWwgcG9wdWxhdGlvbiwgQjAyMDAxID0gdG90YWwgQmxhY2sgcG9wdWxhdGlvbiwgQjE5MDEzID0gbWVkaWFuIGhvdXNlaG9sZCBpbmNvbWUuIFdlIGdldCB0aGVzZSBjb2RlcyB1c2luZyB0aGUgQUNTIGNyb3Nzd2FsayB3ZSBsb2FkZWQgZWFybGllciAoQUNTXzIwMDEpIGFuZCB0aGlzIHdlYnNpdGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3RvcGljcy90YWJsZS1jb2Rlcy9cbmNlbnN1c19kYXRhX3NtYWxsX3N0YXRlc18yMDIxIDwtIGxhcHBseShzdGF0ZXNfdW5kZXJfNTAsIGZ1bmN0aW9uKHN0YXRlKSB7XG4gIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJwbGFjZVwiLFxuICAgICAgICAgIHZhcmlhYmxlcyA9IGMoXCJCMDEwMDNfMDAxXCIsIFwiQjAyMDAxXzAwM1wiLCBcIkIxOTAxM18wMDFcIiksXG4gICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgc3RhdGUgPSBzdGF0ZSxcbiAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIilcbn0pXG5gYGAifQ== -->

```r
# Grab the relevant census data for that state. Note: B01003 = total population, B02001 = total Black population, B19013 = median household income. We get these codes using the ACS crosswalk we loaded earlier (ACS_2001) and this website: https://censusreporter.org/topics/table-codes/
census_data_small_states_2021 <- lapply(states_under_50, function(state) {
  get_acs(geography = "place",
          variables = c("B01003_001", "B02001_003", "B19013_001"),
          year = 2021,
          state = state,
          output = "wide")
})
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzExJyBmb3Igc3RhdGUgJ0RDJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzMyJyBmb3Igc3RhdGUgJ05WJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzU0JyBmb3Igc3RhdGUgJ1dWJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzEwJyBmb3Igc3RhdGUgJ0RFJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzA5JyBmb3Igc3RhdGUgJ0NUJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQ2JyBmb3Igc3RhdGUgJ1NEJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzE2JyBmb3Igc3RhdGUgJ0lEJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzMwJyBmb3Igc3RhdGUgJ01UJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzM1JyBmb3Igc3RhdGUgJ05NJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzM4JyBmb3Igc3RhdGUgJ05EJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzMzJyBmb3Igc3RhdGUgJ05IJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzQ0JyBmb3Igc3RhdGUgJ1JJJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzU2JyBmb3Igc3RhdGUgJ1dZJ1xuR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzAyJyBmb3Igc3RhdGUgJ0FLJ1xuIn0= -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '11' for state 'DC'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '32' for state 'NV'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '54' for state 'WV'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '10' for state 'DE'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '09' for state 'CT'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '46' for state 'SD'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '16' for state 'ID'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '30' for state 'MT'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '35' for state 'NM'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '38' for state 'ND'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '33' for state 'NH'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '44' for state 'RI'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '56' for state 'WY'
Getting data from the 2017-2021 5-year ACS
Using FIPS code '02' for state 'AK'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuY2Vuc3VzX2RhdGFfc21hbGxfc3RhdGVzXzIwMjEgPC0gZG8uY2FsbChyYmluZCwgY2Vuc3VzX2RhdGFfc21hbGxfc3RhdGVzXzIwMjEpXG5cbiMgSXQgdHVybnMgb3V0IHRoYXQgbWFueSB0b3ducyBpbiBDb25uZWN0aWN1dCwgTmV3IEhhbXBzaGlyZSwgYW5kIFJob2RlIElzbGFuZCBhcmUgY291bnR5IHN1YmRpdmlzaW9ucywgc28gd2Ugd2lsbCBncmFiIHRoZSByZWxldmFudCBvbmVzIG9mIHRob3NlLCB0b29cbmNlbnN1c19kYXRhX3NtYWxsX3N0YXRlc19zdWJkaXZpc2lvbnNfMjAyMSA8LSBnZXRfYWNzKGdlb2dyYXBoeSA9IFwiY291bnR5IHN1YmRpdmlzaW9uXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBzdGF0ZSA9IGMoXCJDVFwiLCBcIk5IXCIsIFwiUklcIiksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGZpbHRlcihOQU1FID09IFwiRGFyaWVuIHRvd24sIEZhaXJmaWVsZCBDb3VudHksIENvbm5lY3RpY3V0XCIgfCBOQU1FID09IFwiRWFzdCBHcmVlbndpY2ggdG93biwgS2VudCBDb3VudHksIFJob2RlIElzbGFuZFwiIHwgTkFNRSA9PSBcIkZhaXJmaWVsZCB0b3duLCBGYWlyZmllbGQgQ291bnR5LCBDb25uZWN0aWN1dFwiIHwgTkFNRSA9PSBcIkdsYXN0b25idXJ5IHRvd24sIEhhcnRmb3JkIENvdW50eSwgQ29ubmVjdGljdXRcIiB8IE5BTUUgPT0gXCJHcmFudGhhbSB0b3duLCBTdWxsaXZhbiBDb3VudHksIE5ldyBIYW1wc2hpcmVcIiB8IE5BTUUgPT0gXCJIb2xsaXMgdG93biwgSGlsbHNib3JvdWdoIENvdW50eSwgTmV3IEhhbXBzaGlyZVwiIHwgTkFNRSA9PSBcIktlbnQgdG93biwgTGl0Y2hmaWVsZCBDb3VudHksIENvbm5lY3RpY3V0XCIgfCBOQU1FID09IFwiTmV3IEZhaXJmaWVsZCB0b3duLCBGYWlyZmllbGQgQ291bnR5LCBDb25uZWN0aWN1dFwiIHwgTkFNRSA9PSBcIlBvbWZyZXQgdG93biwgV2luZGhhbSBDb3VudHksIENvbm5lY3RpY3V0XCIgfCBOQU1FID09IFwiUm9ja3kgSGlsbCB0b3duLCBIYXJ0Zm9yZCBDb3VudHksIENvbm5lY3RpY3V0XCIgfCBOQU1FID09IFwiU3VmZmllbGQgdG93biwgSGFydGZvcmQgQ291bnR5LCBDb25uZWN0aWN1dFwiIHwgTkFNRSA9PSBcIlRydW1idWxsIHRvd24sIEZhaXJmaWVsZCBDb3VudHksIENvbm5lY3RpY3V0XCIgfCBOQU1FID09IFwiV2FsbGluZ2ZvcmQgdG93biwgTmV3IEhhdmVuIENvdW50eSwgQ29ubmVjdGljdXRcIiB8IE5BTUUgPT0gXCJXZXN0IFdhcndpY2sgdG93biwgS2VudCBDb3VudHksIFJob2RlIElzbGFuZFwiIHwgTkFNRSA9PSBcIldlc3Rwb3J0IHRvd24sIEZhaXJmaWVsZCBDb3VudHksIENvbm5lY3RpY3V0XCIgfCBOQU1FID09IFwiV2lsdG9uIHRvd24sIEZhaXJmaWVsZCBDb3VudHksIENvbm5lY3RpY3V0XCIgfCBOQU1FID09IFwiV2luZHNvciB0b3duLCBIYXJ0Zm9yZCBDb3VudHksIENvbm5lY3RpY3V0XCIpXG5gYGAifQ== -->

```r
census_data_small_states_2021 <- do.call(rbind, census_data_small_states_2021)

# It turns out that many towns in Connecticut, New Hampshire, and Rhode Island are county subdivisions, so we will grab the relevant ones of those, too
census_data_small_states_subdivisions_2021 <- get_acs(geography = "county subdivision",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           state = c("CT", "NH", "RI"),
                           output = "wide") %>%
  filter(NAME == "Darien town, Fairfield County, Connecticut" | NAME == "East Greenwich town, Kent County, Rhode Island" | NAME == "Fairfield town, Fairfield County, Connecticut" | NAME == "Glastonbury town, Hartford County, Connecticut" | NAME == "Grantham town, Sullivan County, New Hampshire" | NAME == "Hollis town, Hillsborough County, New Hampshire" | NAME == "Kent town, Litchfield County, Connecticut" | NAME == "New Fairfield town, Fairfield County, Connecticut" | NAME == "Pomfret town, Windham County, Connecticut" | NAME == "Rocky Hill town, Hartford County, Connecticut" | NAME == "Suffield town, Hartford County, Connecticut" | NAME == "Trumbull town, Fairfield County, Connecticut" | NAME == "Wallingford town, New Haven County, Connecticut" | NAME == "West Warwick town, Kent County, Rhode Island" | NAME == "Westport town, Fairfield County, Connecticut" | NAME == "Wilton town, Fairfield County, Connecticut" | NAME == "Windsor town, Hartford County, Connecticut")
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG5Vc2luZyBGSVBTIGNvZGUgJzA5JyBmb3Igc3RhdGUgJ0NUJ1xuVXNpbmcgRklQUyBjb2RlICczMycgZm9yIHN0YXRlICdOSCdcblVzaW5nIEZJUFMgY29kZSAnNDQnIGZvciBzdGF0ZSAnUkknXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
Using FIPS code '09' for state 'CT'
Using FIPS code '33' for state 'NH'
Using FIPS code '44' for state 'RI'
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBHZW5lcmFsIGNsZWFuaW5nIG9mIGNlbnN1cyBkYXRhIHRvIHByZXBhcmUgZm9yIGpvaW4gd2l0aCBob21ldG93bnMvcm9zdGVyIGRhdGEuXG5jZW5zdXNfZGF0YV9zbWFsbF9zdGF0ZXNfMjAyMSA8LSBjZW5zdXNfZGF0YV9zbWFsbF9zdGF0ZXNfMjAyMSAlPiVcbiAgY2xlYW5fbmFtZXMoKSAlPiVcbiAgc2VwYXJhdGUobmFtZSwgaW50byA9IGMoXCJjaXR5XCIsIFwic3RhdGVcIiksIHNlcCA9IFwiLCBcIiwgcmVtb3ZlID0gRkFMU0UpICU+JVxuICBtdXRhdGUoY2l0eSA9IGdzdWIoXCJcXFxcYih0b3dufGNpdHl8Q0RQfHZpbGxhZ2V8bXVuaWNpcGFsaXR5KVxcXFxiXCIsIFwiXCIsIGNpdHkpKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBzdHJfc3F1aXNoKGNpdHkpKSAlPiVcbiAgc2VsZWN0KGdlb2lkLCBjaXR5LCBzdGF0ZSwgYjAxMDAzXzAwMWUsIGIwMjAwMV8wMDNlLCBiMTkwMTNfMDAxZSkgJT4lXG4gIHJlbmFtZSh0b3RhbF9wb3AgPSBiMDEwMDNfMDAxZSwgYmxhY2tfcG9wID0gYjAyMDAxXzAwM2UsIG1lZGlhbl9pbmNvbWUgPSBiMTkwMTNfMDAxZSkgJT4lXG4gIG11dGF0ZShwY3RfYmxhY2sgPSByb3VuZChibGFja19wb3AvdG90YWxfcG9wKjEwMCwgMSkpXG5cbmNlbnN1c19kYXRhX3NtYWxsX3N0YXRlc19zdWJkaXZpc2lvbnNfMjAyMSA8LSBjZW5zdXNfZGF0YV9zbWFsbF9zdGF0ZXNfc3ViZGl2aXNpb25zXzIwMjEgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIHNlcGFyYXRlKG5hbWUsIGludG8gPSBjKFwiY2l0eVwiLCBcImNvdW50eVwiLCBcInN0YXRlXCIpLCBzZXAgPSBcIiwgXCIsIHJlbW92ZSA9IEZBTFNFKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBnc3ViKFwiXFxcXGIodG93bnxjaXR5fENEUHx2aWxsYWdlfG11bmljaXBhbGl0eSlcXFxcYlwiLCBcIlwiLCBjaXR5KSkgJT4lXG4gIG11dGF0ZShjaXR5ID0gc3RyX3NxdWlzaChjaXR5KSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIGIwMTAwM18wMDFlLCBiMDIwMDFfMDAzZSwgYjE5MDEzXzAwMWUpICU+JVxuICByZW5hbWUodG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKVxuXG5jZW5zdXNfZGF0YV9zbWFsbF9zdGF0ZXNfMjAyMSA8LSBiaW5kX3Jvd3MoY2Vuc3VzX2RhdGFfc21hbGxfc3RhdGVzXzIwMjEsIGNlbnN1c19kYXRhX3NtYWxsX3N0YXRlc19zdWJkaXZpc2lvbnNfMjAyMSlcblxuIyBDbGVhbmluZyBvZiBjZW5zdXMgZGF0YSB0byBwcmVwYXJlIGZvciBqb2luIHdpdGggaG9tZXRvd25zL3Jvc3RlciBkYXRhLlxuc3RhdGVfY3Jvc3N3YWxrX21vZGlmaWVkIDwtIHN0YXRlX2Nyb3Nzd2FsayAlPiVcbiAgbXV0YXRlKHN0YXRlX25hbWVzID0gc3RyX3RvX3RpdGxlKHN0YXRlX25hbWVfY2FwcykpICU+JVxuICBtdXRhdGUoc3RhdGVfbmFtZXMgPSBjYXNlX3doZW4oXG4gICAgc3RhdGVfbmFtZXMgPT0gJ1dhc2hpbmd0b24sIERjJyB+IFwiRGlzdHJpY3Qgb2YgQ29sdW1iaWFcIixcbiAgICBUUlVFIH4gc3RhdGVfbmFtZXMpKSAlPiVcbiAgc2VsZWN0KHN0YXRlX2FiYiwgc3RhdGVfbmFtZXMpXG5cbmNlbnN1c19kYXRhX3NtYWxsX3N0YXRlc18yMDIxIDwtIGNlbnN1c19kYXRhX3NtYWxsX3N0YXRlc18yMDIxICU+JVxuICBsZWZ0X2pvaW4oc3RhdGVfY3Jvc3N3YWxrX21vZGlmaWVkLCBieSA9IGMoXCJzdGF0ZVwiID0gXCJzdGF0ZV9uYW1lc1wiKSkgJT4lXG4gIG11dGF0ZShzdGF0ZSA9IGNlbnN1c19kYXRhX3NtYWxsX3N0YXRlc18yMDIxJHN0YXRlX2FiYikgJT4lIFxuICBtdXRhdGUoY2l0eSA9IGNhc2Vfd2hlbihcbiAgICBjaXR5ID09ICdCb2lzZSBDaXR5JyB+IFwiQm9pc2VcIixcbiAgICBUUlVFIH4gY2l0eSkpXG5gYGAifQ== -->

```r
# General cleaning of census data to prepare for join with hometowns/roster data.
census_data_small_states_2021 <- census_data_small_states_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|municipality)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_small_states_subdivisions_2021 <- census_data_small_states_subdivisions_2021 %>%
  clean_names() %>%
  separate(name, into = c("city", "county", "state"), sep = ", ", remove = FALSE) %>%
  mutate(city = gsub("\\b(town|city|CDP|village|municipality)\\b", "", city)) %>%
  mutate(city = str_squish(city)) %>%
  select(geoid, city, state, b01003_001e, b02001_003e, b19013_001e) %>%
  rename(total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1))

census_data_small_states_2021 <- bind_rows(census_data_small_states_2021, census_data_small_states_subdivisions_2021)

# Cleaning of census data to prepare for join with hometowns/roster data.
state_crosswalk_modified <- state_crosswalk %>%
  mutate(state_names = str_to_title(state_name_caps)) %>%
  mutate(state_names = case_when(
    state_names == 'Washington, Dc' ~ "District of Columbia",
    TRUE ~ state_names)) %>%
  select(state_abb, state_names)

census_data_small_states_2021 <- census_data_small_states_2021 %>%
  left_join(state_crosswalk_modified, by = c("state" = "state_names")) %>%
  mutate(state = census_data_small_states_2021$state_abb) %>% 
  mutate(city = case_when(
    city == 'Boise City' ~ "Boise",
    TRUE ~ city))
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiV2FybmluZzogVGhlcmUgd2FzIDEgd2FybmluZyBpbiBgbXV0YXRlKClgLlxu4oS5IEluIGFyZ3VtZW50OiBgc3RhdGUgPSBjZW5zdXNfZGF0YV9zbWFsbF9zdGF0ZXNfMjAyMSRzdGF0ZV9hYmJgLlxuQ2F1c2VkIGJ5IHdhcm5pbmc6XG4hIFVua25vd24gb3IgdW5pbml0aWFsaXNlZCBjb2x1bW46IGBzdGF0ZV9hYmJgLlxuIn0= -->

```
Warning: There was 1 warning in `mutate()`.
ℹ In argument: `state = census_data_small_states_2021$state_abb`.
Caused by warning:
! Unknown or uninitialised column: `state_abb`.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuY2Vuc3VzX2RhdGFfc21hbGxfc3RhdGVzXzIwMjEgPC0gY2Vuc3VzX2RhdGFfc21hbGxfc3RhdGVzXzIwMjEgJT4lXG4gIHJlbmFtZShzdGF0ZSA9IHN0YXRlX2FiYilcblxuIyBKb2luIHRoZSBjZW5zdXMgZGF0YSB0byB0aGUgbGlzdCBvZiBob21ldG93bnMuXG5ob21ldG93bnNfc21hbGxfc3RhdGVzX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19zbWFsbF9zdGF0ZXMgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9zbWFsbF9zdGF0ZXNfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIE5vdyB3ZSBoYXZlIHRvIGZpZ3VyZSBvdXQgaG93IHRvIGFkZHJlc3MgZWFjaCBvZiB0aGUgTkEgdmFsdWVzLlxuIyBGb3IgT25hLCBXViwgdGhlIHppcCBjb2RlICgyNTU0NSkgc2VlbXMgdG8gYmUgYSBnb29kIHN1YnN0aXR1dGU6IGh0dHBzOi8vY2Vuc3VzcmVwb3J0ZXIub3JnL3Byb2ZpbGVzLzg2MDAwVVMyNTU0NS0yNTU0NS9cbmNlbnN1c19kYXRhX29uYV93dl8yMDIxIDwtIGdldF9hY3MoZ2VvZ3JhcGh5ID0gXCJ6Y3RhXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICB2YXJpYWJsZXMgPSBjKFwiQjAxMDAzXzAwMVwiLCBcIkIwMjAwMV8wMDNcIiwgXCJCMTkwMTNfMDAxXCIpLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgeWVhciA9IDIwMjEsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBcIndpZGVcIikgJT4lXG4gIGNsZWFuX25hbWVzKCkgJT4lXG4gIGZpbHRlcihuYW1lID09IFwiWkNUQTUgMjU1NDVcIikgJT4lXG4gIHJlbmFtZShjaXR5ID0gbmFtZSwgdG90YWxfcG9wID0gYjAxMDAzXzAwMWUsIGJsYWNrX3BvcCA9IGIwMjAwMV8wMDNlLCBtZWRpYW5faW5jb21lID0gYjE5MDEzXzAwMWUpICU+JVxuICBtdXRhdGUocGN0X2JsYWNrID0gcm91bmQoYmxhY2tfcG9wL3RvdGFsX3BvcCoxMDAsIDEpKSAlPiVcbiAgbXV0YXRlKHN0YXRlID0gXCJXVlwiKSAlPiVcbiAgbXV0YXRlKGNpdHkgPSBjYXNlX3doZW4oXG4gICAgY2l0eSA9PSBcIlpDVEE1IDI1NTQ1XCIgfiBcIk9uYVwiKSkgJT4lXG4gIHNlbGVjdChnZW9pZCwgY2l0eSwgc3RhdGUsIHRvdGFsX3BvcCwgYmxhY2tfcG9wLCBtZWRpYW5faW5jb21lLCBwY3RfYmxhY2spXG5gYGAifQ== -->

```r
census_data_small_states_2021 <- census_data_small_states_2021 %>%
  rename(state = state_abb)

# Join the census data to the list of hometowns.
hometowns_small_states_complete <- distinct_hometowns_small_states %>%
  left_join(census_data_small_states_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# Now we have to figure out how to address each of the NA values.
# For Ona, WV, the zip code (25545) seems to be a good substitute: https://censusreporter.org/profiles/86000US25545-25545/
census_data_ona_wv_2021 <- get_acs(geography = "zcta",
                           variables = c("B01003_001", "B02001_003", "B19013_001"),
                           year = 2021,
                           output = "wide") %>%
  clean_names() %>%
  filter(name == "ZCTA5 25545") %>%
  rename(city = name, total_pop = b01003_001e, black_pop = b02001_003e, median_income = b19013_001e) %>%
  mutate(pct_black = round(black_pop/total_pop*100, 1)) %>%
  mutate(state = "WV") %>%
  mutate(city = case_when(
    city == "ZCTA5 25545" ~ "Ona")) %>%
  select(geoid, city, state, total_pop, black_pop, median_income, pct_black)
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiR2V0dGluZyBkYXRhIGZyb20gdGhlIDIwMTctMjAyMSA1LXllYXIgQUNTXG4ifQ== -->

```
Getting data from the 2017-2021 5-year ACS
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBXZSBub3cgaGF2ZSB0byBhcHBlbmQgdGhlc2Ugc3BlY2lhbCBjYXNlcyB0byBvdXIgc3RhdGUgY2Vuc3VzIGRhdGEsIHJlZG8gdGhlIGpvaW4sIGFuZCBydW4gb25lIG1vcmUgY2hlY2sgZm9yIE5BIHZhbHVlcy5cbmNlbnN1c19kYXRhX3NtYWxsX3N0YXRlc18yMDIxIDwtIGJpbmRfcm93cyhjZW5zdXNfZGF0YV9zbWFsbF9zdGF0ZXNfMjAyMSwgY2Vuc3VzX2RhdGFfb25hX3d2XzIwMjEpXG4gXG5ob21ldG93bnNfc21hbGxfc3RhdGVzX2NvbXBsZXRlIDwtIGRpc3RpbmN0X2hvbWV0b3duc19zbWFsbF9zdGF0ZXMgJT4lXG4gIGxlZnRfam9pbihjZW5zdXNfZGF0YV9zbWFsbF9zdGF0ZXNfMjAyMSwgYnkgPSBjKFwiaG9tZXRvd25fY2l0eV9jbGVhblwiID0gXCJjaXR5XCIsIFwiaG9tZXRvd25fc3RhdGVfY2xlYW5cIiA9IFwic3RhdGVcIikpICU+JVxuICBtdXRhdGUocGxheWVyc19wZXJfdGhvdXNhbmQgPSByb3VuZCgodG90YWxfcGxheWVycyoxMDAwKS90b3RhbF9wb3AsMSkpICU+JVxuICBhcnJhbmdlKGRlc2MocGxheWVyc19wZXJfdGhvdXNhbmQpKVxuXG4jIElmIG5lZWRlZCwgdW5jb21tZW50IG91dCB0byBjcmVhdGUgYSBDU1ZcbiN3cml0ZV9jc3YoaG9tZXRvd25zX3NtYWxsX3N0YXRlc19jb21wbGV0ZSwgZmlsZSA9IFwiaG9tZXRvd25zX3NtYWxsX3N0YXRlcy5jc3ZcIilcblxuYGBgIn0= -->

```r
# We now have to append these special cases to our state census data, redo the join, and run one more check for NA values.
census_data_small_states_2021 <- bind_rows(census_data_small_states_2021, census_data_ona_wv_2021)
 
hometowns_small_states_complete <- distinct_hometowns_small_states %>%
  left_join(census_data_small_states_2021, by = c("hometown_city_clean" = "city", "hometown_state_clean" = "state")) %>%
  mutate(players_per_thousand = round((total_players*1000)/total_pop,1)) %>%
  arrange(desc(players_per_thousand))

# If needed, uncomment out to create a CSV
#write_csv(hometowns_small_states_complete, file = "hometowns_small_states.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuZGlzdGluY3Rfc3RhdGVzX2NvbXBsZXRlIDwtIGRhdGEuZnJhbWUoaG9tZXRvd25fc3RhdGVfY2xlYW4gPSBob21ldG93bl9zdGF0ZXNfY29tcGxldGUpXG5cbmBgYCJ9 -->

```r
distinct_states_complete <- data.frame(hometown_state_clean = hometown_states_complete)

```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiRXJyb3IgaW4gZGF0YS5mcmFtZShob21ldG93bl9zdGF0ZV9jbGVhbiA9IGhvbWV0b3duX3N0YXRlc19jb21wbGV0ZSkgOiBcbiAgb2JqZWN0ICdob21ldG93bl9zdGF0ZXNfY29tcGxldGUnIG5vdCBmb3VuZFxuIn0= -->

```
Error in data.frame(hometown_state_clean = hometown_states_complete) : 
  object 'hometown_states_complete' not found
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuXG4jIE9USEVSIC0gdXNlIGZvciBtZXNzaW5nIGFyb3VuZFxuXG4jZGlzdHJpYnV0aW9uIDwtIGhvbWV0b3duc19jb21wbGV0ZSAlPiVcbiAgI2dyb3VwX2J5KHRvdGFsX3BsYXllcnMpICU+JVxuICAjc3VtbWFyaXNlKHRvdGFsID0gbigpKVxuXG4jZml2ZV9wbHVzIDwtIGhvbWV0b3duc19jb21wbGV0ZSAlPiVcbiAgI2ZpbHRlcih0b3RhbF9wbGF5ZXJzID49IDUpICU+JVxuICAjYXJyYW5nZShkZXNjKHBsYXllcnNfcGVyX3Rob3VzYW5kKSlcblxuI3dyaXRlX2NzdihmaXZlX3BsdXMsIGZpbGUgPSBcImZpdmVfcGx1c19wbGF5ZXJzLmNzdlwiKVxuXG5gYGAifQ== -->

```r

# OTHER - use for messing around

#distribution <- hometowns_complete %>%
  #group_by(total_players) %>%
  #summarise(total = n())

#five_plus <- hometowns_complete %>%
  #filter(total_players >= 5) %>%
  #arrange(desc(players_per_thousand))

#write_csv(five_plus, file = "five_plus_players.csv")

```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->

