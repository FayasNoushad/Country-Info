from countryinfo import CountryInfo


def info(name):
    try:
        country = CountryInfo(name)
        info = f"""Country Information

Name : {country.name()}
Native Name : {country.native_name()}
Capital : {country.capital()}
Population : {country.population()}
Region : {country.region()}
Sub Region : {country.subregion()}
Top Level Domains : {country.tld()}
Calling Codes : {country.calling_codes()}
Currencies : {country.currencies()}
Residence : {country.demonym()}
Timezone : {country.timezones()}
Wikipedia : {country.wiki()}
Google : {country.google()}"""
        return info
    except Exception as error:
        return error


def main():
    country = input("Enter country name :- ")
    print(info(country))
    again = input("If you need to country information again?\ny for yes n for no\n:- ")
    if again.lower() == "n":
        print("\nThanks for using")
        return
    else:
        print("")
        return main()

main()
