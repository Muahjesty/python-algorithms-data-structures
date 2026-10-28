
# 🐍 CS 210: Data Structures & Algorithms in Python (Homework 1)

A collection of foundational Python algorithms and mathematical data processing utilities implemented from first principles without external analytical packages.

---

## 💡 Overview

This repository contains pure Python 3 solutions for algorithmic tasks covering prime factorization, string frequency sorting, digit sequence analysis, descriptive statistics, and combinatorial multi-pointer target searching.

---

## 🧩 Program Specifications & Algorithm Details

### 1. Prime Factorization (`factor.py`)
* **Objective**: Computes prime factors for an integer $n \ge 2$ supplied via command-line arguments.
* **Algorithm**: Implements iterative trial division, continuously reducing $n$ while printing prime factors in non-decreasing order.
* **Command Usage**:
  ```bash
  python3 factor.py 40
  # Output: 2 2 2 5
  ```

### 2. Character Frequency Counter (`countLetters.py`)
* **Objective**: Parses standard text input, calculates case-insensitive letter occurrences, and outputs counts in descending frequency order.
* **Key Operations**: String filtering via `.isalpha()`, dictionary accumulation, and custom key-value tuple sorting (`sorted(..., key=lambda item: item[1], reverse=True)`).
* **Command Usage**:
  ```bash
  python3 countLetters.py
  # Input: count letters in this string
  ```

### 3. Increasing Digits Enumerator (`increasingDigits.py`)
* **Objective**: Counts all positive integers $1 \le i \le n$ where adjacent digits satisfy strict monotonicity ($d_1 < d_2 < \dots < d_k$).
* **Algorithm**: String representation parsing to inspect sequential digit bounds.
* **Command Usage**:
  ```bash
  python3 increasingDigits.py 30
  # Output: 24
  ```

### 4. Mathematical Descriptive Statistics (`stats.py`)
* **Objective**: Calculates sample mean ($\mu$), sample median, and sample standard deviation ($\sigma$) from streaming user input terminated by sentinel value `-12345`.
* **Formulas Implemented**:
  * **Mean**: $\mu = \frac{1}{n} \sum_{i=1}^n x_i$
  * **Standard Deviation**: $\sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (x_i - \mu)^2}$
* **Command Usage**:
  ```bash
  python3 stats.py
  ```

### 5. Zero-Sum Triplet Search (`zeroTriples.py`)
* **Objective**: Identifies all unique 3-element combinations ($x_i, x_j, x_k$) in an array that sum to zero ($x_i + x_j + x_k = 0$).
* **Algorithm**: Non-repeating combinatorial exhaustive loop maintaining unique element indexing without duplicate reuse.
* **Command Usage**:
  ```bash
  python3 zeroTriples.py
  ```

---

## 🛠️ Constraints & Technical Stack

* **Language**: Python 3
* **Allowed Modules**: Standard library (`math` module only)
* **Design Guidelines**: First-principles implementation without third-party statistical or numerical frameworks (e.g., `numpy`, `pandas`).

---

## 🚀 How to Run Locally

Clone the repository and run any script using Python 3:

```bash
git clone https://github.com/your-username/cs210-python-algorithms-hw1.git
cd cs210-python-algorithms-hw1
python3 stats.py
```
