import requests, re, sys, os, urllib, pprint
from bs4 import BeautifulSoup
import logging
import csv

GUIDE_ROOT_URL = "http://guide.hfea.gov.uk/guide/"
CACHE_FOLDER = "/home/mark/tmp/cache/"

def cached_soup( url, filename ):
    import codecs
    try:
        with codecs.open( os.path.join(CACHE_FOLDER, filename), "r", "utf-8" ) as f:
            bs = BeautifulSoup( f.read() )
    except IOError:
        r = requests.get( url )
        codecs.open( os.path.join(CACHE_FOLDER, filename), "w", "utf-8" ).write( r.text )
        bs = BeautifulSoup( r.text )
    return bs

def index_clinics():
    clinics = {}
    for index in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 
        logging.debug( index )
        bs = cached_soup(
            GUIDE_ROOT_URL + "AllClinics.aspx?x=%s" % (index, ),
            "clinic_list_%s.html" % (index, )
        )
        try:
            rows = bs.find_all("table", "results")[0].find_all("tr")
            for row in rows:
                # ignore satellite clinics for now by only looking for treatment facilities 
                if re.search("Treatment", row.text, re.I):
                    tel = re.search("tel:([0-9 ]+)", row.text, re.I)
                    if tel:
                        tel = tel.group(1).strip()
                    else:
                        tel = u'';
                    # case insensitive cos they mix 'code' and 'Code' (mental .net mentalists)
                    link = row.find("a", href=re.compile('Overview\.aspx\?code\=', re.I) )
                    code =  re.search("code=([0-9]+)", link["href"], re.I).group(1)
                    clinics[ int(code) ] = {
                        "hfea_link": GUIDE_ROOT_URL + link["href"],
                        "name": link.text,
                        "tel": tel,
                        "code": int(code),
                    }
        except IndexError:
            logging.debug( "No results" )
    return clinics.values()


def get_clinic_data( code ):
    clinic = {}
    bs = cached_soup(
        GUIDE_ROOT_URL + "Overview.aspx?Code=%i&s=l&nav=1" % (code, ),
        "clinic_overview_%i.html" % (code, )
    )

    try:
        clinic[ "website" ] = bs.find("a", rel="external", text=re.compile("website", re.I) )["href"]
    except TypeError:
        clinic[ "website" ] = ""

    def extract_count( t ):
        m = re.search(":\s*([0-9]+)\s*$", t)
        if m:
            return int( m.group(1) )
    clinic["cycles_ivf"] = extract_count( bs.find(id='ctl00_cph_dvSuccessRatesSummary').find('li', text=re.compile('IVF')).text )
    clinic["cycles_icsi"] = extract_count( bs.find(id='ctl00_cph_dvSuccessRatesSummary').find('li', text=re.compile('ICSI')).text )

    clinic.update( get_clinic_headline_data( code ) )
    clinic.update( get_clinic_icsi_data( code ) )
    clinic.update( get_clinic_icsi_3year_data( code ) )

    return clinic

def get_clinic_headline_data( code ):
    clinic = {}
    bs = cached_soup(
        GUIDE_ROOT_URL + "HeadlineData.aspx?code=%i&s=l&&nav=2&rate=i&rate_sub=FSO" % (code, ),
        "clinic_headline_%i.html" % (code, )
    )
    def extract_count( t ):
        m = re.search("([0-9]+) out of ([0-9]+)", t)
        if m:
            return ( int( m.group(1) ), int( m.group(2) ) )

    success_cycle = extract_count( bs.select( '#ctl00_cph_panTblLiveBirths tbody' )[0].find( 'th', text=re.compile('Under 35') ).find_next_sibling("td").text )
    success_embryo = extract_count( bs.select( '#ctl00_cph_panTblEmbryos tbody' )[0].find( 'th', text=re.compile('Under 35') ).find_next_sibling("td").text )
    clinic[ "overall_births" ] = success_cycle[0]
    clinic[ "overall_embryos" ] = success_embryo[1]
    clinic[ "overall_cycles" ] = success_cycle[1]

    clinic[ "live_births_per_cycle" ] = float( clinic[ "overall_births" ] ) / float( clinic[ "overall_cycles" ] )
    return clinic

def get_clinic_icsi_data( code ):
    clinic = {}
    bs = cached_soup(
        GUIDE_ROOT_URL + "CloserLook.aspx?code=%i&s=l&&nav=2&rate=i&rate_sub=FSO&bdy=2011&bda=b35&bds=FSO&bdt=icsi" % (code, ),
        "clinic_icsi_%i.html" % (code, )
    )
    def extract_count( t ):
        m = re.search("([0-9]+) out of ([0-9]+)", t)
        if m:
            return ( int( m.group(1) ), int( m.group(2) ) )
    success_cycle = extract_count( bs.find( 'tr', id='ctl00_cph_tr_lb_c' ).find_all( "td" )[1].text )
    success_embryo = extract_count( bs.find( 'tr', id='ctl00_cph_tr_lb_et' ).find_all( "td" )[1].text )
    total_embryo = int( bs.find( 'tr', id='ctl00_cph_tr_etran' ).find_all( "td" )[1].text )
    clinic[ "icsi_births" ] = success_cycle[0]
    clinic[ "icsi_embryos" ] = total_embryo
    clinic[ "icsi_cycles" ] = success_cycle[1]

    clinic[ "live_births_per_icsi_cycle" ] = float( clinic[ "icsi_births" ] ) / float( clinic[ "icsi_cycles" ] )
    return clinic

def get_clinic_icsi_3year_data( code ):
    clinic = {}
    bs = cached_soup(
        GUIDE_ROOT_URL + "CloserLook.aspx?code=%i&s=l&&nav=2&rate=i&rate_sub=FSO&bdy=2999&bda=b35&bds=FSO&bdt=icsi" % (code, ),
        "clinic_icsi_3yr_%i.html" % (code, )
    )
    def extract_count( t ):
        m = re.search("([0-9]+) out of ([0-9]+)", t)
        if m:
            return ( int( m.group(1) ), int( m.group(2) ) )
    success_cycle = extract_count( bs.find( 'tr', id='ctl00_cph_tr_lb_c' ).find_all( "td" )[1].text )
    success_embryo = extract_count( bs.find( 'tr', id='ctl00_cph_tr_lb_et' ).find_all( "td" )[1].text )
    total_embryo = int( bs.find( 'tr', id='ctl00_cph_tr_etran' ).find_all( "td" )[1].text )
    clinic[ "3year_icsi_births" ] = success_cycle[0]
    clinic[ "3year_icsi_embryos" ] = total_embryo
    clinic[ "3year_icsi_cycles" ] = success_cycle[1]

    clinic[ "3year_live_births_per_icsi_cycle" ] = float( clinic[ "3year_icsi_births" ] ) / float( clinic[ "3year_icsi_cycles" ] )
    return clinic

def get_all_clinic_data():

    does_imsi = {
        157: "maybe",
        44:  "yes",
        101: "maybe",
        76:  "maybe",
        6:   "yes",
    }

    clinics = index_clinics()
    out_clinics = []
    logging.debug( pprint.pformat( clinics ) )
    for clinic in clinics:
        logging.info( clinic[ "name" ] )
        try:
            summary = get_clinic_data( clinic["code"] )
            clinic.update( summary )
            if does_imsi.has_key( clinic[ "code" ] ):
                summary[ "does_imsi" ] = does_imsi[ clinic[ "code" ] ]
            else:
                summary[ "does_imsi" ] = ""
            logging.debug( pprint.pformat( summary ) )
            out_clinics.append( clinic )
        except (IndexError, AttributeError):
            logging.debug( "Not enough data" )
    
    return out_clinics
        

#logging.debug( pprint.pformat( clinics ) )

#print r.text.encode('utf-8')

if __name__ == "__main__":
    logging.basicConfig( level=logging.INFO )
    clinics = get_all_clinic_data()
    csvop = csv.DictWriter( sys.stdout, fieldnames = [
        "name",
        "website",
        "does_imsi",
        "live_births_per_cycle",
        "live_births_per_icsi_cycle",
        "3year_live_births_per_icsi_cycle",
        "hfea_link",
        "overall_births",
        "overall_embryos",
        "overall_cycles",
        "icsi_births",
        "icsi_embryos",
        "icsi_cycles",
        "3year_icsi_births",
        "3year_icsi_embryos",
        "3year_icsi_cycles",
        "tel",
    ], extrasaction="ignore" )
    csvop.writeheader()
    for clinic in clinics:
        csvop.writerow( clinic )
