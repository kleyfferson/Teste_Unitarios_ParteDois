class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'

        if len(number) < 0:
            return 'Numero invalido'  # erro na escrita

        # Validar com o cliente a regra correta
        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name not in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        tamanho = int(len(self.entries))
        if tamanho > 0:
            if name != None:
                for key, number in self.entries.items():
                    if name == key:
                        self.entries.pop(key, number)
                        return "Numero deletado"
                return "Usuario não encontrado"
            else:
                return "O nome passado não pode ser None"
        else:
            return "Não existe registrados cadastrados"

    def change_number(self, name, number):
        tamanho = int(len(self.entries))
        if tamanho > 0:
            if (name != None) or (number != None):
                for key, value in self.entries.items():
                    if name == key:
                        self.entries.update({name: number})
                        return "Numero atualizado"
                return "Usuario não encontrado"
            else:
                return "O nome ou o número passado não pode ser None"
        else:
            return "Não existe registrados cadastrados"

    def get_name_by_number(self, number):
        tamanho = int(len(self.entries))
        if tamanho > 0:
            if number != None:
                for key, value in self.entries.items():
                    if number == value:
                        return key
            else:
                return "O nome ou o número passado não pode ser None"
        else:
            return "Não existe registrados cadastrados"

