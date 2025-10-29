import re
import random


class PasswordGame:
    def __init__(self):
        self.numero_sorteado = random.randint(11, 99)

        self.rules = [
            self._rule1_min_5_chars,
            self._rule2_has_number,
            self._rule3_has_uppercase,
            self._rule4_has_special_char,
            self._rule5_digits_sum_25,
            self._rule6_has_roman_numeral,
            self._rule7_has_random_number,
            self._rule8_has_palindrome,
            self._rule9_has_emoji,
            self._rule10_has_consecutive_letters,
            self._rule11_has_letter_sequence,
            self._rule12_has_math_equation
        ]

        self.rule_descriptions = [
            "Sua senha deve ter pelo menos 5 caracteres",
            "Sua senha deve incluir um número",
            "Sua senha deve incluir uma letra maiúscula",
            "Sua senha deve incluir um caractere especial",
            "Os dígitos na sua senha devem somar 25",
            "Sua senha deve incluir um número romano",
            f"Sua senha deve incluir o número {self.numero_sorteado}",
            "Sua senha deve incluir um palíndromo de pelo menos 3 caracteres",
            "Sua senha deve incluir um emoji (pode ser textual como :) :D <3)",
            "Sua senha deve incluir 3 letras consecutivas do alfabeto (ex: abc, xyz)",
            "Sua senha deve conter uma sequência onde a soma ASCII de 3 caracteres seguidos seja par",
            "Sua senha deve incluir uma equação matemática simples com resultado correto (ex: 2+2=4)"
        ]

    def _rule1_min_5_chars(self, password):
        return len(password) >= 5

    def _rule2_has_number(self, password):
        return bool(re.search(r'\d', password))

    def _rule3_has_uppercase(self, password):
        return bool(re.search(r'[A-Z]', password))

    def _rule4_has_special_char(self, password):
        return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    def _rule5_digits_sum_25(self, password):
        digits = re.findall(r'\d', password)
        if not digits:
            return False
        return sum(int(d) for d in digits) == 25

    def _rule6_has_roman_numeral(self, password):
        roman_pattern = r'[IVXLCDM]+'
        return bool(re.search(roman_pattern, password.upper()))

    def _rule7_has_random_number(self, password):
        return str(self.numero_sorteado) in password

    def _rule8_has_palindrome(self, password):
        for i in range(len(password) - 2):
            for j in range(i + 2, len(password)):
                substring = password[i:j + 1].lower()
                if substring == substring[::-1] and len(substring) >= 3:
                    return True
        return False

    def _rule9_has_emoji(self, password):
        emojis = [':)', ':(', ':D', ':P', ';)', ':O', '<3', '=)', '=D', 'XD', ':|', ':*', ':\\']
        return any(emoji in password for emoji in emojis)

    def _rule10_has_consecutive_letters(self, password):
        password_lower = password.lower()
        for i in range(len(password_lower) - 2):
            if (password_lower[i].isalpha() and
                    password_lower[i + 1].isalpha() and
                    password_lower[i + 2].isalpha() and
                    ord(password_lower[i + 1]) == ord(password_lower[i]) + 1 and
                    ord(password_lower[i + 2]) == ord(password_lower[i]) + 2):
                return True
        return False

    def _rule11_has_letter_sequence(self, password):
        for i in range(len(password) - 2):
            ascii_sum = ord(password[i]) + ord(password[i + 1]) + ord(password[i + 2])
            if ascii_sum % 2 == 0:
                print(f"Sequência '{password[i:i + 3]}': Soma ASCII = {ascii_sum} (par)")
                return True
        return False

    def _rule12_has_math_equation(self, password):
        equation_patterns = [
            r'(\d+)\+(\d+)=(\d+)',
            r'(\d+)-(\d+)=(\d+)',
            r'(\d+)\*(\d+)=(\d+)',
            r'(\d+)/(\d+)=(\d+)'
        ]

        for pattern in equation_patterns:
            matches = re.findall(pattern, password)
            for match in matches:
                if pattern == r'(\d+)\+(\d+)=(\d+)':
                    if int(match[0]) + int(match[1]) == int(match[2]):
                        return True
                elif pattern == r'(\d+)-(\d+)=(\d+)':
                    if int(match[0]) - int(match[1]) == int(match[2]):
                        return True
                elif pattern == r'(\d+)\*(\d+)=(\d+)':
                    if int(match[0]) * int(match[1]) == int(match[2]):
                        return True
                elif pattern == r'(\d+)/(\d+)=(\d+)':
                    if int(match[1]) != 0 and int(match[0]) / int(match[1]) == int(match[2]):
                        return True

        return False

    def check_password(self, password):
        results = []
        for i, rule in enumerate(self.rules):
            passed = rule(password)
            results.append({
                'rule_number': i + 1,
                'description': self.rule_descriptions[i],
                'passed': passed
            })
        return results

    def play(self):
        print("🔒 BEM-VINDO AO PASSWORD GAME! 🔒\n")
        print("Crie uma senha que atenda a todas as regras que aparecem.")
        print("As regras vão ficando mais difíceis conforme você avança!\n")

        current_rule = 0

        while current_rule < len(self.rules):
            print(f"\n📋 REGRAS ATIVAS (Total: {current_rule + 1}):")
            for i in range(current_rule + 1):
                print(f"   ➡️ Regra {i + 1}: {self.rule_descriptions[i]}")

            print(f"\n🎯 Você precisa passar em TODAS as regras acima para continuar!")
            password = input("\n Digite sua senha: ")

            if not password.strip():
                print("❌ Senha não pode estar vazia!")
                continue

            results = []
            all_passed = True

            for i in range(current_rule + 1):
                passed = self.rules[i](password)
                results.append({
                    'rule_number': i + 1,
                    'description': self.rule_descriptions[i],
                    'passed': passed
                })

                if not passed:
                    all_passed = False

            # Mostrar resultados
            print("\n📊 Resultado da verificação:")
            for result in results:
                status = "✅" if result['passed'] else "❌"
                print(f"   {status} Regra {result['rule_number']}: {result['description']}")

            if all_passed:
                current_rule += 1
                if current_rule < len(self.rules):
                    print(f"\n✅ SUCESSO! Nova regra desbloqueada: {self.rule_descriptions[current_rule]}")
                else:
                    print("\n🎉 PARABÉNS! VOCÊ VENCEU O PASSWORD GAME! 🎉")
                    print(f"Sua senha final: {password}")
                    print("Você conseguiu criar uma senha que atende a todas as regras malucas!")
                    break
            else:
                print("\n❌ Você ainda precisa corrigir algumas regras antes de continuar.")


def main():
    game = PasswordGame()
    game.play()


if __name__ == "__main__":
    main()