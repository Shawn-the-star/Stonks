PRINT("Please enter your numbers")
VAR a = INPUT_INT()
VAR b = INPUT_INT()

FUN add(a, b)
    PRINT("SUM OF " + PRINT_RET(a) + " AND " + PRINT_RET(b) + " IS:")
    PRINT(a + b)
END
add(a, b)