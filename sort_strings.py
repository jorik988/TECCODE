# функция сортировки строк по длине
def sort_strings(strings):

    strings.sort(key=len)
    print("Сортировка по возрастанию:", strings)

    strings.sort(key=len, reverse=True)
    print("Сортировка по убыванию:", strings)


strings_list = ["медведь", "заяц", "ёж", "бурундук", "соболь"]
sort_strings(strings_list)
