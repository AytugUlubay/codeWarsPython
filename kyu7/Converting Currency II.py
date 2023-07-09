"""Given the current exchange rate between the USD and the EUR is 1.1363636 write a function that will accept the Curency type to be returned and a list of the amounts that need to be converted.

Don't forget this is a currency so the result will need to be rounded to the second decimal.

'USD' Return format should be '$100,000.00'

'EUR' Return format for this kata should be '100,000.00€'

to_currency is a string with values 'USD','EUR' , values_list is a list of floats

solution(to_currency,values)

#EXAMPLES:

solution('USD',[1394.0, 250.85, 721.3, 911.25, 1170.67]) 
= ['$1,584.09', '$285.06', '$819.66', '$1,035.51', '$1,330.31']

solution('EUR',[109.45, 640.31, 1310.99, 669.51, 415.54]) 
= ['96.32€', '563.47€', '1,153.67€', '589.17€', '365.68€']"""
def solution(to_cur, value):
    if "USD" == to_cur:
        k = []
        for i in range(len(value)):
            m = value[i] * 1.1363636
            k.append(round(m, 2))
        dolar_ekli_liste = []
        for eleman in k:
            formatted_eleman = '${:,.2f}'.format(eleman)
            dolar_ekli_liste.append(formatted_eleman)
        return dolar_ekli_liste
    elif "EUR" == to_cur:
        k = []
        for i in range(len(value)):
            m = value[i] / 1.1363636
            k.append(round(m, 2))
        euro_ekli_liste = []
        for eleman in k:
            formatted_eleman = '{:,.2f}€'.format(eleman)
            euro_ekli_liste.append(formatted_eleman)
        return euro_ekli_liste
