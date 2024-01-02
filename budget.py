class Category:

    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.get_balance() < amount:
            return False
        else:
            self.ledger.append({"amount": 0 - amount, "description": description})
            return True

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, destination_budget):
        if self.get_balance() < amount:
            return False
        else:
            self.withdraw(amount, f"Transfer to {destination_budget.budget_category}")
            destination_budget.deposit(amount, f"Transter from {self.budget_category}")
            return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def __repr__(self):
        title_len = len(self.budget_category)
        star_times = (30 - title_len) / 2
        star = "*" * int(star_times)
        result = f"{star}{self.budget_category}{star}"
        for item in self.ledger:
            amount_str = f"{item['amount']:.2f}"
            key_len = len(amount_str)
            value_len = len(item["description"])
            space = " " * (30 - key_len - value_len)
            if (value_len + key_len + 1) < 30:
                result = result + f"\n{item['description']}{space}{amount_str}"
            else:
                result = result + f"\n{item['description'][0:29-key_len]}{space} {amount_str}"
        result = result + f"\nTotal: {self.get_balance():.2f}"
        return result


def create_spend_chart(categories):
    line_100 = "100|"
    line_90 = " 90|"
    line_80 = " 80|"
    line_70 = " 70|"
    line_60 = " 60|"
    line_50 = " 50|"
    line_40 = " 40|"
    line_30 = " 30|"
    line_20 = " 20|"
    line_10 = " 10|"
    line_0 = "  0|"
    line_ground = "    "

    total = 0
    for category in categories:
        for items in category.ledger:
            if items["amount"] < 0:
                total += items["amount"]
            else:
                continue

    for category in categories:
        category_total = 0
        for items in category.ledger:
            if items["amount"] < 0:
                category_total += items["amount"]
            else:
                continue
        percent = category_total / total * 100
        if percent > 0:
            line_0 = line_0 + " o "
        else:
            line_0 = line_0 + "   "
        if percent > 10:
            line_10 = line_10 + " o "
        else:
            line_10 = line_10 + "   "
        if percent > 20:
            line_20 = line_20 + " o "
        else:
            line_20 = line_20 + "   "
        if percent > 30:
            line_30 = line_30 + " o "
        else:
            line_30 = line_30 + "   "
        if percent > 40:
            line_40 = line_40 + " o "
        else:
            line_40 = line_40 + "   "
        if percent > 50:
            line_50 = line_50 + " o "
        else:
            line_50 = line_50 + "   "
        if percent > 60:
            line_60 = line_60 + " o "
        else:
            line_60 = line_60 + "   "
        if percent > 70:
            line_70 = line_70 + " o "
        else:
            line_70 = line_70 + "   "
        if percent > 80:
            line_80 = line_80 + " o "
        else:
            line_80 = line_80 + "   "
        if percent > 90:
            line_90 = line_90 + " o "
        else:
            line_90 = line_90 + "   "
        if percent == 100:
            line_100 = line_100 + " o "
        else:
            line_100 = line_100 + "   "
    line_90 = line_90 + "  "
    line_100 = line_100 + " "
    line_80 = line_80 + " "
    line_70 = line_70 + " "
    line_60 = line_60 + " "
    line_50 = line_50 + " "
    line_40 = line_40 + " "
    line_30 = line_30 + " "
    line_20 = line_20 + " "
    line_10 = line_10 + " "
    line_0 = line_0 + " "

    lenth_category = None
    for category in categories:
        if lenth_category is None or lenth_category < len(category.budget_category):
            lenth_category = len(category.budget_category)

    boundary = "---"
    string_category = ""
    for i in range(lenth_category):
        string_category = string_category + "    "
        for category in categories:
            string_split = list(category.budget_category)
            try:
                string_category = string_category + f" {string_split[i]} "
            except:
                string_category = string_category + "   "
        string_category = string_category + "\n"
    result = "Percentage spent by category\n" \
             f"{line_100}\n" \
             f"{line_90}\n" \
             f"{line_80}\n" \
             f"{line_70}\n" \
             f"{line_60}\n" \
             f"{line_50}\n" \
             f"{line_30}\n" \
             f"{line_20}\n" \
             f"{line_10}\n" \
             f"{line_0}\n" \
             f"    {boundary * len(categories)}\n" \
             f"{string_category}"
    return result



