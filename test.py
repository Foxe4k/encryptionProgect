from function import encryptedMessege
lang=input("Введите язык(RU-Русский;EN-Английский)")
def test(realResult,expertResult):
    realResult=encryptedMessege(realResult,lang)

    print("Кейс должен вернуть",realResult ==expertResult )
if lang=="RU":
    test("абв","бвг")
    test("россия","спттйа")
    test("виктория","гйлупсйа")
    test("луканафт","мфлбобху")
    test("ййююььъъёё","ккяяээыыжж")
    test("укентравиротерияырувуи","флёоусбгйспуёсйаьсфгфй")
    test("йодентовуройсебударийскиялдеровойтагоудцтедслцславсоаитпнрворвдкшарлдущооррор","кпеёоупгфспктёвфебсйктлйамеёспгпкубдпфечуёетмчтмбгтпбйуросгпсгелщбсмефъппсспс")
    test("йцукенгшщзхъээээждлорпавыфячсмитьбюйукенгшщзххъъфывапролджэячсмитьбюнпцашнцпнцпапйцнепненпгцацугцуаагцуацуагнуанкенгш","кчфлёодщъицыююююземпсрбгьхаштнйуэвякфлёодщъиццыыхьгбрспмезюаштнйуэвяорчбщочрочрбркчоёроёордчбчфдчфббдчфбчфбдофболёодщ")
if lang == "EN":
    test("abc","bcd")

    test("ivan","jwbo")
    test("ferrarui","gfssbsvj")
    test("lolkekarbidol","mpmlflbscjepm")
    test("vilolrthyrbhfbhfhfjhfjhfhfghfguuyguyguyg","wjmpmsuizscigcigigkigkigighighvvzhvzhvzh")
    test("dqadada","erbebeb")
    test("wasd","xbte")
