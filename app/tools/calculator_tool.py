import re


def calculator_tool(expression: str):

    try:

        cleaned_expression = re.sub(
            r"[^0-9\+\-\*\/\(\)\.\ ]",
            "",
            expression
        )

        result = eval(cleaned_expression)

        return str(result)

    except Exception:

        return "Invalid mathematical expression."