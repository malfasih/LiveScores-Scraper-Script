#Requirements:
#  -BeautifulSoup. urllib.request.
#Usage:
#  -Para executar o script basta escrever na linha de comandos:
#		Sem parametro - Imprime todos os jogos da pagina:
#			python livescores.py
#		Com parametro -    --active -> apenas jogos finalizados ou a decorrer.  --not_active -> jogos ainda por iniciar.
#			python livescores.py --active    /    python livescores.py --not_active

from bs4 import BeautifulSoup
import urllib.request
import sys

def check_hours_format(string):
	valid = True
	#Valida o formato das horas.
	# Aceita FT HT etc.
	# Aceita 10:20,  20:30,  etc
	# Nao aceita  10:20 Delay blablabla - Para casos em que o resultado nao seja fiavel.
	if(len(string)>=5):
		if(len(string)>7):
			return False
		else:
			for i in (0,1,3,4):
				if(type(string[i]) is int):
					pass
				else:
					valid=not valid
		
	return valid

#Retorna uma lista com os jogos que estao presentes na pagina.
# Disclaimer: Ainda nao filtra so os jogos do dia actual.
def get_today_games(content):
	lis_final = []
	for elm in content:
		dic_jogo={}

		#HORAS
		hours_ = (elm.find('div', class_='min').getText())
		if (check_hours_format(hours_)) == True:
			dic_jogo['hours'] = hours_
			# print(hours_)
		
		#EQUIPA 1
		team1_ = elm.find('div', class_='ply tright name').getText()
		dic_jogo['team1'] = team1_

		#EQUIPA 2
		team2_ = elm.find('div', class_='ply name').getText()
		dic_jogo['team2'] = team2_

		#RESULTADO
		result_ = elm.find('div', class_='sco').getText()
		dic_jogo['result'] = result_

		lis_final.append(dic_jogo)

	return lis_final

#Verifica se o resultado tem numeros . Serve para filtrar apenas jogos finalizados ou a decorrer na funcao pretty_print
def has_numbers(string):
	has_numbers = False
	for c in string:
		try:
			elm = int(c)
			if(type(elm) is int):
				has_numbers = True
		except:
			pass
	return has_numbers

#Funcao helper para imprimir de acordo com o parametro passado na console.
def pretty_print(lis_final, param = None):
	if(param==None):
		for elm in lis_final:
			try:
				print_content = elm['hours'] + "\t" + elm['team1'] + " " + elm['result'] + " " + elm['team2']
				print(print_content)
			except:
				pass
		return

	if(param == '--active'):
		for elm in lis_final:
			if(has_numbers(elm['result']) == True):
				try:
					print_content = elm['hours'] + "\t" + elm['team1'] + " " + elm['result'] + " " + elm['team2']
					print(print_content)
				except:
					pass
			else:
				pass
	elif(param == '--not_active'):
		for elm in lis_final:
			if(has_numbers(elm['result']) == False):
				try:
					print_content = elm['hours'] + "\t" + elm['team1'] + " " + elm['result'] + " " + elm['team2']
					print(print_content)
				except:
					pass
			else:
				pass
	elif(param == '--json'):
		print(lis_final)


def main(args):	
	r = urllib.request.urlopen('http://www.livescores.com/').read()
	soup = BeautifulSoup(r, 'lxml')

	#Obter todas as divs com a class 'row-gray even'
	content = soup.findAll('div', class_='row-gray even')

	#adicina objectos do tipo dicionario a uma lista, de acordo com os dados retirados do site
	lis_final = get_today_games(content)

		if(len(args)>1):
		pretty_print(lis_final, args[1])
	else:
		pretty_print(lis_final)
	


if __name__ == '__main__':
	main(sys.argv)
