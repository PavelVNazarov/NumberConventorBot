# NumberConverterFunc.py
def number_to_words(num):
    if num == 0:
        return "Zero"

    thousands = ["", "Thousand", "Million", "Billion"]
    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def helper(n):
        if n < 20:
            return below_20[n]
        elif n < 100:
            return tens[n // 10] + (" " + below_20[n % 10] if n % 10 != 0 else "")
        else:
            return below_20[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")

    result = []
    for i, word in enumerate(thousands):
        if num % 1000 != 0:
            result.append(helper(num % 1000) + (" " + word if word else ""))
        num //= 1000

    return ' '.join(result[::-1]).strip()

# Примеры использования
print(number_to_words(123))      # Вывод: "One Hundred Twenty Three"
print(number_to_words(12345))    # Вывод: "Twelve Thousand Three Hundred Forty Five"
