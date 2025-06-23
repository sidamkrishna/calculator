Terminal Calculator in Python

This is a basic calculator I built in Python that runs in the terminal.

I started this to understand how Python works differently from C++. In C++, I usually write `int main()` and separate logic in `void` functions —
but Python doesn't need `main()`, so I learned how to use `def main()` and the `if __name__ == "__main__"` structure to mimic that flow.


 Features

- Addition, Subtraction, Multiplication, Division
- Runs in a loop until you choose to exit
- Handles invalid input using `try-except`
- Clean terminal output

 What I Learned

- Python functions don't need return types like `void` or `int` — just use `def`
- You can structure code like C++ by defining a `main()` and calling it under `__main__`
- `input()` always returns strings, so `int()` or `float()` is needed to do math
- `while True:` and `break` make repeating logic clean and simple
- Error handling in Python is easier than C++'s try-catch



 📦 How to Run

1. Make sure Python is installed (`python --version`)
2. Clone this repo:
   ```bash
   git clone https://github.com/sidamkrishna/calculator.git
   cd calculator
