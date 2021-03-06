import requests, re, sys, os, urllib
from bs4 import BeautifulSoup

har = [
    {
        # validated by .NET, so ignore, but do not remove or change
        "name": "ctl00_cph_rsm_TSM",
        "value": "%3B%3BSystem.Web.Extensions%2C+Version%3D1.0.61025.0%2C+Culture%3Dneutral%2C+PublicKeyToken%3D31bf3856ad364e35%3Aen-US%3A1f0f78f9-0731-4ae9-b308-56936732ccb8%3Aea597d4b%3Ab25378d2%3BTelerik.Web.UI%2C+Version%3D2010.2.713.20%2C+Culture%3Dneutral%2C+PublicKeyToken%3D121fae78165ba3d4%3Aen-US%3Af582e5dd-2549-4dd3-b0ef-95cf4b5dc277%3A16e4e7cd%3Aed16cbdc%3Ab7778d6c%3Af7645509%3A24ee1bba%3A1e771326%3Aaa288e2d%3A874f8ea2%3A19620875%3A39040b5c%3B"
    },
    {
        # validated by .NET, so ignore, but do not remove or change
        "name": "__VIEWSTATE",
        # page 1
        "value": "%2FwEPDwULLTE2Mzc"
        + "zODMyNDEPZBYCZg9kFgQCAw8WAh4EVGV4dAUfPGxpPkFkdmFuY2VkIGNsaW5pYyBzZWFyY2g8L2xpPmQCBQ9kFgICAQ9kFgYCAw9kFgoCAQ8UKwAIDxYGHhdFbmFibGVBamF4U2tpblJlbmRlcmluZ2geDUxhYmVsQ3NzQ2xhc3MFB3JpTGFiZWwfAAUIU1cxOCA1TFhkFgYeBVdpZHRoGwAAAAAAQF9AAQAAAB4IQ3NzQ2xhc3MFEXJpVGV4dEJveCByaUhvdmVyHgRfIVNCAoICFgYfAxsAAAAAAEBfQAEAAAAfBAURcmlUZXh0Qm94IHJpRXJyb3IfBQKCAhYGHwMbAAAAAABAX0ABAAAAHwQFE3JpVGV4dEJveCByaUZvY3VzZWQfBQKCAhYGHwMbAAAAAABAX0ABAAAAHwQFE3JpVGV4dEJveCByaUVuYWJsZWQfBQKCAhYGHwMbAAAAAABAX0ABAAAAHwQFFHJpVGV4dEJveCByaURpc2FibGVkHwUCggIWBh8DGwAAAAAAQF9AAQAAAB8EBRFyaVRleHRCb3ggcmlFbXB0eR8FAoICFgYfAxsAAAAAAEBfQAEAAAAfBAUQcmlUZXh0Qm94IHJpUmVhZB8FAoICZAIFDxQrAAIPFggfAAUNU2VsZWN0IHJlZ2lvbh4TY2FjaGVkU2VsZWN0ZWRWYWx1ZWQfAWgeB0VuYWJsZWRoZBAWDmYCAQICAgMCBAIFAgYCBwIIAgkCCgILAgwCDRYOFCsAAg8WAh4IU2VsZWN0ZWRnZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYEHwhoHwdoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQUKwACDxYCHwhoZGQPFg5mZmZmZmZmZmZmZmZmZhYBBXdUZWxlcmlrLldlYi5VSS5SYWRDb21ib0JveEl0ZW0sIFRlbGVyaWsuV2ViLlVJLCBWZXJzaW9uPTIwMTAuMi43MTMuMjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MTIxZmFlNzgxNjViYTNkNBYcAgIPDxYCHwhnZGQCAw8PFgIfCGhkZAIEDw8WAh8IaGRkAgUPDxYCHwhoZGQCBg8PFgQfCGgfB2hkZAIHDw8WAh8IaGRkAggPDxYCHwhoZGQCCQ8PFgIfCGhkZAIKDw8WAh8IaGRkAgsPDxYCHwhoZGQCDA8PFgIfCGhkZAINDw8WAh8IaGRkAg4PDxYCHwhoZGQCDw8PFgIfCGhkZAIHDxYCHghkaXNhYmxlZAUIZGlzYWJsZWRkAgkPDxYEHwdoHwFoZGQCDQ8UKwACDxYIHwAFCE5hdGlvbmFsHwZkHwFoHwdnZBAWCmYCAQICAgMCBAIFAgYCBwIIAgkWChQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGdkZA8WCmZmZmZmZmZmZmYWAQV3VGVsZXJpay5XZWIuVUkuUmFkQ29tYm9Cb3hJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEwLjIuNzEzLjIwLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRv"
        + "a2VuPTEyMWZhZTc4MTY1YmEzZDQWFAICDw8WAh8IaGRkAgMPDxYCHwhoZGQCBA8PFgIfCGhkZAIFDw8WAh8IaGRkAgYPDxYCHwhoZGQCBw8PFgIfCGhkZAIIDw8WAh8IaGRkAgkPDxYCHwhoZGQCCg8PFgIfCGhkZAILDw8WAh8IZ2RkAgUPDxYCHwFoZGQCDQ9kFgICAQ8UKwACDxYGHwAFCEFsbCBhZ2VzHwFoHwZkZBAWB2YCAQICAgMCBAIFAgYWBxQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGhkZBQrAAIPFgIfCGdkZA8WB2ZmZmZmZmYWAQV3VGVsZXJpay5XZWIuVUkuUmFkQ29tYm9Cb3hJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEwLjIuNzEzLjIwLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTEyMWZhZTc4MTY1YmEzZDQWDgICDw8WAh8IaGRkAgMPDxYCHwhoZGQCBA8PFgIfCGhkZAIFDw8WAh8IaGRkAgYPDxYCHwhoZGQCBw8PFgIfCGhkZAIIDw8WAh8IZ2RkGAQFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxZNBRNjdGwwMCRjcGgkcmNiUmVnaW9uBQ5jdGwwMCRjcGgkclRUMQUdY3RsMDAkY3BoJHJjYlBvc3RDb2RlRGlzdGFuY2UFE2N0bDAwJGNwaCRyYlByaXZhdGUFD2N0bDAwJGNwaCRyYk5IUwUWY3RsMDAkY3BoJHJkUHJpdmF0ZU5IUwUaY3RsMDAkY3BoJHJjYlVwcGVyQWdlTGltaXQFEmN0bDAwJGNwaCRjYklWRl9MVAUTY3RsMDAkY3BoJGNiSUNTSV9MVAURY3RsMDAkY3BoJGNiRVRfTFQFEmN0bDAwJGNwaCRjYlBHRF9MVAUSY3RsMDAkY3BoJGNiUEdTX0xUBRZjdGwwMCRjcGgkY2JTVE9SRUdHX0xUBRVjdGwwMCRjcGgkY2JTVE9SRU1fTFQFFmN0bDAwJGNw"
        + "aCRjYlNUT1JFU1BfTFQFFmN0bDAwJGNwaCRjYlNUT1JFT1ZfTFQFF2N0bDAwJGNwaCRjYlNUT1JFVEVTX0xUBRFjdGwwMCRjcGgkY2JJTl9MVAUTY3RsMDAkY3BoJGNiR0lGVF9MVAUSY3RsMDAkY3BoJGNiSVZNX0xUBR1jdGwwMCRjcGgkY2JWaXJhbEluZmVjdElWRl9FQwUgY3RsMDAkY3BoJGNiVmlyYWxJbmZlY3RESUdJRlRfRUMFGGN0bDAwJGNwaCRjYkRPTk9SSUNTSV9MVAUXY3RsMDAkY3BoJGNiRE9OT1JJVkZfTFQFF2N0bDAwJGNwaCRjYkRPTk9SRUdHX0xUBRZjdGwwMCRjcGgkY2JET05PUkVNX0xUBRljdGwwMCRjcGgkY2JTVE9SRUlWRkVNX0xUBRFjdGwwMCRjcGgkY2JDRV9MVAUTY3RsMDAkY3BoJGNiVFNCQ19MVAUTY3RsMDAkY3BoJGNiVEVCQ19MVAUSY3RsMDAkY3BoJGNiRlBFX0xUBRNjdGwwMCRjcGgkY2JGRUNFX0xUBRJjdGwwMCRjcGgkY2JGT0JfTFQFEWN0bDAwJGNwaCRjYlZFX0xUBRFjdGwwMCRjcGgkY2JWQl9MVAUSY3RsMDAkY3BoJGNiTEFWX0xUBRRjdGwwMCRjcGgkY2JURU1CQ19MVAUTY3RsMDAkY3BoJGNiQ1BUVF9MVAUQY3RsMDAkY3BoJGNiVl9MVAURY3RsMDAkY3BoJGNiQUhNQ0wFEmN0bDAwJGNwaCRjYkVITV9MVAUSY3RsMDAkY3BoJGNiQU9FX0xUBRVjdGwwMCRjcGgkY2JJQ1NJREVfTFQFFWN0bDAwJGNwaCRjYkdJRlREU19MVAUVY3RsMDAkY3BoJGNiR0lGVERFX0xUBRNjdGwwMCRjcGgkY2JFR0dDX0xUBRJjdGwwMCRjcGgkY2JTUENfTFQFE2N0bDAwJGNwaCRjYk9WVENfTFQFEWN0bDAwJGNwaCRjYlNQX0xUBRNjdGwwMCRjcGgkY2JFR0dQX0xUBRNjdGwwMCRjcGgkY2JUUldHX0xUBRFjdGwwMCRjcGgkY2JDU19MVAUSY3RsMDAkY3BoJGNiTklBX0xUBRJjdGwwMCRjcGgkY2JDVUxfTFQFEWN0bDAwJGNwaCRjYkFIX0xUBRRjdGwwMCRjcGgkY2JNT1JQSF9MVAUTY3RsMDAkY3BoJGNiTUFOSV9MVAUUY3RsMDAkY3BoJGNiVFJXQkVfTFQFEmN0bDAwJGNwaCRjYkZPU19MVAUTY3RsMDAkY3BoJGNiRk9UVF9MVAURY3RsMDAkY3BoJGNiRkVfTFQFFWN0bDAwJGNwaCRjYlZJVEVHR19MVAUTY3RsMDAkY3BoJGNiRk9PVF9MVAUTY3RsMDAkY3BoJGNiU0VPUF9MVAUUY3RsMDAkY3BoJGNiU09UT1BfTFQFE2N0bDAwJGNwaCRjYlNQT1BfTFQFFWN0bDAwJGNwaCRjYlNFR0dPUF9MVAUUY3RsMDAkY3BoJGNiU1RUT1BfTFQFGmN0bDAwJGNwaCRjYlJlY0RvblNwZXJtX0RSBRpjdGwwMCRjcGgkY2JSZWNFZ2dEb25vcl9EUgUaY3RsMDAkY3BoJGNiUmVjRW1iRG9ub3JfRFIFGWN0bDAwJGNwaCRjYktub3duRG9ub3JfRFIFHWN0bDAwJGNwaCRjYlJlY090aGVyc0Rvbm9yX0RSBRpjdGwwMCRjcGgkY2JSZWNSZXNEb25vcl9EUgUbY3RsMDAkY3BoJGNiU3Blcm1TaGFyaW5nX0RSBRljdGwwMCRjcGgkY2JFZ2dTaGFyaW5nX0RSBR9jdGwwMCRjcGgkc3VibWl0QWxsQ2xpbmljU2VhcmNoBRpjdGwwMCRjcGgkcmNiVXBwZXJBZ2VMaW1pdA8UKwACBQhBbGwgYWdlcwUBMWQFHWN0bDAwJGNwaCRyY2JQb3N0Q29kZURpc3RhbmNlDxQrAAIFCE5hdGlvbmFsBQQxMDAwZAUTY3RsMDAkY3BoJHJjYlJlZ2lvbg8UKwACBQ1TZWxlY3QgcmVnaW9uBQEwZJ9Mqjp2Q2AWn83KdAZGAkxWLHek"
        # page 2
        #"value": "%2FwEPDwUJNTk2MzU3ODY0D2QWAmYPZBYEAgMPFgIeBFRleHQFFzxsaT5TZWFyY2ggcmVzdWx0czwvbGk%2BZAIFD2QWAgIBD2QWCAIBD2QWBgIBDxYCHwAFAzEyOWQCAw8WBB8ABRYxMDAwIG1pbGVzIG9mIFNXMTggNUxYHgdWaXNpYmxlZ2QCBw8PFgIfAWdkFg4CAQ8PFgYfAAUIUHJldmlvdXMeD0NvbW1hbmRBcmd1bWVudAUBMB8BaGRkAgMPFgIfAAUBMWQCCQ8PFgQfAAUETmV4dB8CBQEyZGQCCw8WAh8ABRNNaWxlcyBmcm9tIHBvc3Rjb2RlZAINDxYCHwAF%2BxU8dHI%2BPHRkPjxhIGhyZWY9T3ZlcnZpZXcuYXNweD9jb2RlPTI5OSZzPXAmcHY9U1cxODVMWCZkPTIuNiZuYXY9MT5DUkVBVEUgQ2VudHJlIGZvciBSZXByb2R1Y3Rpb24gYW5kIEFkdmFuY2VkIFRlY2hub2xvZ3k8L2E%2BPHVsPjxsaT48c3Ryb25nPkZ1bmRpbmcgZm9yIHRyZWF0bWVudDo8L3N0cm9uZz4gVHJlYXRzIE5IUyBwYXRpZW50cyxUcmVhdHMgcHJpdmF0ZSBwYXRpZW50czwvbGk%2BPGxpPjxzdHJvbmc%2BVHJlYXRtZW50czo8L3N0cm9uZz4gSW5zZW1pbmF0aW9uLElWRixJQ1NJPC9saT48L3VsPjwvdGQ%2BPHRkIGNsYXNzPSJyZXN1bHRzQ29sMiI%2BMi42PC90ZD48L3RyPjx0cj48dGQ%2BPGEgaHJlZj1PdmVydmlldy5hc3B4P2NvZGU9MTU4JnM9cCZwdj1TVzE4NUxYJmQ9Mi44Jm5hdj0xPkNoZWxzZWEgJiBXZXN0bWluc3RlciBIb3NwaXRhbDwvYT48dWw%2BPGxpPjxzdHJvbmc%2BRnVuZGluZyBmb3IgdHJlYXRtZW50Ojwvc3Ryb25nPiBUcmVhdHMgTkhTIHBhdGllbnRzLFRyZWF0cyBwcml2YXRlIHBhdGllbnRzPC9saT48bGk%2BPHN0cm9uZz5UcmVhdG1lbnRzOjwvc3Ryb25nPiBJbnNlbWluYXRpb24sR0lGVCxJVkYsSUNTSTwvbGk%2BPC91bD48L3RkPjx0ZCBjbGFzcz0icmVzdWx0c0NvbDIiPjIuODwvdGQ%2BPC90cj48dHI%2BPHRkPjxhIGhyZWY9T3ZlcnZpZXcuYXNweD9jb2RlPTYmcz1wJnB2PVNXMTg1TFgmZD0zLjYmbmF2PTE%2BVGhlIExpc3RlciBGZXJ0aWxpdHkgQ2xpbmljPC9hPjx1bD48bGk%2BPHN0cm9uZz5GdW5kaW5nIGZvciB0cmVhdG1lbnQ6PC9zdHJvbmc%2BIFRyZWF0cyBOSFMgcGF0aWVudHMsVHJlYXRzIHByaXZhdGUgcGF0aWVudHM8L2xpPjxsaT48c3Ryb25nPlRyZWF0bWVudHM6PC9zdHJvbmc%2BIDwvbGk%2BPC91bD48L3RkPjx0ZCBjbGFzcz0icmVzdWx0c0NvbDIiPjMuNjwvdGQ%2BPC90cj48dHI%2BPHRkPjxhIGhyZWY9T3ZlcnZpZXcuYXNweD9jb2RlPTI3MCZzPXAmcHY9U1cxODVMWCZkPTQuMSZuYXY9MT5LaW5nc3RvbiBIb3NwaXRhbCBBQ1U8L2E%2BPHVsPjxsaT48c3Ryb25nPkZ1bmRpbmcgZm9yIHRyZWF0bWVudDo8L3N0cm9uZz4gVHJlYXRzIE5IUyBwYXRpZW50cyxUcmVhdHMgcHJpdmF0ZSBwYXRpZW50czwvbGk%2BPGxpPjxzdHJvbmc%2BVHJlYXRtZW50czo8L3N0cm9uZz4gPC9saT48L3VsPjwvdGQ%2BPHRkIGNsYXNzPSJyZXN1bHRzQ29sMiI%2BNC4xPC90ZD48L3RyPjx0cj48dGQ%2BPGEgaHJlZj1PdmVydmlldy5hc3B4P2NvZGU9MjU5JnM9cCZwdj1TVzE4NUxYJmQ9NC41Jm5hdj0xPkVwc29tIEFuZCBTdCBIZWxpZXIgTkhTIFRydXN0PC9hPjx1bD48bGk%2BPHN0cm9uZz5GdW5kaW5nIGZvciB0cmVhdG1lbnQ6PC9zdHJvbmc%2BIFRyZWF0cyBOSFMgcGF0aWVudHMsVHJlYXRzIHByaXZhdGUgcGF0aWVudHM8L2xpPjxsaT48c3Ryb25nPlRyZWF0bWVudHM6PC9zdHJvbmc%2BIDwvbGk%2BPC91bD48L3RkPjx0ZCBjbGFzcz0icmVzdWx0c0NvbDIiPjQuNTwvdGQ%2BPC90cj48dHI%2BPHRkPjxhIGhyZWY9T3ZlcnZpZXcuYXNweD9jb2RlPTEwOSZzPXAmcHY9U1cxODVMWCZkPTUmbmF2PTE%2BQXNzaXN0ZWQgQ29uY2VwdGlvbiBVbml0LCBLaW5nJ3MgQ29sbGVnZSBIb3NwaXRhbDwvYT48dWw%2BPGxpPjxzdHJvbmc%2BRnVuZGluZyBmb3IgdHJlYXRtZW50Ojwvc3Ryb25nPiBUcmVhdHMgTkhTIHBhdGllbnRzLFRyZWF0cyBwcml2YXRlIHBhdGllbnRzPC9saT48bGk%2BPHN0cm9uZz5UcmVhdG1lbnRzOjwvc3Ryb25nPiA8L2xpPjwvdWw%2BPC90ZD48dGQgY2xhc3M9InJlc3VsdHNDb2wyIj41PC90ZD48L3RyPjx0cj48dGQ%2BPGEgaHJlZj1PdmVydmlldy5hc3B4P2NvZGU9Nzgmcz1wJnB2PVNXMTg1TFgmZD01LjEmbmF2PTE%2BSVZGIEhhbW1lcnNtaXRoPC9hPjx1bD48bGk%2BPHN0cm9uZz5GdW5kaW5nIGZvciB0cmVhdG1lbnQ6PC9zdHJvbmc%2BIFRyZWF0cyBOSFMgcGF0aWVudHMsVHJlYXRzIHByaXZhdGUgcGF0aWVudHM8L2xpPjxsaT48c3Ryb25nPlRyZWF0bWVudHM6PC9zdHJvbmc%2BIEluc2VtaW5hdGlvbixJVkYsSUNTSSxQR0QsUEdTPC9saT48L3VsPjwvdGQ%2BPHRkIGNsYXNzPSJyZXN1bHRzQ29sMiI%2BNS4xPC90ZD48L3RyPjx0cj48dGQ%2BPGEgaHJlZj1PdmVydmlldy5hc3B4P2NvZGU9ODAmcz1wJnB2PVNXMTg1TFgmZD01LjEmbmF2PTE%2BQW5kcm9sb2d5IFVuaXQsIEhhbW1lcnNtaXRoIEhvc3BpdGFsPC9hPjx1bD48bGk%2BPHN0cm9uZz5GdW5kaW5nIGZvciB0cmVhdG1lbnQ6PC9zdHJvbmc%2BIFRyZWF0cyBOSFMgcGF0aWVudHMsVHJlYXRzIHByaXZhdGUgcGF0aWVudHM8L2xpPjxsaT48c3Ryb25nPlRyZWF0bWVudHM6PC9zdHJvbmc%2BIDwvbGk%2BPC91bD48L3RkPjx0ZCBjbGFzcz0icmVzdWx0c0NvbDIiPjUuMTwvdGQ%2BPC90cj48dHI%2BPHRkPjxhIGhyZWY9T3ZlcnZpZXcuYXNweD9jb2RlPTI5MyZzPXAmcHY9U1cxODVMWCZkPTUuNSZuYXY9MT5BbmRyb2xvZ3kgU29sdXRpb25zPC9hPjx1bD48bGk%2BPHN0cm9uZz5GdW5kaW5nIGZvciB0cmVhdG1lbnQ6PC9zdHJvbmc%2BIFRyZWF0cyBOSFMgcGF0aWVudHMsVHJlYXRzIHByaXZhdGUgcGF0aWVudHM8L2xpPjxsaT48c3Ryb25nPlRyZWF0bWVudHM6PC9zdHJvbmc%2BIEluc2VtaW5hdGlvbjwvbGk%2BPC91bD48L3RkPjx0ZCBjbGFzcz0icmVzdWx0c0NvbDIiPjUuNTwvdGQ%2BPC90cj48dHI%2BPHRkPjxhIGhyZWY9T3ZlcnZpZXcuYXNweD9jb2RlPTMyNyZzPXAmcHY9U1cxODVMWCZkPTUuNiZuYXY9MT5Cb3N0b24gUGxhY2U8L2E%2BPHVsPjxsaT48c3Ryb25nPlRyZWF0bWVudHM6PC9zdHJvbmc%2BIEluc2VtaW5hdGlvbixJVkYsSUNTSTwvbGk%2BPC91bD48L3RkPjx0ZCBjbGFzcz0icmVzdWx0c0NvbDIiPjUuNjwvdGQ%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YCHwloZGQCBw8PFgIfCWhkZAIIDw8WAh8JaGRkGAQFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxZNBRNjdGwwMCRjcGgkcmNiUmVnaW9uBQ5jdGwwMCRjcGgkclRUMQUdY3RsMDAkY3BoJHJjYlBvc3RDb2RlRGlzdGFuY2UFE2N0bDAwJGNwaCRyYlByaXZhdGUFD2N0bDAwJGNwaCRyYk5IUwUWY3RsMDAkY3BoJHJkUHJpdmF0ZU5IUwUaY3RsMDAkY3BoJHJjYlVwcGVyQWdlTGltaXQFEmN0bDAwJGNwaCRjYklWRl9MVAUTY3RsMDAkY3BoJGNiSUNTSV9MVAURY3RsMDAkY3BoJGNiRVRfTFQFEmN0bDAwJGNwaCRjYlBHRF9MVAUSY3RsMDAkY3BoJGNiUEdTX0xUBRZjdGwwMCRjcGgkY2JTVE9SRUdHX0xUBRVjdGwwMCRjcGgkY2JTVE9SRU1fTFQFFmN0bDAwJGNwaCRjYlNUT1JFU1BfTFQFFmN0bDAwJGNwaCRjYlNUT1JFT1ZfTFQFF2N0bDAwJGNwaCRjYlNUT1JFVEVTX0xUBRFjdGwwMCRjcGgkY2JJTl9MVAUTY3RsMDAkY3BoJGNiR0lGVF9MVAUSY3RsMDAkY3BoJGNiSVZNX0xUBR1jdGwwMCRjcGgkY2JWaXJhbEluZmVjdElWRl9FQwUgY3RsMDAkY3BoJGNiVmlyYWxJbmZlY3RESUdJRlRfRUMFGGN0bDAwJGNwaCRjYkRPTk9SSUNTSV9MVAUXY3RsMDAkY3BoJGNiRE9OT1JJVkZfTFQFF2N0bDAwJGNwaCRjYkRPTk9SRUdHX0xUBRZjdGwwMCRjcGgkY2JET05PUkVNX0xUBRljdGwwMCRjcGgkY2JTVE9SRUlWRkVNX0xUBRFjdGwwMCRjcGgkY2JDRV9MVAUTY3RsMDAkY3BoJGNiVFNCQ19MVAUTY3RsMDAkY3BoJGNiVEVCQ19MVAUSY3RsMDAkY3BoJGNiRlBFX0xUBRNjdGwwMCRjcGgkY2JGRUNFX0xUBRJjdGwwMCRjcGgkY2JGT0JfTFQFEWN0bDAwJGNwaCRjYlZFX0xUBRFjdGwwMCRjcGgkY2JWQl9MVAUSY3RsMDAkY3BoJGNiTEFWX0xUBRRjdGwwMCRjcGgkY2JURU1CQ19MVAUTY3RsMDAkY3BoJGNiQ1BUVF9MVAUQY3RsMDAkY3BoJGNiVl9MVAURY3RsMDAkY3BoJGNiQUhNQ0wFEmN0bDAwJGNwaCRjYkVITV9MVAUSY3RsMDAkY3BoJGNiQU9FX0xUBRVjdGwwMCRjcGgkY2JJQ1NJREVfTFQFFWN0bDAwJGNwaCRjYkdJRlREU19MVAUVY3RsMDAkY3BoJGNiR0lGVERFX0xUBRNjdGwwMCRjcGgkY2JFR0dDX0xUBRJjdGwwMCRjcGgkY2JTUENfTFQFE2N0bDAwJGNwaCRjYk9WVENfTFQFEWN0bDAwJGNwaCRjYlNQX0xUBRNjdGwwMCRjcGgkY2JFR0dQX0xUBRNjdGwwMCRjcGgkY2JUUldHX0xUBRFjdGwwMCRjcGgkY2JDU19MVAUSY3RsMDAkY3BoJGNiTklBX0xUBRJjdGwwMCRjcGgkY2JDVUxfTFQFEWN0bDAwJGNwaCRjYkFIX0xUBRRjdGwwMCRjcGgkY2JNT1JQSF9MVAUTY3RsMDAkY3BoJGNiTUFOSV9MVAUUY3RsMDAkY3BoJGNiVFJXQkVfTFQFEmN0bDAwJGNwaCRjYkZPU19MVAUTY3RsMDAkY3BoJGNiRk9UVF9MVAURY3RsMDAkY3BoJGNiRkVfTFQFFWN0bDAwJGNwaCRjYlZJVEVHR19MVAUTY3RsMDAkY3BoJGNiRk9PVF9MVAUTY3RsMDAkY3BoJGNiU0VPUF9MVAUUY3RsMDAkY3BoJGNiU09UT1BfTFQFE2N0bDAwJGNwaCRjYlNQT1BfTFQFFWN0bDAwJGNwaCRjYlNFR0dPUF9MVAUUY3RsMDAkY3BoJGNiU1RUT1BfTFQFGmN0bDAwJGNwaCRjYlJlY0RvblNwZXJtX0RSBRpjdGwwMCRjcGgkY2JSZWNFZ2dEb25vcl9EUgUaY3RsMDAkY3BoJGNiUmVjRW1iRG9ub3JfRFIFGWN0bDAwJGNwaCRjYktub3duRG9ub3JfRFIFHWN0bDAwJGNwaCRjYlJlY090aGVyc0Rvbm9yX0RSBRpjdGwwMCRjcGgkY2JSZWNSZXNEb25vcl9EUgUbY3RsMDAkY3BoJGNiU3Blcm1TaGFyaW5nX0RSBRljdGwwMCRjcGgkY2JFZ2dTaGFyaW5nX0RSBR9jdGwwMCRjcGgkc3VibWl0QWxsQ2xpbmljU2VhcmNoBRpjdGwwMCRjcGgkcmNiVXBwZXJBZ2VMaW1pdA8UKwACBQ5VbmRlciAzNSB5ZWFycwUCMzVkBR1jdGwwMCRjcGgkcmNiUG9zdENvZGVEaXN0YW5jZQ8UKwACBQhOYXRpb25hbAUEMTAwMGQFE2N0bDAwJGNwaCRyY2JSZWdpb24PFCsAAgUNU2VsZWN0IHJlZ2lvbgUBMGQyy%2Fp9vUl2VC%2FKsoyYNtyyROlyhQ%3D%3D"
    },
    {
        "name": "__EVENTTARGET",
        "value" : "",
        # page 1
        #"value": "ctl00%24cph%24pgLinkUpper%251"
        # page 2
        #"value": "ctl00%24cph%24pgLinkUpper%252"
    },
    {
        "name": "__EVENTARGUMENT",
        "value": ""
    },
    {
        # validated by .NET, so ignore, but do not remove or change
        "name": "__EVENTVALIDATION",
        # page 1
        "value": "%2FwEWSgKx1cyeAQKWhYsLArXN5qILArTXtakPApmC8P0KAqrox4AOAuDIvesLAvjR77gPAqHXt6IPAtzExs8PAsznzqAOAtv1%2F88OApHIq%2BECArms3%2BoNArTI1fELAsHjiNMHAsKHuOcKAqyS%2BOcFAp7ZkaMFAoj93JkLAonZnNYNAt68mZYFAonv0JEIAsfqmPUMAprKgf0LAor8r5EHAor856MHAuW%2B4cYJAveQ6OAFAqjenLECAo%2FFgf0LAo%2FFhf4LAu6TqekNArvzpOYLAsOPqJgOAp7Ar4kLAtqIsJYJAt6H8PgKAoK%2F7cUJAunT6dkGAtrGm58BAtrG47EBAvry7E8CjsOuxwwCj4vUzwcC6sTN7wsC%2BvKYjQkC%2Bfm7lwYCmsrJ7gsC4ZeOewL9n4ZZAtzJ7fcLApihxpANAp%2Fh5f0BAquwvb0MAvPal5oPAuaOtJcOAr%2FJgf0LAubOou8HArPzyesCAuDuwfgEArTAvZcEAuDu7esEApb%2F9rUKArTA2ZQEAqja2qgGApr97s0LApzO66oMAtrTrqQOAojjotkCAsPVyooHAqLmqtsJAr6S89YOAsS2i4cBGIhFUmozftkN8hMzS2DuA5JjnBc%3D"
        # "value": "%2FwEWcgLG2cLvCwKRh9nIBQLpwqqwAwKflebaBwLw0L%2BaBgLV56GFDAKmo%2FvECgKLut0vAtz1tu8OAsGMmdoEAunC6pgBAunC1r0IAunCwuIPAunCrocHAqCn%2F48BAo%2BbqqEIAqGi%2F5IFAtf0ur0JApqU6qgCArX9h74MAtDmpdMGAuvPw2gCru%2Fy0wkCydiQ6QMCoaK%2F%2BwICoaKroAoCoaKXxQECoaKD6ggC4sW1kAcCs%2BbkqQwC24u%2BpwUC24vSgg4C24va3wkC24vuugIC24uClgsC24uW8QMC24uqzAwC24vm3QYC24v6uA8CtObkqQwCtebkqQwCloWLCwK1zeaiCwK017WpDwKZgvD9CgKq6MeADgLgyL3rCwL40e%2B4DwKh17eiDwLcxMbPDwLM586gDgLb9f%2FPDgKRyKvhAgK5rN%2FqDQK0yNXxCwLB44jTBwLCh7jnCgKskvjnBQKe2ZGjBQKI%2FdyZCwKJ2ZzWDQLevJmWBQKJ79CRCALH6pj1DAKayoH9CwKK%2FK%2BRBwKK%2FOejBwLlvuHGCQL3kOjgBQKo3pyxAgKPxYH9CwKPxYX%2BCwLuk6npDQK786TmCwLDj6iYDgKewK%2BJCwLaiLCWCQLeh%2FD4CgKCv%2B3FCQLp0%2BnZBgLaxpufAQLaxuOxAQL68uxPAo7DrscMAo%2BL1M8HAurEze8LAvrymI0JAvn5u5cGAprKye4LAuGXjnsC%2FZ%2BGWQLcye33CwKYocaQDQKf4eX9AQKrsL29DALz2peaDwLmjrSXDgK%2FyYH9CwLmzqLvBwKz88nrAgLg7sH4BAK0wL2XBALg7u3rBAKW%2F%2Fa1CgK0wNmUBAKo2tqoBgKa%2Fe7NCwKczuuqDALa066kDgKI46LZAgLD1cqKBwKi5qrbCQK%2BkvPWDgLEtouHAS%2B419pVUVxnShJHV5rpoARlkVwc"
        # page 2
        #"value": "%2FwEWcALZnZOUCwK6%2FoPwAQKflebaBwLw0L%2BaBgLV56GFDAKmo%2FvECgKLut0vAtz1tu8OAsGMmdoEAunC6pgBAunC1r0IAunCwuIPAunCrocHAqCn%2F48BAryLnagPAtf0ur0JApqU6qgCArX9h74MAtDmpdMGAuvPw2gCru%2Fy0wkCydiQ6QMCoaK%2F%2BwICoaKroAoCoaKXxQECoaKD6ggC4sW1kAcCs%2BbkqQwC24u%2BpwUC24vSgg4C24va3wkC24vuugIC24uClgsC24uW8QMC24uqzAwC24vm3QYC24v6uA8CtObkqQwCtebkqQwCloWLCwK1zeaiCwK017WpDwKZgvD9CgKq6MeADgLgyL3rCwL40e%2B4DwKh17eiDwLcxMbPDwLM586gDgLb9f%2FPDgKRyKvhAgK5rN%2FqDQK0yNXxCwLB44jTBwLCh7jnCgKskvjnBQKe2ZGjBQKI%2FdyZCwKJ2ZzWDQLevJmWBQKJ79CRCALH6pj1DAKayoH9CwKK%2FK%2BRBwKK%2FOejBwLlvuHGCQL3kOjgBQKo3pyxAgKPxYH9CwKPxYX%2BCwLuk6npDQK786TmCwLDj6iYDgKewK%2BJCwLaiLCWCQLeh%2FD4CgKCv%2B3FCQLp0%2BnZBgLaxpufAQLaxuOxAQL68uxPAo7DrscMAo%2BL1M8HAurEze8LAvrymI0JAvn5u5cGAprKye4LAuGXjnsC%2FZ%2BGWQLcye33CwKYocaQDQKf4eX9AQKrsL29DALz2peaDwLmjrSXDgK%2FyYH9CwLmzqLvBwKz88nrAgLg7sH4BAK0wL2XBALg7u3rBAKW%2F%2Fa1CgK0wNmUBAKo2tqoBgKa%2Fe7NCwKczuuqDALa066kDgKI46LZAgLD1cqKBwKi5qrbCQK%2BkvPWDgLEtouHATfHQuQIgSX0C3erAGStdpooc8uN"
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
        # validated by .NET, so ignore, but do not remove or change
        "name": "ctl00%24cph%24submitAllClinicSearch.x",
        "value": "74"
    },
    {
        # validated by .NET, so ignore, but do not remove or change
        "name": "ctl00%24cph%24submitAllClinicSearch.y",
        "value": "14"
    },
]

harhdr = [
    {
      "name": "Cookie",
      "value": "ASP.NET_SessionId=zatmde2mbwixolr4lmcp3yyb"
    },
    {
      "name": "Origin",
      "value": "http://guide.hfea.gov.uk"
    },
    {
      "name": "Accept-Encoding",
      "value": "gzip,deflate,sdch"
    },
    {
      "name": "Host",
      "value": "guide.hfea.gov.uk"
    },
    {
      "name": "Accept-Language",
      "value": "en-GB,en-US;q=0.8,en;q=0.6"
    },
    {
      "name": "User-Agent",
      "value": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22"
    },
    {
      "name": "Content-Type",
      "value": "application/x-www-form-urlencoded"
    },
    {
      "name": "Accept",
      "value": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    },
    {
      "name": "Cache-Control",
      "value": "max-age=0"
    },
    {
      "name": "Referer",
      "value": "http://guide.hfea.gov.uk/guide/AdvancedSearch.aspx"
    },
    {
      "name": "Connection",
      "value": "keep-alive"
    },
    {
      "name": "Content-Length",
      "value": "7105"
    },
    {
      "name": "Accept-Charset",
      "value": "ISO-8859-1,utf-8;q=0.7,*;q=0.3"
    }
]

payload = {}
for i in har:
    payload[ urllib.unquote_plus(i["name"]) ] = urllib.unquote_plus(i["value"])

headers = {}
#for h in harhdr:
#    headers[ urllib.unquote(h["name"]) ] = urllib.unquote(h["value"])

r = requests.post( "http://guide.hfea.gov.uk/guide/AdvancedSearch.aspx", data=payload, headers=headers )

bs = BeautifulSoup( r.text )

links = bs.find_all("a", href=re.compile('Overview\.aspx\?code\=') )
print links

#print r.text.encode('utf-8')

