# 仮の値（売上と経費）
sales = 12_000_000      # 売上
expenses = 4_500_000    # 経費（現状）

# 法人実効税率の仮定（30%）
tax_rate = 0.30

# 節税施策で追加できる経費（例: 研修費・設備投資など）
additional_deductible_expense = 800_000

# 節税前の課税所得と税額
taxable_income_before = sales - expenses
tax_before = taxable_income_before * tax_rate

# 節税後の課税所得と税額
taxable_income_after = sales - (expenses + additional_deductible_expense)
tax_after = taxable_income_after * tax_rate

# 節税金額
tax_saving = tax_before - tax_after

print("=== 節税シミュレーター（仮の値）===")
print(f"売上: {sales:,} 円")
print(f"経費（現状）: {expenses:,} 円")
print(f"追加可能な経費: {additional_deductible_expense:,} 円")
print("-" * 35)
print(f"節税前の税額: {tax_before:,.0f} 円")
print(f"節税後の税額: {tax_after:,.0f} 円")
print(f"節税できる金額: {tax_saving:,.0f} 円")
