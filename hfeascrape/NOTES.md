
1. Get a list:

POST to http://guide.hfea.gov.uk/guide/AdvancedSearch.aspx

Fields
    Location :
        ## ctl00$cph$rcbRegion = 'London'

        ctl00$cph$tbPostCode / ctl00_cph_tbPostCode_text = 'SW18 5LX'
        ctl00$cph$rcbPostCodeDistance / ctl00_cph_rcbPostCodeDistance_Input = 'National'

    Type
        ctl00$cph$radFundingForTreatment / ctl00_cph_rbPrivate = 1

    Age
        ctl00$cph$rcbUpperAgeLimit / ctl00_cph_rcbUpperAgeLimit_Input = 35 / 'Under 35 years'
        or
        ctl00_cph_rcbUpperAgeLimit_ClientState = {"logEntries":[],"value":"35","text":"Under 35 years","enabled":true}

    Facilities
        ctl00$cph$cbICSI_LT / ctl00_cph_cbICSI_LT = 1830

HAR for post captured from chrome

              {
                "name": "ctl00_cph_rsm_TSM",
                "value": "%3B%3BSystem.Web.Extensions%2C+Version%3D1.0.61025.0%2C+Culture%3Dneutral%2C+PublicKeyToken%3D31bf3856ad364e35%3Aen-US%3A1f0f78f9-0731-4ae9-b308-56936732ccb8%3Aea597d4b%3Ab25378d2%3BTelerik.Web.UI%2C+Version%3D2010.2.713.20%2C+Culture%3Dneutral%2C+PublicKeyToken%3D121fae78165ba3d4%3Aen-US%3Af582e5dd-2549-4dd3-b0ef-95cf4b5dc277%3A16e4e7cd%3Aed16cbdc%3Ab7778d6c%3Af7645509%3A24ee1bba%3A1e771326%3Aaa288e2d%3A874f8ea2%3A19620875%3A39040b5c%3B"
              },
              {
                "name": "__EVENTTARGET",
                "value": ""
              },
              {
                "name": "__EVENTARGUMENT",
                "value": ""
              },
              {
                "name": "__VIEWSTATE",
                "value": "%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1YmEzZDQWDgICDw8WAh8IaGRkAgMPDxYCHwhoZGQCBA8PFgIfCGhkZAIFDw8WAh8IaGRkAgYPDxYCHwhoZGQCBw8PFgIfCGhkZAIIDw8WAh8IZ2RkGAQFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxZNBRNjdGwwMCRjcGgkcmNiUmVnaW9uBQ5jdGwwMCRjcGgkclRUMQUdY3RsMDAkY3BoJHJjYlBvc3RDb2RlRGlzdGFuY2UFE2N0bDAwJGNwaCRyYlByaXZhdGUFD2N0bDAwJGNwaCRyYk5IUwUWY3RsMDAkY3BoJHJkUHJpdmF0ZU5IUwUaY3RsMDAkY3BoJHJjYlVwcGVyQWdlTGltaXQFEmN0bDAwJGNwaCRjYklWRl9MVAUTY3RsMDAkY3BoJGNiSUNTSV9MVAURY3RsMDAkY3BoJGNiRVRfTFQFEmN0bDAwJGNwaCRjYlBHRF9MVAUSY3RsMDAkY3BoJGNiUEdTX0xUBRZjdGwwMCRjcGgkY2JTVE9SRUdHX0xUBRVjdGwwMCRjcGgkY2JTVE9SRU1fTFQFFmN0bDAwJGNwaCRjYlNUT1JFU1BfTFQFFmN0bDAwJGNwaCRjYlNUT1JFT1ZfTFQFF2N0bDAwJGNwaCRjYlNUT1JFVEVTX0xUBRFjdGwwMCRjcGgkY2JJTl9MVAUTY3RsMDAkY3BoJGNiR0lGVF9MVAUSY3RsMDAkY3BoJGNiSVZNX0xUBR1jdGwwMCRjcGgkY2JWaXJhbEluZmVjdElWRl9FQwUgY3RsMDAkY3BoJGNiVmlyYWxJbmZlY3RESUdJRlRfRUMFGGN0bDAwJGNwaCRjYkRPTk9SSUNTSV9MVAUXY3RsMDAkY3BoJGNiRE9OT1JJVkZfTFQFF2N0bDAwJGNwaCRjYkRPTk9SRUdHX0xUBRZjdGwwMCRjcGgkY2JET05PUkVNX0xUBRljdGwwMCRjcGgkY2JTVE9SRUlWRkVNX0xUBRFjdGwwMCRjcGgkY2JDRV9MVAUTY3RsMDAkY3BoJGNiVFNCQ19MVAUTY3RsMDAkY3BoJGNiVEVCQ19MVAUSY3RsMDAkY3BoJGNiRlBFX0xUBRNjdGwwMCRjcGgkY2JGRUNFX0xUBRJjdGwwMCRjcGgkY2JGT0JfTFQFEWN0bDAwJGNwaCRjYlZFX0xUBRFjdGwwMCRjcGgkY2JWQl9MVAUSY3RsMDAkY3BoJGNiTEFWX0xUBRRjdGwwMCRjcGgkY2JURU1CQ19MVAUTY3RsMDAkY3BoJGNiQ1BUVF9MVAUQY3RsMDAkY3BoJGNiVl9MVAURY3RsMDAkY3BoJGNiQUhNQ0wFEmN0bDAwJGNwaCRjYkVITV9MVAUSY3RsMDAkY3BoJGNiQU9FX0xUBRVjdGwwMCRjcGgkY2JJQ1NJREVfTFQFFWN0bDAwJGNwaCRjYkdJRlREU19MVAUVY3RsMDAkY3BoJGNiR0lGVERFX0xUBRNjdGwwMCRjcGgkY2JFR0dDX0xUBRJjdGwwMCRjcGgkY2JTUENfTFQFE2N0bDAwJGNwaCRjYk9WVENfTFQFEWN0bDAwJGNwaCRjYlNQX0xUBRNjdGwwMCRjcGgkY2JFR0dQX0xUBRNjdGwwMCRjcGgkY2JUUldHX0xUBRFjdGwwMCRjcGgkY2JDU19MVAUSY3RsMDAkY3BoJGNiTklBX0xUBRJjdGwwMCRjcGgkY2JDVUxfTFQFEWN0bDAwJGNwaCRjYkFIX0xUBRRjdGwwMCRjcGgkY2JNT1JQSF9MVAUTY3RsMDAkY3BoJGNiTUFOSV9MVAUUY3RsMDAkY3BoJGNiVFJXQkVfTFQFEmN0bDAwJGNwaCRjYkZPU19MVAUTY3RsMDAkY3BoJGNiRk9UVF9MVAURY3RsMDAkY3BoJGNiRkVfTFQFFWN0bDAwJGNwaCRjYlZJVEVHR19MVAUTY3RsMDAkY3BoJGNiRk9PVF9MVAUTY3RsMDAkY3BoJGNiU0VPUF9MVAUUY3RsMDAkY3BoJGNiU09UT1BfTFQFE2N0bDAwJGNwaCRjYlNQT1BfTFQFFWN0bDAwJGNwaCRjYlNFR0dPUF9MVAUUY3RsMDAkY3BoJGNiU1RUT1BfTFQFGmN0bDAwJGNwaCRjYlJlY0RvblNwZXJtX0RSBRpjdGwwMCRjcGgkY2JSZWNFZ2dEb25vcl9EUgUaY3RsMDAkY3BoJGNiUmVjRW1iRG9ub3JfRFIFGWN0bDAwJGNwaCRjYktub3duRG9ub3JfRFIFHWN0bDAwJGNwaCRjYlJlY090aGVyc0Rvbm9yX0RSBRpjdGwwMCRjcGgkY2JSZWNSZXNEb25vcl9EUgUbY3RsMDAkY3BoJGNiU3Blcm1TaGFyaW5nX0RSBRljdGwwMCRjcGgkY2JFZ2dTaGFyaW5nX0RSBR9jdGwwMCRjcGgkc3VibWl0QWxsQ2xpbmljU2VhcmNoBRpjdGwwMCRjcGgkcmNiVXBwZXJBZ2VMaW1pdA8UKwACBQhBbGwgYWdlcwUBMWQFHWN0bDAwJGNwaCRyY2JQb3N0Q29kZURpc3RhbmNlDxQrAAIFCE5hdGlvbmFsBQQxMDAwZAUTY3RsMDAkY3BoJHJjYlJlZ2lvbg8UKwACBQ1TZWxlY3QgcmVnaW9uBQEwZJ9Mqjp2Q2AWn83KdAZGAkxWLHek"
              },
              {
                "name": "__EVENTVALIDATION",
                "value": "%2FwEWSgKx1cyeAQKWhYsLArXN5qILArTXtakPApmC8P0KAqrox4AOAuDIvesLAvjR77gPAqHXt6IPAtzExs8PAsznzqAOAtv1%2F88OApHIq%2BECArms3%2BoNArTI1fELAsHjiNMHAsKHuOcKAqyS%2BOcFAp7ZkaMFAoj93JkLAonZnNYNAt68mZYFAonv0JEIAsfqmPUMAprKgf0LAor8r5EHAor856MHAuW%2B4cYJAveQ6OAFAqjenLECAo%2FFgf0LAo%2FFhf4LAu6TqekNArvzpOYLAsOPqJgOAp7Ar4kLAtqIsJYJAt6H8PgKAoK%2F7cUJAunT6dkGAtrGm58BAtrG47EBAvry7E8CjsOuxwwCj4vUzwcC6sTN7wsC%2BvKYjQkC%2Bfm7lwYCmsrJ7gsC4ZeOewL9n4ZZAtzJ7fcLApihxpANAp%2Fh5f0BAquwvb0MAvPal5oPAuaOtJcOAr%2FJgf0LAubOou8HArPzyesCAuDuwfgEArTAvZcEAuDu7esEApb%2F9rUKArTA2ZQEAqja2qgGApr97s0LApzO66oMAtrTrqQOAojjotkCAsPVyooHAqLmqtsJAr6S89YOAsS2i4cBGIhFUmozftkN8hMzS2DuA5JjnBc%3D"
              },
              {
                "name": "ctl00_cph_tbPostCode_text",
                "value": "SW18+5LX"
              },
              {
                "name": "ctl00%24cph%24tbPostCode",
                "value": "SW18+5LX"
              },
              {
                "name": "ctl00_cph_tbPostCode_ClientState",
                "value": ""
              },
              {
                "name": "ctl00_cph_rcbRegion_ClientState",
                "value": "%7B%22logEntries%22%3A%5B%5D%2C%22value%22%3A%220%22%2C%22text%22%3A%22Select+region%22%2C%22enabled%22%3Afalse%7D"
              },
              {
                "name": "ctl00_cph_rTT1_ClientState",
                "value": ""
              },
              {
                "name": "ctl00%24cph%24rcbPostCodeDistance",
                "value": "National"
              },
              {
                "name": "ctl00_cph_rcbPostCodeDistance_ClientState",
                "value": "%7B%22logEntries%22%3A%5B%5D%2C%22value%22%3A%221000%22%2C%22text%22%3A%22National%22%2C%22enabled%22%3Atrue%7D"
              },
              {
                "name": "ctl00%24cph%24radFundingForTreatment",
                "value": "rbPrivate"
              },
              {
                "name": "ctl00%24cph%24rcbUpperAgeLimit",
                "value": "Under+35+years"
              },
              {
                "name": "ctl00_cph_rcbUpperAgeLimit_ClientState",
                "value": "%7B%22logEntries%22%3A%5B%5D%2C%22value%22%3A%2235%22%2C%22text%22%3A%22Under+35+years%22%2C%22enabled%22%3Atrue%7D"
              },
              {
                "name": "ctl00%24cph%24cbICSI_LT",
                "value": "1830"
              },
              {
                "name": "ctl00%24cph%24submitAllClinicSearch.x",
                "value": "74"
              },
              {
                "name": "ctl00%24cph%24submitAllClinicSearch.y",
                "value": "14"
              }
