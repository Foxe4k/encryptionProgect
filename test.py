from function import encryptedMessege
def test(realResult,expertResult):
    realResult=encryptedMessege(realResult)

    print("Кейс должен вернуть",realResult ==expertResult )
print("РУССКИЙ")
test("абв","бвг")
test("россия","спттйа")
test("виктория","гйлупсйа")
test("луканафт","мфлбобху")
test("ййююььъъёё","ккяяээыыжж")
test("укентравиротерияырувуи","флёоусбгйспуёсйаьсфгфй")
test("йодентовуройсебударийскиялдеровойтагоудцтедслцславсоаитпнрворвдкшарлдущооррор","кпеёоупгфспктёвфебсйктлйамеёспгпкубдпфечуёетмчтмбгтпбйуросгпсгелщбсмефъппсспс")
test("йцукенгшщзхъээээждлорпавыфячсмитьбюйукенгшщзххъъфывапролджэячсмитьбюнпцашнцпнцпапйцнепненпгцацугцуаагцуацуагнуанкенгш","кчфлёодщъицыююююземпсрбгьхаштнйуэвякфлёодщъиццыыхьгбрспмезюаштнйуэвяорчбщочрочрбркчоёроёордчбчфдчфббдчфбчфбдофболёодщ")
print("АНГЛИЙСКИЙ")
test("abc","bcd")
test("ivan","jwbo")
test("ferrarui","gfssbsvj")
test("lolkekarbidol","mpmlflbscjepm")
test("vilolrthyrbhfbhfhfjhfjhfhfghfguuyguyguyg","wjmpmsuizscigcigigkigkigighighvvzhvzhvzh")
test("dqadada","erbebeb")
test("wasd","xbte")
