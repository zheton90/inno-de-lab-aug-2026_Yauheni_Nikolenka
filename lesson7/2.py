raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]
clean_transactions = [t[8:] for t in raw_transactions if t.startswith('SUCCESS') and int(t[8:]) > 0]
# clean_price_transactions = [t[8:] for t in clean_success_transactions ]
# clean_positive_transactions = [t for t in clean_price_transactions if int(t) > 0]

print(f"Очищенные транзакции: {clean_transactions}")
