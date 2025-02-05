from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    sum_divisors = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
        i += 1
    return sum_divisors == n

def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_param = request.args.get('number')

    try:
        number = int(number_param)
    except (ValueError, TypeError):
        # Return the exact input value provided by the user
        return jsonify({
            "number": number_param,
            "error": True
        }), 400

    prime_status = is_prime(number)
    perfect_status = is_perfect(number)
    armstrong_status = is_armstrong(number)
    ds = digit_sum(number)
    
    parity = "even" if number % 2 == 0 else "odd"
    properties = [parity] if not armstrong_status else ["armstrong", parity]

    fun_fact = ""
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math", timeout=5)
        if response.status_code == 200:
            fun_fact = response.text
        else:
            fun_fact = "No fun fact available."
    except Exception:
        fun_fact = "No fun fact available."

    result = {
        "number": number,
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": ds,
        "fun_fact": fun_fact
    }

    return jsonify(result), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
